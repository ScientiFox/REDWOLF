# REDWOLF

## Introduction
Redwolf is a package of local AI tools, joint combinations of modern and classical techniques, intended for general purpose use in problem solving, brain storming, research assistance, and similar. It puts focus on three design goals:

- Being fully local and private. Thanks to the open-sourcing of the LLMs, you can absolutely run powerful tools fully locally. That means that the big companies can't use your data (which they outright admit), you can have it for free, it doesn't break when the internet is out, and you can poke and prod at it at will.
- Being resourceful. Running local means not using massive datacenters and GPU clusters as a crutch. We use combinations of efficient classical algorithms to force-multiple on smaller, faster models to make good use of what a regular laptop has. While it does require a little more patience, it also means you aren't contributing to the exponential power power costs that cloud systems require for speed by layering LLMs on top of LLMs to fix problems LLMs cause.
- Being reliable. We all know about the hallucinations. We believe those are embedded in the structure of the training structure and data. So, we put a lot of effort into using a combination of external source analysis, multi-model checking, synthesis methods, and adversarial processing to constrain the output to reasonable results.

The name is borrowed from an old IRC bot we made back in '09-'11 that did some AIML chatting and basic command execution.

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

## Techniques

There's a few particular techniques we use to get the most bang for your buck on a local system, and make sure execution times for complex, multistep processes are within acceptable and practically useful ranges for everyday work.

#### Recommended Models
For each module, we refine both the prompts used and the models selected to respond to those prompts with a large number of tests, selecting down the recommended modules to a subset of those which perform well while requiring the least computation time. Sometimes these tests are objectively verifiable, such as with the mathSolver module, which must produce answers which are verifiably correct, while others are semi-subjective ('is this summary factually accurate but brief') and others fully subjective ('Does this brainstorming suggestion further creative thought?').

#### Divide and Conquer
In addition to choosing the most efficient model for a given task, decomposing full tasks into appropriately small subtasks is also important to making use of the limited resources of a local system. Firstly, dividing tasks which are LLM suitable (summaries, answering questions) from those which can or should be handled by other methods (extracting lists, searching for keyword) allocates cognitive loading to the most effective places possible.

#### Tactical Submodules
Because, in general, processing time costs scale nonlinearly with input size, it is extremely beneficial to not only divide up the tasks, but also apply submodules to portions of the task with appropriately allocated portions. This means, for instance, using a small module for a small task that requires less cognitive depth, such as using the smallest, and fastest, reliable model to do tasks that do not require synthesis or analytical processing, like summarizing. This reserves using more sophisticated models for more sophisticated tasks, like using mid-range models for analysis, and larger, more complex ones for the sparing integration and synthesis tasks.

This also means applying models to segments of subtasks tactically, using the relative advantage of the efficienct of smaller modules, grouped, to replace that of larger, more coherent modules where they are too inefficient. For example, a 0.5b model may not be able to fully maintain coherence during the summarization of a 10 page text, where a 13b model would succeed, but far slower. But, applying the 0.5b model ten times over, to overlapping portions of the 10 page text which *are* within its coherence range will often be an order of magnitude faster, and equally efficacious, to the 13b model if applied with finesse.

##### Pyramid Processing
One such finesse method we use frequently (at time of writing within the summarizor, textAnalysis, and chatter) is a pyramid approach to text analysis, illustrated in the following diagram:

<img width="1167" height="696" alt="pyramid_processing" src="https://github.com/user-attachments/assets/f11a258f-b07a-48eb-b7c5-ec391b3147ce" />

The idea here is that some module processes segments of the text (ideally overlapping segments, to ensure that segues and transitions are incorporated and preserved, and to prevent the subsections from becoming disjoint) rather than the full text, are processed in parallel by a module, and then the results are either further individually processed, or joined for later processing by other modules, depending on the task. This way, we can leverage the advantage of the exponentially escalating cost for input size, while maintaining a reasonable input length, avoiding context limits, and incorporating transitional information.

Note that this method does not only apply to multistep summaries, or even single-task layers! Within the textAnalysis module, the first layer is a set of text-compressing summaries, then the next tier is answering a set of analysis questions, and then the next layer groups subsets of the analysis questions to answer syntheis questions!

#### Multiagent Systems

#### Feedback Controls

## Modules

#### 



## Prospective Additions
