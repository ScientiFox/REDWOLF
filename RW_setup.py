####
#
# Script to setup REDWOLF from Python install only
#
####

import re,time,glob
import REDWOLF_core_prompts
import urllib.request
import subprocess

#Get library requirements
print("Installing requirements")
chk_opt = subprocess.check_output(["pip", "install", "-r", "requirements.txt"])
for ln in str(chk_opt).split("\\n"):
    print(ln)

#Grab reccomended LLMs
toGet = set()
var = vars(REDWOLF_core_prompts).copy()

for a in var:
    if 'Recc' in a:
        for b in var[a]:
            toGet.add(b)

import ollama
for md in toGet:
    print("getting:",md)
    try:
        ollama.pull(md)
    except:
        print("  could not pull: ",md)

#Check for ZIMs and suggest download- they're big so don't assume the user
#   is cool with you picking which!
ZIM_site = "https://dumps.wikimedia.org/kiwix/zim/wikipedia/"
has_ZIM = False #len(glob.glob("*.zim")) > 0

if not(has_ZIM):
    req = urllib.request.Request("https://dumps.wikimedia.org/kiwix/zim/wikipedia/")
    resp = urllib.request.urlopen(req)
    dat = resp.read().decode('utf-8')
    lnks = re.findall("<a href=\"wikipedia_en_all.*\n",dat)

    print("No ZIM file found for Reference Searcher!")
    print("We recommend downloading one of these full archives, ideally the no pictures version:")
    for ln in lnks:
        st = re.findall(">(.*)<",ln)[0]
        sz = int(re.findall("(\d+)\r",ln)[-1])
        if sz >= 1000000000:
            sz = round(sz/1000000000,1)
            sz = str(sz)+" Gb"
        elif sz > 1000000:
            sz = round(sz/1000000,1)
            sz = str(sz)+" Mb"
        else:
            sz = round(sz/1000,1)
            sz = str(sz)+" kb"
        print("    ",st,sz)

    inp = input("Open wiki downloads page? [y/n]")
    if inp in ['y','Y','yes','Yes']:
        print("Remember to download it into the REDWOLF directory!")
        time.sleep(1.5)
        import webbrowser
        webbrowser.open(ZIM_site)
        input("done?")
    else:
        print("Just remember the reference searcher won't work!")

import nltk

#Grab the nltk corpus we need
nltk.download("wordnet31")
nltk.download("vader_lexicon")
nltk.download('subjectivity')

#All done!
print("Done!")
