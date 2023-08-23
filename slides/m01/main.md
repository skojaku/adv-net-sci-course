---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
style: |
  center {
    margin-top: 15%;
  }
---

<style>
  .container {
    display:flex;
  }
  .col {
    flex: 1
  }
</style>


![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

# **Advanced Topics in Network Science**

SSIE 641

Module 1

Sadamori Kojaku

https://github.com/skojaku/adv-net-sci-course

---

# For EngiNet™ students


#### WARNING

All rights reserved.  No part of the course materials used in the instruction of this course may be reproduced in any form or by any electronic or mechanical means, including the use of information storage and retrieval systems, without written approval from the copyright owner.

©2023  Binghamton University state University of New York

---

# EngiNet Office Staff

- Janice Kinzer
  - Email:  enginet@binghamton.edu
  - Phone:  1-800-478-0718 or 607-777-4965
- Media Production Operator:
  - Anisha Ahmed

---

# About my self

- Sadamori Kojaku
- 幸若 完壮 (Japanese writing)
- Fresh assist. prof. joining Bing. in 2023
- Recovering computer scientist
- Contacts
  - skojaku@binghamton.edu
  - Office J19
  - @skojaku (X), skojaku.github.io

![bg right:30% 60%](https://pbs.twimg.com/profile_images/1678198971989147649/toxo1lCg_400x400.jpg)

---

# <center>Shuffle the seats, and introduce each other!</center>


---

# About this course

### [Course syllabus](https://skojaku.github.io/attachments/docs/advnetsci/syllabus.pdf)
### [Course Wiki](https://github.com/skojaku/adv-net-sci-course/wiki)
### [Course GitHub](https://github.com/skojaku/adv-net-sci-course)

---

# Before jumping in

<iframe width="80%" height="80%" src="https://www.youtube.com/embed/RQaW2bFieo8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

# <center>What are networks? Why networks? Why do we care?<center>

---

![bg right:30% 100%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

# <center>What are networks?</center>
- Networks = Nodes + Edges
- Networks describe *relationships*.
- Networks appear everywhere.

---

# <center>Discussion</center>

![bg right:30% 100%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

  - List as many networks as possible.
  - What are the strength of network representation?

---

# <center>Zoo of networks!</center>


---

# <center style="background-color: rgba(255, 255, 255, 0.6)"><font color="k" style="font-size: 100px">Food Web</font></center>

![bg](https://askabiologist.asu.edu/sites/default/files/resources/plosable/Marine_Food_Web/marine-ecosystem.png)

---

# <center style="background-color: rgba(255, 255, 255, 0.6)"><b><font color="red" style="font-size: 100px;">Mutualistic Networks</font></b></center>

![bg](https://mlurgi.github.io/networks_for_r/lesson-images/plant-pollinator.png)

---

# <center ><b><font color="white" style="font-size: 100px;">Brain 🧠</font></b></center>

![bg](https://assets.thehansindia.com/h-upload/2020/03/08/952035-brain.webp)

---

# <center ><b><font color="k" style="font-size: 100px;background-color: rgba(255, 255, 255, 0.6)">Drug-Drug interaction</font></b></center>

![bg](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41746-019-0141-x/MediaObjects/41746_2019_141_Fig1_HTML.png?as=webp)

---

# <center ><b><font color="red" style="font-size: 100pxl">Protein-Protein Interaction</font></b></center>

![bg 50%](https://upload.wikimedia.org/wikipedia/commons/5/56/1dfj_RNAseInhibitor-RNAse_complex.jpg)

---

# <center><font color="blue" style="font-size: 100px;background-color: rgba(255, 255, 255, 0.6)">Social Networks</font></center>


![bg](https://miro.medium.com/v2/resize:fit:1400/1*4MXaZGRjWL_X-LgDNjd-9w.png)

---

# <center><font color="k" style="font-size: 100px;background-color: rgba(255, 255, 255, 0.6)">Financial Networks</font></center>


![bg 70%](https://www.researchgate.net/publication/26692139/figure/fig1/AS:652592984096773@1532601700652/A-sample-of-the-international-financial-network-where-the-nodes-represent-major.png)

---


![bg ](https://www.researchgate.net/publication/287325801/figure/fig1/AS:613998437363713@1523400043126/Map-of-the-US-airport-network-for-July-13-Airports-are-represented-as-nodes-and-edges-as.png)

---

# <center><font color="k" style="font-size: 100px;background-color: rgba(255, 255, 255, 0.6)">Airport networks 🛫</font></center>

![bg ](https://www.researchgate.net/publication/287325801/figure/fig1/AS:613998437363713@1523400043126/Map-of-the-US-airport-network-for-July-13-Airports-are-represented-as-nodes-and-edges-as.png)


---

![bg](https://www.sciencenews.org/wp-content/uploads/2020/02/021520_power_inline-1_680.png)

---

# <center><font color="blue" style="font-size: 100px;background-color: rgba(255, 255, 255, 0.6)">Power Grid 💡</font></center>

![bg](https://www.sciencenews.org/wp-content/uploads/2020/02/021520_power_inline-1_680.png)

---



![bg](https://www.treehugger.com/thmb/ScAa4BnU5Ld_rzGNo0IIZNv91U4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8747607969_65098e4af6_o-f3ebcfa0d1894613995f1c086d1442ac.png)

---
# <center><font color="red" style="font-size: 100px">River</font></center>


![bg](https://www.treehugger.com/thmb/ScAa4BnU5Ld_rzGNo0IIZNv91U4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8747607969_65098e4af6_o-f3ebcfa0d1894613995f1c086d1442ac.png)

---

# <center><font color="white" style="font-size: 100px">Internet</font></center>


![bg](https://www.researchgate.net/publication/325794369/figure/fig2/AS:639787606220801@1529548660141/Example-of-large-and-complex-networks-Visualization-of-the-Internet-graph-by-the-Opte.png)

---

# <center><font style="font-size: 80px">Citation networks</font></center>

![bg right:60% 100%](https://rs.resalliance.org/wp-content/uploads/2010/11/mapofscience.jpg)

---

# <center><font style="font-size: 80px">Knowledge Graph</font></center>

![bg left:55% 100%](https://miro.medium.com/v2/resize:fit:617/1*chWX0v67nJ0JUzbGiN8ulQ.png)

---

## <center style="margin-top:-5%;">...and some fun networks</center>


![bg 80%](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep00196/MediaObjects/41598_2011_Article_BFsrep00196_Fig2_HTML.jpg)

---

## <center style="margin-top:-5%;">...and some fun networks</center>

![bg 80%](https://leadersayswhat.com/wp-content/uploads/2015/05/kevin-bacon-7656918.png)

---

# <center>Key strength of network representation?</center>

---

<img style="float: left;width:50%" src="https://askabiologist.asu.edu/sites/default/files/resources/plosable/Marine_Food_Web/marine-ecosystem.png">
<img style="float: left;width:50%" src="https://mlurgi.github.io/networks_for_r/lesson-images/plant-pollinator.png">
<img style="float: left;width:50%" src="https://assets.thehansindia.com/h-upload/2020/03/08/952035-brain.webp">
<img style="float: left;width:50%" src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41746-019-0141-x/MediaObjects/41746_2019_141_Fig1_HTML.png">
<img style="float: left;width:50%" src="https://www.researchgate.net/publication/26692139/figure/fig1/AS:652592984096773@1532601700652/A-sample-of-the-international-financial-network-where-the-nodes-represent-major.png">
<img style="float: left;width:50%" src="https://www.researchgate.net/publication/287325801/figure/fig1/AS:613998437363713@1523400043126/Map-of-the-US-airport-network-for-July-13-Airports-are-represented-as-nodes-and-edges-as.png">
<img style="float: left;width:50%" src="https://www.researchgate.net/publication/325794369/figure/fig2/AS:639787606220801@1529548660141/Example-of-large-and-complex-networks-Visualization-of-the-Internet-graph-by-the-Opte.png">
<img style="float: left;width:50%" src="https://rs.resalliance.org/wp-content/uploads/2010/11/mapofscience.jpg">
<img style="float: left;width:50%" src="https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep00196/MediaObjects/41598_2011_Article_BFsrep00196_Fig2_HTML.jpg">

<img style="float: left;width:50%" src="https://leadersayswhat.com/wp-content/uploads/2015/05/kevin-bacon-7656918.png">

![bg right:50%](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/national/4_social%2520network%2520analysis.png)


---

## <center>Advantages of Network Representation</center>

- **Abstraction**: Abstract away complicated aspects
- **Transdomain**: The same tools can be applied to networks across different domains.
- **Universality**: Can reveal fundamental principles underlying complex systems across different domains.

---

# <center>Discussion</center>
  - Why do we care networks 🤔?
  - Why is focusing on nodes not enough? Why should we care *relationships*?

---

<div class="container">

<div class="col">

> # The whole is greater than the sum of its parts.
by ~~Aristotle~~ 

This is Aristotle *misquote*! But captures the core value of networks.

</div class = "col">

<div class="col">

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">No, Aristotle Didn’t Write “A Whole is Greater Than the Sum of Its Parts” <a href="https://t.co/4UHNV89aEa">https://t.co/4UHNV89aEa</a></p>&mdash; sententiae antiquae (@sentantiq) <a href="https://twitter.com/sentantiq/status/1015254883992207360?ref_src=twsrc%5Etfw">July 6, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

</div class = "col">

</div>

---


# Reductionism

- Assert that our world can be explained by combinations of its parts.
- Rooted from Ancient Greek philosophy **Alche**, which means *a first principle from which other principles are derived.* E.g., [Aristotelian four elements](), [Humorism](), [Pancha mahabhuta](), [五行]()
- Fig: Digesting Duck created by Jacques de Vaucanson in 1739.

![bg right:35% 100%](https://www.newworldencyclopedia.org/d/images/7/75/Duck_of_Vaucanson.jpg)

---

# Emergence

Schooling of animals
![bg right:50% 100%](https://www.researchgate.net/publication/278009687/figure/fig8/AS:627209299578887@1526549758739/Unexpected-emergent-behaviour-of-the-mass-on-the-example-of-a-bird-flock-Simple.png)

<iframe width="100%" height="315" src="https://www.youtube.com/embed/Y-5ffl5_7AI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

# <center>Gestalt</center>

![bg right:60% 80%](https://www.pastorinpajamas.com/wp-content/uploads/2018/03/Gestalt-woman.gif)

---

# <center>Our word is not a simple sum of its parts. Their *relationships* matter!</center>

---

# Case example 1

- Jacob Levy Moreno
- Group Psychotherapy
  - Treat a social group as a group and treat individuals in the context of a group setting.
- Invented *sociogram* (network!) to understand groups

![bg right:20% 100%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)
![bg right:50% 100%](https://upload.wikimedia.org/wikipedia/commons/7/7c/Moreno_mit_bueste_%28cropped%29.gif)

---

# Case example 2

- Richard Feynman (left) and Freeman Dyson (right)
- A story revolved around the revolutionary Feynman diagram.

![bg right:50% 100%](https://upload.wikimedia.org/wikipedia/commons/1/1a/RichardFeynman-PaineMansionWoods1984_copyrightTamikoThiel_bw.jpg)
![bg right:50% 85%](https://upload.wikimedia.org/wikipedia/commons/0/03/Freeman_Dyson_%282005%29.jpg)

<!--
- When Richard Feynman first introduced his revolutionary Feynman diagram but was met with confusion at the Pocono conference.
- Feynman did not publish anything about his invention.
- The Feynman diagram becomes a canon of theoretical physics today, thanks to Freeman Dyson
- Freeman was a graduate student at Cornell and learned from Feynman about the diagram.
- Freeman published two papers that provided step-by-step rules for drawing the diagram and its mathematical elements, making it more accessible and understandable for others.
- Freeman then moved to Advanced Study at Princeton, working togehter with Oppenheimer.
- They created a *"postdoc cascade"*, in which they trained many postdoc to master the diagrammatic techniques and then send them to other institutios across the country.
- This network created by Dyson allowed the Feynman diagram to become a fundamental tool in theoretical physics.
-->


---

## Networks underpin idea spreading

-  [Prestige drives epistemic inequality in the diffusion of scientific ideas | EPJ Data Science | Full Text](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-018-0166-4)


![bg right:50% 100%](https://media.springernature.com/lw685/springer-static/image/art%3A10.1140%2Fepjds%2Fs13688-018-0166-4/MediaObjects/13688_2018_166_Fig3_HTML.png)

---

![bg](https://media.tenor.com/bD9vHNiR1rQAAAAd/boom-mind-blown.gif)


---

# <center>Are you an analytic thinker or holistic thinker?</center>

Let's do a psychological test!

---

# Which two go together?

![bg right:50% 100%](https://d3i71xaburhd42.cloudfront.net/620f29d1de2852615c53afbb95a73018890d7a42/3-Figure1-1.png)

---

- *Analytic thinking*: The chicken and cow should be grouped together because they both belong to the category of animals.
- *Holistic thinking*: The cow and grass should be grouped together because cows are typically grazing on grass.

![bg right:50% 100%](https://d3i71xaburhd42.cloudfront.net/620f29d1de2852615c53afbb95a73018890d7a42/3-Figure1-1.png)

---

# Which group does the target object belong to?
![bg right:50% 100%](https://www.researchgate.net/publication/10579289/figure/fig2/AS:280330863955976@1443847494993/Which-group-does-the-target-object-belong-to-Target-bears-a-family-resemblance-to.png)

---

- *Analytic thinking*: The flower should belong to Group 2 since they all have straight stem.
- *Holistic thinking*: The flower should belong to Group 1 because of the strong family resemblance to the group

![bg right:50% 100%](https://www.researchgate.net/publication/10579289/figure/fig2/AS:280330863955976@1443847494993/Which-group-does-the-target-object-belong-to-Target-bears-a-family-resemblance-to.png)

---

### Culture deeply influences our way of thinking

<iframe width="100%" height="100%" src="https://www.youtube.com/embed/Opy-SjDU0UY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

### Culture deeply influences our way of thinking

<center style="margin-top:0%">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Interesting trivia about Hindi🇮🇳. &quot;Yesterday&quot; and &quot;Tomorrow&quot; are the same word, &quot;कल&quot; (kal?) in Hindi. You have to judge based on the context 🤯. In Hindi, time is relative. <a href="https://t.co/N2RGEGgzcs">pic.twitter.com/N2RGEGgzcs</a></p>&mdash; Sadamori Kojaku (@skojaku) <a href="https://twitter.com/skojaku/status/1694375572921548938?ref_src=twsrc%5Etfw">August 23, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

---

# <center>Network thinking is *a* holistic thinking</center>

What are other ways to describe relationships?

---

# <center>Correlation</center>

![bg right:60% 80%](https://www.jneurosci.org/content/jneuro/41/12/2684/F4.large.jpg)

---

# <center>Geometry</center>

![bg](https://2.bp.blogspot.com/-yL_425HS2ck/WEDZLk5cq0I/AAAAAAAABcI/kwy4F4Cmfi4jyG_InIiYu6F7y2-BKTXWQCLcB/s640/embedding-mnist.gif)


---

# <center>Discussion</center>
What distinguishes networks from geometric representation and correlations?

---

# <center>Discussion</center>
What distinguishes networks from geometric representation and correlations?
- **Discrete relationship**: Represent binary relationships.
- **Independence**: Often presume that dyadic relationships are independent of each other.

---


---

- *We made it!* This is the end of the long class.
- Don't forget to **subscribe our slack**!
- **Bring your own pen and paper** for the next attendance quiz.
- The assignment is due on the next class.
- Feel free to reach out skojaku@binghamton.edu for questions!

![bg right:40%](https://media.tenor.com/bD9vHNiR1rQAAAAd/boom-mind-blown.gif)


---

# References

#### About complex networks
- [Complex systems & Networks by Petter Holme](https://videopress.com/v/oLdj0PQX)


#### Analytic vs Holistic thinking
- [Are You a Holistic or a Specific Thinker?](https://hbr.org/2014/04/are-you-a-holistic-or-a-specific-thinker)
- [How culture made Japanese Internet design "Weird" - YouTube](https://www.youtube.com/watch?v=Opy-SjDU0UY)
- [Culture and point of view | PNAS](https://www.pnas.org/doi/full/10.1073/pnas.1934527100)


---

# Reference (.cont)

#### Jacob Moreno
- [The Early Beginnings of Social Network Analysis and the Potential Use for Homeland Security | by Angi English | Homeland Security | Medium](https://medium.com/homeland-security/the-early-beginnings-of-social-network-analysis-and-the-potential-use-for-homeland-security-26213c86949b)
- [Firsts in network science – Petter Holme](https://petterhol.me/2019/04/15/firsts-in-network-science/)
- [Models and Methods in Social Network Analysis - Google Books](https://books.google.com/books?hl=en&lr=&id=4Ty5xP_KcpAC&oi=fnd&pg=PA248&dq=Graphical+Techniques+for+Exploring+Social+Network+Data&ots=9OMHufy5D2&sig=C1TBa1eHoTBp7PNdW2-uJht9LwA#v=onepage&q=Graphical%20Techniques%20for%20Exploring%20Social%20Network%20Data&f=false)

---

# Reference (.cont)


#### Feynman diagram
- [Freeman Dyson and the Postdoc Cascade | Drawing Theories Apart: The Dispersion of Feynman Diagrams in Postwar Physics | Chicago Scholarship Online | Oxford Academic](https://academic.oup.com/chicago-scholarship-online/book/23068/chapter/183889084)
- [Freeman Dyson - Linking the ideas of Feynman, Schwinger and Tomanaga (76/157) - YouTube](https://www.youtube.com/watch?v=i3RcN5UGwgI)
- [Freeman Dyson - How difficult was it to understand Schwinger? (73/157) - YouTube](https://www.youtube.com/watch?v=UKbp85zpdcY)
- [Freeman Dyson - Richard Feynman and his work (58/157) - YouTube](https://www.youtube.com/watch?v=pToteaNcIdk)


#### Misc
[Prestige drives epistemic inequality in the diffusion of scientific ideas | EPJ Data Science | Full Text](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-018-0166-4)
