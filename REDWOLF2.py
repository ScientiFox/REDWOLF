####
#   REDWOLF Architecture, 2nd revision
#       Implements the back end of the multi-model and feedback based
#       Redwolf LLM systems, which revolve around the use of classical
#       algorithms to regularize and establish feedback on LLM outputs
#       produced undered structured queries
#       The objective of this method is to constrain the output of the
#       LLMs used to reliably useful information, make efficacious use
#       of limited resources under local execution, and take advantage
#       of the capacity to use multiple-source and scope models in the
#       same system on a personal basis
#       
####

#Basics
import math,time,random
import ast,re
import warnings
import pickle

#JS stuff
import asyncio,websockets
import webbrowser
from websockets.sync.client import connect
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

#File stuff
import glob
import markdown
import pymupdf,pymupdf4llm

#Math stuff
import numpy as np
import cv2

#LLM stuff
import base64
import ollama

#For the math-solver
global RES_OUT
RES_OUT = None

#NLP
import nltk.corpus
import nltk.sentiment.util
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

###
#   Utility components
#       Components for processing and regularizing text, as
#       well as interfacing with other assets, such as NLTK,
#       wikipedia ZIM files, and websites
###

#Import for structured queries and module structures
from REDWOLF_core_prompts import *

#ZIM library interface for Redwolf to execute wiki searches
from ZIM_for_REDWOLF import *


class nltk_assets:
    #Class for NLTK library assets, most useful for word-checking,
    #   definition and synonym free-association, and word analysis

    '''
    # Corpus used in this class can be downloaded with:

    nltk.download("wordnet31")
    nltk.download("vader_lexicon")
    nltk.download('subjectivity')
    '''

    def __init__(self,_language='eng',_wn=nltk.corpus.wordnet31):
        #Initialize the NLTK tools- mainly a class to keep track of the
        #   subjectivity file
        #Note that it is reasonable to not trust a pickle file, but it can
        #   be created manually through the NLTK package
        self.wn = _wn
        f = open("sa_subjectivity.pickle","rb")
        self.subjAn = pickle.load(f)
        f.close()
        self.sentAn = nltk.sentiment.SentimentIntensityAnalyzer()

    def get_near_spellings(self,word,N):
        #Finds words which are close to the spelling of a provided word, up
        #   to a Jaccard distance of N
        correct_words = nltk.corpus.wordnet31.words()
        chk = [(jaccard_distance(set(ngrams(word,2)),set(ngrams(w,2))),w) for w in correct_words]
        chk.sort(key=lambda x:x[0])
        return chk[:N]

    def get_word(self,word):
        #Draw set of useful features for a word from the synsets and dictionary
        #   Includes the lexical name, definition, synontms, and text examples
        #   for the word
        synsets = self.wn.synsets(word)
        synos = self.wn.synonyms(word)
        wrds = []
        for i in range(len(synsets)):
            name = synsets[i].name().split(".")[0]
            lex = synsets[i].lexname
            defi = synsets[i].definition()
            exs = synsets[i].examples()
            syns = synos[i]
            wrd = {"name":name,"lexical":lex,"definition":defi,"synonyms":syns,"examples":exs}
            wrds = wrds + [wrd]
        return wrds

    def sub_analyze(self,text):
        #Wrapper for the subjectivity analysis function
        return self.subjAn(text)

    def sent_analyze(self,text):
        #Wrapper for the sentiment analyzer analysis function
        polar = self.sentAn.polarity_scores(text)
        print(polar)
        resp = np.argmax([polar[a] for a in ['neg','neu','pos']])
        resp = ['neg','neu','pos'][resp]
        return resp

def construct_prompt(prmpt,keys):
    #Construct a prompt from a prompt template and input keys
    #   replaces all present tags with the keys provided
    op_prmpt = prmpt+""
    for key in keys:
        if not(key[0] == "{"):
            key = "{" + key
        if not(key[-1] == "}"):
            key = key + "}"
        op_prompt = op_prompt.replace(key,keys[key])
    return op_prompt

def block_extractor(text,key):
    #Extract a block from LLM markup, usually signified with
    #   ```type [...]```
    #   Mainly used to extract python code or JSONs
    #
    #   Takes in a specific type key to pull elements!
    text = text.encode("ascii","ignore").decode()

    l_out = []
    to_block = text.split("```")

    output_block = None
    for seg in to_block:
        if seg[:len(key)] == key:
            output_block = seg[len(key):]
        else:
            pass

    return output_block

def timeproof_code(pde,question,t_max=5.0):
    #A utility function to convert extracted Python code from LLM
    #   outputs to have a strict, universal time limit for execution
    #   prevents LLM code from spinning forever when we execute it

    #Make sure time is imported, and an explicit runtime variable is injected
    pde = "import time\nruntime_init=time.time()\n"+pde
    pde_lines = pde.split("\n")
    op_nums = re.findall("\d+",question) #Find all numeric components of the original question

    #Building the output system:
    pde_o = ""
    for lne in pde_lines: #Over each line
        wh_line = re.findall("\s*while .+:",lne) #select out if it's the start of a while loop
        inp_line = re.findall("input\(.*?\)",lne) #Identify if there's a user input
        if len(wh_line) == 1: #if there's a while loop
            wh_line = wh_line[0][:-1] #snag the terminus of the while condition
            wh_line = wh_line + " and (time.time()-runtime_init <"+str(t_max)+"):" #Append a timeout
            pde_o = pde_o + wh_line + "\n" #reconstruct line
        elif (len(inp_line) == 1): #If an input
            lne = lne.replace(inp_line[0],op_nums[-1]) #Replace the input request with values from the prompt
            pde_o = pde_o + lne + "\n"
        else:
            pde_o = pde_o + lne + "\n"

    #Return the altered code
    return pde_o

def result_finder(question,p_cde,mode='code'):
    #Function to extract the final output answer from a python script
    #   that executes to solve a problem. Takes several tactics to find
    #   where the script might produce the answer

    #Find all the digits in the original question
    nums_inp = re.findall("\d+",question)
    pde = re.sub("\n\n+","\n",p_cde).strip() #Parse the code to standard spacing

    #If not executing on actual code, just grab the last number in the text-
    #   if it's not a code block it's a direct answer
    if mode != 'code':
        op_nums = re.findall("\d+",p_cde)
        return "RES_OUT = " + op_nums[-1]

    #Get lines which are not inside a function or a loop
    functions = re.findall("(def .+:)",pde) #Find the functions
    fns_labs = [f.split(" ")[1].split("(")[0] for f in functions]

    #Find all lines that are at depth 0, but not functions or loops
    outer_txt = []
    for lne in pde.split("\n"):
        if (not(lne) in functions) and (re.findall("^\s",lne)==[]) and (re.findall("^(while|for|try|except)",lne) == []) and not(lne[0] == "#"):
            outer_txt = outer_txt + [lne]
        if len(re.findall("^\s+",lne))>0:
            outer_txt = []

    #Do a sequence of checks to find the last variable
    #   referenced in the non-function/loop lines
    outer_txt.reverse()
    for last_line in outer_txt:
        if ("=" in last_line) and not(last_line[-1] == ":"): #Assignments
            l_val = last_line.split("=")[0].strip() #grab assignee and append holder variable
            pde = pde + "\n" + "RES_OUT = "+l_val
            return pde
        elif last_line[:6] == "print(": #If it's printing a result
            in_print = re.findall("\(.+\)",last_line) #strip the results
            if in_print != []: #peel off the () and split around CSV
                in_print = in_print[0][1:-1]
                in_print = in_print.split(",")
                inp_o = None
                for ip in in_print: #over each ,-separated segment
                    if re.findall("\"\'",ip) == []: #leave out anything with quotes
                        inp_o = ip
                    else:
                        pass
                if inp_o != None: #If you found a return value in the print, append holder with it
                    pde = pde + "\n" + "RES_OUT = "+inp_o
                    return pde
        elif last_line.split("(")[0] in fns_labs: #If those didn't work, but there's a return /function/
            pde = pde.split("\n") #split by lines
            pde = pde[:-1] #grab all but the last bit
            pde = pde + ["RES_OUT = "+last_line] #replace with appended assignment to output function
            pde_out = ""
            for p in pde:
                pde_out = pde_out + p + "\n" #add new last line and return
            return pde_out

    #If nothing in the last outer-lines to call the result, call the last function on whatever inputs we can find
    if len(functions) > 0: #If there's a function to call
        last_fn = functions[-1].split(" ")[1][:-1] #get the function name, w/o 'def' and ':'
        to_sp = last_fn.split("(") #separate function and args
        fn = to_sp[0]
        args = to_sp[1][:-1].split(",")

        #Build a new last line, function w/ supplied args)
        fin_line = "\n"+"RES_OUT = " + fn + "("

        if args != ['']: #If some args
            for i in range(len(args)): #loop over and add them to the called function
                if i < len(nums_inp):
                    fin_line = fin_line + nums_inp[i] + ","
                else:
                    fin_line = fin_line + "None," #supply None if out of options
            fin_line = fin_line[:-1]

        fin_line = fin_line + ")" #finish call and return
        pde = pde + fin_line

        return pde

    #So there's no outer line assignments, prints, or functions calls, and no functions to try calling?
    # maybe some stuff in a loop... without other definitions outside. Try snagging any final print or assignment

    #Final print?
    prints = re.findall("print\(.+\)",pde) #find the prints
    if len(prints) > 0: #if something there
        l_print = prints[-1] #grab the last pring
        l_print = re.findall("\(.+\)",l_print)[0][1:-1] #extrace what is printed
        in_print = l_print.split(",") #separate printed thingd
        
        inp_o = None #loop over the print arguments
        for ip in in_print:
            if re.findall("\"\'",ip) == []: #extract things not in quotes
                inp_o = ip
            else:
                pass
        if inp_o != None: #if you found something there
            pde = pde + "\n" + "RES_OUT = " #append output holder line
            for ip in in_print:
                pde = pde + ip + "," #and include all valid outputs
            pde = pde[:-1]
            return pde #return updated code

    #Final assignment?
    last_asn = re.findall(".+[^\+\=\-\*\<\>]=[^\+\=\-\*\<\>].+",pde) #select all assignment lines
    if last_asn != []: #if something in there
        last_asn = last_asn[-1] #grab the last
        last_asn = last_asn.split("=")[0].strip() #sanitize
        pde = pde + "\n" + "RES_OUT = " + last_asn #append output holder and return
        return pde

    #No assignments? Last number, then.
    nums = re.findall("\d+",pde) #go looking for numbers
    if nums != []: #if you find something
        last_num = nums[-1] #grab the last one
        pde = pde + "\n" + "RES_OUT = " + last_num #append holder
        return pde

    #Nothing? No functions, assignments, variables, numbers, or returns?
    #   You're on your own, homes.
    return pde

def list_output_gatherer(text):
    #This utility takes a segment of text expected to contain a list of some form
    #   and collects the list members for extraction. It is based on searching for
    #   repeated lead element combinations common to lists as formed by LLM systems
    #   but also human sensibilities. It also extracts machine format lists such as
    #   [,]{,}(,) or JSON objects 

    #First, process the text to visible chars. Hacky, I know.
    text = text.encode("ascii","ignore").decode()
    text = re.sub("\n\n+","\n",text) #Standardize line spacing and remove blanks

    #First off, peel out raw embdeeded lists, they make those a lot
    l_out = [] #output list
    to_dict = text.split("json") #search for json blocks
    to_dict.reverse() #re-order back to front

    for seg in to_dict: #look over all json possible segs for raw lists
        try: #try to process:
            #try and execute an assignment on a stripped and cleaned line
            op = ast.literal_eval(seg.replace("```","").strip())
            if type(op) == type([]): #if there's a list in there
                l_out = op #make it the output
            else: #if nor:
                for k in op: #zip over the output and see if there's a list in there
                    if type(op[k]) == type([]): #check again
                        l_out = op[k] #try assign again
                    else: #Otherwise, welp
                        pass
        except: #Other-otherwise, welp^2
            pass

    #If there's an actual JSON in there and you didn't find a list before
    if ("```json" in text) and (l_out == []):
        ops = [] #output list
        for seg in to_dict: #looking at all JSON segs
            inner_l = re.findall("\[[^\]\}]+\]",seg) #grab []{}() lists
            inner_l.reverse() #go back to front
            ops = ops + inner_l #add to list output
        while len(ops[0]) == 0: #until you find one that's not empty
            ops = ops[1:]#cycle through until you do or run out
        l_out = ast.literal_eval(ops[0]) #make literal version of list

    #If nothing found yet, go looking for embedded lists w/ natural repeating
    #   delimiters like 1. A- b) (7) * - etc.
    if (l_out == []):
        text = re.sub("\d+[:.-]","|",text) #check for digit and marker
        text = re.sub("[:;*]","|",text) #check for A:, A;
        text = re.sub("\[\d+\]","|",text) #check for [1]
        text = re.sub("- ","|",text) #check for x-

        by_line = text.split("\n") #break into lines

        # list of lists and out list
        l_list = []
        l_out = []
        for line in by_line: #looping over the lines
            lne = line.strip() #remove outside whitespace
            if lne == "": #if a blank line
                lne = "^" #annotated skip
            if lne[0] == "|": #If a delimiter was on the start of the line
                lne = lne.split("|") #grab stuff after delim
                i = 0 #loop over delim set
                while ((lne[i].strip()=='')and(i<len(lne))): #pass over spaces
                    i+=1
                if i < len(lne): #if remaining text
                    l_out = l_out + [lne[i].strip()] #add in stripped list element
                else: #otherwise, at end of list-ish section
                    if len(l_out)>0: #if not empty
                        l_list = l_list + [l_out] #add whole contents to list-list
                    l_out = [] #reset out list
            else: #if no delimitter
                if len(l_out)>0: #if something list-y in it
                    l_list = l_list + [l_out] #add to list-list
                l_out = [] #reset output list
        if l_out != []: #if something found in sweep
            l_list = l_list + [l_out]   #add to the output lists

        #if some lists found
        if len(l_list)>0:
            l_max = [(i,len(l_list[i])) for i in range(len(l_list))] #get the list lengths
            l_max.sort(key=lambda x:x[1]) #order the lists by length
            l_out = l_list[l_max[-1][0]] #grab the longest one
        else:
            l_out = [] #otherwise, nothing yet to return

    #If still nothing has been found
    if l_out == []:
        brack_match = re.findall("[{\[(][^{}()\[\]]+[)\]}]",text) #go looking for things inside of []{}()
        if len(brack_match)>0: #if something in brackets found
            l_out = brack_match[-1][1:-1] #grab the stuff inside the last one
        else: #otherwise
            l_out = text #set output to the text itself
        l_out = re.sub("( - |,|;|#)","$%^",l_out) #either way, break up by delimiters w/ unique sequence 
        l_out = l_out.split("$%^") #split around that sequence to get the list itself

    #process things in quotes
    l_quotes = []
    for l in l_out: #for anything in the output list
        l = l.replace("\'s","&%$") #mark possessives to save for later
        found = re.findall("[\"\'\`][^\"\'\`]+[\"\'\`]",l) #select out all quotation sets
        if len(found)>0: #if some in there, add list of the stuff in quotes w/o quotes
            l_quotes = l_quotes + [re.findall("[\"\'\`][^\"\'\`]+[\"\'\`]",l)[0][1:-1]]
        else: #otherwise, just add it
            l_quotes = l_quotes + [l]

    #Then, go through and wipe all quotes pulled
    l_quotes = [l.replace("\"","") for l in l_quotes]
    l_quotes = [l.replace("\'","") for l in l_quotes]
    l_quotes = [l.replace("\`","") for l in l_quotes]
    l_quotes = [l.replace("&%$","\'s") for l in l_quotes] #put the possessives back in

    #returned the pruned quotes as the final output
    return l_quotes

def new_listifier(text):
    #This is an additional list extractor, but one that goes looking for
    #   repeated sequences starting off lines in a regular order of a given
    #   format. Specifically for human-readable lists, not for machine lists:
    #       [,,,...], etc.
    #   Assumes each line in a list will have the same structure encoded in
    #   digits, characters, and letters at the start of each line
    #   1.      A)      *      
    #   2.      B)      *
    #   3.      C)      *       etc.

    #Preconditioning
    c_txt = re.sub("\n\n+","\n",text) #take out multiline blanks
    lines = c_txt.split("\n") #divide up into lines

    lists = [] #lists found
    curr_list = [] #current list building
    line_codes = [] #lines encoded into common format codes for character type

    i = 0 #looping over all the lines
    while i < len(lines):
        lne = lines[i] #grab this line
        line_enc = re.sub("[a-zA-Z]+\s?","l",lne) #replace letters with l
        line_enc = re.sub("\d+","d",line_enc) #replace numbers with d
        line_enc = re.sub("[\.,<>;:\'\"!@#$%^&°\*\|\-_\?=+/\\\]","p",line_enc) #p for a special character
        line_enc = re.sub("[\(\)]","e",line_enc) #() with e
        line_enc = re.sub("[\[\]]","b",line_enc) #[] with b
        line_enc = re.sub("[\{\}]","c",line_enc) #{} with c
        line_enc = re.sub("\s+"," ",line_enc) #chunk whitespace down to one space
        line_codes = line_codes + [line_enc] #Add newly encoded line to list

        if len(line_codes) > 2: #if there's enough converted lines to check
            c1 = line_codes[-2] #grab prior line
            c2 = line_codes[-1] #grab recent line

            #grab the longest common sequence of codes from last to current line
            sim = sum([c1[:i]==c2[:i] for i in range(1+min([len(c1),len(c2)]))[1:]])
            demarc = set(c1[:sim]) != {" ","l"} #find the demarcation sequence
            if demarc and (sim > 1): #if the demarcation found and an overlap
                if len(curr_list)==0: #if nothing in the current list
                    curr_list = curr_list + [lines[i-1],lines[i]] #Add prior and this line to new list
                else: #otherwise, add the current line into the current list
                    curr_list = curr_list + [lines[i]]
            else: #if not a continuance:
                if curr_list != []: #if some list already found
                    lists = lists + [curr_list] #add to the list of lists
                    curr_list = [] #reset current lest
        i+=1 #loop over the lines

    #return the found lists
    return lists

def print_prep(txt):
    #Utility function to convert text to a prinatable form
    #   uses a bunch of regex to convert MD text to HTML

    n_txt = "\n" + txt #add in a newline for processing spaces
    n_txt = re.sub("(\w)(-)(\w)","\\1§\\3",n_txt) #mark - in conjunctions for replacement later

    n_txt = re.sub("[^\S\n](:|\.|!|\?|\~|\-)","\\1",n_txt) #peel whitespace preceeding special characters

    #Convert out bracketed word characters with delimiter sets and newlines into standard "index. BOLD" line formats
    n_txt = re.sub("(\n[^\S\n]*)[\(\[\{]?[^\S\n]*(\w+)([^\S\n]*[\)\]\}\.\-:])[^\S\n]*(.+?)(:|-)","\\1\\2. <b>\\4</b>:",n_txt)

    #Convert out already bolded text with ** ** to bold only
    n_txt = re.sub("<b>\*\*+(.+)\*\*</b>","<b>\\1</b>",n_txt)

    #Convert out remaining ** ** to bold
    n_txt = re.sub("\*\*+(.+)\*\*+","<b>\\1</b>",n_txt)
    n_txt = re.sub("\*(.+)\*","<i>\\1</i>",n_txt) #replace * * to italics
    n_txt = re.sub("##+(.+)\n","<i><u>\\1</u></i>\n",n_txt) #convert ### section titles to underlined italics


    n_txt = re.sub("(\w)(§)(\w)","\\1-\\3",n_txt) #put the conjunction - back in
    n_txt = n_txt[1:] #strip out lead newline
    n_txt = re.sub("\n","<br>",n_txt) #convert newlines to breaks
    return n_txt #return final text

def make_analysis_report(fname,ctxt,fsum,thes,ans,syn,_writeOut=False):
    #Utility to format analysis reports into proper HTML displays

    #Initial text 
    report_text = ""

    #Header with title
    report_text = report_text + "<span style=\"display:block;width:750px;word-wrap:break-word\">"
    report_text = report_text + "<h1> Report</h1><hr>"

    #Display the extracted main thesis
    report_text = report_text + "<h3>Thesis:</h3>"
    report_text = report_text + "<div style=\"margin-left:40px\">"
    report_text = report_text + thes
    report_text = report_text + "</div>"
    report_text = report_text + "<br>"
    report_text = report_text + "<hr>"

    #Display the joint summary of the text
    report_text = report_text + "<h3>Joint Summary:</h3>"
    report_text = report_text + "<div style=\"margin-left:40px\">"
    report_text = report_text + fsum
    report_text = report_text + "</div>"
    report_text = report_text + "<br>"
    report_text = report_text + "<hr>"

    #Display the compactified text
    report_text = report_text + "<h3> Concise Text:</h3>"
    report_text = report_text + "<div style=\"margin-left:40px\">"
    report_text = report_text + ctxt
    report_text = report_text + "</div>"
    report_text = report_text + "<br>"
    report_text = report_text + "<hr>"

    #Build the display for the analysis questions
    report_text = report_text + "<h2> Questions:</h2>"

    #For each question asked, display a block
    for Q in ans:
        A = ans[Q]
        report_text = report_text + "<h3> " + Q+"</h3>"
        report_text = report_text + "<div style=\"margin-left:40px\">"
        report_text = report_text + print_prep(A)
        report_text = report_text + "</div>"
        report_text = report_text + "<br>"
        report_text = report_text + "<hr>"

    #Build the display for the synthesis questions
    report_text = report_text + "<h2> Synthesis:</h2>"

    #For each synthesis question, display a block
    for S in syn:
        R = syn[S]
        report_text = report_text + "<h3>" + S + "</h3>"
        report_text = report_text + "<div style=\"margin-left:40px\">"
        report_text = report_text + print_prep(R)
        report_text = report_text + "</div>"
        report_text = report_text + "<br>"
        report_text = report_text + "<hr>"

    #Close the main span, and replace all newlines with breaks
    report_text = report_text + "</span>"
    html_out = re.sub("\n","<br>",report_text)

    #Write an output HTML file if asked to
    if _writeOut:
        f = open("MD_"+fname.split(".")[0]+".html","w+")
        f.write(html_out)
        f.close()
        feedPrint("Output to: "+"MD_"+fname.split(".")[0]+".html")

    #Return the processed report HTML
    return html_out

def make_modules_list(lst):
    #Helper to make a list of modules for display on a module panel

    output = "" #Output list HTML

    #Start off the select element
    output = output + "<select id=\"modulesList\">"
    for modu in lst: #loop over the list and add a module for each element
        output = output + "<option value=\""+modu['name']+"\">"+modu['name']+"</option>"

    #close the select block
    output = output + "</select>"
    return output #return the select list block

def make_models_list(sugg,name,i):
    #Helper to make a list of /models/, including a separator between suggested
    #   models and the rest of them. i is the number of instances of this type
    #   of list to make, so it cycles through all the suggested models of the
    #   requisite system

    #cycle through to ith model for this suggestion set
    sugg = sugg[i:]+sugg[:i]

    #Strip ':latest: from the model names
    models = [re.sub(":latest","",a.model) for a in ollama.list()['models']]
    output = "" #HTML output

    #start select block
    output = output + "<select id=\""+name+"\">"
    for mod in sugg: #add in the suggested options
        output = output + "<option value=\""+mod+"\">"+mod+"</option>"
    output = output + "<hr>" #add in a line to separate suggestions from others
    for mod in models: #loop over the full models list
        if not mod in sugg: #if not in the suggestions, add to the block
            output = output + "<option value=\""+mod+"\">"+mod+"</option>"
        else: #otherwise, skip
            pass

    #close the select block and return
    output = output + "</select>"
    return output

def make_panel(prototype):
    #Helper to make the HTML block for a module selection panel
    #   takes a prototype for a module and builds the per-element lists and boxes
    #   from it
    #prototype: {"name":name,"models":models,"prompt":prompt,"inputs":inputs,"guidance":guidance]
    #   models: {modelname:(reqs,N),modelname:(reqs,N),...}
    #   inputs: {input:optional,input:optional,...}

    #Start output with root divs and style formatting for title and prompt
    output = ""
    output = output + "<div style=\"padding:1px;\"><b><u>Module:</u></b> <span id=\"moduleName\" style=\"color:rgba(47, 57, 47, 1);\">"+prototype["name"]+"</span></div>\n"
    output = output + "<div class=\"boxedDiv\" style=\"text-shadow: 0px 0px 1px #FFFF00;\">" + re.sub("(\{[^\{\}]*\})","<span style=\"color:darkgreen;\">\\1</span>",prototype["prompt"]) + "</div>\n"

    #Looping over the models in the prototype
    for modelname in prototype["models"]:
            #make a selector for each model type, for the number of that type needed for execution
            for i in range(prototype["models"][modelname][1]):
                output = output + "<div style=\"padding:1px;\"><i>"+modelname+(" "+str(i))*(prototype["models"][modelname][1]>1)+"</i>: "
                output = output + make_models_list(prototype["models"][modelname][0],modelname+" "+str(i),i) + "</div>\n"

    #For each input in the prototype
    for inp in prototype["inputs"]: #Make an input color based on whether optional
        if prototype["inputs"][inp]:
            color = "blue;"
        else:
            color = "green;"
        if prototype["inputs"][inp]: #set the value for the box if optional
            val = "OPTIONAL"
        else:
            val = ""

        #Build a container for each and insert the label, value, and box
        output = output + "<div class=\"mainContainer\" style=\"padding:1px;\">\n"
        output = output + "<div class=\"lineItem\" style=\"width:15em;color:"+color+"\">"+inp+"</div>\n"
        output = output + "<input type=\"text\" style=\"width:30em;\" id=\""+inp+"\" onkeydown=\"\" value=\""+val+"\"/>\n"
        output = output + "</div>\n"

    #Add the block for advice text, if present
    if "guidance" in prototype:
        for gd in prototype["guidance"]:
            output = output + "<span style=\"color:darkred;\">"+gd+"</span><br>"

    #return the panel block
    return output

def clientCall(data):
    #Tiny utility to send a websocket message to the server and get a reply
    uri = "ws://127.0.0.1:8080"
    with connect(uri) as websocket:
        websocket.send(data)
        resp = websocket.recv()
    return resp

def feedPrint(*strs,is_warn=False):
    #Utility to send a message to be printed in the feed box 
    print(strs) #print to standard IO
    st_o = "" #construct output string
    for s in strs: #add all the strings in the supplied list together
        st_o = st_o + " " + str(s)
    if not(is_warn): #if not a warning, send to feed "&F"
        clientCall("&F"+st_o)
    else: #otherwise send to warning box "&W"
        clientCall("&W"+st_o)
        warnings.warn(st_o) #emit a regular IO warning, too

def panelPrint(panel):
    #Utility to send a module panel for display
    resp = clientCall("&P"+panel)
    print(resp)
    return resp

def inpPrint(*inp):
    #Utility to print an input block to the interaction box
    inp = " ".join(inp)
    print("Input: ","&I"+inp)
    resp = clientCall("&I"+inp)
    return resp

def opPrint(*op):
    #Utility to pring an output block to the interaction box
    op = " ".join(op)
    op = print_prep(op)
    resp = clientCall("&O"+op)
    print("Output: ","&O"+op)
    return resp

def do_warn(txt):
    #Simplified warning wrapper
    resp = feedPrint(txt,is_warn=True)
    return resp

def decodeInput(msg,modules_lookup):
    #Parse an input string message from the server

    entries = msg.split("§") #collect the entries (key,value)
    modVals = {entries[0::2][a]:entries[1::2][a] for a in range(len(entries[0::2]))} #make entries a dict

    #Grab the module name and lookup value
    modName = modVals['name']
    moduleType = modules_lookup[modVals['name']]

    #Looping through the module's inputs, add each into the input dict
    inp_sets = {}
    for inp in moduleType['inputs']:
        inp_sets[inp] = modVals[inp]
        modVals[inp]

    #Grab the system command value
    sysCmd = modVals["SYSTEM"]

    #Return the called module, input, and system command
    return modName,inp_sets,sysCmd

def decodeModule(msg,modules_lookup):
    #Parse a module string from the server

    #Break up the entries and make them a dict
    entries = msg.split("§")
    modVals = {entries[0::2][a]:entries[1::2][a] for a in range(len(entries[0::2]))}
    
    #Grab the module name, 
    modName = modVals['name']
    moduleType = modules_lookup[modVals['name']]
    del modVals['name']

    #Grab each type and number of models used in the module
    mod_collections = [(a,moduleType['models'][a][1]) for a in moduleType['models']]

    #For each type and number pair
    mod_sets = {}
    for cl in mod_collections:
        #create the numerical indexed names for each individual model used
        mods = [modVals[cl[0]+" "+str(a)] for a in range(cl[1])]
        mod_sets[cl[0]] = mods
        for a in range(cl[1]): #remove each type from the list
            del modVals[cl[0]+" "+str(a)]

    #Loop over the inputs, and grab the associated value collected
    inp_sets = {}
    for inp in moduleType['inputs']:
        inp_sets[inp] = modVals[inp]
        modVals[inp]

    #Grab the system command
    sysCmd = modVals["SYSTEM"]
    del modVals["SYSTEM"]

    #Grab any additional parameters attached to the message
    exVals = {}
    for val in modVals:
        if not(val in mod_sets) and not(val in inp_sets) and not(val=="SYSTEM"):
            exVals[val] = modVals[val]

    #Return the module name, sets of models used, inputs, system commands, and extras
    return modName,mod_sets,inp_sets,sysCmd,exVals

def snag_URL(URL):
    #Utility to grab data from a URL

    #Build a request using a browser header (most sites reject without it these days)
    req = urllib.request.Request(URL,data=None, headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"})
    resp = urllib.request.urlopen(req) #open the page and download
    dat = resp.read().decode('utf-8') #read the content

    dat = re.sub("<h(\d).*>(.*)</h\\1>","§\\2§",dat) #parse out headers

    #read HTML to text
    soup = BeautifulSoup(dat,'html.parser')
    txt = soup.getText(separator=' ')

    txt = re.sub("\n\s+\n*","\n",txt) #remove blank space
    txt = re.sub("\n\n*","\n",txt) #remove multilines
    txt = re.sub("§(.*)§","\n\n###\\1§\n\n",txt) #Substitute in ### for section headers

    #Return processed page text
    return txt

def check_if_URL(st):
    #Utility to check if a string is a valid URL

    #Parse the url from urllib
    res = urlparse(st)
    if (res.netloc != ''): #needs a netloc
        if (res.scheme != ''): #and if so, a scheme
            return True,st
        else:
            return True,"https://"+st #if no scheme, still works, needs the scheme added
    else: #otherwise, not a URL
        return False,None

def check_YN(inp):
    #Simple utility that determines if a string expected to say 'yes' or 'no' says yes
    inp = re.sub("[^\w]","",inp)
    return len(re.findall("^y[es]*",re.sub("[^\w]","",inp).lower())) > 0


####
#   LLM Modules
#       These modules implement the actual LLM based systems, adding classical
#       proessing on top of LLM outputs, and implementing feedback controlling
#       and output regularization. Each draws on structured prompts and ordered
#       execution processes to produce reliable outputs. Each module implements
#       a singular task model.
####

class simple_module():
    #Simple modules are a standard parent class for many of the modules, or sub modules
    #   used below. As a skeleton module, they take in a reference prompt with variable
    #   inputs enclosed in {}, which are replaced on execution through an input dict.
    #   They do not preserve memory- one input is fed in, one response out.

    def __init__(self,reference_prompt,_model="driaforall/tiny-agent-a:1.5b",_description="",_system=None):
        #Initialization saves the root model, a description if supplied, any basic system command
        #   and the prompt the module implements. It also saves an output and input history, not
        #   to supply to the LLM, but for diagnostics
        self.model = _model
        self.prompt = reference_prompt
        self.description = _description
        self.is_described = _description != ""
        self.system = _system

        self.op_hist = []
        self.inp_hist = []
        self.times = []

        #Grab the input labels from the prompt
        self.get_input_labels()

    def set_SYSTEM(self,_system):
        #Wrapper function to update the stored system level command
        self.system = _system

    def new_prompt(self,_prompt):
        #Update the prompt with a new one, and new labels
        self.prompt = _prompt
        self.get_input_labels()

    def get_input_labels(self):
        #Parse out the input labels in {}, and store
        self.input_labels = re.findall("[{][\da-zA-Z]*[}]",self.prompt)

    def get_input_str(self,inputs):
        #Craft an input string from the reference prompt and an input dict

        to_prompt = self.prompt+"" #prompt copy
        for inp in self.input_labels: #For each input in the labels for this prompt
            if inp in inputs: #insert the value into the key's location in the prompt
                to_prompt = to_prompt.replace(inp,inputs[inp])
            else: #If you can't find an input for one of the labels, return an error, since the input is wrong
                return False

        #Return the prompt with values filled in
        return to_prompt

    def direct_run(self):
        #An optional run for testing- runs by prompting the user for each input
        inp = {} #input dict to construct
        for tag in self.input_labels: #for each of the labels in the prompt
            get_inp = input("Provide input for "+tag+":") #Ask the user for the value
            inp[tag] = get_inp #load it into the dict

        #Add the input to the history
        self.inp_hist = self.inp_hist  + [inp]
        output = self.run_module(inp) #do the standard run on the manually made input
        self.op_hist = self.op_hist + [output] #add result to output history

        #Return the output
        return output

    def run_module(self,inputs,_verbose=False):
        #Primary run method for the simple module, taking an input dict and converting, then
        #   submitting to the LLM

        #Copy the prompt
        to_prompt = self.prompt+""
        for inp in self.input_labels: #For each label
            if inp in inputs: #Add the input from the dict in place of the label
                to_prompt = to_prompt.replace(inp,inputs[inp])
            else: #if not, return false- missing inputs
                return False

        #If no system command, build the message without any
        if self.system == None:
            msg = [{'role':'user','content':to_prompt}]
        else: #if there is one, add in a system to the msg list
            msg = [{'role':'system','content':self.system},{'role':'user','content':to_prompt}]
        if _verbose: #if verbose, pring the input to the feed
            feedPrint("Asking ",self.model,": ",to_prompt)
        self.inp_hist = self.inp_hist + [msg] #store the input to the history
        t1 = time.time() #track the time to respond
        response = ollama.chat(model=self.model,messages=msg,keep_alive=0) #send the prompt to the LLM
        t2 = time.time()
        output = response['message']['content'] #extract the output

        #Add the output and times to the histories
        self.op_hist = self.op_hist + [output]
        self.times = self.times + [t2-t1]

        #Return the output
        return output

    def make_input_template(self):
        #Helper to build a printable template for input dict
        s_out = "{"
        for I in self.input_labels:
            s_out = s_out + I + ":,"
        s_out = s_out[:-2] + "}"
        return s_out

    def make_description(self):
        #Function to ask the LLM to make a description for this module, if one's not present
        #   and you need one
        if self.is_described == False:
            msg = [{'role':'system','content':self_describe_1+self.prompt+self_describe_2}]
            response = ollama.chat(model=self.model,messages=msg,keep_alive=0)
            self.description = response['message']['content']
            self.is_described = True
        else:
            pass
        return True

class contextListor(simple_module):
    #A submodule which extends the simple module, which finds a set of suggested
    #   article search terms for a supplied question

    def __init__(self,_model=None):
        #Init mainly initializes the parent class with the article source prompt, and checks
        #   if the selected module is suggested or not
        if _model == None: #If no model provided, init with the default
            super().__init__(article_source_prompt_3)
        elif _model in contextListorRecc: #if recommended, init with it
            super().__init__(article_source_prompt_3,_model=_model)
        else: #if not recommended, still init, but push a warning
            do_warn("Using a model not recommended for contextListor- results may be erratic")
            super().__init__(article_source_prompt_3,_model=_model)

    def run(self,question,topic=None):
        #Run method, mainly executes through the parent
        inp = {"{question}":question} #make the input for the search prompt
        if topic != None: #if a topic provided, supply it
            inp["{topic}"] = topic
        else: #if not, feed in the question for it- works better
            inp["{topic}"] = question

        #Run the parent on the input
        res = super().run_module(inp)
        lst = list_output_gatherer(res) #convert the result to a list
        if lst != []: #if it's not empty, return the list
            return lst
        else: #otherwise, return the result itself
            return res

class basicSummarizor(simple_module):
    #A module that runs as both its own module, and as a submodule in a number
    #   of other modules, and serves to take in source text, and summarize it,
    #   or compress it in some cases

    def __init__(self,_model=None):
        #Init by checking supplied module, and submitting warning if not using
        #   a recommended one
        if _model == None:
            super().__init__(summarizor_template)
        elif _model in basicSummarizorRecc:
            super().__init__(summarizor_template,_model=_model)
        else:
            do_warn("Using a model not recommended for basicSummarizor- results may be erratic")
            super().__init__(summarizor_template,_model=_model)

    def run(self,text):
        #Submit to the LLM through the parent method with the input text
        inp = {"{text}":text}
        res = super().run_module(inp)
        res = re.sub("\n\n+","\n",res)
        return res

class mathSolver(simple_module):
    #A module to answer mathematics questions by writing a python script to evaluate the
    #   problem and produce an answer.

    def __init__(self,_model=None):
        #Initialization checks recommended modules, warns if not recommended
        if _model == None:
            super().__init__(math_prompt)
        elif _model in mathSolverRecc:
            super().__init__(math_prompt,_model=_model)
        else:
            do_warn("Using a model not recommended for mathSolver- results may be erratic")
            super().__init__(math_prompt,_model=_model)

    def run(self,problem):
        #This run submits the problem an prompt to the LLM, but also produces as output
        #   (or attempts to produce) the code block that will execute the solution, which
        #   is actually performed later

        #Construct the input and send through the parent to the LLM
        inp = {"{problem}":problem}
        res = super().run_module(inp)

        #Extract out python code from the response
        p_cde = block_extractor(res,"python")
        feedPrint(p_cde) #Send what's extracted to the feed
        if p_cde != None: #If some code block was found
            res = result_finder(problem,p_cde) #Run result finder in code mode
            return res
        else:
            res = result_finder(problem,res,mode="noncode") #If no code, run in noncode mode
            return res

class multiAnswerer:
    #A module that asks multiple LLM models a question, then a supervisor
    #   synthesizes all their answers together into a coherent final response

    def __init__(self,_models=None,_nAIs=3,_supervisor="granite4:350m"):
        #Initialize the internal lists
        self.asks = [] #history of inputs
        self.resps = [] #history of responses
        self.ops = [] #list of outputs
        self.AIs = [] #list of AI modules used

        #Flag for if any of the modules used are not recommended
        TOWARN = False
        if _models != None: #If models supplies
            while len(self.AIs) < max([len(_models),_nAIs]): #While models sill to check
                if not(_models[len(self.AIs)%len(_models)] in multiAnswererRecc): #If the model isn't in the reccomended
                    TOWARN = True #Not a warning is needed
                #Make up a simple module with the ask prompt for the selected model
                AIi = simple_module(multianswer_ask,_model = _models[len(self.AIs)%len(_models)])
                self.AIs = self.AIs + [AIi] #Add that LLM to the list of them
        #If no models supplies
        else:
            cands = [i for i in range(len(multiAnswererRecc))] #make a candidate list of recommended models
            while len(self.AIs) < _nAIs: #While still filling in enough modules
                i = random.randint(0,len(cands)-1) #Grab on of the candidates remaining
                AIi = simple_module(multianswer_ask,_model=multiAnswererRecc[cands[i]]) #make a simple module with the ask prompt
                cands = cands[:i]+cands[i+1:] #Remove the used candidate from the list
                self.AIs = self.AIs + [AIi] #Add the LLM to the list of modules in use
                if len(cands) == 0: #If all candidates used, make a fresh list of them
                    cands = [i for i in range(len(multiAnswererRecc))]

        #If a non recommended model was used
        if TOWARN:
            #Issue a warning about it
            do_warn("Using a multiAnswerer answerer not recommended- results may be erratic")

        #If the supervisor isn't recommended
        if not(_supervisor in multiSuperRecc):
            #Warn about it
            do_warn("Using a multiAnswerer supervisor not recommended- results may be erratic")
        #Set the supervisor to a simple module with the synthesis prompt
        self.supervisor = simple_module(multianswer_prompt,_model=_supervisor)

    def set_SYSTEM(self,_system):
        #wrapper to set the system message for all the LLMs in use
        for ai in self.AIs: #Set for all answerers through their parent method
            ai.set_SYSTEM(_system)
        self.supervisor.set_SYSTEM(_system) #Set supervisor through parent

    def run(self,inp,_verbose):
        #Run by asking all the answerers, then synthesizing a final answer

        #Construct the input for the asker and for the synthesizer
        inp_ask = {"{input}":inp}
        inp_super = {"{number}":str(len(self.AIs)),"{input}":inp,"{responses}":None}

        #Add input to the history
        self.asks = self.asks + [inp]

        #Output and time lists for each answerer
        ops = []
        times = []

        #Looping over each asker
        for AI in self.AIs: 
            t1 = time.time() #Track time to execute
            res = AI.run_module(inp_ask) #Run through parent
            t2 = time.time()
            times = times + [t2-t2] #save time
            ops = ops + [res] #save response
            if _verbose: #Verbose feedback to feed
                feedPrint("  ",AI.model," thought for ",round(t2-t1,1), "seconds")
                feedPrint("    Resp: "," ".join(res.split(" ")[:16])+"...")

        #Save output list to history
        self.ops = self.ops + [ops]

        #Format all outputs together for supply to supervisor
        resps = ""
        for op in ops[:-1]: #Add each output but last one together with spacers
            resps = resps + op + "\n----\n"
        resps = resps + ops[-1] #Add in final output w/0 spacer, since it's last
        inp_super["{responses}"] = resps #Put full response set into the supervisor input

        t1 = time.time() #record this time too
        joint_resp = self.supervisor.run_module(inp_super) #Send synthesis request to supervisor
        t2 = time.time()
        self.resps = self.resps + [joint_resp] #Save full respones

        if _verbose: #Verbose output reporting
            feedPrint("----")
            feedPrint("  ",self.supervisor.model," supervisor thought for ",round(t2-t1,1),"seconds")
            feedPrint("    Resp: ",joint_resp)
            feedPrint("----")

        #Return final full response
        return joint_resp

class debator:
    #A module which takes in a topic and some points about it, and pits two LLMs against one another,
    #   debating the topics from different views, followed by a final overview which integrates
    #   the points they bring against one another into a broad overview

    def __init__(self,_topic,_debators,_moderator="granite4:350m",_points=None):
        #Initialization takes the topic and points if supplied, or tries to generate
        #   points if not or partially supplied

        self.topic = _topic #Save the topic

        #Construct both debators, with opening argument prompt at first
        self.debators = [simple_module(opening_argument,_model=model) for model in _debators]
        self.moderator = simple_module(mod_summarize,_model=_moderator) #Moderator with round summary prompt

        #Full history of the debate
        self.debate_hist = []

        #If points not supplied
        if _points == None or _points == []:
            #Make a temporart module to build points, using moderator model and point generation prompt
            make_pts = simple_module(make_points,_model=_moderator)

            inp = {"{topic}":_topic} #Supply the topic 
            op = make_pts.run_module(inp) #Ask it to make the points
            pts = list_output_gatherer(op) #Extract the points as a list
            if len(pts) > 1: #If at least two points created
                self.points = [pts[0],pts[1]] #Set them as the points
            elif len(pts) == 1: #If only one, it and its converse are the points
                self.points = [pts[0],"The converse of: "+pts[1]]
            else: #Otherwise warn that the points weren't generated, and make them generic.
                do_warn("Failed to autogenerate points.")
                self.points = ["Pro","Con"]
        else: #If points supplied
            if len(_points)>=2: #If at least two, make them the points
                self.points = _points[:2]
            elif len(points) == 1: #If one, it and its converse
                self.points = [_points[0],"The converse of: "+_points[0]]

    def set_SYSTEM(self,_system):
        #Wrapper to set system commands
        for deb in self.debators: #Call each debator through its parent method
            deb.set_SYSTEM(_system)
        self.moderator.set_SYSTEM(_system) #Call moderator with its parent too

    def run(self,n_cycles,_verbose=False):
        #The debate runs through a series of rounds, the first generating opening arguments,
        #   and each after asking each debator to reply to its opponent's prior argument,
        #   using the summary of its own point and the opponent's as input

        #Track execution time
        ti = time.time()
        if _verbose: #Verbose outputs
            feedPrint("Debating the topic: ",self.topic)
            feedPrint()

        #Initial arguments construction for debator one
        inp1 = {"{topic}":self.topic,"{position}":self.points[0]}
        t1 = time.time() #Track time
        pos1arg = self.debators[0].run_module(inp1) #Make first argument
        t2 = time.time()

        self.debate_hist = self.debate_hist + [(self.points[0],pos1arg)] #Add to history

        if _verbose: #Verbose output
            feedPrint("Point: ",self.points[0],round(t2-t1,1))
            feedPrint("    ",pos1arg)
            feedPrint()

        #Make debator two opening argument
        inp2 = {"{topic}":self.topic,"{position}":self.points[1]}
        t3 = time.time()
        pos2arg = self.debators[1].run_module(inp2) #Make first argument
        t4 = time.time()

        #Output debator one and two arguments to interaction box
        inpPrint("<u>Debator One:</u>: <br>"+pos1arg)
        opPrint("<u>Debator Two:</u>: <br>"+pos2arg)

        #Update debate history
        self.debate_hist = self.debate_hist + [(self.points[1],pos2arg)]

        #Reset debators with reply prompts instead of opening argument prompts
        self.debators = [simple_module(reply_argument,_model=deb.model,_system=deb.system) for deb in self.debators]

        if _verbose: #More verbose output
            feedPrint("Point: ",self.points[1],round(t4-t3))
            feedPrint("    ",pos2arg)
            feedPrint("----")

        #Loop to bounce back and forth for the number of rounds
        for rnd in range(n_cycles):
            if _verbose: #Verbose output
                feedPrint("Round "+str(rnd+1)+":")
                feedPrint()

            #Construct reply input for debator one
            inp1 = {"{topic}":self.topic,"{position}":self.points[0],"{yourArgument}":pos1arg,"{theirArgument}":pos2arg}
            t1 = time.time()
            pos1arg = self.debators[0].run_module(inp1) #Get response
            t2 = time.time()

            self.debate_hist = self.debate_hist + [(self.points[0],pos1arg)] #Update history

            #Construct input for debator two
            inp2 = {"{topic}":self.topic,"{position}":self.points[1],"{yourArgument}":pos2arg,"{theirArgument}":pos1arg}
            t3 = time.time()
            pos2arg = self.debators[1].run_module(inp2) #Get response
            t4 = time.time()

            self.debate_hist = self.debate_hist + [(self.points[1],pos2arg)]#Update history

            #Make input for moderator to summarize debator one's points
            inpMod1 = {"{topic}":self.topic,"{point}":pos1arg}
            t5 = time.time()
            pos1arg = self.moderator.run_module(inpMod1) #Get summary
            t6 = time.time()

            #Make input for moderator to summarize debator two's points
            inpMod2 = {"{topic}":self.topic,"{point}":pos2arg}
            t7 = time.time()
            pos2arg = self.moderator.run_module(inpMod2) #Get summary
            t8 = time.time()

            #Output the summary of the dabators' points to interaction box
            inpPrint("<u>Debator One:</u>: <br>"+pos1arg)
            opPrint("<u>Debator Two:</u>: <br>"+pos2arg)

            if _verbose: #Verbose output
                feedPrint("Point: ",self.points[0],round(t2-t1,1),round(t6-t5,1))
                feedPrint("    ",pos1arg)
                feedPrint()

                feedPrint("Point: ",self.points[1],round(t4-t3,1),round(t8-t7,1))
                feedPrint("    ",pos2arg)
                feedPrint("----")

        #When rounds are complete, reset moderator to conclusion building prompt
        self.moderator = simple_module(debate_conclusion,_model=self.moderator.model,_system=self.moderator.system)
        #Build input to moderator around the final points and topic
        concInp = {"{topic}":self.topic,"{pointOne}":self.points[0],"{argOne}":self.points[1],"{pointTwo}":pos1arg,"{argTwo}":pos2arg}

        t1 = time.time()
        res = self.moderator.run_module(concInp) #Get final response
        t2 = time.time()

        tf = time.time() #Track full time

        if _verbose: #Verbose output
            feedPrint("Conclusion: ",round(t2-t1,1),round(tf-ti,1))
            feedPrint("    ",res)
            feedPrint("----")

        #Return the final response
        return res

class referenceSearcher:
    #Module to answer a user quesiton by first identifying some promising article search tags,
    #   pull the text from those searched articles, then identify relevant sections to answer the
    #   question, and finally bring together the set of relevant sections from the pulled articles 
    #   into a final response that answers the question with that collected information

    def __init__(self,_searcher,_models=['granite4:3b','granite4:350m','granite4:350m','driaforall/tiny-agent-a:3b']):
        #Init takes in the four requisite models and a searcher object
        self.models = _models
        self.searcher = _searcher

        #The searcher object must support a method to get suggestions, and to grab reference text
        #   grab must divide it into sections with headings
        if len({'suggestions','grab'}&{a for a in dir(self.searcher)}) != 2:
            #If not, warn the user that this module will fail
            do_warn("searcher object must support '.suggestions' and '.grab' methods- this one is going to break!")

        #Check if using recommended modules
        if len(set(self.models)&set(referenceSearchRecc)) != len(set(self.models)):
            do_warn("Using reference searcher models not recommended- results may be erratic")

        #Construct the four submodules- one to find sources, on to pick relevant sections
        #   one to summarize sections, and one to build the final answer
        self.sourceFinder = simple_module(article_source_prompt,_model=self.models[0])
        self.sectionRelevance = simple_module(relevant_sections,_model=self.models[1])
        self.secSummary = simple_module(sec_summary_prmpt,_model=self.models[2])
        self.finalSummary = simple_module(answer_prmpt,_model=self.models[3])

    def set_SYSTEM(self,_system):
        #Wrapper to set the system commands for all four submodules
        self.sourceFinder.set_SYSTEM(_system)
        self.sectionRelevance.set_SYSTEM(_system)
        self.secSummary.set_SYSTEM(_system)
        self.finalSummary.set_SYSTEM(_system)

    def run(self,question,topic=None,_verbose=False):
        #Run executes the steps outlined above, with an eye towards regularizing the outputs
        #   so that the search, extract, and report components can all work reliably

        #Construct the initial source search input- with the question itself and optional focusing topic
        inp = {"{question}":question}|{"{topic}":topic if (topic != None) else question}

        #First step is to build a list of sources
        src_list = []
        ctx = 0

        #Take at most 3 attempts to get a list of possible sources
        while (src_list == []) and (ctx <3):
            t1 = time.time() #track time
            output = self.sourceFinder.run_module(inp,_verbose=True) #Ask for sources
            t2 = time.time()

            #Convert reply into article sources list
            src_list = list_output_gatherer(output)
            ctx+=1 #increment try counter

        if _verbose: #Verbose output
            feedPrint(t2-t1,"s",output)

        #Try to grab sources from the suggested tags from above
        to_grabs = []
        for src in src_list: #Looping over each possible source
            targets = self.searcher.suggestions(src) #Use the searcher suggestion method to get target texts

            if _verbose: #verbose output
                feedPrint("targets: ",targets)

            if len(targets)>0: #If some options
                to_grabs = to_grabs + [targets[0]] #Use the top suggestion
            else: #Otherwise
                targets = self.searcher.suggestions(src.split(" ")[0]) #Try and grab with the first word
                if len(targets)>0: #If something
                    to_grabs = to_grabs + [targets[0]] #Add first of these suggestions to the grab list
                else: #Otherwise let it go
                    pass

        if _verbose: #verbose output
            feedPrint("to_grabs: ",to_grabs)

        #Once some targets we can grab are found
        arts = [] #List of articles
        found = [] #list of the ones actually pulled, in case of duplicates
        for grab in to_grabs:
            article = self.searcher.grab(grab) #Grab the text for the target

            if article != []: #If actually something there
                if not(article[0][0] in found): #If not already pulled
                    found = found + [article[0][0]] #Add the name to the lookup since we found it
                    art_proc = [] #List of processed text parts
                    for sec in article: #For each section
                        title = BeautifulSoup(sec[0],features="lxml").get_text() #Peel out the text
                        content  = re.sub("\n+","\n",BeautifulSoup(sec[1],features="lxml").get_text()) #Process the text, clear xml and multiline blanks
                        art_proc = art_proc + [(title,content)] #Add the processed section content and title to the article list
                    arts = arts + [art_proc] #Add the processed article to the list of all of them
                else: #Otherwise, pass over a text we already found
                    pass
            else: #other-otherwise, pass over empty texts
                pass

        if _verbose: #Verbose output
            feedPrint("article sections:") #Output the section list
            for a in arts: #Over each article
                feedPrint("  ",a[0][0]) #Output the section title
                for b in a: #For each section, print it out
                    feedPrint("    ",b[0],len(b[1]))

        #Next, we grab the relevant sections from those in the selected articles
        sec_list = [] #List of sections to read
        for art in arts: #For each article

            secs = [a[0] for a in art] #Get the section titles

            #Construct the input for the relevant section checker
            inp = {"{article}":art[0][0],"{sections}":str(secs),"{question}":question}

            if _verbose: #Verbose output
                feedPrint("Getting relevant for: ",art[0][0])

            t1 = time.time() #Record time
            output = self.sectionRelevance.run_module(inp,_verbose=True) #Ask the LLM which sections are relevant
            secs = list_output_gatherer(output) #Convert the sections to a list
            t2 = time.time()

            if _verbose: #Verbose output
                feedPrint(t2-t1,"s  Sections:",secs)

            sec_list = sec_list + [(art[0][0],secs)] #append list of relevant sections with article

        #Build the text to search
        art_text = ""
        i = 0
        for art in arts: #Going through each article
            art_text = art_text + "###Article: "+art[0][0] + "\n" #Add a label and title to the text

            if _verbose: #Verbose output
                feedPrint("Pulling from: ",art[0][0])

            for sec in art: #For each section in this article
                if sec_list[i][1] != []: #if something in the list of sections
                    to_pull = sec_list[i][1]+[art[0][0]] #Grab articles
                else: #otherwise, nothing
                    to_pull = []

                #If the section is one of the relevant ones
                if sec[0] in to_pull:

                    if _verbose: #Verbose ourput
                        feedPrint("    pull section:",art[0][0],":",sec[0])

                    #Make the input for the section summarizer
                    inp = {"{question}":question,"{section}":sec[1]}
                    t1 = time.time() 
                    sec_sum = self.secSummary.run_module(inp) #Get a summarized version of the pulled section
                    t2 = time.time()

                    if _verbose: #Verbose output
                        feedPrint("sec summary: ",round(t2-t1,1))
                        feedPrint(sec_sum)

                    #Add summarized section under section title
                    art_text = art_text + sec[0] + "\n" + sec_sum+"\n"
                else:
                    pass

            #Add a line break between article texts
            art_text = art_text + "\n"
            i+=1

        if _verbose: #Verbose output
            feedPrint("background text: ")
            feedPrint("--------")
            feedPrint(art_text)
            feedPrint("--------")
            feedPrint("Getting answer")

        #Prepare input for the final answer summary of the collected information
        inp = {"{question}":question,"{artText}":art_text}
        t1 = time.time() #Mark time
        output = self.finalSummary.run_module(inp,_verbose=True) #Ask LLM for final answer
        t2 = time.time()

        if _verbose: #Verbose output
            feedPrint(t2-t1,"s","Final answer:")
            feedPrint("--------")
            feedPrint(output)
            feedPrint("--------")

        #Return final answer
        return output

class chatter:
    #This module implements an interactive module, direct chat functionality between the user
    #   and the LLM via the interaction box. To keep the input to the LLM constrained, a 
    #   threshold length of the conversation is compressed into a summary of pertinent points,
    #   with a recent leeway of the conversation retained as-is for continuity

    def __init__(self,_model,_summarizor="granite4:350m",_contextLim=1200,_depth=3):
        #Initialization sets the model, checks if recommended and sets up temporary and full
        #   histories for the conversation and summarization

        self.model = _model #LLM model to chat with

        #Check if using a recommended model, and warn if not
        if not(_model in chatterMainRecc):
            do_warn("Using a non-recommended main chatter- results may be erratic")
        if not(_summarizor in chatterSummRecc):
            do_warn("Using a non-recommended chat summarizor- results may be erratic")        

        #Initialize the summarizer as a simple module with the chat summary prompt
        self.summarizor = simple_module(summary_prompt,_model=_summarizor)
        self.conLim = _contextLim #Set the context limit
        self.depth = _depth #Set the continuity overlap depth

        #Initialize the long term, short term memory
        self.full_history = []
        self.prev_summ = []
        self.current_summary = ''
        self.curr_history = []

        #Set the topic, system summary injection prompt, and system instructions prompt
        self.topic = None
        self.system = chatter_system_general.replace("{summary}",self.current_summary)
        self.system_prmpt = None

    def set_SYSTEM(self,_system):
        #Wrapper to set system commands
        self.summarizor.set_SYSTEM(_system)
        self.system = _system

    def set_topic(self,_topic):
        #Wrapper to set a chat topic
        self.topic = _topic
        self.system_prmpt = chatter_system_topic.replace("{topic}",self.topic)

    def run(self,message,_verbose=False):
        #Primary run serves to monitor the recent history for exceeding the context limit
        #   and make a fresh summary if so, and roll the current history back to the depth
        #   limit if so

        #Make a history string representing the recent history thus far
        hist = "\n".join([h['role']+":\n"+h['content'] for h in self.curr_history])
        if len(hist) >= self.conLim: #If that history is over the context limit

            if _verbose: #Verbose output
                feedPrint("----")
                feedPrint("Summarizing:")

            #Build the input for the summarizer- from current history and summary
            to_summ = "\n### Prior summary:\n" + self.current_summary + "\n ###Conversation:\n" + hist
            summ_inp = {"{conversation}":to_summ}

            self.prev_summ = self.prev_summ + [self.current_summary] #Save new summary

            t1 = time.time() #Mark time
            self.current_summary = self.summarizor.run_module(summ_inp) #Send to summarizer
            t2 = time.time()

            #Update current history to depth limit and update summary prompt
            self.curr_history = self.curr_history[-1*self.depth:]#[]
            self.system = chatter_system_general.replace("{summary}",self.current_summary)

            if _verbose: #Verbose output
                feedPrint("%%%%")
                feedPrint(self.current_summary)
                feedPrint("%%%%")
                feedPrint("----",round(t2-t1,1))

        #Create the next message with the input message
        n_msg = {'role':'user','content':message}
        if self.system_prmpt == None: #If no system prompt
            #Add in just the summary system message with the history and new message
            to_send = [{'role':'system','content':self.system}] + self.curr_history + [n_msg]
        else: #otherwise
            # add in system prompt and summary, plus history and new message
            to_send = [{'role':'system','content':self.system_prmpt+"\n"+self.system}] + self.curr_history + [n_msg]

        #Add new message to current and full history
        self.curr_history = self.curr_history + [n_msg]
        self.full_history = self.full_history + [n_msg]

        t1 = time.time() #Mark time
        response = ollama.chat(model=self.model,messages=to_send,keep_alive=0) #Send current history conversation w/ summary to LLM
        t2 = time.time()

        #Save response to short and long term history
        self.curr_history = self.curr_history + [response['message']]
        self.full_history = self.full_history + [response['message']]

        #Grab output
        output = response['message']['content']

        #Return output from this message
        return output

class textCleaner:
    #A wrapper-adjacent module that cleans markup from text

    def __init__(self,_model="reader-lm:0.5b"):
        #Init only needs the model
        self.model = _model

    def run(self,inp):
        #Run constructs a message with the to-clean text, sends to the LLM, and fetches output to return
        msg = [{'role':'user','content':inp}]
        cleaned = ollama.chat(model=self.model,messages=msg,keep_alive=0)
        inpPrint(msg[-1]['content'])
        return cleaned['message']['content']

class textAnalysis:
    #This module takes as input a text source and processes it at multiple levels to perform a general analysis
    #   of the presented material. It divides the text into segments, summarizes those segments, derives a general
    #   overview from those segments, followed by analyzing the text with a series of questions derived from
    #   several critical thinking checklists. Finally, from there, it applies several groups of further synthesis
    #   questions to further develop on the material, find strengths, weaknesses, context, and paths for further
    #   investigation and analysis

    def __init__(self,_deep="driaforall/tiny-agent-a:3b",_mid="driaforall/tiny-agent-a:1.5b",_shallow="granite4:350m"):
        #The initialization instantiates five modules, to summarize material, extract a thesis, ask questions, analyze
        #   results, and synthesize information. Rather than each have its own model, we specify models for deep, middling
        #   and shallow work, and assign to the modules below appropriate selections based on the presumed cognitive load
        #   associated with its task

        #The summarizor is a shallow task, restating information compactly
        self.summarizor = basicSummarizor(_model=_shallow)

        #The thesis extractor, question asker, and synthesizer are all middling depth tasks, reorganizing, stitching, or
        #   combining prior information or making short logical jumps
        self.thesis_ext = simple_module(topic_extract,_model=_mid)
        self.asker = simple_module(question_asker,_model=_mid)
        self.synthesizer = simple_module(synthesis_prompt,_model=_mid)

        #The analyzer is a deep task, presumed to be making more substantive associations, identifying extrapolative
        #   information, or deriving conclusions from data
        self.analyzer = basicSummarizor(_model=_deep)


    def set_SYSTEM(self,_system):
        #Wrapper to set system level instructions for all the modules
        self.summarizor.set_SYSTEM(_system)
        self.thesis_ext.set_SYSTEM(_system)
        self.asker.set_SYSTEM(_system)
        self.analyzer.set_SYSTEM(_system)
        self.synthesizer.set_SYSTEM(_system)

    def run(self,text,_verbose=False):
        #Run iterates over the document to prepare the partial and full summaries, from which the additional
        #   questions are applied to the sub texts and then integrated into synthesis information, from the
        #   set of questions defined in the prototype definition

        #List of execution times for monitoring
        run_times = []

        #Split the text by multilines, replacing all places of 2 or more \n with §
        t_split = re.sub("\n\n+","§",text)
        t_split = t_split.split("§") #Then splitting by all §

        #Run through each segment from above and summarize it
        sum_segs = []
        for seg in t_split: #Looping over each segment

            #Ignore only whitespace segments
            if len(re.findall("\S",seg)) > 0:

                if _verbose: #Verbose output
                    feedPrint("Summarizing: "," ".join(seg.split(" ")[:12])+"...")

                #If more than 25 words:
                if len(seg.split(" ")) > 25:
                    t1 = time.time() #Mark time
                    summ = self.summarizor.run(seg) #Summarize the segment
                    t2 = time.time()
                    run_times = run_times + [t2-t1] #Note runtimes
                    sum_segs = sum_segs + [summ] #Save the segment summary
                else: #Otherwise, direct include
                    sum_segs = sum_segs + [seg] #Save the segment
            else:
                pass

        #Make a more concise version of the text from the segment summary
        concise_text = "\n".join(sum_segs)
        concise_text_pret = "\n\n".join(sum_segs) #A more easily readable pretty version

        if _verbose: #Verbose output
            feedPrint("Report:") #Report title header
            feedPrint("********")

            feedPrint("Concise text:") #Concise text block
            feedPrint("----")
            feedPrint(concise_text)
            feedPrint("----")

            feedPrint("Joint Summary:") #Summary of full text

        #Summarize the concise text to get a full-text overview
        t1 = time.time()
        full_summ = self.analyzer.run(concise_text)
        t2 = time.time()
        run_times = run_times + [t2-t1]

        if _verbose: #Verbose output
            feedPrint("    ",full_summ,round(t2-t1,1))
            feedPrint("----")

            feedPrint("Thesis:")

        #Extract the thesis of the text from the full summary
        inp = {"{text}":full_summ}
        t1 = time.time()
        thesis = self.thesis_ext.run_module(inp)
        t2 = time.time()
        run_times = run_times + [t2-t1]

        if _verbose: #Verbose output
            feedPrint("    ",thesis,round(t2-t1,1))
            feedPrint("----")
            feedPrint("Questions:")

        #Run the analysis section by going through each prompt question
        answers = {}
        for Q in analysis_questions: #For each question

            if _verbose: #Verbose output for the question
                feedPrint(Q,":")

            #Build the input for each question to ask
            inp = {"{text}":full_summ,"{question}":Q}
            t1 = time.time()
            Ans = self.asker.run_module(inp) #Ask that question
            t2 = time.time()
            run_times = run_times + [t2-t1]
            answers[Q] = Ans #Save the answer to that question

            if _verbose: #Verbose output for each answer
                feedPrint("    ",Ans,round(t2-t1,1))
                feedPrint("--")

        if _verbose: #Verbose output
            feedPrint("----")
            feedPrint("Synthesis:")

        #Run the synthesis section much the same as the analysis, but also with reference to the
        #   extracted thesis along with the synthesis question, and joining source text from the
        #   relevant prior analysis questions
        synthesis_pts = {}
        for p in synthesis_inps: #For each synthesis question

            if _verbose: #Verbose output
                feedPrint(p[1])

            #Grab the answeres from the relevant questions in the analysis section
            As = [answers[q] for q in p[0]]
            txt = "\n".join(As) #Join the answers into the source text
            inp = {"{text}":txt,"{topic}":thesis,"{question}":p[1]} #Built input for synthesis module
            t1 = time.time()
            p_out = self.synthesizer.run_module(inp) #Get the synthesis output
            t2 = time.time()
            run_times = run_times + [t2-t1]
            synthesis_pts[p[1]] = p_out #Save the result

            if _verbose: #Verbose output for synthesis point
                feedPrint("    ",p_out,round(t2-t1,1))
                feedPrint("----")

        #Return the compressed text, full summary, thesis, analysis answers, thesis points, and run time
        return concise_text_pret,full_summ,thesis,answers,synthesis_pts,run_times

class refiner:
    # This module is interactive, taking a source statement and iteratively trying to improve it based
    #   on user feedback, prompting for approval or disapproval, and proceeding anew with each approved
    #   revision to further edits

    def __init__(self,_context,_statement,_model='driaforall/tiny-agent-a:3b'):
        #Initialization notes the model, supplied context, and initial statement
        self.model = _model
        self.context = _context
        self.statement = _statement #Will change as edits are made!

        self.n_statement = None #New statement, during approval steps

        self.msgs = [] #History of messages
        self.refiner = simple_module(refine_statement,_model=self.model) #Simple module with refine prompt
        self.chk_state = 0 #Toggle state for edit/approval stages

    def set_SYSTEM(self,_system):
        #Wrapper to set the system message for the simple module
        self.refiner.set_SYSTEM(_system)

    def run(self,feedback,_verbose=False):
        #Run toggles between editing and approving stages, prompting the user at each stage
        #   and updating the working statement if so, and not otherwise

        if self.chk_state == 0:
            #In the refinement phase

            inp = {"{statement}":self.statement,"{feedback}":feedback} #Prepare input for module
            inpPrint("<u>Feedback</u>:<br>"+feedback) #print feedback to input side of interaction block
            self.n_statement = self.refiner.run_module(inp,_verbose=_verbose) #run the refiner module with the feedback

            #Ask about the revised version on the output side of the interaction block
            opPrint("Is <br><span style=\"color:green;\"><i>"+self.n_statement+"</i></span><br> better than the previous iteration?")
            self.chk_state = 1 #Toggle to approval stage

        elif self.chk_state == 1:
            #In the approval state

            if check_YN(feedback): #Check if the input is some version of 'yes'
                inpPrint("<span style=\"color:green;\">Accepted revisions-</span>") #Note acceptance
                self.statement = self.n_statement #Update the working statement to the new ont
                self.n_statement = None #Clear the new statement

                #Prompt for feedpack on the new statement
                q = "What is your feedback on the " + self.context + ":<br><span style=\"color:green;\"><i>" + self.statement + "</i></span>"
            else: #Otherwise
                inpPrint("<span style=\"color:red;\">Rejected Revisions-</span>") #Note rejection
                #Prompt for alternartive feedback
                q = "Provide alternative feedback on the " + self.context + ":<br><span style=\"color:green;\"><i>" + self.statement + "</i></span>?"

            #Print whichever user prompt was made to the output side of the interaction block
            opPrint(q)
            self.chk_state = 0 #Toggle to refinement state

        #Return the final state
        return self.statement


###
#   Primary execution loop
#       Runs the loop, checking with the server for module and input updates,
#       and submits panel and response output to the UI page. 
###

#List of the installed modules for checking
modules = [basicSummarizorPrototype,
            mathSolverPrototype,
            multiAnswererPrototype,
            referenceSearchPrototype,
            chatterPrototype,
            debatorPrototype,
            textAnalysisPrototype,
            refinerPrototype,
            ]
modules_lookup = {mod['name']:mod for mod in modules} #Build a name lookup for checking modules

#Main run block
if __name__ == '__main__':

    #On startup, send an '&R' to clear the server cache
    clientCall("&R")
    time.sleep(0.5) #A brief wait for the reset
    clientCall("&S"+make_modules_list(modules)) #Send call to make the module list in UI
    feedPrint("WARNINGS",is_warn=True) #Start up warnings
    feedPrint("OUTPUT FEED",is_warn=False) #Start up feed

    #Initialize current module empty
    currentModule = None

    #Execution time mark
    tme = time.time()
    while True:
        #Run indefinitely

        #Run the poll intermittently
        if time.time()-tme > 0.5:

            #Make an update call every time
            resp = clientCall("&U")

            #If there's a select call, grab the module prototype and send the new panel
            if resp[0] == "S":
                module = modules_lookup[resp[1:]]
                panelPrint(make_panel(module))

            #For a reset call
            elif resp[0] == "R":
                clientCall("&R") #clear the server cache
                time.sleep(0.5) #wait to let the clear go through
                clientCall("&S"+make_modules_list(modules)) #Send a select refresh with modules list
                feedPrint("WARNINGS",is_warn=True) #Reset warnings
                feedPrint("OUTPUT FEED",is_warn=False) #Reset feed

            #For a modules call
            elif resp[0] == "M":

                #Decode the values from the message
                mod_type,mod_sets,inp_sets,sysCmd,exVals = decodeModule(resp[1:],modules_lookup)

                inpPrint("<hr>") #Send separator for new inputs in interaction box
                opPrint("<hr>") #Send separator for new outputs in interaction box

                #Diagnostic outputs on this side
                print()
                print("New Model:",mod_type)
                print(mod_sets)
                print(inp_sets)
                print(sysCmd)
                print(exVals)

                #If asking for the summarizor
                if mod_type == "basicSummarizor":
                    #Just set model to be a summarizor
                    currentModule = basicSummarizor(_model = mod_sets["model"][0])

                #If asking for the math solver
                elif mod_type == "mathSolver":
                    #Just set current module to math solver
                    currentModule = mathSolver(_model = mod_sets["model"][0])

                #If asking for the multi answer
                elif mod_type == "multiAnswer":
                    #Just set the current module to the multi answer
                    currentModule = multiAnswerer(_models = mod_sets["models"],_supervisor=mod_sets["supervisor"][0])

                #If asking for the reference searcher
                elif mod_type == "referenceSearcher":

                    #Load in a zim archive
                    zms = glob.glob("../*.zim")+glob.glob("*.zim")

                    #if an archive found
                    if zms != []:
                        #Make the archive object
                        arc = archive(zms[0])
                        #Set the current module with the archive
                        currentModule = referenceSearcher(_searcher=arc,_models = [mod_sets["sourceFinder"][0],mod_sets["relevanceChecker"][0],mod_sets["sectionSummary"][0],mod_sets["finalSummary"][0]])
                    else:
                        #If not, print out to warning no archive, and issue a warning
                        currentModule = None
                        feedPrint("No available archive to search",is_warn=True)

                #If asking for the chatter
                elif mod_type == "chatter":
                    #Set the current module to the chatter
                    currentModule = chatter(_model=mod_sets["model"][0],_summarizor=mod_sets["summarizer"][0])

                #If asking for the debator
                elif mod_type == "debator":

                    #Check the debate points, and build setup as needed
                    if (inp_sets["{pointOne}"] in ["","OPTIONAL"]) and (inp_sets["{pointTwo}"] in ["","OPTIONAL"]):
                        #If no points, supply 'None'
                        currentModule = debator(_topic=inp_sets["{topic}"],_debators=mod_sets['debators'],_moderator=mod_sets['moderator'][0],_points=None)
                    elif (inp_sets["{pointOne}"] in ["","OPTIONAL"]) and not(inp_sets["{pointTwo}"] in ["","OPTIONAL"]):
                        #If only point two, add it as the sole point
                        currentModule = debator(_topic=inp_sets["{topic}"],_debators=mod_sets['debators'],_moderator=mod_sets['moderator'][0],_points=[inp_sets["{pointTwo}"]])
                    elif not(inp_sets["{pointOne}"] in ["","OPTIONAL"]) and (inp_sets["{pointTwo}"] in ["","OPTIONAL"]):
                        #Same for point one
                        currentModule = debator(_topic=inp_sets["{topic}"],_debators=mod_sets['debators'],_moderator=mod_sets['moderator'][0],_points=[inp_sets["{pointOne}"]])
                    else:
                        #Supply both points if both supplied!
                        currentModule = debator(_topic=inp_sets["{topic}"],_debators=mod_sets['debators'],_moderator=mod_sets['moderator'][0],_points=[inp_sets["{pointOne}"],inp_sets["{pointTwo}"]])

                #If asking for the text analyzer
                elif mod_type == "textAnalyzer":
                    #Just set the current module to the analyzer
                    currentModule = textAnalysis(_deep=mod_sets['deep'][0],_mid=mod_sets['mid'][0],_shallow=mod_sets['shallow'][0])

                #If asking for the refiner
                elif mod_type == "refiner":
                    #Assign the current module to the refiner
                    currentModule = refiner(inp_sets["{context}"],inp_sets["{statement}"],_model=mod_sets["model"][0])
                    #Build the initial question for the user
                    q = "What is your feedback on the " + currentModule.context + ":<br><span style=\"color:green;\"><i>" + currentModule.statement + "</i></span>"
                    inpPrint("") #Blank newline, starting from LLM side output
                    opPrint(q) #Print the question

                #If no system command
                if sysCmd != "":
                    #Each module needs a set_SYSTEM method, call it here
                    currentModule.set_SYSTEM(sysCmd)
                else:
                    currentModule.set_SYSTEM(None) #If nothing, send None

            #For an input call
            elif resp[0] == "I":

                #Decode the input supplied
                mod_type,inp_sets,sysCmd = decodeInput(resp[1:],modules_lookup)

                if sysCmd != "": #If a system command supplied
                    currentModule.set_SYSTEM(sysCmd) #send the new system command to the module
                else:
                    currentModule.set_SYSTEM(None) #if nothing, set to None

                #If working with a basic summarizer
                if mod_type == "basicSummarizor":

                    #Check if the source is a URL
                    isURL,URL = check_if_URL(inp_sets["{text}"])

                    #If it is a URL
                    if isURL:
                        #Grab the actual site contents for processing
                        txt = snag_URL(URL)
                        txt = txt.split("###") #Split around annotated section breaks
                        inpPrint("<u>Summarizing Webpage:</u> <br>"+URL) #Print activity log
                        summs = [] #list of summaries
                        for tx in txt: #Looping over each section
                            inpPrint("Section: "+tx.split("§")[0]) #Print section title
                            feedPrint(tx) #print section text
                            res = currentModule.run(tx) #Run summary on text
                            opPrint(print_prep(res)) #Print results to feed
                            summs = summs + [res] #save output in summary list
                        summ = "\n\n".join(summs) #combine section summaries
                        inpPrint("<u>Final Summary:</u> ")
                        res = currentModule.run(summ) #Summarize full text
                        opPrint(print_prep(res)) #Output final summary

                    #Check if a file descriptor in the text
                    elif inp_sets["{text}"].split("://")[0] == "file":
                        #If so, it's a drag and drop file
                        f = re.sub("%20"," ",inp_sets["{text}"][7:]) #Replace URL spaces note with actual spaces and extract path
                        txt = inp_sets["{text}"] #Start with text as contents of file string
                        is_found = False #Flag if we found something
                        try: #Try to open the file and read
                            if f.split(".")[-1] != 'pdf': #if it's not a pdf
                                fl = open(f,'r') #Open the file
                                txt = fl.read(-1) #Read everything
                                fl.close() #close the file
                            else: #If it is a pdf, special read
                                doc = pymupdf.open(f) #Open the pdf
                                txt = "" #reset text
                                for page in doc: #read by page
                                    text = page.get_text() #get the text
                                    txt = txt + text + "\n" #Add to full text
                            is_found = True #If try works, we found something
                        except: #If the read didn't work
                            feedPrint("Could not read file:"+inp_sets["{text}"],is_warn=True) #Warn the file couldn't be opened

                        #If some text was found
                        if is_found:
                            inpPrint("<u>Summarizing document:</u> <br>"+f) #Activity log
                            txt = re.sub("\n\n+","\n\n",txt) #remove multiline blanks
                            txt = txt.split("\n\n") #split by double newlines
                            summs = [] #list of summaries
                            for tx in txt: #for each segment
                                inpPrint(" ".join(tx.split(" ")[:15])) #Print a bit of the text to interaction box
                                feedPrint(tx)  #print text to feed
                                res = currentModule.run(tx) #Run summary on the segment
                                opPrint(print_prep(res)) #Output result
                                summs = summs + [res] #Add summary to list
                            summ = "\n\n".join(summs) #Join the summaries together
                            inpPrint("<u>Final Summary:</u> ")
                            res = currentModule.run(summ) #get full summary
                            opPrint(print_prep(res)) #Output full summary
                        else: #If nothing found
                            inpPrint("File-like object not read.") #Note that there's nothing
                            opPrint("Remove \'file://\' to analyze a string as-is") #Give advice about location versus rawtext

                    #If not supplied a file or URL, it's raw text
                    else:
                        inpPrint("<u>Summarizing:</u> <br>"+" ".join(inp_sets["{text}"].split(" ")[:15])+"...") #Activity log
                        res = currentModule.run(inp_sets["{text}"]) #Run summary on text
                        opPrint(print_prep(res)) #output results

                #If solving a math problem
                elif mod_type == "mathSolver":

                    #Print the problem to the input side of the interaction block
                    inpPrint("<u>Math problem:</u> <br>",inp_sets["{problem}"])

                    #Grab the problem to solve, and get the output
                    op = currentModule.run(inp_sets["{problem}"])
                    op_timeproof = timeproof_code(op,inp_sets["{problem}"],t_max=5.0) #Then add the time proofing to the output code

                    try: #Try to execute the produced code
                        exec(op_timeproof)
                    except: #If not, note that the execution failed to the output block
                        opPrint("<b>exec FAILED</b>")

                    if RES_OUT == None: #If a result was not generated
                        opPrint("    RESULT:",str(RES_OUT)) #Print out that 'None'
                    elif type(RES_OUT) in [str,float]: #If there is a result that's a string or a float
                        try:
                            float(RES_OUT) #Try to make it a float
                        except: #if it doesn't work
                            RES_OUT = re.findall("\d+",RES_OUT)[-1] #Go looking for all digits
                        opPrint("    RESULT:",str(RES_OUT)) #output whatever's extracted above
                    elif RES_OUT.bit_count() < 60000: #If the bitcount isn't extreme
                        opPrint("    RESULT:",str(RES_OUT)) #output it
                    else: #If it is too long
                        do_warn("RES_OUT too long! Probably a bad loop.") #Report that- probably an overrunning loop timed out
                        RES_OUT = np.inf*(-1)**(1*(RES_OUT<0)) # Make output infinity
                        opPrint("    RESULT:",str(RES_OUT)) #Output that

                    RES_OUT = None #Clear the result 

                #If asking for a multianswer reply
                elif mod_type == "multiAnswer":
                    inpPrint("<u>MultiAnswer:</u> <br>",inp_sets["{input}"]) #Construct the input
                    res = currentModule.run(inp_sets["{input}"],True) #Ask the LLM
                    opPrint(print_prep(res)) #Report it!

                #If asking for a reference search and review
                elif mod_type == "referenceSearcher":
                    inpPrint("<u>Researching:</u> <br>",inp_sets["{question}"]) #Print the search to the input side of interaction block
                    if inp_sets["{topic}"] in ["","OPTIONAL"]: #If there's not a guiding topic provided
                        res = currentModule.run(inp_sets["{question}"]) #Run without the 
                        opPrint(print_prep(res)) #Output the result to the output side of the block
                    else: #If there is a guiding topic
                        #Run the reference search with a topic
                        res = currentModule.run(inp_sets["{question}"],topic=inp_sets["{topic}"],_verbose=True)
                        opPrint(print_prep(res)) #Output result to the output side of the block

                #If talking to the chatter module
                elif mod_type == "chatter":
                    inpPrint(inp_sets["{message}"]) #Print the user message to the input side of the interaction block
                    res = currentModule.run(inp_sets["{message}"],_verbose=True) #talk to the LLM
                    opPrint(print_prep(res)) #Output the response to the output block

                #If prompting the debator
                elif mod_type == "debator":
                    inpPrint("Debating Topic:") #Put out the topic on the input block
                    opPrint(inp_sets["{topic}"]) #Put the topic on the output block

                    #Try interpreting the number of rounds
                    try:
                        n_cycles = int(inp_sets["rounds"])
                    except: #If not, warn and set to the default of 3 rounds
                        feedPrint("Cannot convert cycles to int- using 3",is_warn=True)
                        n_cycles = 3

                    #Run the debator module on the number of cycles selected
                    res = currentModule.run(n_cycles,_verbose=True)
                    inpPrint("Final Summary:") #Output the note for the final summary on the input side
                    opPrint(print_prep(res)) #Output the final result to the output side

                #If running the text analysis module
                elif mod_type == "textAnalyzer":

                    #Check if the supplied 'text' is a URL
                    isURL,URL = check_if_URL(inp_sets["{text}"])

                    if isURL: #If it is a URL
                        txt = snag_URL(URL) #Grab the page text
                        txt = txt.split("###") #Split around the section marker

                        #Print to the input block what page you're analyzing
                        inpPrint("<u>Analyzing Webpage:</u> <br>"+URL)

                        #Run the text analyzer on the pulled text
                        ctxt,fsum,thes,ans,syn,run_times = currentModule.run("\n\n".join(txt),_verbose=True)

                        #Convert the text to an HTML output
                        html_res = make_analysis_report("analysis_report.txt",ctxt,fsum,thes,ans,syn,_writeOut=False)

                        #Print the HTML-ized result to the output block
                        opPrint(html_res)

                    #If instead has a file marker
                    elif inp_sets["{text}"].split("://")[0] == "file":
                        f = re.sub("%20"," ",inp_sets["{text}"][7:]) #Pull out the file location and replace URL spaces with real ones
                        txt = inp_sets["{text}"] #grab the file string as default text, just in case
                        is_found = False #flag if the file is found properly
                        try: #Try to extract the file text
                            if f.split(".")[-1] != 'pdf': #If not a PDF
                                fl = open(f,'r') #Open the file
                                txt = fl.read(-1) #Read everything
                                fl.close() #close the file
                                txt = re.sub("\n\n+","\n",txt) #Remove all multiline blanks
                                txt = re.sub("\n","\n\n",txt) #Set all single lines to doubles
                            else: #If a PDF, special extraction
                                doc = pymupdf.open(f) #Open the PDF
                                txt = "" #Set text to nothing
                                for page in doc: #over each page
                                    text = page.get_text() #Get the page text
                                    txt = txt + text + "\n" #Append page text to full text with space
                            is_found = True #Mark found if something extracted
                        except: #If nothing extracted
                            #Warn that no file could be read
                            feedPrint("Could not read file:"+inp_sets["{text}"],is_warn=True)
                        if is_found: #If you find some text
                            #Note you're analyzing the file to the input block
                            inpPrint("<u>Analyzing document:</u> <br>"+f)

                            #Run the analyzer on the text and make to HTML
                            ctxt,fsum,thes,ans,syn,run_times = currentModule.run(txt,_verbose=True)
                            html_res = make_analysis_report(f.split("/")[-1]+"_report.txt",ctxt,fsum,thes,ans,syn,_writeOut=True)

                            #Output the HTML to the output block
                            opPrint(html_res)
                        else: #Otherwise
                            #Note that no object could be read and output suggestion about reading the file as text
                            inpPrint("File-like object not read.")
                            opPrint("Remove \'file://\' to analyze a string as-is")
                    else: #If not a file or webpage, direct text pasted in
                        #Print analysis note and a bit of text from it
                        inpPrint("<u>Analyzing:</u> <br>"+" ".join(inp_sets["{text}"].split(" ")[:55])+"...")

                        #Run the analyzer on the text and make to HTML
                        ctxt,fsum,thes,ans,syn,run_times = currentModule.run(inp_sets["{text}"],_verbose=True)
                        html_res = make_analysis_report("analysis_report.txt",ctxt,fsum,thes,ans,syn,_writeOut=True)

                        #Output results to output block
                        opPrint(html_res)

                #If running the refiner
                elif mod_type == "refiner":
                    #Print the feedback to the feed
                    feedPrint(inp_sets["{feedback}"])

                    #Run the module on the feedback supplied
                    res = currentModule.run(inp_sets["{feedback}"])

                    #Print the results to the feed
                    feedPrint(res)

            #Otherwise
            else:
                pass #Do nothing

            #Track the time
            tme = time.time()

###
# Testing segments
#   The snips below implement stand-alone tests for the different modules defined above, using locally defined
#   test cases, or those defined in the core prompts package.
###

# Test the text analysis module
'''
if __name__ == '__main__':

    fname = "test_text_1.txt"
    f = open(fname,'r')
    text = "".join(f.readlines())
    f.close()

    lis = textAnalysis()
    ctxt,fsum,thes,ans,syn,run_times = lis.run(text,_verbose=True)
    print(sum(run_times))

    html_out = make_analysis_report(fname,ctxt,fsum,thes,ans,syn,_writeOut=True)
'''

# Test the chatter module
'''
if __name__ == '__main__':

    #lis = chatter("driaforall/tiny-agent-a:0.5b",_summarizor="driaforall/tiny-agent-a:0.5b")
    lis = chatter("llama3.2")

    RUN = True
    while RUN:
        inp = input(">:")
        if (inp == "X"):
            RUN = False
        else:
            rep,tme = lis.run(inp)
            print("    ",rep,tme)
'''

# Test the reference searcher
'''
if __name__ == '__main__':

    zms = glob.glob("../*.zim")+glob.glob("*.zim")
    arc = archive(zms[0])

    lis = referenceSearcher(arc)
    lis.run(Tsearch2)
'''

# Test the debate module
'''
if __name__ == '__main__':

    topic = "Predestination"
    debators = ["granite4:1b","driaforall/tiny-agent-a:1.5b"]#["qwen3","llama3.2"]
    mod = "granite4:350m"

    #pts = ["Predestination is not scripturally supported","Predestination is established in the Bible."]

    deb = debator(topic,debators,_moderator=mod,_points=None)
    deb = debator(topic,debators,_moderator=mod,_points=pts)

    deb.run(3,_verbose=True)
'''

#Test multiple models on answering questions
'''
if __name__ == '__main__':

    for model in quick_testers:
        lis = simple_module(multianswer_ask,_model=model)

        print(model)

        for Q in [multiQ1,multiQ2,multiQ3]:
            print("  ",Q)
            for i in range(3):
                inp = {'{input}':Q}
                t1 = time.time()
                op = lis.run_module(inp)
                t2 = time.time()
                print("    ",round(t2-t1,1)," ".join(op.split(" ")[:12])[:50].replace("\n","")+"...")
        print("----")
'''

#Test the multianswer
'''
if __name__ == '__main__':

    outputs = {}

    for model in multiSuperRecc:

        print(model)
        print(" ")

        outputs[model] = []

        for Q in [multiQ1,multiQ2,multiQ3]:
            print("Input: ",Q)
            print(" ")

            for i in range(1):

                lis = multiAnswerer(_supervisor=model)

                t1 = time.time()
                op = lis.run(Q)
                t2 = time.time()

                outputs[model] = outputs[model] + [(Q,lis.ops,lis.resps)]

        print("--------")
        print(" ")
'''


#Test the context listor, basic summarizer, or math solver
'''
if __name__ == '__main__':

    outputs = {}

    for model in slow_testers:#quick_testers:
        print(model)
        print(" ")

        #lis = contextListor(_model=model)
        #lis = basicSummarizor(_model=model)
        lis = mathSolver(_model=model)

        outputs[model] = []

        for i in range(3):
            t1 = time.time()
            op = lis.run(mathProblem1)
            t2 = time.time()

            outputs[model] = outputs[model] + [lis.op_hist[-1]]

            print("    ----")
            print("    ",op.split("\n")[-1])

            op_timeproof = timeproof_code(op,mathProblem1,t_max=5.0)
            try:
                exec(op_timeproof)
            except:
                print("    exec FAILED")

            if RES_OUT == None:
                print("    RESULT:",RES_OUT,round(t2-t1,1))
            elif type(RES_OUT) in [str,float]:
                try:
                    float(RES_OUT)
                except:
                    RES_OUT = re.findall("\d+",RES_OUT)[-1]
                print("    RESULT:",RES_OUT,round(t2-t1,1))
            elif RES_OUT.bit_count() < 60000:
                print("    RESULT:",RES_OUT,round(t2-t1,1))
            else:
                do_warn("RES_OUT too long! Probably a bad loop.")
                RES_OUT = np.inf*(-1)**(1*(RES_OUT<0))
                print("    RESULT:",RES_OUT,round(t2-t1,1))

            RES_OUT = None
                
        print("----")
        print(" ")
'''

