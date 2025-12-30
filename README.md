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

#### Divide and Conquer

#### Tactical Submodules

#### Pyramid Processing

#### Multiagent Systems

## Modules

## Prospective Additions
