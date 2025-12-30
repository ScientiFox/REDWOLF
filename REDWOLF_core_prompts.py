####
#   Core prompts for REDWOLF workers, along with module prototypes and some material for testing
#       as well as lists of modules for various uses
#
#       Each module has a prototype which defines the prompts used by the module, any component 
#       texts which are used in the processing, lists of modules recommended for each submodule,
#       Guidance text for printing on the panel, and the inputs to be provided.
#
####

###
# General purpose prompts, not restricted to any single module
###

#Simple module self-describe prompt
self_describe = "You are an LLM-based software module which operates by responding to the prompt: {prompt}, where terms enclosed in {} are abstract markers to be filled with concrete subject matter in operation. Succinctly describe your intended functionality."

###
# General Model Lists
###

###
# Fast models
#   These modles are small, and run quickly, with varying levels of accuracy
###

quick_testers = ["driaforall/tiny-agent-a:0.5b",
                        "driaforall/tiny-agent-a:1.5b",
                        "driaforall/tiny-agent-a:3b",
                        "granite4:1b",
                        "granite4:3b",
                        "granite4:350m",
                        "driatasker",
                        "tinyllama",
                        "smollm:135m", #kind of dangerous- overruns badly? Might be experimental, though.
                        "smollm:360m", #All the smollm need mods to increase rep penalty and cap output
                        "smollm",
                        "minicpm-v",
                        "nemotron-mini",
                        "stablelm2",
                        "tinydolphin",
                        "orca-mini",
    ]

###
# Slow Models
#   These models are larger and slower, but generally more sophisticated and accurate
###

slow_testers = ["qwen3",
                "openchat",
                "phi3.5",
                "zephyr",
                "phi",
                "llama2-uncensored",
                "qwen2.5",
                "llama3.2"
    ]

###
# Context Listor Assets
#   The context listor grabs article title search tags for the reference searcher
###
article_source_prompt = '''
For the topic "{topic}", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "{question}". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }
'''
article_source_prompt_3 = '''
Reply in the following template with three simple topic tags which may be used to search for information to answer the question: "{question}". Reply with no other content but the filled template. Supply only a list of tags in the 'tags' field.
### Template {"Tags":[] }'''

#This module works best with middle-size fast modules, the bigger ones extemporize too much, plus
#   it's a tasker type module, so it should be quick and concise anyway
contextListorRecc = ["driatasker",   
                        "driaforall/tiny-agent-a:1.5b",
                        "driaforall/tiny-agent-a:0.5b",
                        "driaforall/tiny-agent-a:3b",
                        "granite4:1b",
                        "granite4:3b",
                        "minicpm-v",
                        "orca-mini",
                     ]
contextListorModels = {"model":(contextListorRecc,1)}
contextListorInputs = {"{question}":False,"{topic}":True}
contextListorPrototype = {"name":"Context Listor","models":contextListorModels,"inputs":contextListorInputs,"prompt":article_source_prompt_3,}



###
# Basic Summary Assets
#   The summarizor takes a volume of text and compresses it to concise representation of the core points
###
summarizor_template = """
Summarize the following text as compactly as possible:
{text}
Reply with only the central points.
"""

#This module works well with quick, small modules. The very small ones typically do a good job, and
#   it's a common submodule that shouldn't take up too much time.
basicSummarizorRecc = ["granite4:350m",
                       "driaforall/tiny-agent-a:0.5b",
                       "tinyllama",
                       "tinydolphin",
                       "stablelm2",
                       "smollm",
                       "driaforall/tiny-agent-a:1.5b",
                       "driaforall/tiny-agent-a:3b",
                       "granite4:1b",
                       "granite4:3b"
                       ]

basicSummarizorGuidance = ["Accepts text, URL, and local files (drag to {text} field)"]
basicSummarizorModels = {"model":(basicSummarizorRecc,1)}
basicSummarizorInputs = {"{text}":False,}
basicSummarizorPrototype = {"name":"basicSummarizor","models":basicSummarizorModels,"inputs":basicSummarizorInputs,"prompt":summarizor_template,"guidance":basicSummarizorGuidance}



###
# Math Problem Solver Assets
#   This module solves a math problem by writing a python script to answer it, then executing it
###

math_prompt = """
Write a Python script which will produce the answer of the following math question: \"{problem}\" Do not use any library functions that are not strictly necessary. Think briefly, do not produce any explanation.
"""

#This module is tricky- the faster modules sometimes work well, and sometimes not. Only some of the
#   larger ones actually work regularly, though. Commented below for the ones that have been tested
#   are the ratio of successes on test problems, as well as median run times for each. Qwen is *slow*
#   but generally the most reliable
mathSolverRecc = ["qwen3",#(3/3,169.8),
                "llama3.2",#(3/3,14.2),
                "granite4:3b",#(5/6,9.6),
                "driaforall/tiny-agent-a:3b",#(5/6,27.0),
                "driaforall/tiny-agent-a:0.5b",#(1/3,7.0),
                "driaforall/tiny-agent-a:1.5b",#(2/3,16.0),
                "openchat",#(2/3,50.6)
                ]
mathSolverModels = {"model":(mathSolverRecc,1)}
mathSolverInputs = {"{problem}":False,}
mathSolverPrototype = {"name":"mathSolver","models":mathSolverModels,"inputs":mathSolverInputs,"prompt":math_prompt}



###
# Multi-answerer Assets
#   This module asks a set of models a question, and then an additional one joins their answers into
#   one cohesive whole
###

multianswer_prompt = """Combine the {number} distinct responses to the prompt {input} found below into a single, coherent response
### Responses
{responses}
"""
multianswer_ask = """Respond concisely but completely to the following input: {input}"""

#This module has two types of models- ones used for answering, and the supervisor. It's advised to
#   make each answerer a different model, so that you get diverse replies to stitch together. It's 
#   ideal to have the answerers be relatively fast, and the supervisor a bit larger
multiAnswererRecc = ["driaforall/tiny-agent-a:1.5b",
                     "granite4:350m",
                     "driaforall/tiny-agent-a:0.5b",
                     "granite4:1b",
                     "tinydolphin",
                     "orca-mini",
                     "driaforall/tiny-agent-a:3b",
                     "granite4:3b",
                     "tinyllama",
                     "stablelm2",
                     "llama3.2",
                     "nemotron-mini",
                     "minicpm-v"
                ]
multiSuperRecc = ["granite4:3b",
                  "granite4:1b",
                  "granite4:350m",
                  "driaforall/tiny-agent-a:3b",
                  "driaforall/tiny-agent-a:1.5b",
                  "driaforall/tiny-agent-a:0.5b",
                  "minicpm-v",
                  "llama3.2",
                ]
multiAnswererModels = {"models":(multiAnswererRecc,3),"supervisor":(multiSuperRecc,1)}
multiAnswererInputs = {"{input}":False,}
multiAnswererPrototype = {"name":"multiAnswer","models":multiAnswererModels,"inputs":multiAnswererInputs,"prompt":multianswer_prompt+"<br>"+multianswer_ask}



###
# Reference Searcher Assets
#   This module searches a reference source, and reads material from it to answer a question
###

article_source_prompt = '''
For the topic "{topic}", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "{question}". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }
'''
article_source_prompt_3 = '''
Reply in the following template with three simple topic tags which may be used to search for information to answer the question: "{question}". Reply with no other content but the filled template. Supply only a list of tags in the 'tags' field.
### Template {"Tags":[] }
'''
relevant_sections = """
For the article "{article}", with the following section titles: "{sections}"; which sections are the most relevant to answer the question "{question}"? Reply exclusively in the following template without any other content:
### Template
{"{article}":["section","section","section"]}
"""
sec_summary_prmpt = """Concisely summarize into one paragraph the following text in context of answering the question "{question}":\n {section}"""
answer_prmpt = """Summarize and synthesize the information in the attached articles to answer the question "{question}. Reply briefly with a summary point answering the question and a short list of single-sentence follow-ups on the main point.\n ###Articles: \n" {artText}"""

#This module has several modules, although they are all drawn from the same pool of recommended models
#   mainly because the submodules are all of generally the same level of complexity
referenceSearchRecc = ["driaforall/tiny-agent-a:1.5b",
                        "driaforall/tiny-agent-a:3b",
                        "granite4:1b",
                        "granite4:3b",
                        "granite4:350m",
                        "driaforall/tiny-agent-a:0.5b",
                        "minicpm-v",
                        "stablelm2",
                        "tinydolphin",
                        "nemotron-mini"
                        ]
referenceSearchModels = {"sourceFinder":(referenceSearchRecc[:3]+referenceSearchRecc[3:],1),"relevanceChecker":(referenceSearchRecc[4:]+referenceSearchRecc[:4],1),"sectionSummary":(referenceSearchRecc[4:]+referenceSearchRecc[:4],1),"finalSummary":(referenceSearchRecc[1:]+referenceSearchRecc[:1],1)}
referenceSearchInputs = {"{question}":False,"{topic}":True}
referenceSearchPrototype = {"name":"referenceSearcher","models":referenceSearchModels,"inputs":referenceSearchInputs,"prompt":article_source_prompt_3+"<br>"+relevant_sections+"<br>"+sec_summary_prmpt+"<br>"+answer_prmpt}



###
# Chatter Assets
#   This module engages in a conversation with the user, either with or without a guiding topic
###

summary_prompt = """Summarize this conversation as a compact description, incorporating the prior summary, and making sure to note anything you would be expected to remember later in a conversation: {conversation}"""
chatter_system_topic = """You are conversing with a user about {topic}. Be helpful and constructive, but not syncophantic. Be open to explore, but remain on topic.  Do not mention the prior summary. The conversation thus far has been summarized as:\n ### Summary: {summary}"""
chatter_system_general = """You are conversing with a user. Be helpful and constructive, but not syncophantic. Be open to explore, but remain on topic.  Do not mention the prior summary. The conversation thus far has been summarized as:\n ### Summary: {summary}"""

#This module has two models- the one the user converses with directly, and the one that handles the
#   summary of the older conversation. The primary is best a mid-scale small model, and the summarizer
#   is ideally a small, fast one
chatterMainRecc = ["driaforall/tiny-agent-a:3b",
                    "granite4:3b",
                    "stablelm2",
                    "tinydolphin",
                    "orca-mini",
                    "minicpm-v",
                    "smollm",
                    "qwen3",
                    "openchat",
                    "zephyr",
                    "llama3.2"
                    ]
chatterSummRecc = ["granite4:350m",
                   "driaforall/tiny-agent-a:0.5b",
                    "tinyllama",
                    "tinydolphin",
                    "stablelm2",
                    "smollm"
                    ]
chatterModels = {"model":(chatterMainRecc,1),"summarizer":(chatterSummRecc,1)}
chatterInputs = {"{message}":False,}
chatterPrototype = {"name":"chatter","models":chatterModels,"inputs":chatterInputs,"prompt":summary_prompt+"<br>"+chatter_system_general}



###
# Debator Assets
#   This module takes a topic and points related to it, and pits two AIs against one another
#   to debate those points, ideally working against one another to generate a more nuanced
#   look at the topic
###

make_points = """List two concise primary debate positions for the topic: {topic}."""
mod_summarize = """Concisely summarize the following argument in a debate on the topic "{topic}":
Argument:
{point}
"""
opening_argument = """You are debating the topic "{topic}", taking the position {position}. Make a concise and strong argument in favor of your position."""
reply_argument = """You are debating the topic "{topic}", taking the position {position}. Your current argument is {yourArgument}, reply to your opponent, who is currently arguing: {theirArgument}"""
debate_conclusion = """Summarize the following two concluding arguments from a debate on the topic "{topic}", emphasizing contributions from both points:
For point {pointOne}:
{argOne}
For point {pointTwo}:
{argTwo}
"""

#This model is much more flexible, so has recommendations for the debators themselves
#   as all the modules, and the summarizor just as those suggested for the summary module
debatorGuidance = ["Most productive when supplied with the specific points you want to see argued or polarizing ones that prompt strong synthesis"]
debatorModels = {"debators":(quick_testers+slow_testers,2),"moderator":(basicSummarizorRecc,1)}
debatorInputs = {"{topic}":False,"{pointOne}":True,"{pointTwo}":True,"rounds":True}
debatorPrototype = {"name":"debator","models":debatorModels,"inputs":debatorInputs,"prompt":opening_argument+"<br>"+reply_argument+"<br>"+debate_conclusion,"guidance":debatorGuidance}



###
# Text Analysis Assets
#   This module examines a text by compressing, summarizing, and asking direct critical questions and
#   then synthesizing those into more sophisticated analysis sources
###

topic_extract = """
### Template
"In one sentence, what is the thesis of the following text?"\n
### Text\n
\"{text}\"
"""
key_points="""
Make a bullets list of the main points made in this text:
{text}
"""
question_asker ="""
### Text:
{text}
### Prompt:
About the preceeding text, answer the following question:
{question}
"""

#The analysis questions extract basic who/what/when/where/how type information from the text
analysis_questions = ["Who are relevant parties to this information?",
             "Who might benefit from this?",
             "Who might be harmed by this?",
             "What are some arguments in favor of the points here?",
             "What are some arguments against the points here?",
             "What are some alternatives to this topic?",
             "What are some strengths in these points?",
             "What are some weaknesses in these points?",
             "What contrasts against this?",
             "Where are there similar concepts?",
             "Where can one get more information about this topic?",
             "Under what conditions is this beneficial?",
             "Under what conditions is this a problem?",
             "Why is this important?",
             "Why should people know about this?",
             "How do we know we can trust this?",
             "How can we question this?",
             "How can we approach this safely?"
            ]
synthesis_prompt = """
### Information
{text}
### Prompt
Summarize the prior text in the context of the topic \"{topic}\" to answer the question \"{question}\"
"""

#The synthesis questions combine responses from the analysis questions with a central prompt
#   to unify them- the lists below are the questions which feed each synthesis
analysis_context = [
"What are some alternatives to this topic?",
"What contrasts against this?",
"Where are there similar concepts?",
    ]
analysis_supporting = [
"What are some arguments in favor of the points here?",
"What are some strengths in these points?",
"Under what conditions is this beneficial?",
    ]
analysis_questioning = [
"What are some arguments against the points here?",
"What are some weaknesses in these points?",
"Under what conditions is this a problem?",
    ]
analysis_relevance =["Who are relevant parties to this information?",
"Who might benefit from this?",
"Who might be harmed by this?",
    ]
analysis_meaning = [
"Why is this important?",
"Why should people know about this?",
    ]
analysis_further = [
"How do we know we can trust this?",
"How can we question this?",
"Where can one get more information about this topic?",
    ]

#The synthesis inputs list the analysis questions to draw from, and the unifying question for
#   that synthesis prompt
synthesis_inps = [
    (analysis_context,"How can we contextualize these ideas?"),
    (analysis_supporting,"What supports these ideas?"),
    (analysis_questioning,"What arguments can be made against these ideas?"),
    (analysis_relevance,"Who are these ideas relevant to?"),
    (analysis_meaning,"Why do these ideas matter?"),
    (analysis_further,"How can we dig deeper on these ideas?"),
    ]

#The text analysis module has three categories of model to use, applied into five different sub
#   modules. It uses a deep module for the syntheis, middling for several breakdown modules, and
#   a shallow module for the summary
deepModelRecc = ["driaforall/tiny-agent-a:3b",
                "granite4:3b",
                "tinyllama",
                "minicpm-v",
                "stablelm2",
                "qwen3",
                "openchat",
                "phi3.5",
                "zephyr",
                "phi",
                "llama2-uncensored",
                "qwen2.5",
                "llama3.2"
                ]
midModelRecc = ["driaforall/tiny-agent-a:1.5b",
                "driaforall/tiny-agent-a:3b",
                "granite4:1b",
                "granite4:3b",
                "tinyllama",
                "smollm",
                "minicpm-v",
                "stablelm2",
                "tinydolphin",
                "orca-mini",
                "zephyr",
                "llama3.2"
                    ]
shallowModelRecc = ["granite4:350m",
                    "driaforall/tiny-agent-a:0.5b",
                    "driaforall/tiny-agent-a:1.5b",
                    "granite4:1b",
                    "driatasker",
                    "tinyllama",
                    "smollm:360m",
                    "nemotron-mini",
                    "stablelm2",
                    ]

textAnalysisGuidance = ["Accepts text, URL, and local files (drag to {text} field)"]
textAnalysisModels = {"deep":(deepModelRecc,1),"mid":(midModelRecc,1),"shallow":(shallowModelRecc,1),}
textAnalysisInputs = {"{text}":False,}
textAnalysisPrototype = {"name":"textAnalyzer","models":textAnalysisModels,"inputs":textAnalysisInputs,"prompt":topic_extract+"<br>"+key_points+"<br>"+question_asker,"guidance":textAnalysisGuidance}



###
# Refiner
#   This module takes a starting statement, along with feedback on it, and attempts to refine the statement
###

refine_statement = """Revise the statement \"{statement}\" based on the criticism \"{feedback}\", reply with ONLY the concise, reworked statement"""

#This module only needs one model, but it needs to be reasonably good at integration, as it needs to
#   transform the input based on feedback, and not extemporize too much
refinerRecc = ["driaforall/tiny-agent-a:3b",
                "granite4:3b",
                "tinyllama",
                "tinydolphin",
                "granite4:1b",
                "driaforall/tiny-agent-a:1.5b",
                "granite4:350m",
                "driaforall/tiny-agent-a:0.5b",
                "smollm",
                "minicpm-v",
                "stablelm2",
                ]

refinerGuidance = ["<b>INTERACTIVE, will prompt you for feedback and change approval</b>"]
refinerModels = {"model":(refinerRecc,1),}
refinerInputs = {"{context}":False,"{statement}":False,"{feedback}":True}
refinerPrototype = {"name":"refiner","models":refinerModels,"inputs":refinerInputs,"prompt":refine_statement,"guidance":refinerGuidance}


####
#   Testing Utility Components
####

###
#Sample Texts for testing
###

#Text searches for multianswer, reference searcher
Tsearch1 = "What is a werewolf?"
Tsearch2 = "What are some important landmarks in Paris for tourism?"

#Statements for summary, topic extraction, refinement, etc.
ST1 = """
See also: Hypertrichosis and Clinical lycanthropy Some modern researchers have tried to explain the reports of werewolf behaviour with recognised medical conditions. Dr Lee Illis of Guy's Hospital in London wrote a paper in 1963 entitled On Porphyria and the Aetiology of Werewolves in which he argues that historical accounts on werewolves could have in fact been referring to victims of congenital porphyria , stating how the symptoms of photosensitivity , reddish teeth, and psychosis could have been grounds for accusing a person of being a werewolf.\[59\] This is, however, argued against by Woodward, who points out how mythological werewolves were almost invariably portrayed as resembling true wolves and that their human forms were rarely physically conspicuous as porphyria victims.\[45\] Others have pointed out the possibility of historical werewolves having been people with hypertrichosis , a hereditary condition manifesting itself in excessive hair growth. However, Woodward dismissed the possibility, as the rarity of the disease ruled it out from happening on a large scale as werewolf cases were in medieval Europe.\[45\] Woodward suggested rabies as the origin of werewolf beliefs, claiming remarkable similarities between the symptoms of that disease and some of the legends. Woodward focused on the idea that being bitten by a werewolf could result in the victim turning into one, which suggested the idea of a transmittable disease like rabies.\[45\] However, the idea that lycanthropy could be transmitted in this way is not part of the original myths and legends and only appears in relatively recent beliefs. Lycanthropy can also be met with as the main content of a delusion, for example, the case of a woman has been reported who during episodes of acute psychosis complained of becoming four different species of animals.\[60\]
"""
ST2 = """
Here's my opening argument on the topic of predestination: **Point 1: The Bible does not explicitly teach predestination**, which means that the concept of predestination is not clearly stated or taught in Scripture. While the Bible does emphasize God's sovereignty and control over human events, it does not provide a systematic explanation for how God chooses certain individuals to salvation before the foundation of the world. **Point 2: The doctrine of predestination contradicts the biblical concept of free will**, which is a fundamental aspect of Christian theology. If God predetermines all events, including human decisions and actions, then do humans truly have control over their choices? This would undermine the idea that God's sovereignty and love are demonstrated through His provision of salvation to humanity. **Point 3: The Bible presents a more nuanced understanding of God's sovereignty**, which emphasizes God's initiative in salvation rather than predetermination. While God may choose certain individuals for salvation, He also initiates the process by calling them out of darkness and empowering them with the Holy Spirit (Ephesians 1:11). This perspective highlights God's active role in human decision-making while still acknowledging His sovereignty over all things. By presenting these three points, I aim to challenge the notion that predestination is a Scripturally supported doctrine and highlight the need for further biblical exposition on this topic." in the context of the topic "Predestination is not biblically supported
"""

#Math problem for solver
mathProblem1 = "What is the smallest cube number greater than 11385?"

#Multiple questions for multianswer, chatter, debator
multiQ1 = "What is a werewolf?"
multiQ2 = "How can I get a small object out of a pipe embedded in concrete?"
multiQ3 = "Give me some ideas for dinner, I have chicken, flour, lentils, and peaches."

#List texts for listifiers
list_txt_1 = '''Sure, let's talk about chat summaries. Let me explain the process first:

1. When a user inputs text into the chat application, they need to create a summary of their message using some techniques:
   - Sentiment analysis: This helps understand what the message is saying.
   - Prepositions and prepositions that indicate context:
     - "The" can show where information begins
     - "A" can signify time period (e.g., "last week")
     - "Of" can indicate a specific subject matter
     - "In" can refer to the whole body of text
   - Using these techniques helps summarize what was sent in a concise way.

2. Here's how we typically create a summary:
   - First, analyze the content using sentiment analysis
   - Look for common words or phrases that convey key points about the message
   - Create an overview with the most significant information
   - Avoid technical jargon and overly detailed summaries

3. When we have a chat application running, it's good practice to:
   - Take notes of the summary you generate
   - Share your thoughts on what works well and what could be improved
   - Discuss how other users might use your system for reference

The goal is to help users understand what the message is trying to convey without being overwhelmed by too much detail. It's important to remember that summaries can be subjective and may not capture all nuances of the text, but they provide a good starting point for understanding the content of the chat session. 9.6
'''
list_txt_2 = '''That sounds like a fun idea! Let me help you find some tips for a weekend getaway:

1. Planning: Start by planning your travel itinerary, including your travel dates and any special activities or accommodations.
2. Budget: Consider your available budget for transportation, accommodation, and any meals.
3. Activities: Think about the most important activities you want to do on your vacation:
   - Family
   - Adventure
   - Relaxation
   - Cultural exploration
4. Transportation Options:
   - Carpool or taxi with friends/commuters
   - Train or bus for longer distance trips
   - Public transportation (if you have access)
5. Accommodation: Look into local accommodations, travel centers, and resorts that offer similar experience.
6. Meal Planning: Decide on your meals based on what you want to spend the weekend on:
   - Local food chains or restaurants
   - Virtual or physical options
   - Restaurant reviews
7. Environmental Considerations:
   - Plan for a safe and environmentally friendly stay
   - Use renewable energy sources if available

Based on this analysis, I can help determine which activities and meals are ideal for your weekend getaway. If you have any specific needs or preferences, feel free to share those details too! 9.2
'''
list_txt_3 = '''Great plan! Let's break this down into items:

1. **Fried Rice**: High protein, low in calories
2. **Broccoli Salad**: High in protein and a balanced serving of veggies
3. **Vegetable Stir-Fry**: Good balance between protein and calorie efficiency
4. **Fruit Salad**: High in fiber and healthy fats

For the vegetable stir-fry, we can consider using mixed greens or other vegetables that could add more flavor without compromising on protein content.

Here's a suggested meal plan:

- 1 cup of frozen broccoli
- 1/2 cup diced tomatoes
- 1 large carrot
- 1 cup sliced bell peppers (optional)
- 1 avocado
- 1/2 cup mixed greens
- 1 teaspoon olive oil
- 1/4 cup granulated sugar
- Salt and pepper to taste
- Olive oil
- Fresh herbs like cilantro or parsley

This meal plan incorporates all four items while providing some variety. You can adjust the amount of each vegetable based on your preferences and dietary requirements.

Would you like me to help make a more personalized suggestion for another item? Or would you prefer to try an alternate meal plan that's different from what I suggested?
'''
multi_list_1 = '''The prior text discusses the **establishment** and evolution of diplomatic tracks within international diplomacy, specifically emphasizing Track I and Track II from 1981. It highlights how these tracks have played a role in facilitating conflict resolution through various strategies, including workshop facilitation.

### here's some content

To dig deeper on these ideas:
(A) **Historical Context**: Review historical documents or articles about Track I and Track II to understand their creation, evolution, and significance.

a) **Case Studies** - Examine specific examples of how diplomatic tracks have been used in different contexts:
   - How Track I and Track II were implemented
   - How these tracks have influenced conflict resolution efforts
   - What types of actors participated (governmental vs. non-governmental)
   - The outcomes of the agreements facilitated by these tracks

3a: **Impact of Workshop Facilitation**: Look at how workshop facilitation has evolved over time:
   - The specific mechanisms used for workshop facilitation
   - How workshops have been structured and what types of issues they have addressed
   - The impact of workshops on diplomatic relations and conflict resolution

 4j. **Examples of Diplomatic Success Stories** : Study examples where diplomatic tracks have led to significant progress in international relations:
   - How Karen villages successfully resolved disputes between Karen ethnic groups in Myanmar
   - How the Living Room Dialogue Group has contributed to peace negotiations between Israelis and Palestinians

 k) **Current Research**: Review current academic research on diplomatic tracks and their effectiveness in conflict resolution:
   - Studies comparing the outcomes of traditional diplomatic mechanisms with those facilitated by these tracks
   - Recent case studies examining how Track I and Track II have been updated or adapted

6 - **Policy Implications**: Analyze the implications for international diplomacy:
   - How these diplomatic tracks fit into broader policy frameworks
   - What challenges these tracks face in modern times
   - The potential for future revisions to these tracks based on empirical evidence

7- **Comparative Analysis**- Compare the development of diplomatic tracks across different countries and historical periods to understand similarities and differences.

By examining these areas, one can gain a **more comprehensive** understanding of how Track I and Track II have contributed to international diplomacy and conflict resolution efforts.'''

