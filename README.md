<img width="922" alt="image" src="https://github.com/user-attachments/assets/b1700143-d615-4c50-a1dc-08f49bb5c43c" />

# REDWOLF

## Introduction
Redwolf is a package of local AI tools, joint combinations of modern and classical techniques, intended for general purpose use in problem solving, brain storming, research assistance, and similar. It puts focus on three design goals:

- Being fully local and private. Thanks to the open-sourcing of the LLMs, you can absolutely run powerful tools fully locally. That means that the big companies can't use your data (which they outright admit), you can have it for free, it doesn't break when the internet is out, and you can poke and prod at it at will.
- Being resourceful. Running local means not using massive datacenters and GPU clusters as a crutch. We use combinations of efficient classical algorithms to force-multiple on smaller, faster models to make good use of what a regular laptop has. While it does require a little more patience, it also means you aren't contributing to the exponential power power costs that cloud systems require for speed by layering LLMs on top of LLMs to fix problems LLMs cause.
- Being reliable. We all know about the hallucinations. We believe those are embedded in the structure of the training structure and data. So, we put a lot of effort into using a combination of external source analysis, multi-model checking, synthesis methods, and adversarial processing to constrain the output to reasonable results.

The name is borrowed from an old IRC bot we made back in '09-'11 that did some AIML chatting and basic command execution.

## Motivation
There's a litany of them:

- AIAAS is not private, they outright [state](http://openai.com/policies/row-privacy-policy/#:~:text=We%20collect%20Personal%20Data%20that%20you%20provide%20in%20the%20input%20to%20our%20Services) that they collect everything you put into them, and use that to train the future models 
- The power consumption for fast execution in the cloud is extraordinary, and the power costs for faster speeds are distinctly nonlinear (meaning that waiting 10 seconds for a reply instead of 5 saves more than double the power)
- For-profit AIAAS systems (even the ones making mone on data sales or adverts) have a perverse incentive to engineer their product to make people want to use it more (more pleasant, more fun, or even set to be just good enough to stretch out the interactions as long as users will tolerate) instead of for robust, reliable, effective, correct output.
- If the internet goes out, your tool is dead in the water
- LLM models are starting to hit a plateau, like all technology does. I mark the start of this phase with Deepseek, a la [G. S. Altshuller's Laws of technical evolution #7](https://en.wikipedia.org/wiki/Laws_of_technical_systems_evolution#Patterns_of_evolution) The value-add now is in structuring the systems built on them to be more effective and sophisticated.
- The quality of open-source LLMs has been apparoaching that of the closed models for a while now, and even if the gap never closes because the incentive to push evaporates (which I think is unlikely- the OS players have a vested interest in matching the CS ones) they're close enough that good accouterment make the gap immaterial

## Overview
The overall structure of Redwolf has three parts: 
- A primary script implementing all the utility modules and a loop to execute and toggle between them
- A browser-based user interface to manage module selection, inputs, and interaction
- A websockets server with queues to manage async contact between the other two

Also, there's two other main supporting components:
- An archive interface (currently for Wiki ZIM files, prospectively for Google Scholar and other assets)
- A source file of genericized prompts for executing structured requests and tests of the modules

The former is a package designed to read ZIM archive files and produce an NLP/LLM friendly set of section-delimited text blocks. Right now, that means it needs a local copy of a ZIM file, which often run to the dozens of gigabytes, but they're readily available, and we keep archived copies as well.

The latter file implements all the prompt engineering side of getting the LLM modules to output reasonably reliable and processable output, as well as guidance to restrict them to more or less sane and useful results. Most of bringing the systems into closed-loop execution is performed with standard NLP and other classical algorithms. It also sets up module prototypes, which allow the UI side to build the interface for the user and manage model selection, input, and SYSTEM messages to the modules.

For the actual interface to the LLMs, Redwolf uses Ollama. A lot of the main nerds will tell you to avoid it, and there is an intend to port the package over to llama.cpp at some point, but for now ollama is easier to use, easier to install, and easier to grab models for, so it's the baseline. We keep archived copies of the ollama package and 

### Requirements
The Redwolf package requires the following additional packages:

`numpy, cv2, ollama, nltk, libzim, bs4`

Additionally, nltk needs the following corpus downloads:

`nltk.download("wordnet31")`
`nltk.download("vader_lexicon")`
`nltk.download('subjectivity')`

And a set of ollama compatile LLMs should be downloaded. We recommend, at a minimum:

`driaforall/tiny-agent-a:0.5b`
`driaforall/tiny-agent-a:1.5b`
`driaforall/tiny-agent-a:3b`
`granite4:1b`
`granite4:3b`
`granite4:350m`
`tinyllama`
`stablelm2`
`minicpm-v`
`qwen3`
`llama3.2`

### Execution

To execute the package, the contents should be downloaded, with a suitable ZIM archive located in the same directory. `RW2_server.py` and `REDWOLF2.py` should then be executed as independent processes. The UI will open in your default browser automatically.

## Techniques

There's a few particular techniques we use to get the most bang for your buck on a local system, and make sure execution times for complex, multistep processes are within acceptable and practically useful ranges for everyday work.

#### Recommended Models
For each module, we refine both the prompts used and the models selected to respond to those prompts with a large number of tests, selecting down the recommended modules to a subset of those which perform well while requiring the least computation time. Sometimes these tests are objectively verifiable, such as with the mathSolver module, which must produce answers which are verifiably correct, while others are semi-subjective ('is this summary factually accurate but brief') and others fully subjective ('Does this brainstorming suggestion further creative thought?').

Some examples of these tests are included in the `output examples` folder, and test articles are included in the `REDWOLF_core_prompts.py` package, as well as source material in the `worker tests` file.

#### Divide and Conquer
In addition to choosing the most efficient model for a given task, decomposing full tasks into appropriately small subtasks is also important to making use of the limited resources of a local system. Firstly, dividing tasks which are LLM suitable (summaries, answering questions) from those which can or should be handled by other methods (extracting lists, searching for keyword) allocates cognitive loading to the most effective places possible.

#### Tactical Submodules
Because, in general, processing time costs scale nonlinearly with input size, it is extremely beneficial to not only divide up the tasks, but also apply submodules to portions of the task with appropriately allocated portions. This means, for instance, using a small module for a small task that requires less cognitive depth, such as using the smallest, and fastest, reliable model to do tasks that do not require synthesis or analytical processing, like summarizing. This reserves using more sophisticated models for more sophisticated tasks, like using mid-range models for analysis, and larger, more complex ones for the sparing integration and synthesis tasks.

This also means applying models to segments of subtasks tactically, using the relative advantage of the efficienct of smaller modules, grouped, to replace that of larger, more coherent modules where they are too inefficient. For example, a 0.5b model may not be able to fully maintain coherence during the summarization of a 10 page text, where a 13b model would succeed, but far slower. But, applying the 0.5b model ten times over, to overlapping portions of the 10 page text which *are* within its coherence range will often be an order of magnitude faster, and equally efficacious, to the 13b model if applied with finesse.

##### Pyramid Processing
One such finesse method we use frequently (at time of writing within the summarizor, textAnalysis, and chatter) is a pyramid approach to text analysis, illustrated in the following diagram:

<img width="700" alt="pyramid_processing" src="https://github.com/user-attachments/assets/f11a258f-b07a-48eb-b7c5-ec391b3147ce" />

The idea here is that some module processes segments of the text (ideally overlapping segments, to ensure that segues and transitions are incorporated and preserved, and to prevent the subsections from becoming disjoint) rather than the full text, are processed in parallel by a module, and then the results are either further individually processed, or joined for later processing by other modules, depending on the task. This way, we can leverage the advantage of the exponentially escalating cost for input size, while maintaining a reasonable input length, avoiding context limits, and incorporating transitional information.

Note that this method does not only apply to multistep summaries, or even single-task layers! Within the textAnalysis module, the first layer is a set of text-compressing summaries, then the next tier is answering a set of analysis questions, and then the next layer groups subsets of the analysis questions to answer syntheis questions!

#### Multiagent Systems
Another advantage of not working with a cloud system owned and operated by a service is that we're not bound by their noncompete clauses! We can freely use models from multiple sources, compare their outputs (as in the multianswer and debator modules), select ideal workers for individual tasks and contexts (as in all modules), or use them to critique one anothers' outputs from different perspectives (as in the debator, reference searcher, and analysis modules), or collect multiple outputs from differnet providers and then stitch them together into a single answer from different sources (again, the multianswer module).

The two real benefits this provides us are checks and balances, for critiquing differnt models from (more or less) independent observers, and the ability to investigate conceptual spaces more thoroughly, eliminating biases and weaknesses in any one-model approach by overlapping different combinations of strengths and weaknesses.

#### Feedback Controls
Finally, the use of feedback, from classical systems, user input, reference sources, and other models to constrain the output to sane, reasonable, and useful outputs is a critical part of making the systems reliable and useful. Although the usefulness of some subjective applications (such as brainstorming) is itself equally subjective, constraining and checking the outputs for such subjective applications to more concrete tasks like problem solving is important to making the modules practically applicable.

Towards that end, all of these means of feedback control are applied throughout all the modules to varying degrees, from the tightly controlled reference searcher, which is tasked with only reporting and collating information from  provided sources, to the very loose chatter, which still uses an additional model to select out salient information for long term recall, to guide the systems towards productive output.

## Modules
The modules currently included are detailed below, with descriptions and operational flowcharts. Every module must include a `run()` method which executes its primary function, and a `set_System()` method which applies SYSTEM commands to its submodules and models.

<img width="420" height="486" alt="simple_module" src="https://github.com/user-attachments/assets/999b8a85-da50-4e48-83eb-3ef5ea3847f0" />

#### Simple Module
The simple module is a parent class for many of the modules and submodules implemented in the later modules, and serves as a simple scaffold for the primary execution of a simple tasker dedicated to performing a singular role. The key notes about the module are that it does not implement any memory- every input submission is sent to the model with no prior history, and is formatted around a common template prompt which takes some keyed inputs which are embedded within the reference prompt in {brackets} which is replaced by the input from the module `run()` method. The reference prompts form the framework for the use of structured prompt engineering to generate outputs which are consistent with individual module goals.

<img width="520" alt="context_listor" src="https://github.com/user-attachments/assets/1968c051-971e-4a98-beb9-3322e6bab521" />

#### Context Listor
The context listor is a submodule which is used within the reference searcher to identify article search strings based on the question which the reference searcher is being asked. It is implemented as a class rather than an instance of a simple module (unlike most other single-purpose submodules) primarily as an example implementation test case and proof of concept from the early stages of development. As such, it is not selectable in the UI.

<img width="520" alt="basic_summarizor" src="https://github.com/user-attachments/assets/a651d9ec-71e4-48c8-986e-140a5c6b0da6" />

#### Basic Summarizor
The basic summarizor module is a strong workhorse submodule which can also be applied as an individually through the UI. It is deigned to take in a source text and summarize it, either by dividing into segments (as described in the section on pyramidal processing above) or as a whole text, and produce a concise compactification of that text which is more brief than the source, but contains the primary points within it. Some slight modifications of this module are implemented elsewhere within the modules which specify bulleted list summaries, but the main implementation is a direct summary.

Can be executed on local source files by drag-and-drop, and the same for web sources via URL, or by direct text supply to the input box.

<img width="840" alt="math_solver" src="https://github.com/user-attachments/assets/c587d9de-0efc-4857-9dac-e502bff0ba7d" />

#### Math Solver
The math solver approaches answering problems by prompting the LLM to generate a python script to answer the question. That code is extracted from the output, then given a basic sanitization to prevent untoward uses and force a timeout limit, and further a global result variable is introduced so that the script can be executed and the results extracted. The result extraction routine is a substantial piece of classical analysis over top of the LLM code output.

It is quite sensitive to model choice in the sense that nearly all modules will generate viable output, but only a few reliably produce correct answers.

<img width="840" alt="multianswer" src="https://github.com/user-attachments/assets/f62ce090-300e-4fda-a10b-3caa583c5db1" />

#### Multianswerer
The Multianswer module takes an input question or prompt and then processes that answer with three different models, and the output from those models is then combined into a single synthetic answer by a supervisor model. This approach seeks to leverage the advantages of having access to multiple different modules with different strengths, and is effective at constraining the output to sane and viable results, on account of the supervisor drawing from information provided to it, rather than performing its own conceptual evaluations.

It is also a strong candidate as a potent building block module for implementing higher level pyramidal processing, for instance by implemeting a sort of soft voting logic for mid-grade complexity tasks addressed by compact models, or for increasing the reliability of small closed-loop tasks like affect analysis or sanity checking (Such as asking a multiasker 'here's what another LLM said, does it make sense and is it relevant?') without having to resort to larger, more sophisticated models.

<img width="840" alt="reference_searcher" src="https://github.com/user-attachments/assets/a2f37f8d-9363-4363-9279-213e205f56eb" />

#### Reference Searcher
The reference searcher is a direct method of reducing false or hallucinatory data in responses, build around engineering the models used to only sort and process data drawn from another source, not within its own generation space. It starts by generating a list of search terms for a given question, then using a search-and-suggest method build into the database or archive which it is drawing from to acquire source texts. Sections from those source texts are then evaluated for relevance to the current question, and those sections are pulled and their main points extracted.

The main points from the relevant sections of each source are then combined, and a final model makes a synthesis summary of all the selected data as the final output. At every step, the LLMs are prompted to manipulate source information, rather than produce their own information, and so in tests thus far the module has been exceptionally constrained in its output, and very reliably factual.

<img width="520" alt="chatter" src="https://github.com/user-attachments/assets/48dda452-1a38-411e-b995-0eb068a9e8f2" />

#### Chatter
The chatter module is the most basic and fundamental sort of interaction system, and the first of these modules with proper user interactions int he sense of an active back and forth. It is also the first with a proper interaction history, as well. In order to keep its context window small and execution efficient, it is designed to monitor the length of the interaction, and when periodically exceeding a set length, summarizes the prior conversation into a set of key points (including the previous summary, if such is available). From there, it truncates the actual message history to a few recent messages, for smooth continuity, and then is provided the key points summary as SYSTEM input for firm guidance of the direction and memory.

The structure of the input message prompts and SYSTEM command are designed to encourage the model to be helpful and avoid syncophantic replies, and to stay on topic. As such, it performs less of a social interaction role, and more of a supportive assistantship. It has demonstrated effective performance in several open-ended back and forth taskes, such as recipe planning, practical problem solving, and brainstorming.

<img width="840" alt="debator" src="https://github.com/user-attachments/assets/13bc5e20-215a-4456-9cbc-8588d81ae4d9" />

#### Debator
The debator module is designed to take advantage of the combination of adversarial feedback which can be had by critiquing one model's output with another model, as well as the benefits of using multi-model analysis to overlap weaknesses with strengths. Supplied with a topic and (possibly) two points regarding that topic, the debator module iteratively provides each of two models with a prompt to first generate an opening argument, and then to modify their own arguments in response to those proposed by their opposite's working arguments and points.

<img width="420" height="770" alt="debator_supervisor" src="https://github.com/user-attachments/assets/238d0e88-7cdd-4a59-9caa-d402510923be" />

After a set number of rounds of iterative feedback, revisions, and rebuttals, the final pair of points and arguments are evaluated by a moderator module, which attempts to draw a nuanced, multifaceted conclusion from the direction the back and forth debate generated.

This module works best, relative to human expectations, when provided with a pair of focused, specific points to debate. However, if provided with one or no points, it is also written to generate an opposition to a single point, or attempt to generate a pair of opposing points from a topic alone. However, these generated points may not be oriented in a direction which feels productive to the user.

<img width="840" alt="text_analysis" src="https://github.com/user-attachments/assets/e9c52c20-b90c-4ba8-a6c1-c5edc7faabfc" />

#### Text Analysis
The text analysis module seeks to integrate the generative capacity of LLMs with well-established guidelines and human-centric prompting for critical thinking. It makes thorough use of both the pyramidal processing scheme and a divide and conquer attitude to implement a thorough analysis of a supplied text, focusing on breaking down the overall source into smaller segments and concise representations that can be efficiently and feely manipulated, rather than trying to ask many broad questions about a whole, large source.

It begins by dividing the source into segments, which are then condensed into shorter keypoint sumamries. Those key points are then joined into a concise version of the text which can be more easily analyzed, and a central thesis and abstract are extracted from it. Those shorter segment representations are then used to answer a set of fundamental 'who, what, when, where, why, how' questions which frame and contextualize the core information. These answers are then grouped into sets of answers which are pertinent to higher-level information synthesis questions, and used as the source information for a further submodule to answer those questions.

The combined set of thesis, abstract, concise text, analysis questions, and synthesis questions are then combined into a final report on the text, outlining its content, relevance, implications, strenghts, weaknesses, possible alternatives, and sources for further investigation as the final output.

<img width="520" alt="refiner" src="https://github.com/user-attachments/assets/57ff6251-eda3-4ea3-92fd-ca0e64e732d8" />

#### Refiner
The refiner is intended as a component of a future brainstorming and problem-solving focused module, however is useful as a stand-alone module for editing and thought clarification uses as well. It is a heavily user interaction-based module, in which the module is provided with an initial statement (typically from a user in the standalone version, but intended to be a first-pass statement from an LLM when used as a submodule) for which the user provides feedback. That feedback is then used by the module to generate a revised form of the statement.

The user is then asked to approve or disapprove of the changes. If the user approves, then the working statement is updated to the new version, and prompted for further revisions. Otherwise, the statement remains the same, and the user is prompted to provide alternative feedback for another pass.

