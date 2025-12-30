Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
arc
<__main__.archive object at 0x72b1387cb6d0>
look = article_lookup(arc)
look.search("What are werewolves?")
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#2>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 738, in search
    msg = [{'role':'system','content':framing_prompt}]
NameError: name 'framing_prompt' is not defined

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
look.search("What are werewolves?")
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#4>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 744, in search
    output = output["content"]
KeyError: 'content'

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
look.search("What are werewolves?")
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

{'model': 'driaforall/tiny-agent-a:1.5b', 'created_at': '2025-10-28T18:49:21.921943722Z', 'message': {'role': 'assistant', 'content': '```json\n{\n  "Articles": [\n    "Werewolf Mythology and Beliefs",\n    "Werewolf History and Culture",\n    " werewolf Psychology"\n  ]\n}\n```'}, 'done_reason': 'stop', 'done': True, 'total_duration': 5647464557, 'load_duration': 1335293880, 'prompt_eval_count': 81, 'prompt_eval_duration': 1637771010, 'eval_count': 38, 'eval_duration': 2672197013}
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#6>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 746, in search
    output = output["content"]
KeyError: 'content'

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
look.search("What are werewolves?")
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

5.509697198867798 s ```json
{
  "Articles": [
    "Werewolf",
    "Introduction to the Mythology of Werewolves",
    "The History and Evolution of Werewolf Beliefs"
  ]
}
```
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#8>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 758, in search
    to_grabs = to_grabs + [targets[0]]
IndexError: list index out of range

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
look.search("What are werewolves?")
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

4.550257444381714 s {"Articles":["African American werewolves", "The History of werewolves", "Werewolf lore from around the world"]}
targets:  []
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#10>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 752, in search
    to_grabs = to_grabs + [targets[0]]
IndexError: list index out of range

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
look.search("What are werewolves?")
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

10.21950888633728 s ```json
{
  "Articles": [
    "Folklore",
    "Mythology",
    "Lycanthropy"
  ]
}
```
targets:  ['A/Folklore', 'A/Adze_(folklore)', 'A/African_folklore', 'A/Afrikaans_folklore', 'A/Akateko_(folklore)', 'A/Akuma_(folklore)', 'A/Al_(folklore)', 'A/Albanian_folklore', 'A/Almas_(folklore)', 'A/Alp_(folklore)', 'A/Alpine_folklore', 'A/American_Folklore', 'A/American_folklore', 'A/Appalachian_folklore', 'A/Applied_folklore', 'A/Arab_Folklore', 'A/Arab_folklore', 'A/Armenian_folklore', 'A/Arshi_(folklore)', 'A/Australian_folklore']
targets:  ['A/Mythology', 'A/!Kung_mythology', 'A/!Xu_mythology', 'A/!Xũ_mythology', 'A/Aba_(mythology)', 'A/Ababil_(mythology)', 'A/Aban_(mythology)', 'A/Abantiades_(mythology)', 'A/Abaris_(mythology)', 'A/Abas_(mythology)', 'A/Abenaki_mythology', 'A/Abia_(mythology)', 'A/Ablerus_(mythology)', 'A/Aboriginal_Mythology', 'A/Aboriginal_mythology', 'A/Aborigine_mythology', 'A/Aborigines_(mythology)', 'A/Abrahamic_Mythology', 'A/Abrahamic_mythology', 'A/Abuk_(mythology)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
to_grabs:  ['A/Folklore', 'A/Mythology', 'A/Lycanthropy']
<h2>Folklore</h2>


Folklore is the body of expressive culture shared by a particular group of <span id="People" title onclick="linkClicked(event);" style="color:blue;">people</span> , <span id="Culture" title onclick="linkClicked(event);" style="color:blue;">culture</span>  or <span id="Subculture" title onclick="linkClicked(event);" style="color:blue;">subculture</span> .[1] This includes <span id="Oral_traditions" title onclick="linkClicked(event);" style="color:blue;">oral traditions</span>  such as <span id="Narrative" title onclick="linkClicked(event);" style="color:blue;">tales</span> , <span id="Myth" title onclick="linkClicked(event);" style="color:blue;">myths</span> , <span id="Legend" title onclick="linkClicked(event);" style="color:blue;">legends</span> ,[lower-alpha 1]
<span id="Proverbs" title onclick="linkClicked(event);" style="color:blue;">proverbs</span> , <span id="Poetry" title onclick="linkClicked(event);" style="color:blue;">poems</span> , <span id="Jokes" title onclick="linkClicked(event);" style="color:blue;">jokes</span> , and other oral traditions.[3][4] This also includes <span id="Material_culture" title onclick="linkClicked(event);" style="color:blue;">material culture</span> , such as traditional building styles common to the group. Folklore also encompasses customary lore, taking actions for folk beliefs, and the forms and rituals of celebrations such as <span id="Christmas" title onclick="linkClicked(event);" style="color:blue;">Christmas</span> , weddings, <span id="Folk_dance" title onclick="linkClicked(event);" style="color:blue;">folk dances</span> , and <span id="Rite_of_passage" title onclick="linkClicked(event);" style="color:blue;">initiation rites</span> .[3]
For other uses, see <span id="Folklore_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Folklore (disambiguation)</span> .
A <span id="European_folklore" title onclick="linkClicked(event);" style="color:blue;">European folk tale</span> , <span id="Little_Red_Riding_Hood" title onclick="linkClicked(event);" style="color:blue;">Little Red Riding Hood</span> ; illustration by <span id="Jessie_Willcox_Smith" title onclick="linkClicked(event);" style="color:blue;">Jessie Willcox Smith</span> , 1911A German folk tale, <span id="Hansel_and_Gretel" title onclick="linkClicked(event);" style="color:blue;">Hansel and Gretel</span> ; illustration by <span id="Arthur_Rackham" title onclick="linkClicked(event);" style="color:blue;">Arthur Rackham</span> , 1909
Each one of these, either singly or in combination, is considered a <span id="Cultural_artifact" title onclick="linkClicked(event);" style="color:blue;">folklore artifact</span>  or <span id="Cultural_expressions" title onclick="linkClicked(event);" style="color:blue;">traditional cultural expression</span> . Just as essential as the form, folklore also encompasses the transmission of these artifacts from one region to another or from one generation to the next. Folklore is not something one can typically gain from a formal school curriculum or study in the <span id="Fine_arts" title onclick="linkClicked(event);" style="color:blue;">fine arts</span> . Instead, these traditions are passed along informally from one individual to another, either through verbal instruction or demonstration.[5]
The academic study of folklore is called <span id="Folklore_studies" title onclick="linkClicked(event);" style="color:blue;">folklore studies</span>  or folkloristics, and it can be explored at the undergraduate, graduate, and Ph.D. levels.[6]

<h3>Overview</h3>

<h3>Origin and development of folklore studies</h3>

<h3>Definition of "folk"</h3>

<h3>Folklore genres</h3>

<h3>Folklore performance in context</h3>

<h3>See also</h3>

For a list of folklore of European countries, see <span id="European_folklore" title onclick="linkClicked(event);" style="color:blue;">European folklore</span> .
<span id="Applied_folklore" title onclick="linkClicked(event);" style="color:blue;">Applied folklore</span> 
<span id="Costumbrismo" title onclick="linkClicked(event);" style="color:blue;">Costumbrismo</span> 
<span id="Intangible_cultural_heritage" title onclick="linkClicked(event);" style="color:blue;">Intangible cultural heritage</span> 
<span id="Memetics" title onclick="linkClicked(event);" style="color:blue;">Memetics</span> 
<span id="The_law_of_conservation_of_misery" title onclick="linkClicked(event);" style="color:blue;">The law of conservation of misery</span> 

<h3>Notes</h3>

A legend is a traditional story sometimes popularly regarded as unauthenticated.[2]
The word folkloristics is favored by Alan Dundes, and used in the title of his publication <span id="#CITEREFDundes1978" class onclick="linkClicked(event);" style="color:blue;">Dundes 1978</span> ; the term folklore studies is defined and used by <span id="Simon_Bronner" title onclick="linkClicked(event);" style="color:blue;">Simon Bronner</span> , see <span id="#CITEREFBronner1986" class onclick="linkClicked(event);" style="color:blue;">Bronner 1986</span> , p. xi.
Contributors of this issue were, among others, Claire Farrer, Joan N. Radner, Susan Lanser, Elaine Lawless, and Jeannie B. Thomas.
<span id="Vladimir_Propp" title onclick="linkClicked(event);" style="color:blue;">Vladimir Propp</span>  first defined a uniform structure in Russian fairy tales in his groundbreaking monograph Morphology of the Folktale, published in Russian in 1928. See <span id="#CITEREFPropp1968" class onclick="linkClicked(event);" style="color:blue;">Propp 1968</span> 
<span id="Henry_Glassie" title onclick="linkClicked(event);" style="color:blue;">Henry Glassie</span> , a distinguished folklorist studying technology in cultural context, notes that in Turkish one word, sanat, refers to all objects, not distinguishing between art and craft. The latter distinction, Glassie emphasizes, is not based on medium but on social class. This raises the question as to the difference between arts and crafts; is the difference found merely in the labeling?
The folklorist <span id="Archie_Green" title onclick="linkClicked(event);" style="color:blue;">Archie Green</span>  specialized in workers' traditions and the lore of labor groups.
A more extensive discussion of this can be found in "The 'Text/Context' Controversy and the Emergence of Behavioral Approaches in Folklore", <span id="#CITEREFGabbert1999" class onclick="linkClicked(event);" style="color:blue;">Gabbert 1999</span> 
See <span id="https://web.archive.org/web/20160303215849/http://www.estonica.org/en/Culture/The_art_of_dance/Folk_dance/" class onclick="linkClicked(event);" style="color:blue;">"Folk dance"</span> . Estonica. Archived from <span id="http://www.estonica.org/en/Culture/The_art_of_dance/Folk_dance/" class onclick="linkClicked(event);" style="color:blue;">the original</span>  on 2016-03-03.
Anderson is best known for his monograph <span id="King_John_and_the_Bishop" title onclick="linkClicked(event);" style="color:blue;">Kaiser und Abt</span>  (Folklore Fellows' Communications 42, Helsinki 1923) on folktales of type AT 922.

<h3>References</h3>

<h3>Further reading</h3>

<h3>Further reading</h3>

Wikimedia Commons has media related to <span id="https://commons.wikimedia.org/wiki/Category:Wiki%20Loves%20Folklore%202024%20in%20Uganda" title onclick="linkClicked(event);" style="color:blue;">Wiki Loves Folklore 2024 in Uganda</span> .
<span id="http://www.folklore.ee/Folklore/" class onclick="linkClicked(event);" style="color:blue;">"Folklore – Electronic Journal of Folklore"</span> . Folklore.ee.

Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#12>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 761, in search
    title = BeautifulSoup(sec[0],features="lxml").get_text()
NameError: name 'BeautifulSoup' is not defined

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
                                                                                                                                                             
look.search("What are werewolves?")
                                                                                                                                                             
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.053185701370239 s ["Werewolf", "Wolf-Like Creatures", "Lycanthropy"]
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  []
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#14>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 753, in search
    to_grabs = to_grabs + [targets[0]]
IndexError: list index out of range

========= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =========
look = article_lookup(arc)
                                                                                                                                                             
look.search("What are werewolves?")
                                                                                                                                                             
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.377872467041016 s {"Articles":["Werewolf", "Lycanthropy", "Cultural and religious depictions of Werewolves"]}
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Werewolf', 'A/Lycanthropy']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#16>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 786, in search
    secs = list_ouput_gatherer(output["message"]['content'])
NameError: name 'list_ouput_gatherer' is not defined. Did you mean: 'list_output_gatherer'?

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
look = article_lookup(arc)
                                                                                                                                                             
look.search("What are werewolves?")
                                                                                                                                                             
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.824974298477173 s ```json
{
  "Articles": [
    "Werewolf",
    "Lycanthropy",
    "History of Werewolves"
  ]
}
```
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Werewolf', 'A/Lycanthropy']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
42.22417998313904 s  Sections: ['The core question is about werewolves, so all sections related to this topic should be considered.', 'Looking at the provided titles, I see']
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#18>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 789, in search
    sec_list = sec_list + [(art[0],secs)]
UnboundLocalError: local variable 'sec_list' referenced before assignment

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

6.627748727798462 s I'm sorry, but I can't assist with that request.
to_grabs:  []
article sections:
background text: 
--------

--------
Getting answer
14.86407470703125 s Final answer:
--------
I'm sorry, but I cannot summarize or synthesize your request as you have not provided any specific information about the articles attached to your message. Could you please provide me with more details about the questions or topics you would like to explore? Additionally, if there is a particular question that you are interested in answering, please let me know and I will do my best to help you analyze it within the context of the available information.
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.652469635009766 s ```json
{
  "Articles": [
    "Werewolf",
    "Werewolf Mythology",
    "Vampires"
  ]
}
```
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  []
targets:  ['A/Vampires', 'A/Vampires_3', 'A/Chicagoland_Vampires', 'A/Countdown_Vampires', 'A/Countdown_vampires', 'A/Daeva_(Vampires)', 'A/Emotional_vampires', 'A/Energy_Vampires', 'A/Hollywood_Vampires', 'A/Les_Vampires', 'A/Les_vampires', 'A/Lesbian_vampires', 'A/Live!_Vampires', 'A/Modern_Vampires', 'A/Morganville_Vampires', 'A/Outback_Vampires', 'A/Philippine_vampires', 'A/Phillipine_vampires', 'A/Psychic_vampires', 'A/Reverse_vampires']
to_grabs:  ['A/Werewolf', 'A/Vampires']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Vampire
     Vampire
     Etymology and word distribution
     Folk beliefs
     Origins of vampire beliefs
     In modern culture
     Notes
     References
Getting relevant for:  Werewolf
3.7227447032928467 s  Sections: ['Names', 'History']
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 867, in <module>
    look.search("What are werewolves?")
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 786, in search
    sec_list = sec_list + [(art[0],secs)]
UnboundLocalError: local variable 'sec_list' referenced before assignment

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.347348690032959 s {"Articles":["List of werewolf myths", "Lycanthropy", "History of werewolf legends"]}
targets:  []
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Lycanthropy']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
4.494686841964722 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 867, in <module>
    look.search("What are werewolves?")
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 791, in search
    art_text = art_text + "###Article: "+art[0] + "\n"
TypeError: can only concatenate str (not "tuple") to str

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.711992263793945 s [1] "Werewolf"
[2] "Lycanthropy"
[3] "Wolfman"
to_grabs:  []
article sections:
--------
--------
[]
--------
--------
background text: 
--------

--------
Getting answer
10.587675333023071 s Final answer:
--------
I'm sorry, but you haven't provided any specific articles for me to analyze. Please attach or provide the articles that you would like me to summarize and synthesize, and I will be happy to help answer your question with a brief summary and follow-up points.
--------
S = """[1] "Werewolf"
[2] "Lycanthropy"
[3] "Wolfman""""
                                                                                                                                                             
SyntaxError: incomplete input
S = """[1] "Werewolf"
[2] "Lycanthropy"
[3] "Wolfman""""
                                                                                                                                                             
SyntaxError: incomplete input
S = """[1] "Werewolf"
[2] "Lycanthropy"
[3] "Wolfman"
"""
                                                                                                                                                             
S
                                                                                                                                                             
'[1] "Werewolf"\n[2] "Lycanthropy"\n[3] "Wolfman"\n'
list_output_gatherer(S)
                                                                                                                                                             
[]
re.sub("\[\d+\]","|",S)
                                                                                                                                                             
'| "Werewolf"\n| "Lycanthropy"\n| "Wolfman"\n'

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.152045726776123 s ["Werewolf (mythology)", "Lycanthropy", "Cultural and Mythological Significance of Werewolves"]
targets:  []
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Lycanthropy']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
19.430088758468628 s  Sections: ['Names', 'History', 'Folk beliefs']
--------
--------
[[('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ('Names', 'The Modern English \nwerewolf descends from the Old English \nwer(e)wulf, which is a cognate  of Middle Dutch \nweerwolf, Middle Low German \nwarwulf, werwulf, Middle High German \nwerwolf, and West Frisian \nwaer-ûl(e).[1] These terms are generally derived from a Proto-Germanic  form reconstructed  as *wira-wulfaz (\'man-wolf\'), itself from an earlier Pre-Germanic  form *wiro-wulpos.[2][3][4] An alternative reconstruction, *wazi-wulfaz (\'wolf-clothed\'), would bring the Germanic compound  closer to the Slavic meaning,[2] with other semantic parallels in Old Norse \núlfheðnar (\'wolf-skinned\') and úlfheðinn (\'wolf-coat\'), Old Irish \nluchthonn (\'wolf-skin\'), and Sanskrit \nVṛkājina (\'Wolf-skin\').[5]\nThe Norse branch underwent taboo modifications , with Old Norse vargúlfr (only attested as a translation of Old French \ngarwaf ~ garwal(f) from Marie\'s lay  of Bisclavret ) replacing *wiraz (\'man\') with vargr (\'wolf, outlaw\'), perhaps under the influence of the Old French expression leus warous ~ lous garous (modern loup-garou), which literally means \'wolf-werewolf\'.[6][7] The modern Norse form varulv (Danish, Norwegian and Swedish) was either borrowed from Middle Low German werwulf,[7] or else derived from an unattested Old Norse *varulfr, posited as the regular descendant of Proto-Germanic *wira-wulfaz.[3] An Old Frankish  form *werwolf is inferred from the Middle Low German variant and was most likely borrowed into Old Norman \ngarwa(l)f ~ garo(u)l, with regular Germanic –Romance  correspondence w- / g- (cf. William / Guillaume, Wales / Galles, etc.).[7][8]\nThe Proto-Slavic  noun *vьlko-dlakь, meaning "wolf-haired" (cf. *dlaka, "animal hair", "fur"),[2] can be reconstructed from Serbian vukòdlak, Slovenian \nvołkodlȃk, and Czech vlkodlak, although formal variations in Slavic languages  (*vьrdl(j)ak, *vьlkdolk, *vьlklak) and the late attestation of some forms pose difficulties in tracing the origin of the term.[9][10] The Greek\nVrykolakas  and Romanian \nVîrcolac, designating vampire-like creatures in Balkan folklores, were borrowed from Slavic languages.[11][12] The same form is also found in other non-Slavic languages of the region, such as Albanian vurvolak and Turkish vurkolak.[12]\nBulgarian \nvьrkolak and Church Slavonic \nvurkolak may be interpreted as back-borrowings from Greek.[10] The name vurdalak  (вурдалак; \'ghoul, revenant\') first appeared in Russian poet Alexander Pushkin \'s work Pesni, published in 1835. The source of Pushkin\'s distinctive form remains debated in scholarship.[13][12]\nA Proto-Celtic  noun *wiro-kū, meaning \'man-dog\', has been reconstructed from Celtiberian \nuiroku, the Old Brittonic  place-name Viroconium  (Old Irish  noun ferchu (\'male dog, fierce dog\'), and the medieval personal names Guurci (Old Welsh ) and Gurki (Old Breton ). Wolves were metaphorically designated as \'dogs\' in Celtic cultures.[14][4]\nThe modern term lycanthropy comes from Ancient Greek \nlukanthrōpía (λυκανθρωπία), itself from lukánthrōpos (λυκάνθρωπος), meaning \'wolf-man\'. Ancient writers used the term solely in the context of clinical lycanthropy , a condition in which the patient imagined himself to be a wolf. Modern writers later used lycanthrope as a synonym of werewolf, referring to a person who, according to medieval superstition, could assume the form of wolves.[15]\n'), ('History', 'Indo-European comparative mythology\nThe European motif of the devilish werewolf devouring human flesh harks back to a common development during the Middle Ages  in the context of Christianity, although stories of humans turning into wolves take their roots in earlier pre-Christian beliefs.[16][17]\nTheir underlying common origin can be traced back to Proto-Indo-European mythology , where lycanthropy is reconstructed as an aspect of the initiation of the kóryos  warrior class, which may have included a cult focused on dogs and wolves identified with an age grade of young, unmarried warriors.[4] The standard comparative overview of this aspect of Indo-European mythology is McCone (1987).[18]\nClassical antiquity\nAncient Greek literature  and Folklore . Herodotus , in his Histories ,[19] wrote that according to what the Scythians and the Greeks settled in Scythia told him, the Neuri , which was a tribe to the north-east of Scythia , were all transformed into wolves once every year for several days and then changed back to their human shape. He added that he is not convinced by the story but the locals swear to its truth.[20] This tale was also mentioned by Pomponius Mela .[21]\nIn the second century BC, the Greek geographer Pausanias  related the story of King Lycaon  of Arcadia, who was transformed into a wolf because he had sacrificed a child in the altar of Zeus Lycaeus.[22] In the version of the legend told by Ovid  in his Metamorphoses ,[23] when Zeus  visits Lycaon disguised as a common man, Lycaon wants to test if he is really a god. To that end, he kills a Molossian hostage and serve his entrails to Zeus. Disgusted, the god turns Lycaon into a wolf. However, in other accounts of the legend, like that of Apollodorus\'  Bibliotheca,[24] Zeus blasts him and his sons with thunderbolts as punishment.\nPausanias also relates the story of an Arcadian man called Damarchus  of Parrhasia, who was turned into a wolf after tasting the entrails of a human child sacrificed to Zeus  Lycaeus. He was restored to human form 10 years later and went on to become an Olympic champion.[25] This tale is also recounted by Pliny the Elder , who calls the man Demaenetus quoting Agriopas .[26] According to Pausanias, this was not a one-off event, but that men have been transformed into wolves during the sacrifices to Zeus Lycaeus since the time of Lycaon. If they abstain from tasting human flesh while being wolves, they would be restored to human form nine years later, but if they do not abstain, they would remain wolves forever.[22]\nLykos (Λύκος) of Athens was a wolf-shaped herο, whose shrine stood by the jurycourt, and the first jurors were named after him.[27]\nPliny the Elder likewise recounts another tale of lycanthropy. Quoting Euanthes,[28] he mentions that in Arcadia , once a year a man was chosen by lot from the Anthus\' clan. The chosen man was escorted to a marsh in the area, where he hung his clothes into an oak  tree, swam across the marsh and transformed into a wolf, joining a pack  for nine years. If during these nine years he refrained from tasting human flesh, he returned to the same marsh, swam back, and recovered his previous human form, with nine years added to his appearance.[29] Ovid also relates stories of men who roamed the woods of Arcadia  in the form of wolves.[30][31]\nVirgil , in his poetic work Eclogues , wrote about a man called Moeris, who used herbs and poisons picked in his native Pontus  to turn himself into a wolf.[32] In prose , the Satyricon , written circa AD 60 by Gaius Petronius Arbiter , one of the characters, Niceros, tells a story at a banquet about a friend who turned into a wolf (chs. 61–62). He describes the incident as follows, "When I look for my buddy I see he\'d stripped and piled his clothes by the roadside... He pees in a circle round his clothes and then, just like that, turns into a wolf!... after he turned into a wolf he started howling and then ran off into the woods."[33]\nEarly Christian authors also mentioned werewolves. In The City of God, Augustine of Hippo  gives an account similar to that found in Pliny the Elder. Augustine explains that "It is very generally believed that by certain witches spells men may be turned into wolves..."[34] Physical metamorphosis was also mentioned in the Capitulatum Episcopi, attributed to the Council of Ancyra  in the 4th century, which became the Church\'s doctrinal text in relation to magic, witches, and transformations such as those of werewolves.[35] The Capitulatum Episcopi states that "Whoever believes that anything can be...transformed into another species or likeness, except by God Himself...is beyond doubt an infidel.\'[35]\nIn these works of Roman writers, werewolves often receive the name versipellis ("turnskin"). Augustine instead uses the phrase "in lupum fuisse mutatum" (changed into the form of a wolf) to describe the physical metamorphosis of werewolves, which is similar to phrases used in the medieval period.\nMiddle Ages\nThere is evidence of widespread belief in werewolves in medieval Europe. This evidence spans much of the Continent, as well as the British Isles. Werewolves were mentioned in Medieval law codes, such as that of King Cnut , whose Ecclesiastical Ordinances inform us that the codes aim to ensure that "...the madly audacious werewolf do not too widely devastate, nor bite too many of the spiritual flock."[36]\nLiutprand of Cremona  reports a rumor that Bajan, son of Simeon I of Bulgaria , could use magic to turn himself into a wolf.[37] The works of Augustine of Hippo had a large influence on the development of Western Christianity, and were widely read by churchmen of the medieval period; and these churchmen occasionally discussed werewolves in their works. Famous examples include Gerald of Wales \'s Werewolves of Ossory , found in his Topographica Hibernica, and in Gervase of Tilbury\'s\nOtia Imperiala , both written for royal audiences.\nGervase reveals to the reader that belief in such transformations (he also mentions women turning into cats and into snakes) was widespread across Europe; he uses the phrase "que ita dinoscuntur" when discussing these metamorphoses, which translates to "it is known". Gervase, who was writing in Germany, also tells the reader that the transformation of men into wolves cannot be easily dismissed, for "...in England we have often seen men change into wolves" ("Vidimus enim frequenter in Anglia per lunationes homines in lupos mutari...").[38] Further evidence of the widespread belief in werewolves and other human-animal transformations can be seen in theological attacks made against such beliefs. Conrad of Hirsau , writing in the 11th century, forbids the reading of stories in which a person\'s reason is obscured following such a transformation.[39] Conrad specifically refers to the tales of Ovid in his tract. Pseudo-Augustine, writing in the 12th century, follows Augustine of Hippo\'s argument that no physical transformation can be made by any but God, stating that "...the body corporeally [cannot], be changed into the material limbs of any animal.\'[40]\nMarie de France \'s poem Bisclavret  (c. 1200) is another example, in which the eponymous nobleman Bisclavret, for reasons not described, had to transform into a wolf every week. When his treacherous wife stole his clothing needed to restore his human form, he escaped the king\'s wolf hunt by imploring the king for mercy and accompanied the king thereafter. His behavior at court was gentle, until his wife and her new husband appeared at court, so much so that his hateful attack on the couple was deemed justly motivated, and the truth was revealed. This lai  (a type of Breton sung-poem) follows many themes found within other werewolf tales – the removal of clothing and attempting to refrain from the consumption of human flesh can be found in Pliny the Elder, as well as in the second of Gervase of Tilbury\'s werewolf stories, about a werewolf by the name of Chaucevaire. Marie also reveals to us the existence of werewolf belief in Breton and Norman France, by telling us the Franco-Norman word for werewolf: garwulf, which, she explains, are common in that part of France, where "...many men turned into werewolves".[41] Gervase also supports this terminology when he tells us that the French use the term "gerulfi" to describe what the English call "werewolves".[42]\nMelion  and Biclarel are two anonymous lais that share the theme of a werewolf knight being betrayed by his wife.[43]\nThe German word werwolf was recorded by Burchard von Worms  in the 11th century and Bertold of Regensburg  in the 13th century but is not recorded in all of medieval German poetry or fiction. While Baring-Gould argues that references to werewolves were also rare in England, presumably because whatever significance the "wolf-men" of Germanic paganism had carried, the associated beliefs and practices had been successfully repressed after Christianization (or if they persisted, they did so outside of the sphere of literacy available to us), we have sources other than those mentioned above.[44] Such examples of werewolves in Ireland and the British Isles can be found in the work of the 9th century Welsh monk Nennius ; female werewolves appear in the Irish work Tales of the Elders , from the 12th century; and Welsh werewolves in the 12th to 13th century work, Mabinogion .\nGermanic pagan traditions associated with wolf-men persisted longest in the Scandinavian Viking Age . Harald I of Norway  is known to have had a body of Úlfhednar  (wolf-coated [men]), which are mentioned in the Vatnsdœla, Haraldskvæði, and the Völsunga saga , and resemble some werewolf legends. The Úlfhednar were fighters similar to the berserkers, though they dressed in wolf hides  rather than those of bears and were reputed to channel the spirits of these animals to enhance effectiveness in battle.[45] These warriors were resistant to pain and killed viciously in battle, much like wild animals. Úlfhednar and berserkers are closely associated with the Norse god Odin .\nThe Scandinavian traditions of this period may have spread to Kievan Rus\' , giving rise to the Slavic "werewolf" tales. The 11th-century Belarusian  Prince Vseslav of Polotsk  was considered to have been a werewolf, capable of moving at superhuman speeds, as recounted in The Tale of Igor\'s Campaign :\nVseslav the prince judged men; as prince, he ruled towns; but at night he prowled in the guise of a wolf. From Kiev, prowling, he reached, before the cocks crew, Tmutorokan . The path of Great Sun, as a wolf, prowling, he crossed. For him in Polotsk they rang for matins early at St. Sophia the bells; but he heard the ringing in Kiev.\nThe situation as described during the medieval period gives rise to the dual form of werewolf folklore in Early Modern Europe. On one hand the "Germanic" werewolf, which becomes associated with the witchcraft panic , and on the other hand the "Slavic" werewolf or vlkolak , which becomes associated with the concept of the revenant  or "vampire". The "eastern" werewolf-vampire is found in the folklore of Central and Eastern Europe, including Hungary, Romania and the Balkans, while the "western" werewolf-sorcerer is found in France, German-speaking Europe and in the Baltic.\nBeing a werewolf was a common accusation in witch trials throughout their history, and it featured even in the Valais witch trials , one of the earliest such trials altogether, in the first half of the 15th century.[46]\nIn 1539, Martin Luther  used the form beerwolf  to describe a hypothetical ruler worse than a tyrant who must be resisted.[47]\nIn \'Historia de Gentibus Septentrionalibus \' (1555), Olaus Magnus  describes (Book 18, Chapter 45) an annual assembly of werewolves near the Lithuania-Courland border. The participants, including Lithuanian nobility and werewolves from the surrounding areas, gather to test their strength by attempting to jump over a castle wall\'s ruins. Those who succeed are regarded as strong, while weaker participants are punished with whippings.[48]\nEarly modern history\nFurther information: Werewolf witch trials  and Wolfssegen \nThere were numerous reports of werewolf attacks – and consequent court trials – in 16th-century France. In some of the cases there was clear evidence against the accused of murder and cannibalism , but no association with wolves. In other cases people have been terrified by such creatures, such as that of Gilles Garnier  in Dole  in 1573, who was convicted of being a werewolf.[49]\nA peak of attention to lycanthropy came in the late 16th to early 17th century, as part of the European witch-hunts .\nA number of treatises on werewolves were written in France during 1595 and 1615. Werewolves were sighted in 1598 in Anjou , and a teenage werewolf was sentenced to life imprisonment in Bordeaux  in 1603. Henry Boguet  wrote a lengthy chapter about werewolves in 1602. In the Vaud, werewolves were convicted in 1602 and in 1624. A treatise by a Vaud pastor in 1653, however, argued that lycanthropy was purely an illusion. After this, the only further record from the Vaud dates to 1670: it is that of a boy who claimed he and his mother could change themselves into wolves, which was, however, not taken seriously. At the beginning of the 17th century witchcraft  was prosecuted by James I of England , who regarded "warwoolfes" as victims of delusion induced by "a natural superabundance of melancholic".[50]\nAfter 1650, belief in lycanthropy had mostly disappeared from French-speaking Europe, as evidenced in Diderot\'s Encyclopedia , which attributed reports of lycanthropy to a "disorder of the brain".[51] Although there were continuing reports of extraordinary wolflike beasts, they were not considered to be werewolves. One such report concerned the Beast of Gévaudan , which terrorized the general area of the former province  of Gévaudan , now called Lozère , in south-central France; from the years 1764 to 1767, it killed upwards of 80 men, women, and children.\nThe part of Europe which showed more vigorous interest in werewolves after 1650 was the Holy Roman Empire . At least nine works on lycanthropy were printed in Germany between 1649 and 1679. In the Austrian and Bavarian Alps, belief in werewolves persisted well into the 18th century.[52] In any case, as late as in 1853, in Galicia , northwestern Spain, Manuel Blanco Romasanta  was judged and condemned as the author of a number of murders, but he claimed to be not guilty because of his condition of lobishome, werewolf.\nUntil the 20th century, wolf attacks on humans  were an occasional, but still widespread, feature of life in Europe.[53]\nSome scholars have suggested that it was inevitable that wolves, being the most feared predators in Europe, were projected into the folklore of evil shapeshifters. This is said to be corroborated by the fact that areas devoid of wolves typically use different kinds of predator to fill the niche; werehyenas  in Africa, weretigers  in India,[45] as well as werepumas ("runa uturuncu")[54][55] and werejaguars ("yaguaraté-abá" or "tigre-capiango")[56][57] in southern South America.\nAn idea is explored in Sabine Baring-Gould \'s work The Book of Werewolves is that werewolf legends may have been used to explain serial killings . Perhaps the most infamous example is the case of Peter Stumpp  (executed in 1589), the German farmer, and alleged serial killer and cannibal , also known as the Werewolf of Bedburg.[58]\nAsian cultures\nSee also: Asena  and Itbarak \nCommon Turkic folklore  holds a different, reverential light to the werewolf legends in that Turkic Central Asian shamans  after performing long and arduous rites would voluntarily be able to transform into the humanoid "Kurtadam" (literally meaning "Wolfman"). Since the wolf was the totemic ancestor animal of the Turkic peoples, they would be respectful of any shaman who was in such a form.\n'), ('Lycanthropy as a medical condition', "See also: Hypertrichosis  and Clinical lycanthropy \nSome modern researchers have tried to explain the reports of werewolf behaviour with recognised medical conditions. Dr Lee Illis of Guy's Hospital  in London wrote a paper in 1963 entitled On Porphyria and the Aetiology of Werewolves in which he argues that historical accounts on werewolves could have in fact been referring to victims of congenital porphyria , stating how the symptoms of photosensitivity , reddish teeth, and psychosis  could have been grounds for accusing a person of being a werewolf.[59] This is, however, argued against by Woodward, who points out how mythological werewolves were almost invariably portrayed as resembling true wolves and that their human forms were rarely physically conspicuous as porphyria victims.[45] Others have pointed out the possibility of historical werewolves having been people with hypertrichosis , a hereditary condition manifesting itself in excessive hair growth. However, Woodward dismissed the possibility, as the rarity of the disease ruled it out from happening on a large scale as werewolf cases were in medieval Europe.[45]\nWoodward suggested rabies  as the origin of werewolf beliefs, claiming remarkable similarities between the symptoms of that disease and some of the legends. Woodward focused on the idea that being bitten by a werewolf could result in the victim turning into one, which suggested the idea of a transmittable disease like rabies.[45] However, the idea that lycanthropy could be transmitted in this way is not part of the original myths and legends and only appears in relatively recent beliefs. Lycanthropy can also be met with as the main content of a delusion, for example, the case of a woman has been reported who during episodes of acute psychosis complained of becoming four different species of animals.[60]\n"), ('Folk beliefs', 'Further information: Shapeshifting \nCharacteristics\nThe beliefs classed together under lycanthropy are far from uniform, and the term is somewhat capriciously applied. The transformation may be temporary or permanent; the were-animal may be the man himself metamorphosed; may be his double  whose activity leaves the real man to all appearance unchanged; may be his soul , which goes forth seeking whomever it may devour, leaving its body in a state of trance ; or it may be no more than the messenger of the human being, a real animal or a familiar spirit , whose intimate connection with its owner is shown by the fact that any injury to it is believed, by a phenomenon known as repercussion, to cause a corresponding injury to the human being.\nWerewolves were said in European folklore to bear tell-tale physical traits even in their human form. These included the meeting of both eyebrows  at the bridge of the nose, curved fingernails, low-set ears and a swinging stride. One method of identifying a werewolf in its human form was to cut the flesh of the accused, under the pretense that fur would be seen within the wound. A Russian superstition recalls a werewolf can be recognized by bristles under the tongue.[45]\nThe appearance of a werewolf in its animal form varies from culture to culture, though it is most commonly portrayed as being indistinguishable from ordinary wolves save for the fact that it has no tail (a trait thought characteristic of witches in animal form), is often larger, and retains human eyes and a voice. According to some Swedish accounts, the werewolf could be distinguished from a regular wolf by the fact that it would run on three legs, stretching the fourth one backwards to look like a tail.[61] After returning to their human forms, werewolves are usually documented as becoming weak, debilitated and undergoing painful nervous depression.[45]\nOne universally reviled trait in medieval Europe was the werewolf\'s habit of devouring recently buried corpses, a trait that is documented extensively, particularly in the Annales Medico-psychologiques in the 19th century.[45]\nBecoming a werewolf\nVarious methods for becoming a werewolf have been reported, one of the simplest being the removal of clothing and putting on a belt made of wolfskin, probably as a substitute for the assumption of an entire animal skin (which also is frequently described).[62] In other cases, the body is rubbed with a magic salve .[62] Drinking rainwater out of the footprint of the animal in question or from certain enchanted streams were also considered effectual modes of accomplishing metamorphosis.[63]\nThe 16th-century Swedish writer Olaus Magnus  says that the Livonian  werewolves were initiated by draining a cup of specially prepared beer and repeating a set formula. Ralston in his Songs of the Russian People gives the form of incantation still familiar in Russia. In Italy, France and Germany, it was said that a man or woman could turn into a werewolf if he or she, on a certain Wednesday or Friday, slept outside on a summer night with the full moon shining directly on his or her face.[45]\nIn other cases, the transformation was supposedly accomplished by Satanic  allegiance for the most loathsome ends, often for the sake of sating a craving for human flesh. "The werewolves", writes Richard Verstegan  (Restitution of Decayed Intelligence, 1628), are certayne sorcerers, who having annoynted their bodies with an ointment which they make by the instinct of the devil, and putting on a certayne inchaunted girdle, does not only unto the view of others seem as wolves, but to their own thinking have both the shape and nature of wolves, so long as they wear the said girdle. And they do dispose themselves as very wolves, in worrying and killing, and most of humane creatures.\nThe phenomenon of repercussion, the power of animal metamorphosis , or of sending out a familiar , real or spiritual, as a messenger, and the supernormal powers conferred by association with such a familiar, are also attributed to the magician , male and female, all the world over; and witch  superstitions are closely parallel to, if not identical with, lycanthropic beliefs, the occasional involuntary character of lycanthropy being almost the sole distinguishing feature. In another direction the phenomenon of repercussion is asserted to manifest itself in connection with the bush-soul of the West African and the nagual  of Central America ; but though there is no line of demarcation to be drawn on logical grounds, the assumed power of the magician and the intimate association of the bush-soul or the nagual with a human being are not termed lycanthropy.\nThe curse of lycanthropy was also considered by some scholars as being a divine punishment . Werewolf literature shows many examples of God  or saints  allegedly cursing those who invoked their wrath with lycanthropy. Such is the case of Lycaon , who was turned into a wolf by Zeus  as punishment for slaughtering one of his own sons and serving his remains to the gods as a dinner. Those who were excommunicated  by the Roman Catholic Church  were also said to become werewolves.[45]\nThe power of transforming others into wild beasts was attributed not only to malignant sorcerers, but to Christian saints  as well. Omnes angeli, boni et Mali, ex virtute naturali habent potestatem transmutandi corpora nostra ("All angels, good and bad , have the power of transmutating our bodies") was the dictum of St. Thomas Aquinas . St. Patrick  was said to have transformed the Welsh  King Vereticus into a wolf; Natalis  supposedly cursed an illustrious Irish family whose members were each doomed to be a wolf for seven years. In other tales the divine agency is even more direct, while in Russia, again, men supposedly became werewolves when incurring the wrath of the Devil.\nA notable exception to the association of Lycanthropy and the Devil, comes from a rare and lesser known account of an 80-year-old man named Thiess . In 1692, in Jürgensburg , Livonia , Thiess testified under oath that he and other werewolves were the Hounds of God.[64]\nHe claimed they were warriors who descended into hell to battle witches and demons . Their efforts ensured that the Devil and his minions did not carry off the grain from local failed crops down to hell. Thiess was ultimately sentenced to ten lashes for idolatry and superstitious belief .\nRemedies\nVarious methods have existed for removing the werewolf form. In antiquity, the Ancient Greeks and Romans believed in the power of exhaustion in curing people of lycanthropy. The victim would be subjected to long periods of physical activity in the hope of being purged of the malady. This practice stemmed from the fact that many alleged werewolves would be left feeling weak and debilitated after committing depredations.[45]\nIn medieval Europe, traditionally, there are three methods one can use to cure a victim of lycanthropy; medicinally (usually via the use of wolfsbane ), surgically, or by exorcism . However, many of the cures advocated by medieval medical practitioners proved fatal to the patients. A Sicilian belief of Arabic origin holds that a werewolf can be cured of its ailment by striking it on the forehead or scalp with a knife. Another belief from the same culture involves the piercing of the werewolf\'s hands with nails. Sometimes, less extreme methods were used. In the German lowland of Schleswig-Holstein, a werewolf could be cured if one were to simply address it three times by its Christian name, while one Danish belief holds that merely scolding a werewolf will cure it.[45] Conversion to Christianity is also a common method of removing lycanthropy in the medieval period; a devotion to St. Hubert  has also been cited as both cure for and protection from lycanthropes.\nConnection to revenants\nFurther information: Revenant\nvampire  was also linked to the werewolf in East European countries, particularly Bulgaria, Serbia and Slovenia. In Serbia, the werewolf and vampire are known collectively as vulkodlak.[45]\nHungary and Balkans\nIn Hungarian  folklore, werewolves are said to live in the region of Transdanubia , and it was thought that the ability to change into a wolf was obtained in infancy, after suffering parental abuse or by a curse. It is told that at the age of seven the boy or the girl leave home at night to go hunting, and can change to a person or wolf whenever they want. The curse can also be obtained in adulthood if a person passes three times through an arch made of birch  with the help of a wild rose \'s spine.\nThe werewolves were known to exterminate all kind of farm animals, especially sheep. The transformation usually occurred during the winter solstice , Easter  and a full moon. Later in the 17th and 18th century, the trials in Hungary were not only conducted against witches, but against werewolves too, and many records exist documenting connections between the two.  Vampires and werewolves are closely related in Hungarian folklore, both being feared in antiquity.[65]\nAmong the South Slavs , and also among the ethnic Kashubian people  in present-day northern Poland, there was the belief that if a child was born with hair, a birthmark, or a caul on their head, they were supposed to possess shape-shifting abilities. Though capable of turning into any animal they wished, it was commonly believed that such people preferred to turn into a wolf.[66]\nSerbian \nvukodlaks traditionally had the habit of congregating annually in the winter months, when they would strip off their wolf skins and hang them from trees. They would then get a hold of another vulkodlak\'s skin and burn it, releasing from its curse the vukodlak from whom the skin came.[45]\nCaucasus\nAccording to Armenian  lore, there are women who, in consequence of deadly sins, are condemned to spend seven years in wolf form.[67] In a typical account, a condemned woman is visited by a wolfskin-toting spirit, who orders her to wear the skin, which causes her to acquire frightful cravings for human flesh soon after. With her better nature overcome, the she-wolf devours each of her own children, then her relatives\' children in order of relationship, and finally the children of strangers. She wanders only at night, with doors and locks springing open at her approach. When morning arrives, she reverts to human form and removes her wolfskin. The transformation is generally said to be involuntary, but there are alternate versions involving voluntary metamorphosis, where the women can transform at will.\nAmericas and Caribbean\nMain article: Skin-walker \nSee also: Soucouyant  and Rougarou \nThe Naskapis believed that the caribou  afterlife is guarded by giant wolves that kill careless hunters venturing too near. The Navajo people  feared witches in wolf\'s clothing called "Mai-cob".[68]\nWoodward thought that these beliefs were due to the Norse colonization of the Americas .[45]\nWhen the European colonization of the Americas  occurred, the pioneers brought their own werewolf folklore with them and were later influenced by the lore of their neighbouring colonies and those of the Natives. Belief in the loup-garou present in Canada  (thence Acadiana ), the Upper and Lower Peninsulas of Michigan ,[69] and upstate New York  originates from French folklore influenced by Native American stories on the Wendigo . In Mexico , there is a belief in a creature called the nagual . In Haiti , there is a superstition that werewolf spirits known locally as Jé-rouge (red eyes) can possess the bodies of unwitting persons and nightly transform them into cannibalistic lupine creatures. The Haitian jé-rouges typically try to trick mothers into giving away their children voluntarily by waking them at night and asking their permission to take their child, to which the disoriented mother may either reply yes or no. The Haitian jé-rouges differ from traditional European werewolves by their habit of actively trying to spread their lycanthropic condition to others, much like vampires.[45]\n'), ('Modern reception', 'Werewolf fiction\nMain article: Werewolf fiction \nMost modern fiction describes werewolves as vulnerable to silver  weapons and highly resistant to other injuries. This feature appears in German folklore of the 19th century.[70] The claim that the Beast of Gévaudan , an 18th-century wolf or wolflike creature, was shot by a silver bullet appears to have been introduced by novelists retelling the story from 1935 onwards and not in earlier versions.[71][72][73] English folklore, prior to 1865, showed shapeshifters to be vulnerable to silver. "...till the publican shot a silver button over their heads when they were instantly transformed into two ill-favoured old ladies..."[74] c. 1640 the city of Greifswald, Germany was infested by werewolves. "A clever lad suggested that they gather all their silver buttons, goblets, belt buckles, and so forth, and melt them down into bullets for their muskets and pistols. ... this time they slaughtered the creatures and rid Greifswald of the lycanthropes."[75]\nThe 1897 novel Dracula  and the short story "Dracula\'s Guest ", both written by Bram Stoker , drew on earlier mythologies of werewolves and similar legendary demons and "was to voice the anxieties of an age", and the "fears of late Victorian\npatriarchy ".[76] In "Dracula\'s Guest", a band of military horsemen coming to the aid of the protagonist chase off Dracula, depicted as a great wolf stating the only way to kill it is by a "Sacred Bullet".[77] This is also mentioned in the main novel Dracula as well. Count Dracula  stated in the novel that legends of werewolves originated from his Szekely  racial bloodline,[78] who himself is also depicted with the ability to shapeshift  into a wolf at will during the night but is unable to do so during the day except at noon.[79]\nThe 1928 novel The Wolf\'s Bride: A Tale from Estonia, written by the Finnish  author Aino Kallas , tells story of the forester Priidik\'s wife Aalo living in Hiiumaa  in the 17th century, who became a werewolf under the influence of a malevolent forest spirit, also known as Diabolus Sylvarum.[80]\nThe first feature film to use an anthropomorphic  werewolf was Werewolf of London  in 1935. The main werewolf of this film is a dapper London scientist who retains some of his style and most of his human features after his transformation,[81] as lead actor Henry Hull  was unwilling to spend long hours being made up by makeup artist Jack Pierce .[82]\nUniversal Studios  drew on a Balkan tale of a plant associated with lycanthropy as there was no literary work to draw upon, unlike the case with vampires. There is no reference to silver nor other aspects of werewolf lore such as cannibalism.[83]\nA more tragic character is Lawrence Talbot , played by Lon Chaney Jr.  in 1941\'s The Wolf Man . With Pierce\'s makeup more elaborate this time,[84] the movie catapulted the werewolf into public consciousness.[81] Sympathetic portrayals are few but notable, such as the comedic but tortured protagonist David Naughton  in An American Werewolf in London ,[85] and a less anguished and more confident and charismatic Jack Nicholson  in the 1994 film Wolf .[86] Over time, the depiction of werewolves has gone from fully malevolent to even heroic creatures, such as in the Underworld  and Twilight  series, as well as Blood Lad , Dance in the Vampire Bund , Rosario + Vampire , and various other movies, anime , manga , and comic books .\nOther werewolves are decidedly more willful and malevolent, such as those in the novel The Howling  and its subsequent sequels and film adaptations . The form a werewolf assumes was generally anthropomorphic in early films such as The Wolf Man and Werewolf of London, but a larger and powerful wolf in many later films.[87]\nWerewolves are often depicted as immune to damage caused by ordinary weapons, being vulnerable only to silver  objects, such as a silver-tipped cane, bullet  or blade ; this attribute was first adopted cinematically in The Wolf Man.[84] This negative reaction to silver is sometimes so strong that the mere touch of the metal on a werewolf\'s skin will cause burns. Current-day werewolf fiction almost exclusively involves lycanthropy being either a hereditary condition or transmitted like an infectious disease  by the bite of another werewolf. In some fiction, the power of the werewolf extends to human form, such as invulnerability to conventional injury due to their healing factor, superhuman speed and strength, and falling on their feet from high falls. Also, aggressiveness and animalistic urges may be intensified and more difficult to control (hunger, sexual arousal). Usually in these cases, the abilities are diminished in human form. In other fiction, it can be cured by medicine men or antidotes.\nAlong with the vulnerability to the silver bullet, the full moon being the cause of the transformation only became part of the depiction of werewolves on a widespread basis in the twentieth century.[88] The first movie to feature the transformative effect of the full moon was Frankenstein Meets the Wolf Man  in 1943.[89]\nWerewolves are typically envisioned as "working-class" monsters, often being low in socio-economic status, although they can represent a variety of social classes and at times were seen as a way of representing "aristocratic decadence" during 19th century horror literature.[90][91][92]\nNazi Germany\nNazi Germany used Werwolf, as the mythical creature\'s name is spelled in German, in 1942–43 as the codename for one of Hitler\'s headquarters . In the war\'s final days, the Nazi "Operation Werwolf " aimed at creating a commando force that would operate behind enemy lines as the Allies advanced through Germany itself.\nTwo fictional depictions of "Operation Werwolf"\xa0–\nthe US television series True Blood  and the 2012 novel Wolf Hunter by J. L. Benét\xa0–\nmix the two meanings of "Werwolf" by depicting the 1945 die-hard Nazi commandos as being actual werewolves.[93]\n'), ('See also', 'Asena\nDamarchus\nKeibu Keioiba\nKitsune\nNagual\nPricolici\nWerecat\nWulver\nWerewolf witch trials\n'), ('Notes', 'Also spelled werwolf. Usually pronounced /ˈwɛərwʊlf/\nWAIR-wuulf, but also sometimes /ˈwɪərwʊlf/\nWEER-wuulf or /ˈwɜːrwʊlf/\nWUR-wuulf.\nPronounced /ˈlaɪkənθroʊp/\nLY-kən-throhp.\n"... the motif of the full moon is a modern invention, since historical sources do not mention it as an instigator of metamorphosis." (de Blécourt 2015 , pp.\xa03–4).\nPronounced /laɪˈkænθrəpi/\nly-KAN-thrə-pee.\nLorey (2000) records 280 known cases; this contrasts with a total number of 12,000 recorded cases of executions for witchcraft, or an estimated grand total of about 60,000, corresponding to 2% or 0.5% respectively. The recorded cases span the period of 1407 to 1725, peaking during the period of 1575–1657.\nLorey (2000) records six trials in the period 1701 and 1725, all in either Styria or Carinthia; 1701 Paul Perwolf of Wolfsburg, Obdach, Styria (executed); 1705 "Vlastl" of Murau, Styria (verdict unknown); 1705/6 six beggars in Wolfsberg, Carinthia (executed); 1707/8 three shepherds in Leoben and Freyenstein, Styria (one lynching, two probable executions); 1718 Jakob Kranawitter, a mentally disabled beggar, in Rotenfel, Oberwolz, Styria (corporeal punishment); 1725: Paul Schäffer, beggar of St. Leonhard im Lavanttal, Carinthia (executed).\n'), ('Citations', 'Lemma: Weerwolf , Instituut voor de Nederlandse Taal (in Dutch)\nOrel 2003 , p.\xa0463.\nOxford English Dictionary 2021 , s.v. werewolf, n.\nKoch 2020 , p.\xa096.\nWest 2007 , p.\xa0450.\nde Vries 1962 , p.\xa0646.\nDEAF  G:334–338.\nFEW  17:569.\nNichols 1987 , p.\xa0170.\nButler 2005 , pp.\xa0237–238.\nBalinisteanu, Tudor (2016). "Romanian Folklore and Literary Representations of Vampires". Folklore . 127 (2). Oxford, England: Taylor & Francis : 150–172. doi :10.1080/0015587X.2016.1155358 . ISSN \xa00015-587X . S2CID \xa0148481574 .\nZochios, Stamatis (2018). "Interprétation ethnolinguistique de termes mythologiques néohelléniques d\'origine slave désignant des morts malfaisants" . Revue des études slaves. 89 (3): 303–317. doi :10.4000/res.1787 . ISSN \xa00080-2557 . S2CID \xa0192528255 .\nButler 2005 , p.\xa0242.\nDelamarre 2007 , pp.\xa030–31.\nOxford English Dictionary 2021 , s.v. lyncanthropy, n. and lyncanthrope, n.\nOtten 1986 , pp.\xa05–8.\nde Blécourt 2015 , pp.\xa082–83.\nKim R. McCone, "Hund, Wolf, und Krieger bei den Indogermanen" in W. Meid (ed.), Studien zum indogermanischen Wortschatz, Innsbruck, 1987, 101–154\nHerodotus. "IV.105" . Histories.\nHerodotus, The Histories, 4.105 \nPomponius Mela (1998). "2.14". Description of the world. De chorographia.English. University of Michigan Press. ISBN \xa0978-0472107735.\nPausanias . "8.2". Description of Greece.\nOvid . "I 219–239". Metamorphoses.\nApollodorus . "3.8.1". Bibliotheca.\nPausanias 6.8.2\nPliny the Elder , Natural History, viii.82 .\nSuda, eta, 271\nPliny the Elder , Natural History, viii.81 .\nThe tale probably relates to a rite of passage for Arcadian\' youths.Ogden, Daniel (2002). Magic, Witchcraft, and Ghosts in the Greek and Roman Worlds: A Sourcebook. Oxford University Press. p.\xa0178. ISBN \xa00-19-513575-X.\nOvid. "I". Metamorphoses.\nMénard, Philippe (1984). "Les histoires de loup-garou au moyen-âge". Symposium in honorem prof. M. de Riquer (in French). Barcelona UP. pp.\xa0209–238.\nVirgil. "viii". Eclogues. p.\xa098.\nPetronius  (1996). Satyrica. R. Bracht Branham and Daniel Kinney. Berkeley: University of California. p.\xa056. ISBN \xa00-520-20599-5.\nAugustine of Hippo, The City of God, XVIII.17\n"Canon Episcopi" . www.personal.utulsa.edu. Archived from the original  on 2020-12-06. Retrieved 2020-03-27.\nOtten 1986 , pp.\xa05–6.\nAntapodosis 3.29\nGervase of Tilbury, Otia Imperiala, Book I, Chapter 15, translated and edited by S.E. Banks and J.W. Binns, (Oxford: Oxford University Press, 2002), 86–87.\nGeorg Schepss, Conradus Hirsaugiensis (1889). Conradi Hirsaugiensis Dialogus super Auctores sive Didascalon: Eine Literaturgeschichte aus den XII (in Latin). Harvard University. A. Stuber.\nPseudo-Augustine, Liber de Spiritu et Anima, Chapter 26, XVII\nMarie de France, "Bisclavret", translated by Glyn S. Burgess and Keith Busby, in The Lais of Marie de France (London: Penguin Books, 1999), 68.\nGervase of Tilbury, Otia Imperiala, Book I, Chapter 15, translated and edited by S.E. Banks and J.W. Binns, (Oxford: Oxford University Press, 2002), 87.\nHopkins, Amanda (2005). Melion and Biclarel: Two Old French Werewolf Lays. The University of Liverpool. ISBN \xa00-9533816-9-2. Retrieved 26 May 2020.\nBaring-Gould, p. 100.\nWoodward, Ian (1979). The Werewolf Delusion. Paddington Press. ISBN \xa00-448-23170-0.\nModestin, Georg (2005). "Von den hexen, so in Wallis verbrant wurdent» Eine wieder entdeckte Handschrift mit dem Bericht des Chronisten Hans Fründ über eine Hexenverfolgung im Wallis (1428)" \n(PDF). doc.rero.ch. pp.\xa0407–408. Retrieved 19 September 2022.\nCynthia Grant Schonberger (January–March 1979). "Luther and the Justification of Resistance to Legitimate Authority". Journal of the History of Ideas . 40 (1). University of Pennsylvania Press: 3–20. doi :10.2307/2709257 . JSTOR \xa02709257 . S2CID \xa055409226 .; as specified in Luther\'s Collected Works, 39(ii) 41-42\nMagnus, Olaus (1555). "Historia de gentibus septentrionalibus" . runeberg.org (in Latin). Retrieved 2023-10-31.\nRowlands, Alison. Witchcraft and Masculinities in Early Modern Europe. pp.\xa0191–213.\n"iii". Demonologie.\nHoyt, Nelly S.; Cassierer, Thomas, trans. (1965). The Encyclopedia: Selections: Diderot, d\'Alembert and a Society of Men of Letters. Indianapolis: Bobbs-Merrill.{{cite book}}:  CS1 maint: multiple names: authors list (link)\nOtten 1986 , pp.\xa0161–167.\n"Is the fear of wolves justified? A Fennoscandian perspective" \n(PDF). Acta Zoologica Lituanica, 2003, Volumen 13, Numerus 1. Archived from the original \n(PDF) on 2008-03-07. Retrieved 2008-05-09.\nFacundo Quiroga, "The Tiger of the Argentine Prairies" and the Legend of the " runa uturuncu".\nArchived  2017-08-16 at the Wayback Machine \n(in Spanish)\nThe Legend of the  runa uturuncu in the Mythology of the Latin-American Guerilla.\nArchived  2011-07-11 at the Wayback Machine \n(in Spanish)\nThe Guaraní Myth about the Origin of Human Language and the Tiger-men. \n(in Spanish)\nJ.B. Ambrosetti (1976). Fantasmas de la selva misionera ("Ghosts of the Misiones Jungle"). Editorial Convergencia: Buenos Aires.\nSteiger, Brad (2011). The Werewolf Book: The Encyclopedia of Shape-Shifting Beings. Visible Ink Press. p.\xa0267. ISBN \xa0978-1578593675.\nIllis, L (Jan 1964). "On Porphyria and the Ætiology of Werwolves" . Proc R Soc Med. 57 (1): 23–26. PMC \xa01897308 . PMID \xa014114172 .\nDening T R & West A (1989) "Multiple serial lycanthropy". Psychopathology 22: 344–347\nEbbe Schön  (2011-05-16). "Varulv" . Väsen (in Swedish). SVT . Archived from the original  on 2011-04-14. Retrieved 2011-05-16.\nBennett, Aaron. "So, You Want to be a Werewolf?" Fate . Vol. 55, no. 6, Issue 627. July 2002.\nO\'Donnell, Elliot. Werwolves. Methuen. London. 1912. pp. 65–67.\nGershenson, Daniel. Apollo the Wolf-God. (Journal of Indo-European Studies, Monograph, 8.) McLean, Virginia: Institute for the Study of Man, 1991, ISBN \xa00-941694-38-0 pp. 136–137.\nSzabó, György. Mitológiai kislexikon, I–II, Budapest: Merényi Könyvkiadó (év nélkül) Mitólogiai kislexikon. \nWillis, Roy; Davidson, Hilda Ellis  (1997). World Mythology: The Illustrated Guide. Piaktus. ISBN \xa00-7499-1739-3. OCLC \xa037594992 .\nThe Fables of Mkhitar Gosh (New York, 1987), translated with an introduction by R. Bedrosian, edited by Elise Antreassian and illustrated by Anahid Janjigian \nLopez, Barry (1978). Of Wolves and Men. New York: Scribner Classics. ISBN \xa00-7432-4936-4. OCLC \xa054857556 .\nLegends of Grosse Pointe .\nAshliman, D. L.\n"Werewolf Legends from Germany" . pitt.edu. Retrieved January 1, 2022.\nRobert Jackson (1995) Witchcraft and the Occult. Devizes, Quintet Publishing: 25.\nBaud\'huin, Benoît; Bonet, Alain (1995). Gévaudan: petites histoires de la grande bête (in French). Ex Aequo Éditions. p.\xa0193. ISBN \xa0978-2-37873-070-3.\nCrouzet, Guy (2001). La grande peur du Gévaudan (in French). Guy Crouzet. pp.\xa0156–158. ISBN \xa02-9516719-0-3.\nSabine Baring-Gould . "The Book of Were-Wolves". (1865) p. 101\nTemme, J.D.H. Die Volkssagen von Pommern und Rugen. Translated by D.L. Ashliman . Berlin: In de Nicolaischen Buchhandlung, 1840.\nSellers, Susan. Myth and Fairy Tale in Contemporary Women\'s Fiction, Palgrave Macmillan (2001) p. 85.\nStoker, Brett. Dracula\'s Guest\n(PDF). p.\xa011. "A wolf\xa0–\nand yet not a wolf!" ... "No use trying for him without the sacred bullet," a third remarked\nStoker, Bram. "Ch 3, Johnathon Harker\'s Journal". Dracula\n(PDF). p.\xa042. \'We Szekelys have a right to be proud, for in our veins flows the blood of many brave races who fought as the lion fights, for lordship. Here, in the whirlpool of European races, the Ugric tribe bore down from Iceland the fighting spirit which Thor and Wodin gave them, which their Berserkers displayed to such fell intent on the seaboards of Europe, aye, and of Asia and Africa too, till the peoples thought that the werewolves themselves had come.\nStoker, Bram. "Ch 18, Mina Harker\'s Journal". Dracula\n(PDF). His power ceases, as does that all of all evil things, at the coming of the day. Only at certain times can he have limited freedom. If he be not at the place whither he is bound, he can only change himself at noon or exact sunrise or sunset.\nChantal Bourgault Du Coudray, The Curse of the Werewolf\xa0: Fantasy, Horror and the Beast Within. London: I.B. Tauris, 2006. ISBN \xa0978-1429462655 (pp. 112, 169)\nSearles B (1988). Films of Science Fiction and Fantasy. Harry N. Abrams. pp.\xa0165–167. ISBN \xa00-8109-0922-7.\nClemens, pp. 119–120.\nClemens, pp. 117–118.\nClemens, p. 120.\nSteiger, Brad (1999). The Werewolf Book: The Encyclopedia of Shapeshifting Beings. Farmington Hills, MI: Visible Ink. p.\xa012. ISBN \xa01-57859-078-7. OCLC \xa041565057 .\nSteiger, Brad (1999). The Werewolf Book: The Encyclopedia of Shapeshifting Beings. Visible Ink. p.\xa0330. ISBN \xa01-57859-078-7. OCLC \xa041565057 .\nSteiger, Brad (1999). The Werewolf Book: The Encyclopedia of Shapeshifting Beings. Visible Ink. p.\xa017. ISBN \xa01-57859-078-7. OCLC \xa041565057 .\nAndrzej Wicher; Piotr Spyra; Joanna Matyjaszczyk (2014). Basic Categories of Fantastic Literature Revisited. Cambridge Scholars Publishing. pp.\xa095–96. ISBN \xa0978-1-4438-7143-3.\nGlut, Donald F. (2002). The Frankenstein Archive. McFarland. p.\xa019. ISBN \xa00786413530.\nCrossen, Carys Elizabeth. The Nature of the Beast: Transformations of the Werewolf from the 1970s to the Twenty-first Century. University of Wales Press, 2019, p. 206\nSenn, Bryan. The Werewolf Filmography: 300+ Movies. McFarland, 2017, p. 8\nWilson, Natalie. Seduced by Twilight: The allure and contradictory messages of the popular saga. McFarland, 2014, p. 39\nBoissoneault, Lorraine. "The Nazi Werewolves Who Terrorized Allied Soldiers at the End of WWII" . Smithsonian Magazine. The Smithsonian. Retrieved 27 May 2020.\n'), ('References', 'Secondary sources\nButler, Francis (2005). "Russian "vurdalak" \'vampire\' and Related Forms in Slavic". Journal of Slavic Linguistics. 13 (2): 237–250. JSTOR \xa024599657 .\nde Blécourt, Willem  (2015). Werewolf Histories. Springer. ISBN \xa0978-1-137-52634-2.\nDelamarre, Xavier  (2007). "Gallo-Brittonica (suite: 11–21)". Zeitschrift für celtische Philologie. 55 (1). doi :10.1515/ZCPH.2007.29 . ISSN \xa00084-5302 . S2CID \xa0163928150 .\nde Vries, Jan  (1962). Altnordisches Etymologisches Worterbuch (1977\xa0ed.). Brill. ISBN \xa0978-90-04-05436-3.\nDouglas, Adam (1992). The Beast Within: A History of the Werewolf. London: Chapmans. ISBN \xa00-380-72264-X.\nFrost, Brian J. (2003). The Essential Guide to Werewolf Literature. Popular Press. ISBN \xa0978-0-87972-860-1.\nGoens, Jean (1993). Loups-garous, vampires et autres monstres\xa0: enquêtes médicales et littéraires. Paris: CNRS Editions.\nKoch, John T.  (2020). Celto-Germanic, Later Prehistory and Post-Proto-Indo-European vocabulary in the North and West. University of Wales Centre for Advanced Welsh and Celtic Studies. ISBN \xa0978-1907029325.\nLecouteux, Claude  (2003). Witches, Werewolves, and Fairies: Shapeshifters and Astral Doubles in the Middle Ages. Inner Traditions/Bear. ISBN \xa0978-0-89281-096-3.\nNichols, Johanna  (1987). "Russian vurdalak \'werewolf\' and its cognates". In Flier, Michael S.; Karlinsky, Simon (eds.). Language literature linguistics: In honor of Francis Whitfield on his seventieth birthday March 25, 1986. Berkeley Slavic Specialties. ISBN \xa0978-0933884588.\nOrel, Vladimir  (2003). A Handbook of Germanic Etymology. Brill. ISBN \xa0978-90-04-12875-0.\nOtten, Charlotte F. (1986). The Lycanthropy Reader: Werewolves in Western Culture. Syracuse University Press. ISBN \xa0978-0-8156-2384-7.\nOxford English Dictionary Online . Oxford University Press. 2021.\nWest, Martin L.  (2007). Indo-European Poetry and Myth. Oxford University Press . ISBN \xa0978-0-19-928075-9.\nPrimary sources: Wolfeshusius, Johannes Fridericus. \nDe Lycanthropia: An vere illi, ut fama est, luporum & aliarum bestiarum formis induantur. Problema philosophicum pro sententia Joan. Bodini ... adversus dissentaneas aliquorum opiniones noviter assertum... Leipzig: Typis Abrahami Lambergi, 1591. (In Latin; microfilm held by the United States National Library of Medicine ): Prieur, Claude. \nDialogue de la Lycanthropie: Ou transformation d\'hommes en loups, vulgairement dits loups-garous, et si telle se peut faire. Louvain: J. Maes & P. Zangre, 1596.: Bourquelot and \nJean de Nynauld , De la Lycanthropie, Transformation et Extase des Sorciers (Paris, 1615).\nSummers, Montague , The Werewolf London: K. Paul, Trench, Trubner, 1933. (1st edition, reissued 1934 New York: E. P. Dutton; 1966 New Hyde Park, N.Y.: University Books; 1973 Secaucus, N.J.: Citadel Press; 2003 Mineola, N.Y.: Dover, with new title The Werewolf in Lore and Legend). ISBN \xa00-7661-3210-2\n'), ('Further reading', 'Baring-Gould, Sabine (1865). The Book of Werewolves: Being an Account of a Terrible Superstition. London: Smith, Elder & Co.\nGoogle Books\nChisholm, Hugh , ed. (1911). "Werwolf" \xa0. Encyclopædia Britannica  (11th\xa0ed.). Cambridge University Press.: Grimm, \nDeutsche Mythologie , 4, ii. and iii.: Hertz, \nDer Werwolf (Stuttgart, 1862): Leubuscher, \nÜber die Wehrwölfe (1850)\nO\'Donnell, Elliot (1912). Werewolves.\nSconduto, Leslie A. Metamorphoses of the werewolf: a literary study from antiquity through the Renaissance.\nStewart, Caroline Taylor (1909). The origin of the werewolf superstition. University of Missouri Studies. ISBN \xa0978-0524023778.\n')]]
--------
--------
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 874, in <module>
    look.search("What are werewolves?")
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 798, in search
    art_text = art_text + "###Article: "+art[0] + "\n"
TypeError: can only concatenate str (not "tuple") to str

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.325072050094604 s {
  "Articles": [
    "Werewolf",
    "Lycanthropy",
    "Werewolf Myths and Legends"
  ]
}
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Werewolf', 'A/Lycanthropy']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
17.534552574157715 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition', 'Folk beliefs']
Getting relevant for:  Werewolf
29.684285879135132 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition', 'Folk beliefs', 'Modern reception', 'See also', 'Notes', 'Citations', 'References']
--------
--------

--------
--------
background text: 
--------
###Article: Werewolf

###Article: Werewolf


--------
Getting answer
15.758689880371094 s Final answer:
--------
I'm sorry, but I don't have access to the articles you've mentioned. Could you please provide me with the content of the articles or describe them? That way, I can help summarize and synthesize the information to answer your question "{question}".

If there's any specific part of the article you'd like me to focus on or if you could give me a brief summary point to start with, I'll be happy to help create a more focused response.
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.375434160232544 s ```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
to_grabs:  []
article sections:
--------
--------
[]
--------
--------
background text: 
--------

--------
Getting answer
10.004616737365723 s Final answer:
--------
I'll need you to provide me with the articles so I can help summarize and synthesize the information. Once I have that, I'll be able to answer your specific question about "{question}" and generate relevant follow-up points based on the content.
--------
S ="""
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                                                                                                                                                             
list_output_gatherer(S)
                                                                                                                                                             
[]
block_extractor(S)
                                                                                                                                                             
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#29>", line 1, in <module>
TypeError: block_extractor() missing 1 required positional argument: 'key'
to_dict = S.split("json")
                                                                                                                                                             
to_dict
                                                                                                                                                             
['\n```', '\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n']
to_dict.reverse()
                                                                                                                                                             
to_dict
                                                                                                                                                             
['\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n', '\n```']
seg = to_dict[0]
                                                                                                                                                             
op = ast.literal_eval(seg.replace("```","").strip())
                                                                                                                                                             
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#35>", line 1, in <module>
  File "/usr/lib/python3.10/ast.py", line 64, in literal_eval
    node_or_string = parse(node_or_string.lstrip(" \t"), mode='eval')
  File "/usr/lib/python3.10/ast.py", line 50, in parse
    return compile(source, filename, mode, flags,
  File "<unknown>", line 1
    {"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
                                                                     ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
seg
                   
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
s2 = '\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]}\n```\n'
                   
op = ast.literal_eval(s2.replace("```","").strip())
                   
op
                   
{'Articles': ['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']}
s2 = '["Werewolf","Werewolf Lore and Mythology","Vampires"]'
                   
op = ast.literal_eval(s2.replace("```","").strip())
                   
op
                   
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']
seg
                   
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
re.match("\[*\]",seg)
                   
re
                   
<module 're' from '/usr/lib/python3.10/re.py'>
seg
                   
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
re.match("\[*+\]",seg)
                   
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#47>", line 1, in <module>
  File "/usr/lib/python3.10/re.py", line 190, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.10/re.py", line 303, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.10/sre_compile.py", line 788, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.10/sre_parse.py", line 955, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.10/sre_parse.py", line 444, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/usr/lib/python3.10/sre_parse.py", line 672, in _parse
    raise source.error("multiple repeat",
re.error: multiple repeat at position 3
re.match("\[\]",seg)
                       
re.match("Wer",seg)
                       
m = re.match("\[*\]",seg)
                       
m
                       
seg
                       
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
m = re.match("we",seg)
                       
re.search("\[*\]",seg)
                       
<re.Match object; span=(65, 66), match=']'>
m = re.search("\[*\]",seg)
                       
m
                       
<re.Match object; span=(65, 66), match=']'>
m.string
                       
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
m.group
                       
<built-in method group of re.Match object at 0x7d6568fc8440>
m.group()
                       
']'
m = re.search("\[*+\]",seg)
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#60>", line 1, in <module>
  File "/usr/lib/python3.10/re.py", line 200, in search
    return _compile(pattern, flags).search(string)
  File "/usr/lib/python3.10/re.py", line 303, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.10/sre_compile.py", line 788, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.10/sre_parse.py", line 955, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.10/sre_parse.py", line 444, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/usr/lib/python3.10/sre_parse.py", line 672, in _parse
    raise source.error("multiple repeat",
re.error: multiple repeat at position 3
m = re.search("\[.+\]",seg)
                       
m.group()
                       
'["Werewolf","Werewolf Lore and Mythology","Vampires"]]'
m = re.search("\[.+-[\]]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#64>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[.+-\]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#66>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[.+\]",seg)
                       
m.group()
                       
'["Werewolf","Werewolf Lore and Mythology","Vampires"]]'
m = re.search("\[.^[\]]+\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#70>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[.+^[\]]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#72>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[^[\]+]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#74>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[^[\]]+\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#76>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[^[\]]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#78>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
se = "cjshfkb[j]]nlcma,[d]vsmf;knlj"
                       
m = re.search("\[^[\]]\]",se)
                       
m = re.search("\[^[\]]\]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#82>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[ [^ \] ] \]",seg)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#84>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[ [^ \] ] \]",se)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#86>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
m = re.search("\[[^\]]\]",se)
                       
m.group()
                       
'[j]'
m = re.search("\[[^\]]\]",se)
                       
m.group()
                       
'[j]'
m = re.findall("\[[^\]]\]",se)
                       
m.group()
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#92>", line 1, in <module>
AttributeError: 'list' object has no attribute 'group'
[a.group() for a in m]
                       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#93>", line 1, in <module>
  File "<pyshell#93>", line 1, in <listcomp>
AttributeError: 'str' object has no attribute 'group'
m
                       
['[j]', '[d]']
m = re.findall("\[[^\]]\]",seg)
                       
m
                       
[]
seg
                       
'\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n'
m = re.findall("\[[^\]+]\]",seg)
                       
m
                       
[]
m = re.findall("\[[^\]]+\]",seg)
                       
m
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
m[0]
                       
'["Werewolf","Werewolf Lore and Mythology","Vampires"]'
m = re.findall("\[[^\]\}]+\]",seg)
                       
m
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
m = re.findall("\[[^\]\}]+\]",se)
                       
m
                       
['[j]', '[d]']
se
                       
'cjshfkb[j]]nlcma,[d]vsmf;knlj'
se2 = 'cjshfkb[j}]]nlc{ma},{[d]]}vsmf;knlj'
                       
m = re.findall("\[[^\]\}]+\]",se2)
                       
m
                       
['[d]']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.071995258331299 s {
  "Articles": ["Werewolf", "Transformations In Literature", "Cultural Impact Of Werewolves"]
}
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  []
targets:  []
to_grabs:  ['A/Werewolf']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
Getting relevant for:  Werewolf
3.8227248191833496 s  Sections: ['History', 'Names']
--------
--------

--------
--------
    sec: Werewolf
    sec: Names
    sec: History
    sec: Lycanthropy as a medical condition
    sec: Folk beliefs
    sec: Modern reception
    sec: See also
    sec: Notes
    sec: Citations
    sec: References
    sec: Further reading
background text: 
--------
###Article: Werewolf


--------
Getting answer
11.551189422607422 s Final answer:
--------
I apologize, but you haven't provided any specific question or articles for me to summarize. Could you please provide more context about which question and articles you are referring to? Once I have that information, I'll be able to help you summarize the articles and answer your question accurately.
--------
S = """
"""
                       
S = """
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                       
list_output_gatherer(S)
                       
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
[]
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
ops: ['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['\n{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]\n```\n', '\n```']
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       

{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```


```
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['[', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', '', ',', '', 'W', 'e', 'r', 'e', 'w', 'o', 'l', 'f', ' ', 'L', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'M', 'y', 't', 'h', 'o', 'l', 'o', 'g', 'y', '', ',', '', 'V', 'a', 'm', 'p', 'i', 'r', 'e', 's', '', ']']
ops = ['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
                       
ast.literal_eval(ops[0])
                       
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

6.930410385131836 s {"Articles":["Werewolf","Lycanthropy","Wendigo"]}
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  ['A/Wendigo', 'A/The_Wendigo', 'A/Wendigo_(Supernatural)', 'A/Wendigo_(comics)', 'A/Wendigo_(disambiguation)', 'A/Wendigo_(film)', 'A/Wendigo_(fish)', 'A/Wendigo_(song)', 'A/Wendigo_Creek', 'A/Wendigo_psychosis', 'A/The_Wendigo_(film)', 'A/The_Wendigo_(novella)', 'A/Wendigo_(Supernatural_episode)', 'A/Wendigo_(Supernatural_episodes)', 'A/Alone_Against_the_Wendigo', 'A/The_Wendigo_(Charmed_Episode)', 'A/The_Wendigo_(Charmed_episode)', 'A/Wendigo_(Werewolf:_The_Apocalypse)', 'A/Wendigo_(World_of_Darkness)', 'A/Who,_What,_Where,_Wendigo?']
to_grabs:  ['A/Werewolf', 'A/Lycanthropy', 'A/Wendigo']
article sections:
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Werewolf
     Werewolf
     Names
     History
     Lycanthropy as a medical condition
     Folk beliefs
     Modern reception
     See also
     Notes
     Citations
     References
     Further reading
   Wendigo
     Wendigo
     Etymology
     Folklore
     Psychosis
     As a concept or metaphor
     In popular culture
     References
Getting relevant for:  Werewolf
4.440141677856445 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Getting relevant for:  Werewolf
4.1610023975372314 s  Sections: ['History', 'Names', 'Folk beliefs']
Getting relevant for:  Wendigo
4.334822416305542 s  Sections: ['Etymology', 'Psychosis', 'As a concept or metaphor']
--------
--------

--------
--------
    sec: Werewolf
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Names
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: History
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Lycanthropy as a medical condition
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folk beliefs
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Modern reception
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: See also
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Citations
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Further reading
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Werewolf
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Names
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: History
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Lycanthropy as a medical condition
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folk beliefs
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Modern reception
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: See also
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Citations
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Further reading
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Wendigo
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Etymology
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folklore
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Psychosis
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: As a concept or metaphor
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: In popular culture
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['Names', 'History', 'Lycanthropy as a medical condition'])
background text: 
--------
###Article: Werewolf

###Article: Werewolf

###Article: Wendigo


--------
Getting answer
14.421894073486328 s Final answer:
--------
To provide an appropriate response, I'll need to understand what question you're asking. The attached articles appear to be discussing various werewolves or related creatures. Please specify your main question about these creatures so I can provide a relevant summary and follow-up points.

Would you like me to summarize the information from the three werewolf-related articles and suggest follow-up questions based on what specific aspect of them interests you?
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

8.621454000473022 s ```json
{
  "Articles": [
    "Wolves",
    "Lycanthropy",
    "Werewolf Legends"
  ]
}
```
targets:  ['A/Wolves_in_Wolves', 'A/WolVes', 'A/Wolves', 'A/ASU_wolves', 'A/Abyssian_Wolves', 'A/Abyssian_wolves', 'A/Abyssinian_Wolves', 'A/Admiralty_Wolves', 'A/Akwesasne_Wolves', 'A/Algeti_Wolves', 'A/American_Wolves', 'A/Among_Wolves', 'A/Arctic_Wolves', 'A/Arctic_wolves', 'A/Augusta_Wolves', 'A/BC_Wolves', 'A/Baby_wolves', 'A/Bad_Wolves', 'A/Belgrade_wolves', 'A/Billings_Wolves']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  ['A/Legend_of_the_Werewolf']
to_grabs:  ['A/Wolves_in_Wolves', 'A/Lycanthropy', 'A/Legend_of_the_Werewolf']
article sections:
   Wolves in Wolves
     Wolves in Wolves 1291
     The event 1946
     Conclusion of the event 1486
     List of wolf statues 2275
     References 1881
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Legend of the Werewolf
     Legend of the Werewolf 614
     Plot 3643
     Cast 517
     Production 479
     Release 229
     Related items 211
     References 504
Getting relevant for:  Wolves in Wolves
3.972656726837158 s  Sections: ['The event', 'Conclusion of the event']
Getting relevant for:  Werewolf
3.7338199615478516 s  Sections: ['History', 'Names']
Getting relevant for:  Legend of the Werewolf
4.074683666229248 s  Sections: ['Plot', 'Cast', 'References']
--------
--------

--------
--------
    sec: Wolves in Wolves
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: The event
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Conclusion of the event
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: List of wolf statues
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: References
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Werewolf
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Names
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: History
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Lycanthropy as a medical condition
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Folk beliefs
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Modern reception
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: See also
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Notes
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Citations
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: References
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Further reading
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Legend of the Werewolf
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Plot
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Cast
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Production
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Release
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: Related items
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
    sec: References
             (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
background text: 
--------
###Article: Wolves in Wolves

###Article: Werewolf

###Article: Legend of the Werewolf


--------
Getting answer
9.862390995025635 s Final answer:
--------
I apologize, but I'm not able to view or analyze the attached articles without access to them. Could you please provide me with a summary of each article or any specific information from them that would help answer your question?
--------
k = (('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"), ['The event', 'Conclusion of the event'])
                       
k[0]
                       
('Wolves in Wolves', "Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n")
k[1]
                       
['The event', 'Conclusion of the event']
k[0][0]
                       
'Wolves in Wolves'
k[0][1]
                       
"Wolves in Wolves was a public art exhibition  which took place in Wolverhampton , England, between 5 July and 24 September 2017.[1]\n--------\nThe event was conceived and proposed to City of Wolverhampton Council in 2015, through its '100 Bright Ideas' initiative by Council employee Mandeep ('Manor') Singh[2] and when delivered it consisted of 30 two-metre-high wolf sculptures that were located throughout Wolverhampton. The wolves were individually decorated by local and international artists, with sponsorship funding provided by both public and private sector organisations. The wolves formed a 4.5 mile Wolf Trail taking in West Park , Chapel Ash  and Wolverhampton city centre, with a map available to help people track them down.[3] Wolves in Wolves was Wolverhampton's largest public art event ever to this date.[4] Additionally, there was an exhibition of 70 mini-wolves sculptures, designed and painted by pupils from 35 primary schools, community groups and artists, on display at Wolverhampton Art Gallery  for the duration of the event.[5][6]\nThe ambition for Wolves in Wolves was to combine a quality artistic and cultural event with associated public health, educational and economic benefits as well as raising funds and awareness for key local organisations and charities.\n"

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

9.086357593536377 s ["Encyclopedia of Werewolf Lore", "The History of Werewolves Through Literature and Mythology", "Werewolves: Science, Folklore, and Modern Perspectives"]
targets:  []
targets:  []
targets:  []
to_grabs:  []
article sections:
sec list: 
--------
--------
[]
--------
--------
background text: 
--------

--------
Getting answer
8.387461185455322 s Final answer:
--------
I'll need the articles you're referring to in order to provide a summary and synthesis. Please attach them, and I'll help analyze the information and respond to your question about them.
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.19826602935791 s {"Articles":["Lycanthropy","Werewolf Mythology","Folklore and Werewolves"]}
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
targets:  []
to_grabs:  ['A/Lycanthropy']
article sections:
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
Getting relevant for:  Werewolf
4.524758577346802 s  Sections: ['History', 'Lycanthropy as a medical condition', 'Folk beliefs']
sec list: 
   ('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n')
   ['History', 'Lycanthropy as a medical condition', 'Folk beliefs']
--------
--------

--------
--------
    sec: Werewolf
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Names
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: History
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Lycanthropy as a medical condition
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Folk beliefs
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Modern reception
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: See also
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Notes
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Citations
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: References
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
    sec: Further reading
             (('Werewolf', 'In folklore , a werewolf[lower-alpha 1] (from\nOld English\nwerwulf \xa0\'man-wolf\'), or occasionally lycanthrope[lower-alpha 2] (from\nAncient Greek\nλυκάνθρωπος , lykánthrōpos, \'wolf-human\'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic\nhybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).\nSeveral terms  redirect here. For other uses, see Werewolf (disambiguation) ,\nWolf man (disambiguation) ,\nLycanthrope (disambiguation) ,\nand\nLycanthropy (disambiguation) .\nFor the episode of Grimm, see Lycanthropia (Grimm) .\nWerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512\nGrouping: Mythology\nSimilar entities Skinwalker \nFolklore: Worldwide\nOther name(s): Lycanthrope\nPart of a series on theParanormal \nMain articles\nAstral projection\nAstrology\nAura\nBilocation\nBreatharianism\nClairvoyance\nClose encounter\nCold spot\nCrystal gazing\nConjuration\nCryptozoology\nDemonic possession\nDemonology\nEctoplasm\nElectronic voice phenomenon\nExorcism\nExtrasensory perception\nForteana\nFortune-telling\nGhost hunting\nMagic\nMediumship\nMiracle\nOccult\nOrb\nOuija\nParanormal fiction\nParanormal television\nPrecognition\nPreternatural\nPsychic\nPsychic reading\nPsychometry\nReincarnation\nRemote viewing\nRetrocognition\nSpirit photography\nSpirit possession\nSpirit world\nSpiritualism\nStone Tape\nSupernatural\nTelekinesis\nTelepathy\nTable-turning\nUfology \nReportedly haunted locations:\nIndia\nUnited Kingdom\nUnited States\nWorld\nSkepticism\nCold reading\nCommittee for Skeptical Inquiry\nDebunking\nHoax\nJames Randi Educational Foundation\nMagical thinking\nPrizes for evidence of the paranormal\nPseudoskepticism\nScientific literacy\nScientific skepticism\nParapsychology\nAnomalous experiences\nApparitional experiences\nEmpath\nFalse awakening\nHypnosis\nIdeomotor phenomenon\nOut-of-body experiences\nParapsychology\nSynchronicity \nRelated\nAnomalistics\nArgument from ignorance\nArgumentum ad populum\nBandwagon effect\nBegging the question\nCognitive dissonance\nCommunal reinforcement\nFallacy\nFalsifiability\nFringe science\nGroupthink\nHypnosis\nJunk science\nProtoscience\nPseudoscience\nScientific evidence\nScientific method\nSuperstition\nUncertainty\nUrban legend \nThe werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.\nThe persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]\nAfter the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .\n'), ['History', 'Lycanthropy as a medical condition', 'Folk beliefs'])
background text: 
--------
###Article: Werewolf


--------
Getting answer
17.211782693862915 s Final answer:
--------
I'll help you analyze these werewolf articles. However, I need to see the actual articles attached or the specific question asked before providing a complete summary.

To answer your request, could you please provide:
1. The specific question regarding werewolves that needs answering
2. Any particular aspects or characteristics of interest (e.g., folklore, mythology, scientific explanations)
3. Relevant details from the provided articles

This would help me craft an accurate and informative response that addresses your specific query about werewolves.
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

11.126657009124756 s The articles on Wikipedia that provide background information about werewolves include:
- "Werewolf" (Encyclopedia Britannica)
- "Werewolf myth and legend" (Wikipedia)
- "Cyclops" (Encyclopedia Britannica)
to_grabs:  []
article sections:
sec list: 
--------
--------
[]
--------
--------
background text: 
--------

--------
Getting answer
17.773601055145264 s Final answer:
--------
I'll be happy to help summarize and synthesize the information from the attached articles. However, I need to clarify a few things before we proceed:

1. What is the specific question you'd like answered?
2. Can you provide me with access to the articles or any additional context?
3. Are there particular points in the articles that you would like me to focus on?

With more information about what you're looking for, I can help create a comprehensive summary and synthesis of the article content. Please let me know how we can proceed!
--------
S = """The articles on Wikipedia that provide background information about werewolves include:
- "Werewolf" (Encyclopedia Britannica)
- "Werewolf myth and legend" (Wikipedia)
- "Cyclops" (Encyclopedia Britannica)
"""
                       
list_output_gatherer(S)
                       
[]

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
[]
Smalf
                       
'The articles on Wikipedia that provide background information about werewolves include:\n- "Werewolf" (Encyclopedia Britannica)\n- "Werewolf myth and legend" (Wikipedia)\n- "Cyclops" (Encyclopedia Britannica)\n'

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
- "Werewolf" (Encyclopedia Britannica)
- "Werewolf myth and legend" (Wikipedia)
- "Cyclops" (Encyclopedia Britannica)

[]

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

['Werewolf (Encyclopedia Britannica)', 'Werewolf myth and legend (Wikipedia)', 'Cyclops (Encyclopedia Britannica)']
arc.suggestions("Werewolf (Encyclopedia Britannica)")
                       
[]

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

[['"Werewolf"'], ['"Werewolf myth and legend"'], ['"Cyclops"']]

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

['"Werewolf"', '"Werewolf myth and legend"', '"Cyclops"']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

['Werewolf', 'Werewolf myth and legend', 'Cyclops']
Smalf = """
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                       
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#142>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 551, in list_output_gatherer
    l_out = [re.findall("\"[^\"]+\"",l)[0][1:-1] for l in l_out]
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 551, in <listcomp>
    l_out = [re.findall("\"[^\"]+\"",l)[0][1:-1] for l in l_out]
IndexError: list index out of range

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

['Werewolf', 'Werewolf myth and legend', 'Cyclops']
['"Werewolf" (Encyclopedia Britannica)', '"Werewolf myth and legend" (Wikipedia)', '"Cyclops" (Encyclopedia Britannica)']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

XXXXX:  ['Werewolf', 'Werewolf myth and legend', 'Cyclops']
['"Werewolf" (Encyclopedia Britannica)', '"Werewolf myth and legend" (Wikipedia)', '"Cyclops" (Encyclopedia Britannica)']
Smalf = """
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                       
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#146>", line 1, in <module>
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 551, in list_output_gatherer
    l_quotes = [re.findall("[\"\'][^\"\']+[\"\']",l)[0][1:-1] for l in l_out]
  File "/home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py", line 551, in <listcomp>
    l_quotes = [re.findall("[\"\'][^\"\']+[\"\']",l)[0][1:-1] for l in l_out]
IndexError: list index out of range

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Smalf = """
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                       
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
XXXXX:  [[], [], []]
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

XXXXX:  [['"Werewolf"'], ['"Werewolf myth and legend"'], ['"Cyclops"']]
['"Werewolf" (Encyclopedia Britannica)', '"Werewolf myth and legend" (Wikipedia)', '"Cyclops" (Encyclopedia Britannica)']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
list_output_gatherer(Smalf)
                       
The articles on Wikipedia that provide background information about werewolves include|
|"Werewolf" (Encyclopedia Britannica)
|"Werewolf myth and legend" (Wikipedia)
|"Cyclops" (Encyclopedia Britannica)

XXXXX:  ['Werewolf', 'Werewolf myth and legend', 'Cyclops']
['"Werewolf" (Encyclopedia Britannica)', '"Werewolf myth and legend" (Wikipedia)', '"Cyclops" (Encyclopedia Britannica)']
Smalf = """
```json
{"Articles":["Werewolf","Werewolf Lore and Mythology","Vampires"]]
```
"""
                       
list_output_gatherer(Smalf)
                       
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
['["Werewolf","Werewolf Lore and Mythology","Vampires"]']
XXXXX:  ['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']
['Werewolf', 'Werewolf Lore and Mythology', 'Vampires']

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

9.493935108184814 s ```json
{
  "Articles": [
    "Werewolf",
    "Lycanthropy",
    "Folklore and Werewolves"
  ]
}
```
targets:  ['A/Werewolf', 'A/Werewolf_(1996)', 'A/American_Werewolf', 'A/Arizona_Werewolf', 'A/Female_Werewolf', 'A/Garou_(Werewolf)', 'A/Livonian_werewolf', 'A/Mama_Werewolf', 'A/Mr._Werewolf', 'A/Operation_Werewolf', 'A/Radio_Werewolf', 'A/Radio_werewolf', 'A/The_Werewolf', 'A/The_werewolf', 'A/Ultimate_Werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(comics)', 'A/Werewolf_(disambiguation)', 'A/Werewolf_(film)']
targets:  ['A/Lycanthropy', 'A/Clinical_Lycanthropy', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Lycanthropy_(clinical)', 'A/Lycanthropy_(disambiguation)', 'A/Lycanthropy_(song)']
targets:  []
to_grabs:  ['A/Werewolf', 'A/Lycanthropy']
article sections:
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
Getting relevant for:  Werewolf
To answer the question "What are werewolves?", we need to look at the section titles provided. The most relevant sections would be those that directly describe what werewolves are and their characteristics.

Based on the list of section titles|
| 'Names'| This section likely contains specific names associated with werewolves.
| 'History'| This section might give information about the cultural origins and development of werewolf stories and practices.
| 'Lycanthropy as a medical condition'| While this could be relevant, it is more related to science rather than what werewolves are.

Therefore, the most relevant sections to answer the question "What are werewolves? " would be|
|['Names']
|['History']

The answer would include information about various aspects of werewolf identities and folklore.
14.225772380828857 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Getting relevant for:  Werewolf
To address the question "What are werewolves?", the most relevant sections from the article would be|

|["Names", "History"]
|This information is directly from the Names section about how people came to know werewolves and their history, which includes both traditional and modern tales of werewolves.

The History section provides a detailed account of werewolf cultures across different regions and time periods, including both historical records and cultural traditions. The Names section also offers insights into how werewolves have been depicted in literature, art, and folklore, offering a comprehensive view of their characteristics and significance.
11.304616689682007 s  Sections: ['Names', 'This information is directly from the Names section about how people came to know werewolves and their history, which includes both traditional and modern tales of werewolves.']
sec list: 
   Werewolf
   ['Names', 'History', 'Lycanthropy as a medical condition']
   Werewolf
   ['Names', 'This information is directly from the Names section about how people came to know werewolves and their history, which includes both traditional and modern tales of werewolves.']
--------
--------

--------
--------
    sec: Werewolf
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Names
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: History
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Lycanthropy as a medical condition
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folk beliefs
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Modern reception
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: See also
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Citations
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Further reading
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Werewolf
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Names
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: History
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Lycanthropy as a medical condition
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folk beliefs
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Modern reception
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: See also
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Citations
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Further reading
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
background text: 
--------
###Article: Werewolf
Werewolf
In folklore , a werewolf[lower-alpha 1] (from
Old English
werwulf  'man-wolf'), or occasionally lycanthrope[lower-alpha 2] (from
Ancient Greek
λυκάνθρωπος , lykánthrōpos, 'wolf-human'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic
hybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).
Several terms  redirect here. For other uses, see Werewolf (disambiguation) ,
Wolf man (disambiguation) ,
Lycanthrope (disambiguation) ,
and
Lycanthropy (disambiguation) .
For the episode of Grimm, see Lycanthropia (Grimm) .
WerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512
Grouping: Mythology
Similar entities Skinwalker 
Folklore: Worldwide
Other name(s): Lycanthrope
Part of a series on theParanormal 
Main articles
Astral projection
Astrology
Aura
Bilocation
Breatharianism
Clairvoyance
Close encounter
Cold spot
Crystal gazing
Conjuration
Cryptozoology
Demonic possession
Demonology
Ectoplasm
Electronic voice phenomenon
Exorcism
Extrasensory perception
Forteana
Fortune-telling
Ghost hunting
Magic
Mediumship
Miracle
Occult
Orb
Ouija
Paranormal fiction
Paranormal television
Precognition
Preternatural
Psychic
Psychic reading
Psychometry
Reincarnation
Remote viewing
Retrocognition
Spirit photography
Spirit possession
Spirit world
Spiritualism
Stone Tape
Supernatural
Telekinesis
Telepathy
Table-turning
Ufology 
Reportedly haunted locations:
India
United Kingdom
United States
World
Skepticism
Cold reading
Committee for Skeptical Inquiry
Debunking
Hoax
James Randi Educational Foundation
Magical thinking
Prizes for evidence of the paranormal
Pseudoskepticism
Scientific literacy
Scientific skepticism
Parapsychology
Anomalous experiences
Apparitional experiences
Empath
False awakening
Hypnosis
Ideomotor phenomenon
Out-of-body experiences
Parapsychology
Synchronicity 
Related
Anomalistics
Argument from ignorance
Argumentum ad populum
Bandwagon effect
Begging the question
Cognitive dissonance
Communal reinforcement
Fallacy
Falsifiability
Fringe science
Groupthink
Hypnosis
Junk science
Protoscience
Pseudoscience
Scientific evidence
Scientific method
Superstition
Uncertainty
Urban legend 
The werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.
The persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]
After the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .


###Article: Werewolf
Werewolf
In folklore , a werewolf[lower-alpha 1] (from
Old English
werwulf  'man-wolf'), or occasionally lycanthrope[lower-alpha 2] (from
Ancient Greek
λυκάνθρωπος , lykánthrōpos, 'wolf-human'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic
hybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).
Several terms  redirect here. For other uses, see Werewolf (disambiguation) ,
Wolf man (disambiguation) ,
Lycanthrope (disambiguation) ,
and
Lycanthropy (disambiguation) .
For the episode of Grimm, see Lycanthropia (Grimm) .
WerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512
Grouping: Mythology
Similar entities Skinwalker 
Folklore: Worldwide
Other name(s): Lycanthrope
Part of a series on theParanormal 
Main articles
Astral projection
Astrology
Aura
Bilocation
Breatharianism
Clairvoyance
Close encounter
Cold spot
Crystal gazing
Conjuration
Cryptozoology
Demonic possession
Demonology
Ectoplasm
Electronic voice phenomenon
Exorcism
Extrasensory perception
Forteana
Fortune-telling
Ghost hunting
Magic
Mediumship
Miracle
Occult
Orb
Ouija
Paranormal fiction
Paranormal television
Precognition
Preternatural
Psychic
Psychic reading
Psychometry
Reincarnation
Remote viewing
Retrocognition
Spirit photography
Spirit possession
Spirit world
Spiritualism
Stone Tape
Supernatural
Telekinesis
Telepathy
Table-turning
Ufology 
Reportedly haunted locations:
India
United Kingdom
United States
World
Skepticism
Cold reading
Committee for Skeptical Inquiry
Debunking
Hoax
James Randi Educational Foundation
Magical thinking
Prizes for evidence of the paranormal
Pseudoskepticism
Scientific literacy
Scientific skepticism
Parapsychology
Anomalous experiences
Apparitional experiences
Empath
False awakening
Hypnosis
Ideomotor phenomenon
Out-of-body experiences
Parapsychology
Synchronicity 
Related
Anomalistics
Argument from ignorance
Argumentum ad populum
Bandwagon effect
Begging the question
Cognitive dissonance
Communal reinforcement
Fallacy
Falsifiability
Fringe science
Groupthink
Hypnosis
Junk science
Protoscience
Pseudoscience
Scientific evidence
Scientific method
Superstition
Uncertainty
Urban legend 
The werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.
The persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]
After the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .



--------
Getting answer
127.54113578796387 s Final answer:
--------
Summary:
The werewolf is a widespread concept in European folklore, with various variants that evolved during the Christian interpretation of underlying European folklore from medieval period to early modern period. In the New World, belief in werewolves spread through colonialism parallel to witchcraft beliefs. The persecution of supposed werewolves was an integral part of the witch-hunt phenomenon but involved a small fraction of witchcraft trials. After the witch trials ended, the werewolf became of interest in folklore studies and emerging Gothic horror genres. Modern popular culture reflects these ancient beliefs in horror and fantasy genres.

Follow-up points:
1. The evolution of the werewolf concept from European folklore to early modern period and New World colonization.
2. The connection between belief in werewolves and witchcraft trials.
3. The enduring presence of the werewolf concept even after its role in the witch-hunt phenomenon diminished.
4. The shift of interest from medieval folklore to Gothic horror and then into modern popular culture.
--------
arc.grab("Werewolf")
                       

art = arc.grab("Werewolf")
                       
art[0]
                       

art[0][0]
                       
'<h2>Werewolf</h2>'

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

6.932101488113403 s {"Articles":["Wolf", "Cyclops (animal)", "Werewolf mythology"]}
targets:  ['A/Wolf_(Wolf_album)', 'A/Wolf_pack_Wolf', 'A/100%_Wolf', 'A/10th_&_Wolf', 'A/14P/Wolf', 'A/200%_Wolf', 'A/302M_(Wolf)', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/WOLF', 'A/WoLF', 'A/Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329']
targets:  []
targets:  []
to_grabs:  ['A/Wolf_(Wolf_album)']
article sections:
   Wolf (band)
     Wolf (band) 644
     History 619
     Members 543
     Discography 550
     References 1654
Getting relevant for:  Wolf (band)
3.6419055461883545 s  Sections: ['Members', 'Discography']
sec list: 
   Wolf (band)
   ['Members', 'Discography']
--------
--------
[[('Wolf (band)', 'Wolf is a Swedish heavy metal  band from Örebro , not identical to the band Wolf from the United Kingdom. Formed in 1995, the band has since released nine studio albums and toured with Saxon , Evile , Tankard  and more recently, Trivium .[1]\n--------\nWolfBackground information\nOrigin Örebro , Sweden\nGenres Heavy metal , speed metal , power metal Years active: 1995–present\nLabels No Fashion Century Media  (Europe)Prosthetic Records  (North America)\nMembers: Niklas Stålvind  Simon Johansson   Pontus Egberg  Johan KolebergPast members: Henrik JohanssonJohan BülowDaniel BergkvistMikael GodingTobias KellgrenJohannes Losbäck\nWebsite wolf .nu\n'), ('History', 'Formed in 1995,[2] the band has since released nine studio albums[2] and have toured with renowned heavy metal bands Saxon ,[3]\nEvile [4] and more recently, Trivium .[5]  In support of their seventh studio album Devil Seed ,[6] released in August 2014, they toured the UK with Primitai[7] in early February 2015.  Wolf once again teamed up with Primitai in 2019[8] to tour the UK before the release of their eighth studio album Feeding The Machine  (2020).[9][10]\nOn 22 December 2021 the band revealed the title and artwork for their ninth studio album, Shadowland, which was subsequently released on 1 April 2022.[11]\n'), ('Members', 'Current members: Niklas Stålvind – vocals, guitar, bagpipes \n(1995–present): Simon Johansson – guitar \n(2011–present): Pontus Egberg – bass \n(2019–present): Johan Koleberg – drums \n(2019–present)\nFormer members: Henrik Y Johansson – guitar \n(1999–2000; died 2006): Johan Bülow – guitar \n(2000–2002): Daniel Bergkvist – drums \n(1995–2005): Mikael Goding – bass \n(1995–2007): Tobias Kellgren – drums \n(2005–2008): Johannes Losbäck – guitar, backing vocals \n(2002–2011): Anders G Modd – bass \n(2007–2019): Richard A Holmgren – drums \n(2008–2019)\n'), ('Discography', 'Studio albums\nWolf (2000)[12]\nBlack Wings (2002)[13]\nEvil Star (2004)[14]\nThe Black Flame  (2006)[15]\nRavenous  (2009)[16]\nLegions of Bastards  (2011)[17]\nDevil Seed  (2014)[18]\nFeeding the Machine  (2020)[9][10]\nShadowland (2022)\nOther releases\nDemo I [Demo] (1995)\nDemo II [Demo] (1996)\nDemo 98 [Demo] (1998)\nIn The Shadow of Steel [Single] (1999)\nThe Howling Scares Me to Death [Single] (1999)\nMoonlight [CD, EP] (2001)[19]\nA World Bewitched [CD, Single, Promo] (2002)[19]\nNightstalker [7", Single] (2002)[19]\nWolf\'s Blood [CD, Single] (2004)[19]\n'), ('References', 'Wolf at Harley Rock Riders Season 3 in Bangalore , Withjim.com\n"Wolf (3)" . Discogs. Retrieved 12 October 2019.\n"08/14/2009: Bloodstock Open Air 2009 @ Catton Hall | Concert Archives" . www.concertarchives.org. Retrieved 12 October 2019.\n"10/24/2012: Wolf / EVILE / Septic Fatality @ Corporation | Concert Archives" . www.concertarchives.org. Retrieved 12 October 2019.\n"08/07/2015: Bloodstock Open Air 2015 @ Catton Hall | Concert Archives" . www.concertarchives.org. Retrieved 13 October 2019.\n"Wolf: Devil Seed". Tour advertisement. Kerrang! . No.\xa01551. 17 January 2015. p.\xa037.\n"Wolf @ Underworld" . Bandsintown. Retrieved 13 October 2019.\n"PRIMITAI to support Wolf on UK tour & SEVEN SISTERS announce more festival appearances" . R o c k \'N\' L o a d. 10 January 2019. Retrieved 13 October 2019.\n"Century Media Records – Wolf" . www.centurymedia.com. Retrieved 13 October 2019.\nnewsteam (30 September 2019). "Wolf To Release New Album "Feeding The Machine", in 2020, Announces New Members" . Ghost Cult Magazine. Retrieved 13 October 2019.\n"WOLF To Release Shadowland Album In April; Artwork Revealed" . Bravewords. 22 December 2021. Retrieved 22 December 2021.\n"Wolf (3) – Wolf" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – Black Wings" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – Evil Star" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – The Black Flame" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – Ravenous" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – Legions Of Bastards" . Discogs. Retrieved 13 October 2019.\n"Wolf (3) – Devil Seed" . Discogs. Retrieved 13 October 2019.\n"Wolf (3)" . Discogs. Retrieved 13 October 2019.\n')]]
--------
--------
    sec: Wolf (band)
             ('Wolf (band)', ['Members', 'Discography'])
    sec: History
             ('Wolf (band)', ['Members', 'Discography'])
    sec: Members
             ('Wolf (band)', ['Members', 'Discography'])
    sec: Discography
             ('Wolf (band)', ['Members', 'Discography'])
    sec: References
             ('Wolf (band)', ['Members', 'Discography'])
background text: 
--------
###Article: Wolf (band)
Wolf (band)
Wolf is a Swedish heavy metal  band from Örebro , not identical to the band Wolf from the United Kingdom. Formed in 1995, the band has since released nine studio albums and toured with Saxon , Evile , Tankard  and more recently, Trivium .[1]
--------
WolfBackground information
Origin Örebro , Sweden
Genres Heavy metal , speed metal , power metal Years active: 1995–present
Labels No Fashion Century Media  (Europe)Prosthetic Records  (North America)
Members: Niklas Stålvind  Simon Johansson   Pontus Egberg  Johan KolebergPast members: Henrik JohanssonJohan BülowDaniel BergkvistMikael GodingTobias KellgrenJohannes Losbäck
Website wolf .nu



--------
Getting answer
32.56225538253784 s Final answer:
--------
Brief Summary:
Wolf is a Swedish heavy metal band based in Örebro, Sweden. Formed in 1995, they have released nine studio albums and have toured with various bands including Saxon, Evile, Tankard, and Trivium. The band features members like Niklas Stålvind, Simon Johansson, Pontus Egberg, and Johan Koleberg.

Follow-ups:
- What other notable bands Wolf has toured with in addition to the ones mentioned?
- How many studio albums has Wolf released since their formation in 1995?
- Can you provide information on any significant changes in lineup or members over the band's history? 
- Where can fans purchase Wolf's music and follow them online? 

The articles cover these aspects while focusing on the main point that Wolf is a Swedish heavy metal band from Örebro, Sweden.
--------
arc.suggestions("Wolf")
                       
['A/Wolf_(Wolf_album)', 'A/Wolf_pack_Wolf', 'A/100%_Wolf', 'A/10th_&_Wolf', 'A/14P/Wolf', 'A/200%_Wolf', 'A/302M_(Wolf)', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/WOLF', 'A/WoLF', 'A/Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329']
arc.grab("A/200%_Wolf")
                       
[('<h2>100% Wolf</h2>', '\n100% Wolf\n100% Wolf is an Australian animated <span id="Adventure_film" title onclick="linkClicked(event);" style="color:blue;">adventure</span> \n<span id="Fantasy_comedy" title onclick="linkClicked(event);" style="color:blue;">fantasy comedy</span>  film directed by Alexs Stadermann and produced by Alexia Gates-Foale and Barbara Stephen.[6][7][8] It is adapted from Jayne Lyons\' 2009 novel of the same name. It features the voices of <span id="Jai_Courtney" title onclick="linkClicked(event);" style="color:blue;">Jai Courtney</span> , <span id="Samara_Weaving" title onclick="linkClicked(event);" style="color:blue;">Samara Weaving</span> , <span id="Magda_Szubanski" title onclick="linkClicked(event);" style="color:blue;">Magda Szubanski</span> , <span id="Rhys_Darby" title onclick="linkClicked(event);" style="color:blue;">Rhys Darby</span> , Ilai Swindells, <span id="Akmal_Saleh" title onclick="linkClicked(event);" style="color:blue;">Akmal Saleh</span> , <span id="Rupert_Degas" title onclick="linkClicked(event);" style="color:blue;">Rupert Degas</span> , and <span id="Jane_Lynch" title onclick="linkClicked(event);" style="color:blue;">Jane Lynch</span> .\n--------\n100% Wolf\nDirected by: Alexs Stadermann\nWritten by: Fin Edquist\nBased on 100% Wolfby Jayne Lyons\nProduced by Alexia Gates-Foale, Barbara Stephen\nStarring \n<span id="Jai_Courtney" title onclick="linkClicked(event);" style="color:blue;">Jai Courtney</span> \n<span id="Samara_Weaving" title onclick="linkClicked(event);" style="color:blue;">Samara Weaving</span> \n<span id="Magda_Szubanski" title onclick="linkClicked(event);" style="color:blue;">Magda Szubanski</span> \n<span id="Rhys_Darby" title onclick="linkClicked(event);" style="color:blue;">Rhys Darby</span> : Ilai Swindells, \n<span id="Akmal_Saleh" title onclick="linkClicked(event);" style="color:blue;">Akmal Saleh</span> \n<span id="Rupert_Degas" title onclick="linkClicked(event);" style="color:blue;">Rupert Degas</span> \n<span id="Jane_Lynch" title onclick="linkClicked(event);" style="color:blue;">Jane Lynch</span> \n\nCinematography: Heidy Villafane\nEdited by: Simon Klaebe\nMusic by: Ash Gibson GreigProductioncompany<span id="Flying_Bark_Productions" title onclick="linkClicked(event);" style="color:blue;">Flying Bark Productions</span> \nDistributed by <span id="Studio_100" title onclick="linkClicked(event);" style="color:blue;">Studio 100</span> Release date: 29\n\xa0May\xa02020\xa0(2020-05-29)[1]\nRunning time: 96 minutes[2]\nCountry: Australia[3]\nLanguage: English\nBox office: $8.1 million[4][5]\n100% Wolf was produced by <span id="Flying_Bark_Productions" title onclick="linkClicked(event);" style="color:blue;">Flying Bark Productions</span>  and released on May 29, 2020, by <span id="Studio_100" title onclick="linkClicked(event);" style="color:blue;">Studio 100</span> . It received positive reviews from critics and grossed $8.1 million worldwide.\n', ['"Adventure_film" title', '"Fantasy_comedy" title', '"Jai_Courtney" title', '"Samara_Weaving" title', '"Magda_Szubanski" title', '"Rhys_Darby" title', '"Akmal_Saleh" title', '"Rupert_Degas" title', '"Jane_Lynch" title', '"Jai_Courtney" title', '"Samara_Weaving" title', '"Magda_Szubanski" title', '"Rhys_Darby" title', '"Akmal_Saleh" title', '"Rupert_Degas" title', '"Jane_Lynch" title', '"Flying_Bark_Productions" title', '"Studio_100" title', '"Flying_Bark_Productions" title', '"Studio_100" title']), ('<h3>Plot</h3>', '\nFreddy Lupin is the young heir to a <span id="Werewolf" title onclick="linkClicked(event);" style="color:blue;">werewolf</span>  pack that has been protecting their local town for years. When he attempts to follow his family during their nightly patrol using a magical <span id="Moonstone_(gemstone)" title onclick="linkClicked(event);" style="color:blue;">moonstone</span> , he loses the moonstone to Foxwell Cripp, and Flashheart is apparently killed when he falls off a cliff. Freddy\'s uncle, Hotspur, becomes the new pack leader.\nSix years later, the time comes for Freddy to experience his first wolf transformation, but despite the encouragement of long-term housekeeper Mrs. Mutton, he is humiliated when he turns into a <span id="Poodle" title onclick="linkClicked(event);" style="color:blue;">poodle</span>  instead. Faced with the disdain of his pack, Freddy is challenged to prove his wolf status by moonrise the next day or risk being banished. Freddy decides to try and retrieve the moonstone from Cripp.\nWhile searching in town, Freddy befriends Batty, a stray dog also known as \'Houndini\' for her ability to escape the dog catchers consistently. Batty leads him to Cripp, where they are both caught by dog catchers and placed in the Coldfax Dog Pound. After an escape attempt goes wrong, Freddy is sent to a pit with \'the Beast\', an unknown monster that supposedly eats dogs. Freddy learns that the \'Beast\' is actually his father. The dog catchers captured Flasheart after he was injured by the fall, and Hotspur left him in Coldfax with a silver bracelet to keep him trapped in his wolf state. Batty and the other dogs escape into the vents and help Freddy free his father.\nFreddy leads Flasheart and the dogs home to confront Hotspur. Cripp attacks the other wolves with a mass of silver concentrate, but Freddy stops Cripp\'s attack. Hotspur tries to attack while the other wolves are weakened by the silver, but the dogs are able to get the wolves to safety while Freddy lures his uncle to the mansion roof. Transforming back into a poodle in the moonlight and accepting his form, Freddy lets out a loud roar to affirm his status as an alpha wolf, sending Hotspur falling back into the mansion and affirming his failure as a leader.\nSometime later, Freddy\'s reflections reveal that not only have werewolves and dogs gotten on better terms, but the pack has also opened the mansion up to all dogs, with Hotspur and his children reduced to dog-walkers and picking up after the mutts, while Coldfax is shut down. Flasheart has returned to his old role as pack leader, but he assures Freddy that he is proud of him and believes he will be a good leader when the time comes.\n', ['"Werewolf" title', '"Moonstone_(gemstone)" title', '"Poodle" title']), ('<h3>Cast</h3>', ', Jerra Wright Smith as young Freddy Lupin\n<span id="Samara_Weaving" title onclick="linkClicked(event);" style="color:blue;">Samara Weaving</span>  as Batty\n<span id="Jai_Courtney" title onclick="linkClicked(event);" style="color:blue;">Jai Courtney</span>  as Flasheart Lupin\n<span id="Rupert_Degas" title onclick="linkClicked(event);" style="color:blue;">Rupert Degas</span>  as Hotspur Lupin\n<span id="Jane_Lynch" title onclick="linkClicked(event);" style="color:blue;">Jane Lynch</span>  as The Commander\n<span id="Rhys_Darby" title onclick="linkClicked(event);" style="color:blue;">Rhys Darby</span>  as Foxwell Cripp\n<span id="Magda_Szubanski" title onclick="linkClicked(event);" style="color:blue;">Magda Szubanski</span>  as Mrs. Mutton\n<span id="Akmal_Saleh" title onclick="linkClicked(event);" style="color:blue;">Akmal Saleh</span>  as Hamish\n<span id="Loren_Gray" title onclick="linkClicked(event);" style="color:blue;">Loren Gray</span>  (US) and Sarah Harper (AUS) as Twitchy: Michael Bourchier as Lord Hightail, , Kate Hall as Lady Hightail, Adriane Daff as Harriet\n<span id="Liam_Graham" title onclick="linkClicked(event);" style="color:blue;">Liam Graham</span>  as Chariot: Alexs Stadermann as Cerberus, , Jenna Suffern as Dolph, James Marsh as Stu the Dogcatcher, Cam Ralph as Steve the Dogcatcher, Jessica Window as Street Hawker Dog\n', ['"Samara_Weaving" title', '"Jai_Courtney" title', '"Rupert_Degas" title', '"Jane_Lynch" title', '"Rhys_Darby" title', '"Magda_Szubanski" title', '"Akmal_Saleh" title', '"Loren_Gray" title', '"Liam_Graham" title']), ('<h3>Sequel</h3>', '\nA sequel titled 200% Wolf is expected to be released in 2024.[9] On April 29, 2024, Flying Bark Productions announced via social media that the film would be released on August 8, 2024, in Australian cinemas and on August 23, 2024, in the United States.[10]\n', []), ('<h3>Reception</h3>', '\n100% Wolf received positive reviews from critics and earned a total of $7.7 million worldwide.[4][5]\n<span id="Rotten_Tomatoes" title onclick="linkClicked(event);" style="color:blue;">Rotten Tomatoes</span>  the film has an approval rating of 67% based on reviews from 15 critics.[11]\n', ['"Rotten_Tomatoes" title']), ('<h3>TV series</h3>', '\nA 26-episode TV series spin-off, <span id="100%25_Wolf%3A_Legend_of_the_Moonstone" title onclick="linkClicked(event);" style="color:blue;">100% Wolf: Legend of the Moonstone</span> , screened on <span id="ABC_ME" title onclick="linkClicked(event);" style="color:blue;">ABC ME</span>  on December 28, 2020, produced by <span id="Flying_Bark_Productions" title onclick="linkClicked(event);" style="color:blue;">Flying Bark Productions</span>  and <span id="Studio_100_Animation" title onclick="linkClicked(event);" style="color:blue;">Studio 100 Animation</span> .[12] Season 2 (The Book of Hath) aired on ABC ME on May 1, 2023.\n', ['"100%25_Wolf%3A_Legend_of_the_Moonstone" title', '"ABC_ME" title', '"Flying_Bark_Productions" title', '"Studio_100_Animation" title']), ('<h3>References</h3>', '\n<span id="https://web.archive.org/web/20201003192313/https://www.screenwest.com.au/news-events/2020/05/100-wolf-transfigures-small-screen-masterpiece/" class onclick="linkClicked(event);" style="color:blue;">"100% Wolf on Premium Video on Demand from. May 2020"</span> . May 28, 2020. Archived from <span id="https://www.screenwest.com.au/news-events/2020/05/100-wolf-transfigures-small-screen-masterpiece/" class onclick="linkClicked(event);" style="color:blue;">the original</span>  on October 3, 2020. Retrieved June 19, 2020.\n<span id="https://www.screenaustralia.gov.au/sa/media-centre/news/2018/01-17-100-wolf-receives-production-funding" class onclick="linkClicked(event);" style="color:blue;">"Animated family feature 100% Wolf receives production funding :Media centre"</span> . Screen Australia. Australia: <span id="Screen_Australia" title onclick="linkClicked(event);" style="color:blue;">Screen Australia</span> , <span id="Government_of_Australia" title onclick="linkClicked(event);" style="color:blue;">Government of Australia</span> . <span id="https://web.archive.org/web/20190409095857/https://www.screenaustralia.gov.au/sa/media-centre/news/2018/01-17-100-wolf-receives-production-funding" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on April 9, 2019. Retrieved June 18, 2020.\n<span id="https://www.bbfc.co.uk/release/100-wolf-q29sbgvjdglvbjpwwc01mjkzmjy" class onclick="linkClicked(event);" style="color:blue;">"100% Wolf"</span> . <span id="British_Board_of_Film_Classification" title onclick="linkClicked(event);" style="color:blue;">British Board of Film Classification</span> . <span id="https://web.archive.org/web/20230209012508/https://www.bbfc.co.uk/release/100-wolf-q29sbgvjdglvbjpwwc01mjkzmjy" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on February 9, 2023. Retrieved February 9, 2023. 100% WOLF is an Australian animated adventure in which a teenager from a family of werewolves discovers that his own transformation powers turn him into a poodle.\n<span id="https://www.boxofficemojo.com/title/tt8774798/" class onclick="linkClicked(event);" style="color:blue;">"100% Wolf"</span> . <span id="Box_Office_Mojo" title onclick="linkClicked(event);" style="color:blue;">Box Office Mojo</span> . <span id="https://web.archive.org/web/20201101183919/https://www.boxofficemojo.com/title/tt8774798/" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on November 1, 2020. Retrieved June 4, 2021.\n<span id="https://www.the-numbers.com/movie/100-Percent-Wolf-(2020-Oz)#tab onclick="linkClicked(event);" style="color:blue;">"100% Wolf"</span> . <span id="The_Numbers_(website)" title onclick="linkClicked(event);" style="color:blue;">The Numbers</span> . <span id="https://web.archive.org/web/20210215003923/https://www.the-numbers.com/movie/100-Percent-Wolf-(2020-Oz)#tab onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on February 15, 2021. Retrieved June 4, 2021.\n<span id="https://www.screenaustralia.gov.au/the-screen-guide/t/100--wolf-2019/34581/" class onclick="linkClicked(event);" style="color:blue;">"100% Wolf (2019) – The Screen Guide – Screen Australia"</span> . www.screenaustralia.gov.au. Australia: <span id="Screen_Australia" title onclick="linkClicked(event);" style="color:blue;">Screen Australia</span> , <span id="Government_of_Australia" title onclick="linkClicked(event);" style="color:blue;">Government of Australia</span> . <span id="https://web.archive.org/web/20200228213737/https://www.screenaustralia.gov.au/the-screen-guide/t/100--wolf-2019/34581" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on February 28, 2020. Retrieved June 18, 2020.\nHall, Sandra (May 27, 2020). <span id="https://www.smh.com.au/culture/movies/spirited-tale-of-a-wolf-in-poodle-s-clothing-20200527-p54wxq.html" class onclick="linkClicked(event);" style="color:blue;">"Spirited tale of a wolf in poodle\'s clothing"</span> . The Sydney Morning Herald. Sydney, Australia: <span id="The_Sydney_Morning_Herald" title onclick="linkClicked(event);" style="color:blue;">The Sydney Morning Herald</span> . <span id="https://web.archive.org/web/20200615032049/https://www.smh.com.au/culture/movies/spirited-tale-of-a-wolf-in-poodle-s-clothing-20200527-p54wxq.html" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on June 15, 2020. Retrieved June 18, 2020.\n<span id="https://www.awn.com/news/flying-bark-productions-starts-work-100-wolf" class onclick="linkClicked(event);" style="color:blue;">"Flying Bark Productions Starts Work on \'100% Wolf\'"</span> . Animation World Network. <span id="Animation_World_Network" title onclick="linkClicked(event);" style="color:blue;">Animation World Network</span> . <span id="https://web.archive.org/web/20190714145014/https://www.awn.com/news/flying-bark-productions-starts-work-100-wolf" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on July 14, 2019. Retrieved June 18, 2020.\n<span id="https://www.screenaustralia.gov.au/the-screen-guide/t/200--wolf-2023/40314/" class onclick="linkClicked(event);" style="color:blue;">"200% Wolf (2023) - the Screen Guide - Screen Australia"</span> . <span id="https://web.archive.org/web/20220709203842/https://www.screenaustralia.gov.au/the-screen-guide/t/200--wolf-2023/40314/" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on July 9, 2022. Retrieved July 9, 2022.\n<span id="https://www.facebook.com/share/v/dKKJaddXhPkJy24T/?mibextid onclick="linkClicked(event);" style="color:blue;">"Flying Bark Productions\' 200% Wolf release date announcement"</span> . <span id="Facebook" title onclick="linkClicked(event);" style="color:blue;">Facebook</span> . Retrieved April 28, 2024.\n<span id="https://www.rottentomatoes.com/m/100_wolf" class onclick="linkClicked(event);" style="color:blue;">"100% Wolf (2020)"</span> . <span id="Rotten_Tomatoes" title onclick="linkClicked(event);" style="color:blue;">Rotten Tomatoes</span> . <span id="https://web.archive.org/web/20200801143747/https://www.rottentomatoes.com/m/100_wolf" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on August 1, 2020. Retrieved October 20, 2020.\nKnox, David (December 26, 2020). <span id="https://tvtonight.com.au/2020/12/airdate-100-wolf.html/" class onclick="linkClicked(event);" style="color:blue;">"Airdate: 100% Wolf"</span> . tvtonight.com.au. <span id="https://web.archive.org/web/20210208200858/https://tvtonight.com.au/2020/12/airdate-100-wolf.html" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on February 8, 2021. Retrieved September 19, 2021.\nFrater, Patrick (January 18, 2018). <span id="https://variety.com/2018/film/asia/go-karts-100-wolf-head-funding-slate-for-screenwest-screen-australia-1202668020/" class onclick="linkClicked(event);" style="color:blue;">"\'Go Karts,\' \'100% Wolf\' Head Funding Slate for Screenwest, Screen Australia"</span> . Variety. <span id="Variety.com" title onclick="linkClicked(event);" style="color:blue;">Variety.com</span> . <span id="https://web.archive.org/web/20200220030020/https://variety.com/2018/film/asia/go-karts-100-wolf-head-funding-slate-for-screenwest-screen-australia-1202668020/" class onclick="linkClicked(event);" style="color:blue;">Archived</span>  from the original on February 20, 2020. Retrieved June 18, 2020.\n', ['"https://web.archive.org/web/20201003192313/https://www.screenwest.com.au/news-events/2020/05/100-wolf-transfigures-small-screen-masterpiece/" class', '"https://www.screenwest.com.au/news-events/2020/05/100-wolf-transfigures-small-screen-masterpiece/" class', '"https://www.screenaustralia.gov.au/sa/media-centre/news/2018/01-17-100-wolf-receives-production-funding" class', '"Screen_Australia" title', '"Government_of_Australia" title', '"https://web.archive.org/web/20190409095857/https://www.screenaustralia.gov.au/sa/media-centre/news/2018/01-17-100-wolf-receives-production-funding" class', '"https://www.bbfc.co.uk/release/100-wolf-q29sbgvjdglvbjpwwc01mjkzmjy" class', '"British_Board_of_Film_Classification" title', '"https://web.archive.org/web/20230209012508/https://www.bbfc.co.uk/release/100-wolf-q29sbgvjdglvbjpwwc01mjkzmjy" class', '"https://www.boxofficemojo.com/title/tt8774798/" class', '"Box_Office_Mojo" title', '"https://web.archive.org/web/20201101183919/https://www.boxofficemojo.com/title/tt8774798/" class', '"https://www.the-numbers.com/movie/100-Percent-Wolf-(2020-Oz)#tab', '"The_Numbers_(website)" title', '"https://web.archive.org/web/20210215003923/https://www.the-numbers.com/movie/100-Percent-Wolf-(2020-Oz)#tab', '"https://www.screenaustralia.gov.au/the-screen-guide/t/100--wolf-2019/34581/" class', '"Screen_Australia" title', '"Government_of_Australia" title', '"https://web.archive.org/web/20200228213737/https://www.screenaustralia.gov.au/the-screen-guide/t/100--wolf-2019/34581" class', '"https://www.smh.com.au/culture/movies/spirited-tale-of-a-wolf-in-poodle-s-clothing-20200527-p54wxq.html" class', '"The_Sydney_Morning_Herald" title', '"https://web.archive.org/web/20200615032049/https://www.smh.com.au/culture/movies/spirited-tale-of-a-wolf-in-poodle-s-clothing-20200527-p54wxq.html" class', '"https://www.awn.com/news/flying-bark-productions-starts-work-100-wolf" class', '"Animation_World_Network" title', '"https://web.archive.org/web/20190714145014/https://www.awn.com/news/flying-bark-productions-starts-work-100-wolf" class', '"https://www.screenaustralia.gov.au/the-screen-guide/t/200--wolf-2023/40314/" class', '"https://web.archive.org/web/20220709203842/https://www.screenaustralia.gov.au/the-screen-guide/t/200--wolf-2023/40314/" class', '"https://www.facebook.com/share/v/dKKJaddXhPkJy24T/?mibextid', '"Facebook" title', '"https://www.rottentomatoes.com/m/100_wolf" class', '"Rotten_Tomatoes" title', '"https://web.archive.org/web/20200801143747/https://www.rottentomatoes.com/m/100_wolf" class', '"https://tvtonight.com.au/2020/12/airdate-100-wolf.html/" class', '"https://web.archive.org/web/20210208200858/https://tvtonight.com.au/2020/12/airdate-100-wolf.html" class', '"https://variety.com/2018/film/asia/go-karts-100-wolf-head-funding-slate-for-screenwest-screen-australia-1202668020/" class', '"Variety.com" title', '"https://web.archive.org/web/20200220030020/https://variety.com/2018/film/asia/go-karts-100-wolf-head-funding-slate-for-screenwest-screen-australia-1202668020/" class'])]
arc.grab("A/Wolf")
                       

art = arc.grab("A/Wolf")
                       
art[0]
                       
('<h2>Wolf</h2>', '\n\nThe wolf (Canis lupus;[lower-alpha 2]\npl.: wolves), also known as the gray wolf or grey wolf, is a large <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">canine</span>  native to <span id="Eurasia" title onclick="linkClicked(event);" style="color:blue;">Eurasia</span>  and <span id="North_America" title onclick="linkClicked(event);" style="color:blue;">North America</span> . More than thirty <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">subspecies of </span> Canis lupus have been recognized, including the <span id="Dog" title onclick="linkClicked(event);" style="color:blue;">dog</span>  and <span id="Dingo" title onclick="linkClicked(event);" style="color:blue;">dingo</span> , though gray wolves, as popularly understood, only comprise naturally-occurring wild subspecies. The wolf is the largest <span id="Neontology" title onclick="linkClicked(event);" style="color:blue;">extant</span>  member of the family <span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> , and is further distinguished from other <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">Canis</span>  species by its less pointed ears and muzzle, as well as a shorter torso and a longer tail. The wolf is nonetheless related closely enough to smaller Canis species, such as the <span id="Coyote" title onclick="linkClicked(event);" style="color:blue;">coyote</span>  and the <span id="Golden_jackal" title onclick="linkClicked(event);" style="color:blue;">golden jackal</span> , to produce fertile <span id="Canid_hybrid" title onclick="linkClicked(event);" style="color:blue;">hybrids</span>  with them. The wolf\'s fur is usually mottled white, brown, gray, and black, although subspecies in the arctic region may be nearly all white.\nThis article is about the wolf within the species Canis lupus. For other species of wolf or other uses of "wolf" and "wolves", see <span id="Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Wolf (disambiguation)</span> .\n"Grey Wolf" and "Gray Wolf" redirect here. For other uses, see <span id="Grey_Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Grey Wolf (disambiguation)</span> .\nWolfTemporal range: <span id="Middle_Pleistocene" title onclick="linkClicked(event);" style="color:blue;">Middle Pleistocene</span>  – present\n(810,000–0 <span id="Before_Present" title onclick="linkClicked(event);" style="color:blue;">YBP</span> )[1]\n<span id="Eurasian_wolf" title onclick="linkClicked(event);" style="color:blue;">Eurasian wolf</span>  (Canis lupus lupus) at <span id="Polar_Park_(animal_park)" title onclick="linkClicked(event);" style="color:blue;">Polar Park</span>  in Bardu, Norway\n<span id="Conservation_status" title onclick="linkClicked(event);" style="color:blue;">Conservation status</span> \n<span id="Least_Concern" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span> \n\xa0(<span id="IUCN_Red_List" title onclick="linkClicked(event);" style="color:blue;">IUCN 3.1</span> )[2]\n<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span>  Appendix II\xa0(<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span> )[3][lower-alpha 1]\n<span id="Taxonomy_(biology)" title onclick="linkClicked(event);" style="color:blue;">Scientific classification</span> \nDomain:\n<span id="Eukaryote" title onclick="linkClicked(event);" style="color:blue;">Eukaryota</span> \nKingdom:\n<span id="Animal" title onclick="linkClicked(event);" style="color:blue;">Animalia</span> \nPhylum:\n<span id="Chordate" title onclick="linkClicked(event);" style="color:blue;">Chordata</span> \nClass:\n<span id="Mammal" title onclick="linkClicked(event);" style="color:blue;">Mammalia</span> \nOrder:\n<span id="Carnivora" title onclick="linkClicked(event);" style="color:blue;">Carnivora</span> \nFamily:\n<span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> \nGenus:\nCanis\nSpecies:\nC.\xa0lupus\n<span id="Binomial_nomenclature" title onclick="linkClicked(event);" style="color:blue;">Binomial name</span> \nCanis lupus<span id="Carl_Linnaeus" title onclick="linkClicked(event);" style="color:blue;">Linnaeus</span> , <span id="10th_edition_of_Systema_Naturae" title onclick="linkClicked(event);" style="color:blue;">1758</span> [4]\nSubspecies\nSee <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">Subspecies of </span> Canis lupus\nGlobal wolf range based on IUCN\'s 2023 assessment.[2]\nOf all members of the <span id="Genus" title onclick="linkClicked(event);" style="color:blue;">genus</span> \nCanis, the wolf is most <span id="Generalist_and_specialist_species" title onclick="linkClicked(event);" style="color:blue;">specialized</span>  for <span id="Pack_hunter" title onclick="linkClicked(event);" style="color:blue;">cooperative</span> \n<span id="Hunting_behavior_of_gray_wolves" title onclick="linkClicked(event);" style="color:blue;">game hunting</span>  as demonstrated by its physical adaptations to tackling large prey, its more <span id="Sociality" title onclick="linkClicked(event);" style="color:blue;">social nature</span> , and its highly advanced <span id="Wolf_communication" title onclick="linkClicked(event);" style="color:blue;">expressive behaviour</span> , including individual or group <span id="Howling" title onclick="linkClicked(event);" style="color:blue;">howling</span> . It travels in <span id="Nuclear_family" title onclick="linkClicked(event);" style="color:blue;">nuclear families</span>  consisting of a <span id="Mated_pair" title onclick="linkClicked(event);" style="color:blue;">mated pair</span>  accompanied by their offspring. Offspring may leave to form their own <span id="Pack_(canine)" title onclick="linkClicked(event);" style="color:blue;">packs</span>  on the onset of sexual maturity and in response to competition for food within the pack. Wolves are also <span id="Territory_(animal)" title onclick="linkClicked(event);" style="color:blue;">territorial</span> , and fights over territory are among the principal causes of mortality. The wolf is mainly a <span id="Carnivore" title onclick="linkClicked(event);" style="color:blue;">carnivore</span>  and feeds on large wild <span id="Hooved_mammal" title onclick="linkClicked(event);" style="color:blue;">hooved mammals</span>  as well as smaller animals, livestock, <span id="Carrion" title onclick="linkClicked(event);" style="color:blue;">carrion</span> , and garbage. Single wolves or mated pairs typically have higher success rates in hunting than do large packs. <span id="Pathogen" title onclick="linkClicked(event);" style="color:blue;">Pathogens</span>  and parasites, notably the <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies virus</span> , may infect wolves.\nThe global wild wolf population was estimated to be 300,000 in 2003 and is considered to be of <span id="Least-concern_species" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span>  by the <span id="International_Union_for_Conservation_of_Nature" title onclick="linkClicked(event);" style="color:blue;">International Union for Conservation of Nature</span>  (IUCN). Wolves have a long history of interactions with humans, having been despised and hunted in most <span id="Pastoralism" title onclick="linkClicked(event);" style="color:blue;">pastoral</span>  communities because of their attacks on livestock, while conversely being respected in some <span id="Agrarian_society" title onclick="linkClicked(event);" style="color:blue;">agrarian</span>  and <span id="Hunter-gatherer" title onclick="linkClicked(event);" style="color:blue;">hunter-gatherer</span>  societies. Although the fear of wolves exists in many human societies, the majority of recorded attacks on people have been attributed to animals suffering from <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies</span> . <span id="Wolf_attack" title onclick="linkClicked(event);" style="color:blue;">Wolf attacks</span>  on humans are rare because wolves are relatively few, live away from people, and have developed a fear of humans because of their experiences with hunters, farmers, ranchers, and shepherds.\n', ['"Canis" title', '"Eurasia" title', '"North_America" title', '"Subspecies_of_Canis_lupus" title', '"Dog" title', '"Dingo" title', '"Neontology" title', '"Canidae" title', '"Canis" title', '"Coyote" title', '"Golden_jackal" title', '"Canid_hybrid" title', '"Wolf_(disambiguation)" title', '"Grey_Wolf_(disambiguation)" title', '"Middle_Pleistocene" title', '"Before_Present" title', '"Eurasian_wolf" title', '"Polar_Park_(animal_park)" title', '"Conservation_status" title', '"Least_Concern" title', '"IUCN_Red_List" title', '"CITES" title', '"CITES" title', '"Taxonomy_(biology)" title', '"Eukaryote" title', '"Animal" title', '"Chordate" title', '"Mammal" title', '"Carnivora" title', '"Canidae" title', '"Binomial_nomenclature" title', '"Carl_Linnaeus" title', '"10th_edition_of_Systema_Naturae" title', '"Subspecies_of_Canis_lupus" title', '"Genus" title', '"Generalist_and_specialist_species" title', '"Pack_hunter" title', '"Hunting_behavior_of_gray_wolves" title', '"Sociality" title', '"Wolf_communication" title', '"Howling" title', '"Nuclear_family" title', '"Mated_pair" title', '"Pack_(canine)" title', '"Territory_(animal)" title', '"Carnivore" title', '"Hooved_mammal" title', '"Carrion" title', '"Pathogen" title', '"Rabies" title', '"Least-concern_species" title', '"International_Union_for_Conservation_of_Nature" title', '"Pastoralism" title', '"Agrarian_society" title', '"Hunter-gatherer" title', '"Rabies" title', '"Wolf_attack" title'])
arc.search("Wolf")
                       
['A/Wolf_(name)', 'A/Wolfe_(surname)', 'A/Wolf_(disambiguation)', 'A/Juno_(album)', 'A/Eastern_wolf', 'A/Big_Bad_Wolf', 'A/Thomas_Wolfe', 'A/Wolf_Creek', 'A/Chelsea_Wolfe', 'A/Nero_Wolfe', 'A/Randy_Wolf', 'A/James_Wolfe', 'A/Tom_Wolfe', 'A/Wolf_hunting', 'A/Red_wolf', 'A/Danny_Wolfe', 'A/Meow_Wolf', 'A/Indian_wolf', 'A/Tom_Wolf', 'A/Italian_wolf']
sr = arc.search("Wolf")
                       
sg = arc.suggestions("Wolf")
                       
sr
                       
['A/Wolf_(name)', 'A/Wolfe_(surname)', 'A/Wolf_(disambiguation)', 'A/Juno_(album)', 'A/Eastern_wolf', 'A/Big_Bad_Wolf', 'A/Thomas_Wolfe', 'A/Wolf_Creek', 'A/Chelsea_Wolfe', 'A/Nero_Wolfe', 'A/Randy_Wolf', 'A/James_Wolfe', 'A/Tom_Wolfe', 'A/Wolf_hunting', 'A/Red_wolf', 'A/Danny_Wolfe', 'A/Meow_Wolf', 'A/Indian_wolf', 'A/Tom_Wolf', 'A/Italian_wolf']
sg
                       
['A/Wolf_(Wolf_album)', 'A/Wolf_pack_Wolf', 'A/100%_Wolf', 'A/10th_&_Wolf', 'A/14P/Wolf', 'A/200%_Wolf', 'A/302M_(Wolf)', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/WOLF', 'A/WoLF', 'A/Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329']
for a in sg:
                       if not(a in sr):
                       print(a)
                       
SyntaxError: expected an indented block after 'if' statement on line 2

for a in sg:
    if not(a in sr):
        print(a)

                       
A/Wolf_(Wolf_album)
A/Wolf_pack_Wolf
A/100%_Wolf
A/10th_&_Wolf
A/14P/Wolf
A/200%_Wolf
A/302M_(Wolf)
A/302M_(wolf)
A/832F_(wolf)
A/WOLF
A/WoLF
A/Wolf
A/Wolf_1055
A/Wolf_1061
A/Wolf_1061b
A/Wolf_1061c
A/Wolf_1061d
A/Wolf_1069
A/Wolf_1130
A/Wolf_1329
arc.suggestor.suggest("wolf")
                       
<libzim.SuggestionSearch object at 0x726aa73d8a30>
art = arc.grab("A/Wolf")
                       
art[0][0]
                       
'<h2>Wolf</h2>'
art[0][1]
                       
'\n\nThe wolf (Canis lupus;[lower-alpha 2]\npl.: wolves), also known as the gray wolf or grey wolf, is a large <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">canine</span>  native to <span id="Eurasia" title onclick="linkClicked(event);" style="color:blue;">Eurasia</span>  and <span id="North_America" title onclick="linkClicked(event);" style="color:blue;">North America</span> . More than thirty <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">subspecies of </span> Canis lupus have been recognized, including the <span id="Dog" title onclick="linkClicked(event);" style="color:blue;">dog</span>  and <span id="Dingo" title onclick="linkClicked(event);" style="color:blue;">dingo</span> , though gray wolves, as popularly understood, only comprise naturally-occurring wild subspecies. The wolf is the largest <span id="Neontology" title onclick="linkClicked(event);" style="color:blue;">extant</span>  member of the family <span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> , and is further distinguished from other <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">Canis</span>  species by its less pointed ears and muzzle, as well as a shorter torso and a longer tail. The wolf is nonetheless related closely enough to smaller Canis species, such as the <span id="Coyote" title onclick="linkClicked(event);" style="color:blue;">coyote</span>  and the <span id="Golden_jackal" title onclick="linkClicked(event);" style="color:blue;">golden jackal</span> , to produce fertile <span id="Canid_hybrid" title onclick="linkClicked(event);" style="color:blue;">hybrids</span>  with them. The wolf\'s fur is usually mottled white, brown, gray, and black, although subspecies in the arctic region may be nearly all white.\nThis article is about the wolf within the species Canis lupus. For other species of wolf or other uses of "wolf" and "wolves", see <span id="Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Wolf (disambiguation)</span> .\n"Grey Wolf" and "Gray Wolf" redirect here. For other uses, see <span id="Grey_Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Grey Wolf (disambiguation)</span> .\nWolfTemporal range: <span id="Middle_Pleistocene" title onclick="linkClicked(event);" style="color:blue;">Middle Pleistocene</span>  – present\n(810,000–0 <span id="Before_Present" title onclick="linkClicked(event);" style="color:blue;">YBP</span> )[1]\n<span id="Eurasian_wolf" title onclick="linkClicked(event);" style="color:blue;">Eurasian wolf</span>  (Canis lupus lupus) at <span id="Polar_Park_(animal_park)" title onclick="linkClicked(event);" style="color:blue;">Polar Park</span>  in Bardu, Norway\n<span id="Conservation_status" title onclick="linkClicked(event);" style="color:blue;">Conservation status</span> \n<span id="Least_Concern" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span> \n\xa0(<span id="IUCN_Red_List" title onclick="linkClicked(event);" style="color:blue;">IUCN 3.1</span> )[2]\n<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span>  Appendix II\xa0(<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span> )[3][lower-alpha 1]\n<span id="Taxonomy_(biology)" title onclick="linkClicked(event);" style="color:blue;">Scientific classification</span> \nDomain:\n<span id="Eukaryote" title onclick="linkClicked(event);" style="color:blue;">Eukaryota</span> \nKingdom:\n<span id="Animal" title onclick="linkClicked(event);" style="color:blue;">Animalia</span> \nPhylum:\n<span id="Chordate" title onclick="linkClicked(event);" style="color:blue;">Chordata</span> \nClass:\n<span id="Mammal" title onclick="linkClicked(event);" style="color:blue;">Mammalia</span> \nOrder:\n<span id="Carnivora" title onclick="linkClicked(event);" style="color:blue;">Carnivora</span> \nFamily:\n<span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> \nGenus:\nCanis\nSpecies:\nC.\xa0lupus\n<span id="Binomial_nomenclature" title onclick="linkClicked(event);" style="color:blue;">Binomial name</span> \nCanis lupus<span id="Carl_Linnaeus" title onclick="linkClicked(event);" style="color:blue;">Linnaeus</span> , <span id="10th_edition_of_Systema_Naturae" title onclick="linkClicked(event);" style="color:blue;">1758</span> [4]\nSubspecies\nSee <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">Subspecies of </span> Canis lupus\nGlobal wolf range based on IUCN\'s 2023 assessment.[2]\nOf all members of the <span id="Genus" title onclick="linkClicked(event);" style="color:blue;">genus</span> \nCanis, the wolf is most <span id="Generalist_and_specialist_species" title onclick="linkClicked(event);" style="color:blue;">specialized</span>  for <span id="Pack_hunter" title onclick="linkClicked(event);" style="color:blue;">cooperative</span> \n<span id="Hunting_behavior_of_gray_wolves" title onclick="linkClicked(event);" style="color:blue;">game hunting</span>  as demonstrated by its physical adaptations to tackling large prey, its more <span id="Sociality" title onclick="linkClicked(event);" style="color:blue;">social nature</span> , and its highly advanced <span id="Wolf_communication" title onclick="linkClicked(event);" style="color:blue;">expressive behaviour</span> , including individual or group <span id="Howling" title onclick="linkClicked(event);" style="color:blue;">howling</span> . It travels in <span id="Nuclear_family" title onclick="linkClicked(event);" style="color:blue;">nuclear families</span>  consisting of a <span id="Mated_pair" title onclick="linkClicked(event);" style="color:blue;">mated pair</span>  accompanied by their offspring. Offspring may leave to form their own <span id="Pack_(canine)" title onclick="linkClicked(event);" style="color:blue;">packs</span>  on the onset of sexual maturity and in response to competition for food within the pack. Wolves are also <span id="Territory_(animal)" title onclick="linkClicked(event);" style="color:blue;">territorial</span> , and fights over territory are among the principal causes of mortality. The wolf is mainly a <span id="Carnivore" title onclick="linkClicked(event);" style="color:blue;">carnivore</span>  and feeds on large wild <span id="Hooved_mammal" title onclick="linkClicked(event);" style="color:blue;">hooved mammals</span>  as well as smaller animals, livestock, <span id="Carrion" title onclick="linkClicked(event);" style="color:blue;">carrion</span> , and garbage. Single wolves or mated pairs typically have higher success rates in hunting than do large packs. <span id="Pathogen" title onclick="linkClicked(event);" style="color:blue;">Pathogens</span>  and parasites, notably the <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies virus</span> , may infect wolves.\nThe global wild wolf population was estimated to be 300,000 in 2003 and is considered to be of <span id="Least-concern_species" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span>  by the <span id="International_Union_for_Conservation_of_Nature" title onclick="linkClicked(event);" style="color:blue;">International Union for Conservation of Nature</span>  (IUCN). Wolves have a long history of interactions with humans, having been despised and hunted in most <span id="Pastoralism" title onclick="linkClicked(event);" style="color:blue;">pastoral</span>  communities because of their attacks on livestock, while conversely being respected in some <span id="Agrarian_society" title onclick="linkClicked(event);" style="color:blue;">agrarian</span>  and <span id="Hunter-gatherer" title onclick="linkClicked(event);" style="color:blue;">hunter-gatherer</span>  societies. Although the fear of wolves exists in many human societies, the majority of recorded attacks on people have been attributed to animals suffering from <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies</span> . <span id="Wolf_attack" title onclick="linkClicked(event);" style="color:blue;">Wolf attacks</span>  on humans are rare because wolves are relatively few, live away from people, and have developed a fear of humans because of their experiences with hunters, farmers, ranchers, and shepherds.\n'
art = arc.grab("A/WOLF")
                       
art[0][1]
                       
'\n\nThe <span id="Wolf" title onclick="linkClicked(event);" style="color:blue;">wolf</span>  (Canis lupus) is a large canine native to Eurasia and North America.\n"Wolfish" redirects here. For the fish family, see <span id="Wolffish" title onclick="linkClicked(event);" style="color:blue;">Wolffish</span> .\nLook up <span id="https://en.wiktionary.org/wiki/Wolf" title onclick="linkClicked(event);" style="color:blue;">Wolf</span> , <span id="https://en.wiktionary.org/wiki/wolf" title onclick="linkClicked(event);" style="color:blue;">wolf</span> , <span id="https://en.wiktionary.org/wiki/Canis%20lupus" title onclick="linkClicked(event);" style="color:blue;">Canis lupus</span> , <span id="https://en.wiktionary.org/wiki/wolfish" title onclick="linkClicked(event);" style="color:blue;">wolfish</span> , or <span id="https://en.wiktionary.org/wiki/wolve" title onclick="linkClicked(event);" style="color:blue;">wolve</span>  in Wiktionary, the free dictionary.\nWolf or wolves may also refer to:\n'
arc.suggestor.suggest("wolf")sg = arc.suggestions("Wolf")
                       
SyntaxError: invalid syntax
sg = arc.suggestions("Wolf")
                       
sg
                       
['A/Wolf_(Wolf_album)', 'A/Wolf_pack_Wolf', 'A/100%_Wolf', 'A/10th_&_Wolf', 'A/14P/Wolf', 'A/200%_Wolf', 'A/302M_(Wolf)', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/WOLF', 'A/WoLF', 'A/Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329']
import Levenshtein
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#182>", line 1, in <module>
ModuleNotFoundError: No module named 'Levenshtein'
from difflib import SequenceMatcher
for a in sg:
    print(a,SequenceMatcher(None,a,"Wolf").ratio())

    
A/Wolf_(Wolf_album) 0.34782608695652173
A/Wolf_pack_Wolf 0.4
A/100%_Wolf 0.5333333333333333
A/10th_&_Wolf 0.47058823529411764
A/14P/Wolf 0.5714285714285714
A/200%_Wolf 0.5333333333333333
A/302M_(Wolf) 0.47058823529411764
A/302M_(wolf) 0.35294117647058826
A/832F_(wolf) 0.35294117647058826
A/WOLF 0.2
A/WoLF 0.4
A/Wolf 0.8
A/Wolf_1055 0.5333333333333333
A/Wolf_1061 0.5333333333333333
A/Wolf_1061b 0.5
A/Wolf_1061c 0.5
A/Wolf_1061d 0.5
A/Wolf_1069 0.5333333333333333
A/Wolf_1130 0.5333333333333333
A/Wolf_1329 0.5333333333333333
sg
['A/Wolf_(Wolf_album)', 'A/Wolf_pack_Wolf', 'A/100%_Wolf', 'A/10th_&_Wolf', 'A/14P/Wolf', 'A/200%_Wolf', 'A/302M_(Wolf)', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/WOLF', 'A/WoLF', 'A/Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329']
slist = [(s,SequenceMatcher(None,s,"Wolf").ratio()) for s in sg]
sList
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#189>", line 1, in <module>
NameError: name 'sList' is not defined. Did you mean: 'slist'?
slist
[('A/Wolf_(Wolf_album)', 0.34782608695652173), ('A/Wolf_pack_Wolf', 0.4), ('A/100%_Wolf', 0.5333333333333333), ('A/10th_&_Wolf', 0.47058823529411764), ('A/14P/Wolf', 0.5714285714285714), ('A/200%_Wolf', 0.5333333333333333), ('A/302M_(Wolf)', 0.47058823529411764), ('A/302M_(wolf)', 0.35294117647058826), ('A/832F_(wolf)', 0.35294117647058826), ('A/WOLF', 0.2), ('A/WoLF', 0.4), ('A/Wolf', 0.8), ('A/Wolf_1055', 0.5333333333333333), ('A/Wolf_1061', 0.5333333333333333), ('A/Wolf_1061b', 0.5), ('A/Wolf_1061c', 0.5), ('A/Wolf_1061d', 0.5), ('A/Wolf_1069', 0.5333333333333333), ('A/Wolf_1130', 0.5333333333333333), ('A/Wolf_1329', 0.5333333333333333)]
slist.sort(key=lambda x:x[1])
for a in slist:
    print(a)

    
('A/WOLF', 0.2)
('A/Wolf_(Wolf_album)', 0.34782608695652173)
('A/302M_(wolf)', 0.35294117647058826)
('A/832F_(wolf)', 0.35294117647058826)
('A/Wolf_pack_Wolf', 0.4)
('A/WoLF', 0.4)
('A/10th_&_Wolf', 0.47058823529411764)
('A/302M_(Wolf)', 0.47058823529411764)
('A/Wolf_1061b', 0.5)
('A/Wolf_1061c', 0.5)
('A/Wolf_1061d', 0.5)
('A/100%_Wolf', 0.5333333333333333)
('A/200%_Wolf', 0.5333333333333333)
('A/Wolf_1055', 0.5333333333333333)
('A/Wolf_1061', 0.5333333333333333)
('A/Wolf_1069', 0.5333333333333333)
('A/Wolf_1130', 0.5333333333333333)
('A/Wolf_1329', 0.5333333333333333)
('A/14P/Wolf', 0.5714285714285714)
('A/Wolf', 0.8)

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

[Articles]
5.084881067276001 s [Articles]
to_grabs:  []
article sections:
sec list: 
--------
--------
[]
--------
--------
background text: 
--------

--------
Getting answer
9.154477834701538 s Final answer:
--------
To provide an accurate response, I would need access to the attached articles. Please share the relevant information or text so that I can summarize and synthesize it appropriately to answer your specific question "{question}".
--------
sg = arc.suggestions("Wolf")
sg
['A/Wolf', 'A/14P/Wolf', 'A/100%_Wolf', 'A/200%_Wolf', 'A/Wolf_1055', 'A/Wolf_1061', 'A/Wolf_1069', 'A/Wolf_1130', 'A/Wolf_1329', 'A/Wolf_1061b', 'A/Wolf_1061c', 'A/Wolf_1061d', 'A/10th_&_Wolf', 'A/302M_(Wolf)', 'A/Wolf_pack_Wolf', 'A/WoLF', 'A/302M_(wolf)', 'A/832F_(wolf)', 'A/Wolf_(Wolf_album)', 'A/WOLF']
arc.grab(sg[0])

art = arc.grab(sg[0])
art[0][0]
'<h2>Wolf</h2>'
art[0][1]
'\n\nThe wolf (Canis lupus;[lower-alpha 2]\npl.: wolves), also known as the gray wolf or grey wolf, is a large <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">canine</span>  native to <span id="Eurasia" title onclick="linkClicked(event);" style="color:blue;">Eurasia</span>  and <span id="North_America" title onclick="linkClicked(event);" style="color:blue;">North America</span> . More than thirty <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">subspecies of </span> Canis lupus have been recognized, including the <span id="Dog" title onclick="linkClicked(event);" style="color:blue;">dog</span>  and <span id="Dingo" title onclick="linkClicked(event);" style="color:blue;">dingo</span> , though gray wolves, as popularly understood, only comprise naturally-occurring wild subspecies. The wolf is the largest <span id="Neontology" title onclick="linkClicked(event);" style="color:blue;">extant</span>  member of the family <span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> , and is further distinguished from other <span id="Canis" title onclick="linkClicked(event);" style="color:blue;">Canis</span>  species by its less pointed ears and muzzle, as well as a shorter torso and a longer tail. The wolf is nonetheless related closely enough to smaller Canis species, such as the <span id="Coyote" title onclick="linkClicked(event);" style="color:blue;">coyote</span>  and the <span id="Golden_jackal" title onclick="linkClicked(event);" style="color:blue;">golden jackal</span> , to produce fertile <span id="Canid_hybrid" title onclick="linkClicked(event);" style="color:blue;">hybrids</span>  with them. The wolf\'s fur is usually mottled white, brown, gray, and black, although subspecies in the arctic region may be nearly all white.\nThis article is about the wolf within the species Canis lupus. For other species of wolf or other uses of "wolf" and "wolves", see <span id="Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Wolf (disambiguation)</span> .\n"Grey Wolf" and "Gray Wolf" redirect here. For other uses, see <span id="Grey_Wolf_(disambiguation)" title onclick="linkClicked(event);" style="color:blue;">Grey Wolf (disambiguation)</span> .\nWolfTemporal range: <span id="Middle_Pleistocene" title onclick="linkClicked(event);" style="color:blue;">Middle Pleistocene</span>  – present\n(810,000–0 <span id="Before_Present" title onclick="linkClicked(event);" style="color:blue;">YBP</span> )[1]\n<span id="Eurasian_wolf" title onclick="linkClicked(event);" style="color:blue;">Eurasian wolf</span>  (Canis lupus lupus) at <span id="Polar_Park_(animal_park)" title onclick="linkClicked(event);" style="color:blue;">Polar Park</span>  in Bardu, Norway\n<span id="Conservation_status" title onclick="linkClicked(event);" style="color:blue;">Conservation status</span> \n<span id="Least_Concern" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span> \n\xa0(<span id="IUCN_Red_List" title onclick="linkClicked(event);" style="color:blue;">IUCN 3.1</span> )[2]\n<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span>  Appendix II\xa0(<span id="CITES" title onclick="linkClicked(event);" style="color:blue;">CITES</span> )[3][lower-alpha 1]\n<span id="Taxonomy_(biology)" title onclick="linkClicked(event);" style="color:blue;">Scientific classification</span> \nDomain:\n<span id="Eukaryote" title onclick="linkClicked(event);" style="color:blue;">Eukaryota</span> \nKingdom:\n<span id="Animal" title onclick="linkClicked(event);" style="color:blue;">Animalia</span> \nPhylum:\n<span id="Chordate" title onclick="linkClicked(event);" style="color:blue;">Chordata</span> \nClass:\n<span id="Mammal" title onclick="linkClicked(event);" style="color:blue;">Mammalia</span> \nOrder:\n<span id="Carnivora" title onclick="linkClicked(event);" style="color:blue;">Carnivora</span> \nFamily:\n<span id="Canidae" title onclick="linkClicked(event);" style="color:blue;">Canidae</span> \nGenus:\nCanis\nSpecies:\nC.\xa0lupus\n<span id="Binomial_nomenclature" title onclick="linkClicked(event);" style="color:blue;">Binomial name</span> \nCanis lupus<span id="Carl_Linnaeus" title onclick="linkClicked(event);" style="color:blue;">Linnaeus</span> , <span id="10th_edition_of_Systema_Naturae" title onclick="linkClicked(event);" style="color:blue;">1758</span> [4]\nSubspecies\nSee <span id="Subspecies_of_Canis_lupus" title onclick="linkClicked(event);" style="color:blue;">Subspecies of </span> Canis lupus\nGlobal wolf range based on IUCN\'s 2023 assessment.[2]\nOf all members of the <span id="Genus" title onclick="linkClicked(event);" style="color:blue;">genus</span> \nCanis, the wolf is most <span id="Generalist_and_specialist_species" title onclick="linkClicked(event);" style="color:blue;">specialized</span>  for <span id="Pack_hunter" title onclick="linkClicked(event);" style="color:blue;">cooperative</span> \n<span id="Hunting_behavior_of_gray_wolves" title onclick="linkClicked(event);" style="color:blue;">game hunting</span>  as demonstrated by its physical adaptations to tackling large prey, its more <span id="Sociality" title onclick="linkClicked(event);" style="color:blue;">social nature</span> , and its highly advanced <span id="Wolf_communication" title onclick="linkClicked(event);" style="color:blue;">expressive behaviour</span> , including individual or group <span id="Howling" title onclick="linkClicked(event);" style="color:blue;">howling</span> . It travels in <span id="Nuclear_family" title onclick="linkClicked(event);" style="color:blue;">nuclear families</span>  consisting of a <span id="Mated_pair" title onclick="linkClicked(event);" style="color:blue;">mated pair</span>  accompanied by their offspring. Offspring may leave to form their own <span id="Pack_(canine)" title onclick="linkClicked(event);" style="color:blue;">packs</span>  on the onset of sexual maturity and in response to competition for food within the pack. Wolves are also <span id="Territory_(animal)" title onclick="linkClicked(event);" style="color:blue;">territorial</span> , and fights over territory are among the principal causes of mortality. The wolf is mainly a <span id="Carnivore" title onclick="linkClicked(event);" style="color:blue;">carnivore</span>  and feeds on large wild <span id="Hooved_mammal" title onclick="linkClicked(event);" style="color:blue;">hooved mammals</span>  as well as smaller animals, livestock, <span id="Carrion" title onclick="linkClicked(event);" style="color:blue;">carrion</span> , and garbage. Single wolves or mated pairs typically have higher success rates in hunting than do large packs. <span id="Pathogen" title onclick="linkClicked(event);" style="color:blue;">Pathogens</span>  and parasites, notably the <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies virus</span> , may infect wolves.\nThe global wild wolf population was estimated to be 300,000 in 2003 and is considered to be of <span id="Least-concern_species" title onclick="linkClicked(event);" style="color:blue;">Least Concern</span>  by the <span id="International_Union_for_Conservation_of_Nature" title onclick="linkClicked(event);" style="color:blue;">International Union for Conservation of Nature</span>  (IUCN). Wolves have a long history of interactions with humans, having been despised and hunted in most <span id="Pastoralism" title onclick="linkClicked(event);" style="color:blue;">pastoral</span>  communities because of their attacks on livestock, while conversely being respected in some <span id="Agrarian_society" title onclick="linkClicked(event);" style="color:blue;">agrarian</span>  and <span id="Hunter-gatherer" title onclick="linkClicked(event);" style="color:blue;">hunter-gatherer</span>  societies. Although the fear of wolves exists in many human societies, the majority of recorded attacks on people have been attributed to animals suffering from <span id="Rabies" title onclick="linkClicked(event);" style="color:blue;">rabies</span> . <span id="Wolf_attack" title onclick="linkClicked(event);" style="color:blue;">Wolf attacks</span>  on humans are rare because wolves are relatively few, live away from people, and have developed a fear of humans because of their experiences with hunters, farmers, ranchers, and shepherds.\n'

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

7.5660951137542725 s {
"Articles":[
    "Werewolf",
    "Howl",
    "Wolves"
]
}
targets:  ['A/Werewolf', 'A/Mr._Werewolf', 'A/The_Werewolf', 'A/Mama_Werewolf', 'A/Radio_Werewolf', 'A/Werewolf_(1996)', 'A/Female_Werewolf', 'A/Werewolf_(film)', 'A/The_werewolf', 'A/Arizona_Werewolf', 'A/Garou_(Werewolf)', 'A/American_Werewolf', 'A/Ultimate_Werewolf', 'A/Werewolf_(comics)', 'A/Radio_werewolf', 'A/Operation_Werewolf', 'A/Livonian_werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(disambiguation)']
targets:  ['A/Howl', 'A/Boa_Howl', 'A/Howl_(EP)', 'A/Chloe_Howl', 'A/Chlöe_Howl', 'A/Grand_Howl', 'A/Howl_(band)', 'A/Howl_(film)', 'A/Howl_(poem)', 'A/Howl_(song)', 'A/Howl_(album)', 'A/Howl_(sound)', 'A/Howl_(mascot)', 'A/Howl_(Howl_EP)', 'A/Brimstone_Howl', 'A/Howl_(software)', "A/Harmonica's_Howl", 'A/Howl_(disambiguation)', 'A/HOWL_Festival', 'A/HOWL!_Festival']
targets:  ['A/Wolves', 'A/WolVes', 'A/BC_Wolves', 'A/Bad_Wolves', 'A/Among_Wolves', 'A/Algeti_Wolves', 'A/Arctic_Wolves', 'A/ASU_wolves', 'A/Augusta_Wolves', 'A/Baby_wolves', 'A/Abyssian_Wolves', 'A/American_Wolves', 'A/Billings_Wolves', 'A/Wolves_in_Wolves', 'A/Admiralty_Wolves', 'A/Akwesasne_Wolves', 'A/Abyssinian_Wolves', 'A/Arctic_wolves', 'A/Abyssian_wolves', 'A/Belgrade_wolves']
to_grabs:  ['A/Werewolf', 'A/Howl', 'A/Wolves']
article sections:
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Howl
     Howl 201
     Film 143
     Literature 233
     Music 653
   Wolf
     Wolf 3304
     Etymology 781
     Taxonomy 6922
     Description 5719
     Ecology 9179
     Behaviour 11629
     Status and conservation 6428
     Relationships with humans 13626
     Notes 329
     References 28512
     Bibliography 1092
Getting relevant for:  Werewolf
To accurately answer the question "What are werewolves?", we need to consider the most relevant sections from the article. Here's a structured breakdown of which sections are most pertinent|

| ||Names||| Provides basic information about werewolf names and their origins.
| ||History||| Describes the evolution of werewolf myths and beliefs, including ancient traditions and modern interpretations.
| ||Lycanthropy as a medical condition||| Discusses how this belief has manifested medically in different cultures over time.

The most relevant sections would be|
|||Names||
|||History||
|||Lycanthropy as a medical condition||

These sections provide the basic information needed to understand what werewolves are and how their beliefs have evolved over time.
13.725069761276245 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Getting relevant for:  Howl
3.352565050125122 s  Sections: ['Film', 'Literature']
Getting relevant for:  Wolf
4.000508785247803 s  Sections: ['Description', 'Ecology', 'Behaviour']
sec list: 
   Werewolf
   ['Names', 'History', 'Lycanthropy as a medical condition']
   Howl
   ['Film', 'Literature']
   Wolf
   ['Description', 'Ecology', 'Behaviour']
--------
--------

--------
--------
    sec: Werewolf
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Names
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: History
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Lycanthropy as a medical condition
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Folk beliefs
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Modern reception
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: See also
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Citations
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Further reading
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Howl
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Film
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Literature
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Music
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Wolf
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Etymology
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Taxonomy
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Description
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Ecology
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Behaviour
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Status and conservation
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Relationships with humans
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Notes
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: References
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
    sec: Bibliography
             ('Werewolf', ['Names', 'History', 'Lycanthropy as a medical condition'])
background text: 
--------
###Article: Werewolf
Werewolf
In folklore , a werewolf[lower-alpha 1] (from
Old English
werwulf  'man-wolf'), or occasionally lycanthrope[lower-alpha 2] (from
Ancient Greek
λυκάνθρωπος , lykánthrōpos, 'wolf-human'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic
hybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).
Several terms  redirect here. For other uses, see Werewolf (disambiguation) ,
Wolf man (disambiguation) ,
Lycanthrope (disambiguation) ,
and
Lycanthropy (disambiguation) .
For the episode of Grimm, see Lycanthropia (Grimm) .
WerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512
Grouping: Mythology
Similar entities Skinwalker 
Folklore: Worldwide
Other name(s): Lycanthrope
Part of a series on theParanormal 
Main articles
Astral projection
Astrology
Aura
Bilocation
Breatharianism
Clairvoyance
Close encounter
Cold spot
Crystal gazing
Conjuration
Cryptozoology
Demonic possession
Demonology
Ectoplasm
Electronic voice phenomenon
Exorcism
Extrasensory perception
Forteana
Fortune-telling
Ghost hunting
Magic
Mediumship
Miracle
Occult
Orb
Ouija
Paranormal fiction
Paranormal television
Precognition
Preternatural
Psychic
Psychic reading
Psychometry
Reincarnation
Remote viewing
Retrocognition
Spirit photography
Spirit possession
Spirit world
Spiritualism
Stone Tape
Supernatural
Telekinesis
Telepathy
Table-turning
Ufology 
Reportedly haunted locations:
India
United Kingdom
United States
World
Skepticism
Cold reading
Committee for Skeptical Inquiry
Debunking
Hoax
James Randi Educational Foundation
Magical thinking
Prizes for evidence of the paranormal
Pseudoskepticism
Scientific literacy
Scientific skepticism
Parapsychology
Anomalous experiences
Apparitional experiences
Empath
False awakening
Hypnosis
Ideomotor phenomenon
Out-of-body experiences
Parapsychology
Synchronicity 
Related
Anomalistics
Argument from ignorance
Argumentum ad populum
Bandwagon effect
Begging the question
Cognitive dissonance
Communal reinforcement
Fallacy
Falsifiability
Fringe science
Groupthink
Hypnosis
Junk science
Protoscience
Pseudoscience
Scientific evidence
Scientific method
Superstition
Uncertainty
Urban legend 
The werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.
The persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]
After the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .


###Article: Howl

###Article: Wolf


--------
Getting answer
61.17340135574341 s Final answer:
--------
I'm sorry, but it seems there is a mistake in your question format as you did not specify a particular question. Please provide me with the exact question you would like me to answer about these articles and I'll be happy to summarize and synthesize the information accordingly.

If you'd like help finding information specifically related to werewolves, they are mentioned in the Werewolf article which provides detailed information about their folklore, mythology, beliefs, trials, and fiction. Would you like to know something specific about them?
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

16.167898893356323 s ```json
{
  "Articles": [
    "Werewolf",
    "Lycanthropy",
    "The Werewolf"
  ]
}
```
targets:  ['A/Werewolf', 'A/Mr._Werewolf', 'A/The_Werewolf', 'A/Mama_Werewolf', 'A/Radio_Werewolf', 'A/Werewolf_(1996)', 'A/Female_Werewolf', 'A/Werewolf_(film)', 'A/The_werewolf', 'A/Arizona_Werewolf', 'A/Garou_(Werewolf)', 'A/American_Werewolf', 'A/Ultimate_Werewolf', 'A/Werewolf_(comics)', 'A/Radio_werewolf', 'A/Operation_Werewolf', 'A/Livonian_werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(disambiguation)']
targets:  ['A/Lycanthropy', 'A/Lycanthropy_(song)', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Clinical_Lycanthropy', 'A/Lycanthropy_(clinical)', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(disambiguation)']
targets:  ['A/The_Werewolf', 'A/The_werewolf', 'A/Gene_The_Werewolf', 'A/The_Werewolf_(film)', 'A/The_Werewolf_(play)', 'A/Hans_the_Werewolf', 'A/Pete_the_Werewolf', 'A/Ralph_the_Werewolf', 'A/Wolfy_the_Werewolf', 'A/The_Werewolf_Principle', 'A/Cry_of_the_Werewolf', 'A/Howl_of_the_Werewolf', 'A/Gene_the_werewolf', 'A/The_Werewolf_(1913_film)', 'A/The_Werewolf_(1956_film)', 'A/Blood_of_the_Werewolf', 'A/Curse_of_the_Werewolf', 'A/Cycle_of_the_Werewolf', 'A/The_Werewolf_Transformation', 'A/Cycle_of_the_werewolf']
to_grabs:  ['A/Werewolf', 'A/Lycanthropy', 'A/The_Werewolf']
article sections:
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Werewolf (disambiguation)
     Werewolf (disambiguation) 145
     Film and television 489
     Music 463
     Literature 224
     Games 308
     Other uses 253
Getting relevant for:  Werewolf
7.8167760372161865 s  Sections: ['Names', 'History', 'Folk beliefs']
Getting relevant for:  Werewolf (disambiguation)
8.357183456420898 s  Sections: ['Film and television', 'Literature', 'Games']
sec list: 
   Werewolf
   ['Names', 'History', 'Folk beliefs']
   Werewolf (disambiguation)
   ['Film and television', 'Literature', 'Games']
    sec: Werewolf
             Werewolf ('Werewolf', ['Names', 'History', 'Folk beliefs'])
    sec: Names
    sec: History
    sec: Lycanthropy as a medical condition
    sec: Folk beliefs
    sec: Modern reception
    sec: See also
    sec: Notes
    sec: Citations
    sec: References
    sec: Further reading
    sec: Werewolf (disambiguation)
             Werewolf (disambiguation) ('Werewolf (disambiguation)', ['Film and television', 'Literature', 'Games'])
    sec: Film and television
    sec: Music
    sec: Literature
    sec: Games
    sec: Other uses
background text: 
--------
###Article: Werewolf
Werewolf
In folklore , a werewolf[lower-alpha 1] (from
Old English
werwulf  'man-wolf'), or occasionally lycanthrope[lower-alpha 2] (from
Ancient Greek
λυκάνθρωπος , lykánthrōpos, 'wolf-human'), is an individual who can shape-shift  into a wolf  (or especially in modern film, a therianthropic
hybrid  wolf-like creature), either purposely or after being placed under a curse  or affliction (often a bite or the occasional scratch from another werewolf), with the transformations occurring on the night of a full moon .[lower-alpha 3] Early sources for belief in this ability or affliction, called lycanthropy,[lower-alpha 4] are Petronius  (27–66) and Gervase of Tilbury  (1150–1228).
Several terms  redirect here. For other uses, see Werewolf (disambiguation) ,
Wolf man (disambiguation) ,
Lycanthrope (disambiguation) ,
and
Lycanthropy (disambiguation) .
For the episode of Grimm, see Lycanthropia (Grimm) .
WerewolfWoodcut  of a werewolf attack by Lucas Cranach der Ältere , 1512
Grouping: Mythology
Similar entities Skinwalker 
Folklore: Worldwide
Other name(s): Lycanthrope
Part of a series on theParanormal 
Main articles
Astral projection
Astrology
Aura
Bilocation
Breatharianism
Clairvoyance
Close encounter
Cold spot
Crystal gazing
Conjuration
Cryptozoology
Demonic possession
Demonology
Ectoplasm
Electronic voice phenomenon
Exorcism
Extrasensory perception
Forteana
Fortune-telling
Ghost hunting
Magic
Mediumship
Miracle
Occult
Orb
Ouija
Paranormal fiction
Paranormal television
Precognition
Preternatural
Psychic
Psychic reading
Psychometry
Reincarnation
Remote viewing
Retrocognition
Spirit photography
Spirit possession
Spirit world
Spiritualism
Stone Tape
Supernatural
Telekinesis
Telepathy
Table-turning
Ufology 
Reportedly haunted locations:
India
United Kingdom
United States
World
Skepticism
Cold reading
Committee for Skeptical Inquiry
Debunking
Hoax
James Randi Educational Foundation
Magical thinking
Prizes for evidence of the paranormal
Pseudoskepticism
Scientific literacy
Scientific skepticism
Parapsychology
Anomalous experiences
Apparitional experiences
Empath
False awakening
Hypnosis
Ideomotor phenomenon
Out-of-body experiences
Parapsychology
Synchronicity 
Related
Anomalistics
Argument from ignorance
Argumentum ad populum
Bandwagon effect
Begging the question
Cognitive dissonance
Communal reinforcement
Fallacy
Falsifiability
Fringe science
Groupthink
Hypnosis
Junk science
Protoscience
Pseudoscience
Scientific evidence
Scientific method
Superstition
Uncertainty
Urban legend 
The werewolf is a widespread concept in European folklore , existing in many variants, which are related by a common development of a Christian interpretation  of underlying European folklore developed during the medieval period . From the early modern period, werewolf beliefs also spread to the New World  with colonialism . Belief in werewolves developed in parallel to the belief in witches , in the course of the Late Middle Ages  and the early modern period . Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland  (especially the Valais  and Vaud ) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.
The persecution of werewolves and the associated folklore is an integral part of the "witch-hunt " phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[lower-alpha 5] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp  (1589) led to a significant peak in both interest in and persecution of supposed werewolves , primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers  recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia  and Styria .[lower-alpha 6]
After the end of the witch trials, the werewolf became of interest in folklore studies  and in the emerging Gothic horror  genre; werewolf fiction  as a genre has premodern precedents in medieval romances  (e.g., Bisclavret  and Guillaume de Palerme ) and developed in the 18th century out of the "semi-fictional" chapbook  tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture .


###Article: Werewolf (disambiguation)
Werewolf (disambiguation)
A werewolf , in folklore, is a person who changes into a wolf.
Look up werewolf  in Wiktionary, the free dictionary.
Werewolf may also refer to:



--------
Getting answer
132.45019626617432 s Final answer:
--------
I'm sorry, but you haven't provided me with any specific question or context for summarizing and synthesizing the information from those articles. Could you please specify which aspect of werewolves you'd like me to summarize?
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }


======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

14.228371620178223 s {"Articles":["The Werewolf", "Werewolf Lore and Mythology", "Cultural Reception of the Werewolf"]}
targets:  ['A/The_Werewolf', 'A/The_werewolf', 'A/Gene_The_Werewolf', 'A/The_Werewolf_(film)', 'A/The_Werewolf_(play)', 'A/Hans_the_Werewolf', 'A/Pete_the_Werewolf', 'A/Ralph_the_Werewolf', 'A/Wolfy_the_Werewolf', 'A/The_Werewolf_Principle', 'A/Cry_of_the_Werewolf', 'A/Howl_of_the_Werewolf', 'A/Gene_the_werewolf', 'A/The_Werewolf_(1913_film)', 'A/The_Werewolf_(1956_film)', 'A/Blood_of_the_Werewolf', 'A/Curse_of_the_Werewolf', 'A/Cycle_of_the_Werewolf', 'A/The_Werewolf_Transformation', 'A/Cycle_of_the_werewolf']
targets:  []
targets:  []
to_grabs:  ['A/The_Werewolf', 'A/Werewolf', 'A/Cultural']
article sections:
   Werewolf (disambiguation)
     Werewolf (disambiguation) 145
     Film and television 489
     Music 463
     Literature 224
     Games 308
     Other uses 253
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Culture
     Culture 1603
     Description 3041
     Etymology 3187
     Change 3994
     Early modern discourses 5635
     Anthropology 996
     Sociology 3026
     Cultural studies 7268
     Psychology 2487
     Protection of culture 1936
     See also 247
     References 15496
     Further reading 4580
Getting relevant for:  Werewolf (disambiguation)
{"Werewolf (disambiguation)"|[]}`
7.163773536682129 s  Sections: []
Getting relevant for:  Werewolf
8.120195388793945 s  Sections: ['Names', 'History', 'Folk beliefs']
Getting relevant for:  Culture
7.739191055297852 s  Sections: ['Anthropology', 'Sociology']
sec list: 
   Werewolf (disambiguation)
   []
   Werewolf
   ['Names', 'History', 'Folk beliefs']
   Culture
   ['Anthropology', 'Sociology']
*     Werewolf (disambiguation) : Werewolf (disambiguation)
*     Werewolf : Werewolf
*     Culture : Culture
background text: 
--------

--------
Getting answer

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

The following articles may provide relevant information about what werewolves are|

| [Human-Powered Werewolf Mythology]
| [Werewolf Behavior and Psychology]
| [Evolution of Werewolf Legends]
19.77423119544983 s The following articles may provide relevant information about what werewolves are:

1. [Human-Powered Werewolf Mythology]
2. [Werewolf Behavior and Psychology]
3. [Evolution of Werewolf Legends]
to_grabs:  []
article sections:
sec list: 
background text: 
--------

--------
Getting answer

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

12.498090028762817 s {"Articles":["The Werewolf","Lycanthropy","Wolf Man"]}
targets:  ['A/The_Werewolf', 'A/The_werewolf', 'A/Gene_The_Werewolf', 'A/The_Werewolf_(film)', 'A/The_Werewolf_(play)', 'A/Hans_the_Werewolf', 'A/Pete_the_Werewolf', 'A/Ralph_the_Werewolf', 'A/Wolfy_the_Werewolf', 'A/The_Werewolf_Principle', 'A/Cry_of_the_Werewolf', 'A/Howl_of_the_Werewolf', 'A/Gene_the_werewolf', 'A/The_Werewolf_(1913_film)', 'A/The_Werewolf_(1956_film)', 'A/Blood_of_the_Werewolf', 'A/Curse_of_the_Werewolf', 'A/Cycle_of_the_Werewolf', 'A/The_Werewolf_Transformation', 'A/Cycle_of_the_werewolf']
targets:  ['A/Lycanthropy', 'A/Lycanthropy_(song)', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Clinical_Lycanthropy', 'A/Lycanthropy_(clinical)', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(disambiguation)']
targets:  ['A/Wolf_Man', 'A/Wolf-Man', 'A/Wolf_man', 'A/Wolf-man', 'A/The_Wolf_Man', 'A/Wolf_Man_1941', 'A/Wolf_Man_2009', 'A/Wolf_man_Jack', 'A/Wolf_man_film', 'A/Wolf_man_movie', 'A/Astounding_Wolf-Man', 'A/Wolf_Man_(Universal)', 'A/Wolf_Man_(2024_film)', 'A/Wolf_Man_(2025_film)', 'A/Wolf_man_syndrome', 'A/The_Astounding_Wolf-Man', 'A/The_Wolf_Man_(Universal)', 'A/The_Wolf_Man_(character)', 'A/Wolf_Man_(disambiguation)', 'A/Wolf_man_(disambiguation)']
to_grabs:  ['A/The_Werewolf', 'A/Lycanthropy', 'A/Wolf_Man']
article sections:
   Werewolf (disambiguation)
     Werewolf (disambiguation) 145
     Film and television 489
     Music 463
     Literature 224
     Games 308
     Other uses 253
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   Wolf man (disambiguation)
     Wolf man (disambiguation) 134
     Film 503
     In print 260
     People 620
     Other uses 49
Getting relevant for:  Werewolf (disambiguation)
7.69035005569458 s  Sections: ['Literature', 'Games']
Getting relevant for:  Werewolf
8.533435106277466 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Getting relevant for:  Wolf man (disambiguation)
8.188444375991821 s  Sections: ['Other uses', 'Film', 'In print']
sec list: 
   Werewolf (disambiguation)
   ['Literature', 'Games']
   Werewolf
   ['Names', 'History', 'Lycanthropy as a medical condition']
   Wolf man (disambiguation)
   ['Other uses', 'Film', 'In print']
>     ['Literature', 'Games']
>     ['Literature', 'Games']
>     ['Literature', 'Games']
>     ['Literature', 'Games']
*     Werewolf (disambiguation) : Literature
>     ['Literature', 'Games']
*     Werewolf (disambiguation) : Games
>     ['Literature', 'Games']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
*     Werewolf : Names
>     ['Names', 'History', 'Lycanthropy as a medical condition']
*     Werewolf : History
>     ['Names', 'History', 'Lycanthropy as a medical condition']
*     Werewolf : Lycanthropy as a medical condition
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Names', 'History', 'Lycanthropy as a medical condition']
>     ['Other uses', 'Film', 'In print']
>     ['Other uses', 'Film', 'In print']
*     Wolf man (disambiguation) : Film
>     ['Other uses', 'Film', 'In print']
*     Wolf man (disambiguation) : In print
>     ['Other uses', 'Film', 'In print']
>     ['Other uses', 'Film', 'In print']
*     Wolf man (disambiguation) : Other uses
background text: 
--------

--------
Getting answer

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

19.61775279045105 s {"Articles":["Human-Like Animals","Wolf-Derangement Syndrome","Werewolf Mythology"]}
targets:  []
targets:  []
targets:  []
to_grabs:  ['A/Human_Like_a_House', 'A/Werewolf']
article sections:
   Human Like a House
     Human Like a House 520
     Critical reception 447
     Track listing 290
     Personnel 78
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
Getting relevant for:  Human Like a House
{"Human Like a House"|[]}
6.751046657562256 s  Sections: []
Getting relevant for:  Werewolf
7.256527900695801 s  Sections: ['Names', 'History']
Pulling from:  Human Like a House
    pull section: Human Like a House : Human Like a House
Pulling from:  Werewolf
    pull section: Werewolf : Werewolf
    pull section: Werewolf : Names
    pull section: Werewolf : History
background text: 
--------

--------
Getting answer

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

20.39373230934143 s ```json
{
  "Articles": [
    "Werewolf",
    "Lycanthropy",
    "History of Werewolves"
  ]
}
```
targets:  ['A/Werewolf', 'A/Mr._Werewolf', 'A/The_Werewolf', 'A/Mama_Werewolf', 'A/Radio_Werewolf', 'A/Werewolf_(1996)', 'A/Female_Werewolf', 'A/Werewolf_(film)', 'A/The_werewolf', 'A/Arizona_Werewolf', 'A/Garou_(Werewolf)', 'A/American_Werewolf', 'A/Ultimate_Werewolf', 'A/Werewolf_(comics)', 'A/Radio_werewolf', 'A/Operation_Werewolf', 'A/Livonian_werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(disambiguation)']
targets:  ['A/Lycanthropy', 'A/Lycanthropy_(song)', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Clinical_Lycanthropy', 'A/Lycanthropy_(clinical)', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(disambiguation)']
targets:  []
to_grabs:  ['A/Werewolf', 'A/Lycanthropy', 'A/History']
article sections:
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
   History
     History 2889
     Etymology 3217
     Description 3731
     Prehistory 1543
     Historiography 964
     Methods 10940
     Areas of study 17560
     Historians 612
     Judgement 398
     Pseudohistory 499
     Teaching 5072
     See also 39
     References 16363
     Further reading 2136
Getting relevant for:  Werewolf
8.811210870742798 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition']
Getting relevant for:  History
7.60028862953186 s  Sections: ['Description', 'Methods']
Pulling from:  Werewolf
Pulling from:  History
background text: 
--------
###Article: Werewolf

###Article: History


--------
Getting answer
29.34388828277588 s Final answer:
--------
I apologize, but I need more context about what specific question you're asking. Please provide me with the exact question so that I can help you synthesize the information from these articles effectively.

### Follow-Up Questions:
1. What is the definition of a werewolf according to various historical sources?
2. How does this mythical creature compare to other folklore legends in terms of its cultural impact?
3. When and where did the belief in werewolves first appear in recorded history?
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

I apologize, but I cannot assist with that request.
6.667817115783691 s I apologize, but I cannot assist with that request.
to_grabs:  []
article sections:
background text: 
--------

--------
Getting answer
9.942905187606812 s Final answer:
--------
I'm sorry, but I need to see the attached articles in order to provide a summary and synthesis of the information. Please attach the articles or share them here so that I can help you with your question.
--------

======================= RESTART: /home/lancaster/REDWOLF.AIC/REDWOLF_Architecture.py =======================
Asking: 
For the topic "What are werewolves?", reply in the following template with three highly relevant encyclopedia article titles which may be used as background context for the question: "What are werewolves?". Reply with no other content but the filled template. Supply only a list of titles in the 'Articles' field. 
### Template 
{"Articles":[] }

6.475000619888306 s ["Wolves", "Werewolf", "Lycanthropy"]
targets:  ['A/Wolves', 'A/WolVes', 'A/BC_Wolves', 'A/Bad_Wolves', 'A/Among_Wolves', 'A/Algeti_Wolves', 'A/Arctic_Wolves', 'A/ASU_wolves', 'A/Augusta_Wolves', 'A/Baby_wolves', 'A/Abyssian_Wolves', 'A/American_Wolves', 'A/Billings_Wolves', 'A/Wolves_in_Wolves', 'A/Admiralty_Wolves', 'A/Akwesasne_Wolves', 'A/Abyssinian_Wolves', 'A/Arctic_wolves', 'A/Abyssian_wolves', 'A/Belgrade_wolves']
targets:  ['A/Werewolf', 'A/Mr._Werewolf', 'A/The_Werewolf', 'A/Mama_Werewolf', 'A/Radio_Werewolf', 'A/Werewolf_(1996)', 'A/Female_Werewolf', 'A/Werewolf_(film)', 'A/The_werewolf', 'A/Arizona_Werewolf', 'A/Garou_(Werewolf)', 'A/American_Werewolf', 'A/Ultimate_Werewolf', 'A/Werewolf_(comics)', 'A/Radio_werewolf', 'A/Operation_Werewolf', 'A/Livonian_werewolf', 'A/Ultimate_werewolf', 'A/Werewolf_(Buffyverse)', 'A/Werewolf_(disambiguation)']
targets:  ['A/Lycanthropy', 'A/Lycanthropy_(song)', 'A/Lycanthropy_(Album)', 'A/Lycanthropy_(album)', 'A/Clinical_Lycanthropy', 'A/Lycanthropy_(clinical)', 'A/Clinical_lycanthropy', 'A/Lycanthropy_(disambiguation)']
to_grabs:  ['A/Wolves', 'A/Werewolf', 'A/Lycanthropy']
article sections:
   Wolf
     Wolf 3304
     Etymology 781
     Taxonomy 6922
     Description 5719
     Ecology 9179
     Behaviour 11629
     Status and conservation 6428
     Relationships with humans 13626
     Notes 329
     References 28512
     Bibliography 1092
   Werewolf
     Werewolf 4477
     Names 3315
     History 15912
     Lycanthropy as a medical condition 1852
     Folk beliefs 12043
     Modern reception 5939
     See also 92
     Notes 1232
     Citations 9565
     References 2877
     Further reading 645
Getting relevant for:  Wolf
3.6586782932281494 s  Sections: ['Description', 'Behaviour']
Getting relevant for:  Werewolf
4.836586236953735 s  Sections: ['Names', 'History', 'Lycanthropy as a medical condition', 'Folk beliefs']
Pulling from:  Wolf
    pull section: Wolf : Wolf
    pull section: Wolf : Description
    pull section: Wolf : Behaviour
Pulling from:  Werewolf
    pull section: Werewolf : Werewolf
    pull section: Werewolf : Names
    pull section: Werewolf : History
    pull section: Werewolf : Lycanthropy as a medical condition
    pull section: Werewolf : Folk beliefs
background text: 
--------

--------
Getting answer
261.226934671402 s Final answer:
--------
The passage discusses werewolf folklore across different cultures and regions around the world, exploring various aspects such as causes, transformations, treatments, beliefs about revenant spirits, religious associations, and connections to other supernatural creatures. Here's a breakdown of some key points:

1. **Cultural Variations**: Werewolf myths differ significantly by region, with various explanations for their appearance and behavior:
   - In Eastern Europe, wolves were thought to be cursed or exorcized into human form, while in Scandinavia, they were believed to be malevolent.
   - Native American beliefs often featured wolf-like creatures that guarded sacred places or were responsible for killing hunters.

2. **Causation**: Causes of werewolf transformations vary widely:
   - Parental abuse was a common cause in Eastern European folklore
   - The belief that people could become wolves after passing through an arch with birch and rose spine
   - In North America, beliefs often associated lycanthropy with witchcraft or other evil spirits

3. **Transformations**: Transformations described varied:
   - Transformation into a wolf was common but not always immediate
   - Some werewolves could transform at will while others were involuntarily transformed
   - The timing of transformations (Easter, winter solstice) was often significant in some cultures

4. **Cures and Treatments**: Various methods to cure lycanthropy were used:
   - Medieval practitioners advocated medical treatments like wolfsbane or exorcism
   - The conversion to Christianity was also a common method
   - Beliefs about the power of the Devil or saintly powers for transforming others

5. **Belief in Revenants**: Werewolves were often linked to revenant spirits:
   - In Hungarian folklore, vampires and werewolves are closely related
   - The belief that the transformation was involuntary was common
   - Some versions allowed the person to choose their own animal form of transformation

6. **Associations with Other Supernatural Creatures**: Werewolves were often associated with other supernatural beings:
   - In American folklore, they were considered enemies of witches and evil spirits
   - They were sometimes depicted as hunters of vampires
   - The belief that werewolves could spread their condition to others was common in Haitian lore

The passage presents a complex picture of how different cultures interpreted and portrayed the concept of lycanthropy, with various explanations for both the appearance and behavior of werewolf figures. These legends often intertwined supernatural beliefs with religious and cultural practices, reflecting the diverse nature of medieval European society.
--------
