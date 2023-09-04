---
marp: true
theme: gaia
_class:
  - lead
backgroundColor: #fff
paginate: true
style: |
  .vindent {
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

# Quiz

---

# Quiz

1. Outline three advantages of network representation.
1. Why do we care about networks? Explain.
1. Can you identify an alternative method of representing relationships? What is the key strength of network representation in light of this alternative representation?

---

## <center>Advantages of Network Representation</center>

- **Abstraction**: Abstract away complicated aspects
- **Transdomain**: The same tools can be applied to networks across different domains.
- **Universality**: Can reveal fundamental principles underlying complex systems across domains.

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

# Emergence

Schooling of animals
![bg right:50% 100%](https://www.researchgate.net/publication/278009687/figure/fig8/AS:627209299578887@1526549758739/Unexpected-emergent-behaviour-of-the-mass-on-the-example-of-a-bird-flock-Simple.png)

<iframe width="100%" height="315" src="https://www.youtube.com/embed/Y-5ffl5_7AI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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

# <center>Alternative representation?</center>

---
# <center>Correlation</center>

![bg right:60% 80%](https://www.jneurosci.org/content/jneuro/41/12/2684/F4.large.jpg)

---

# <center>Geometry</center>

![bg](https://2.bp.blogspot.com/-yL_425HS2ck/WEDZLk5cq0I/AAAAAAAABcI/kwy4F4Cmfi4jyG_InIiYu6F7y2-BKTXWQCLcB/s640/embedding-mnist.gif)


---

# <center>What distinguishes networks from geometric representation and correlations?</center>


---

# Correlation $\neq$ Causation

![bg 80%](https://www.explainxkcd.com/wiki/images/9/9c/correlation.png)

---

#


![bg 80%](https://images.theconversation.com/files/74771/original/image-20150313-7070-1jqdccg.jpg?ixlib=rb-1.1.0&q=30&auto=format&w=600&h=637&fit=crop&dpr=2)

---

# <center>Shuffle the seats!</center>

---

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

# **Advanced Topics in Network Science**

SSIE 641

Module 2

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
  - Sneha Rawat
- Instructor:
  - Sadamori Kojaku
  - skojaku@iu.edu

---
### Today's menu
# <center class="vindent">Representing networks</center>

---

## Friendship paradox

#### <center class="vindent">Your friends have more friends than you do</center>
<center style="margin-top:0%">on average</center>

- Is this true?
- What is the average number of friends?
- What is the average number of friends that a friend has?

![bg right:50% 80%](https://static01.nyt.com/images/2012/09/06/opinion/strogatz2-fig1/strogatz2-fig1-blog427.jpg)

---

# <center class="vindent">Let's test the friendship paradox with <span style="color:red">networks in wild 🚀</span></center>

---


# But where are networks 🤔?

![bg 80%](https://cdn.geekwire.com/wp-content/uploads/2018/11/bigstock-Chatting-Persons-People-Group-243691576-630x250.jpg)

---

# Questionnaire-based

Social network of students

"Who Shall Survive?: A New Approach to the Problem of Human Interrelations" by J. L. Moreno.

![bg right:50% 100%](https://www.researchgate.net/publication/283794217/figure/fig2/AS:669989904318484@1536749449269/Hand-drawn-social-network-reproduced-from-Jacob-Morenos-book-Who-Shall-Survive.jpg)


---

# Observation-based

Social network of a university karate club.

"An Information Flow Model for Conflict and Fission in Small Groups" by Wayne Zachary.



![bg right:50% 100%](https://www.researchgate.net/publication/236902276/figure/fig2/AS:669252700889094@1536573686332/Zacharys-Karate-Club-network-Colors-and-shapes-show-real-fission-of-the-club.png)



---

![bg left:50% 50%](https://m.media-amazon.com/images/I/51f+aVIOyEL._AC_UF1000,1000_QL80_.jpg)

![right:40% 80%](https://www.media.mit.edu/wearables/images/nokia_6600.jpg)


---

<iframe src="https://player.vimeo.com/video/31490438?h=b474f30ff6" width="640" height="642" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
<p><a href="https://vimeo.com/31490438">Dynamical Contact Patterns in a Primary School.</a> from <a href="https://vimeo.com/sociopatterns">SocioPatterns</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

![bg right:40% 100%](data:image/png;base64,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)


---

# ~~Networks~~ Tables

![bg 80%](https://images.squarespace-cdn.com/content/v1/55b6a6dce4b089e11621d3ed/1600912799264-97NJN5FU6LQSKZ2Y5LH3/Data+table+illustration.png)

---

# <center>Data normalization </center>

<div class ="container">
<div class="col" style="margin-left:10%;flex:1">


<center>

#### Unnormalized

<div  style= "font-size:18px;">

| Person 1 | Person 2 |
| -------- | -------- |
| John     | Yu       |
| Carla    | Yu       |
| Carla    | Celine   |
| Celine   | Yu       |
| Celine   | Robert   |
| Robert   | Chang    |
| Robert   | Rob      |
| Robert   | Yu       |
| Chang    | Hana     |
| Rob      | Wilson   |
| Rob      | Diana    |
| Wilson   | Yu       |
| Simon    | Yu       |

</div>

</center>
</div>

<div class="col" style="flex:0.3;margin-right:5%">

# <center style="margin-top:250%">➡️</center>

</div>

<center class="col">

#### **Node table**

<div style= "font-size:20px;">

| node_id | Name   |
| ------- | ------ |
| 0       | John   |
| 1       | Carla  |
| 2       | Celine |
| 3       | Robert |
| 4       | Chang  |
| 5       | Hana   |
| 6       | Rob    |
| 7       | Diana  |
| 8       | Wilson |
| 9       | Simon  |
| 10      | Yu     |

</div>

</center>

<center class="col" >

#### **Edge table**

<div style= "font-size:18px;">

| src | trg |
| --- | --- |
| 0   | 10  |
| 1   | 10  |
| 1   | 2   |
| 2   | 10  |
| 2   | 3   |
| 3   | 4   |
| 3   | 5   |
| 3   | 6   |
| 4   | 7   |
| 6   | 8   |
| 6   | 9   |
| 8   | 10  |
| 9   | 10  |

</div>

</center>
</div>

---

# <center>Node table</center>

<div class="container">
<div class = "col" style="flex:0.4">

<center style="font-size:22px">

| node_id | Name   |
| ------- | ------ |
| 0       | John   |
| 1       | Carla  |
| 2       | Celine |
| 3       | Robert |
| 4       | Chang  |
| 5       | Hana   |
| 6       | Rob    |
| 7       | Diana  |
| 8       | Wilson |
| 9       | Simon  |
| 10      | Yu     |

</center>
</div>

<div class = "col">

- Consists of IDs and nodes' metadata (e.g., name, timestamp)
- IDs should be unique integers for a quick look-up

</div>
</div>
</div>


---

# <center>Edge table</center>

<div class="container">
<div class = "col">

<center>


| src | trg |
| --- | --- |
| 0   | 10  |
| 1   | 10  |
| 1   | 2   |
| 2   | 10  |
| 2   | 3   |
| ... | ... |

</center>
</div>

<div class = "col">

- Consist of the IDs of two nodes connected by edges
- Described by the node table.

- **🙂 Pros**
  - Space efficient
  - Highly editable and readable
- **😢 Cons**
   Not a convenient format for computing

</div>
</div>
</div>

---

### Adjacency matrix

- ...is a matrix representing a network
- The rows and columns represent the nodes
- Entry $A_{ij}$ indicates the presence ($A_{ij}=1$) or absence ($A_{ij}=0$) of an edge between nodes $i$ and $j.$

![bg right:40% 100%](https://i.stack.imgur.com/GahiR.jpg)

---

### Exercise

<div class="container">
<div class="col" >

- Create the adjacency matrix for the edge table on the right.
  - Make an 11x11 grid
  - Place 1 at an entry where $A_{ij}=1$
  - You can omit marking $A_{ij}=0$

- Think about the pros and cons

</div>

<center class="col" style="font-size:20px;margin-left:0%">

| src | trg |
| --- | --- |
| 0   | 10  |
| 1   | 10  |
| 1   | 2   |
| 2   | 10  |
| 2   | 3   |
| 3   | 4   |
| 3   | 5   |
| 3   | 6   |
| 4   | 7   |
| 6   | 8   |
| 6   | 9   |
| 8   | 10  |
| 9   | 10  |

</center>
</div>

---

<center class="col" style="font-size:26px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>

---

<div class="container">

<center class="col" style="font-size:26px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>

<div col>

#### 😢 Cons
  - Space inefficient, e.g., 100 entries for a network of 10 nodes.

#### 🙂 Pros
- Convenient for computing
  - A network $\iff$ a matrix
  - Network computations $\iff$ matrix operations.

</div>
</div>


---

## Network computations ➡️ matrix operations

Discuss how to compute the following statistics with the $n\times n$ adjacency matrix $A$. They can be computed using the entry value $A_{ij}$, matrix $A$, all-one column vector ${\bf 1}$, and/or the sum operator $\sum$.

- \# of edges in the network
- \# of friends (i.e., degree) of node $i$.
- \# of common friends between nodes $i$ and $j$️
- Average number of friends
- Average number of friends that a friend has

---



---
- \# of edges $\frac{1}{2}\sum_{i,j}A_{ij}$ or $\frac{1}{2}{\bf 1}^\top A {\bf 1}$
- \# of friends (i.e., degree) of node $i$
  - Row sum, i.e., $\sum_{j}A_{ij}$, or $(A \cdot {\bf 1})_i$
- \# of common friends between nodes $i$ and $j$️
  - $(i,j)$th entry of a squared matrix, i.e., $\sum_{k}A_{ik}A_{jk}$
  - or $(A^2)_{ij}$
- Average number of friends
  - $\sum_{ij} A_{ij}/n$ (where $n$ = \# of nodes) or ${\bf 1}^\top A {\bf 1}/n$,
- Average number of friends that a friend has
  - $\sum_{ij} A_{ij}\sum_k A_{jk} / \sum_{ij} A_{ij}$
---

### Average number of friends that a friend has

$$
\sum_{ij} A_{ij}\sum_k A_{jk} / \sum_{ij} A_{ij}
$$
<center>⬇️</center>

$$
\sum_{i,j; A_{ij}=1} \underbrace{\sum_k A_{jk}}_{\text{\# of friends a friend } j \text{ has}} / \underbrace{\sum_{i,j; A_{ij}=1}1}_{\text{\# of friendship ties}}
$$

---

### Let's test the friendship paradox:

<div class="container">
<center class="col" style="font-size:24px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>


<div class="col">

- Average number of friends
  - $\sum_{ij} A_{ij}/n$

- Average number of friends a friend has

$$
\sum_{i,j; A_{ij}=1} \underbrace{\sum_k A_{jk}}_{\text{\# of friends a friend } j \text{ has}} / \underbrace{\sum_{i,j; A_{ij}=1}1}_{\text{\# of friendship ties}}
$$

- You can draw a network

</div>
</div>

---

---

### Let's test the friendship paradox:

<div class="container">
<center class="col" style="font-size:24px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>


<div class="col">

- Average number of friends $\simeq$ 2.36

- Average number of friends a friend has = $3.0$

</div>
</div>

---


### The friendship paradox is a ***mathematical*** fact

![bg right:36% 100%](https://static01.nyt.com/images/2012/09/06/opinion/strogatz2-fig1/strogatz2-fig1-blog427.jpg)

It holds true for any network unless everyone has an equal number of friends.

**Why?**
Popular individuals appear frequently in someone's friend list.
E.g., a person with one friend is counted as a friend with one friend once. But a person with 100 friends is counted as a friend with 100 friends 100 times.

---

### ... and beyond an interesting piece of trivia

- Why is word-of-mouth an effective marketing strategy?

- Why can an infectious disease spread so quickly  🦠?

**Generalized Friendship paradox**

- Why are my friends richer than I am on average 🫢?

- Why are my colleagues so productive than I am 🙈?


---

<div class="container">
<div class="col" style="margin-top:8%">

## Can you find any redundancy?

## Can we make it more space efficient?

</div>
<center class="col" style="font-size:24px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>
</div>

---

<div class="container">
<div class="col" style="margin-top:8%">

#### Adjacency matrix is ***sparse.***

- Most entries are zero.
- Connected node pairs ($A_{ij}=1$) are exceptional.

<center>⬇️</center>
Recording only the exceptional pairs (i.e., non-zero entries) suffices to retain the information.

</div>
<center class="col" style="font-size:24px;margin-right:5%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>
</div>

---

<div class="container">

<div class="col" style="flex:1">

#  COOrdinate format (COO)

- Consists of three arrays
  - *rows*
  - *cols*
  - *data*
- Rows, column indices of non-zero entries, and the corresponding entry values.

</div>
<center class="col" style="flex:0.5;font-size:23px">

| rows | cols | data |
| ---- | ---- | ---- |
| 0    | 10   | 1    |
| 1    | 10   | 1    |
| 1    | 2    | 1    |
| 2    | 10   | 1    |
| 2    | 3    | 1    |
| 3    | 4    | 1    |
| 3    | 5    | 1    |
| 3    | 6    | 1    |
| 4    | 7    | 1    |
| 6    | 8    | 1    |
| 6    | 9    | 1    |
| 8    | 10   | 1    |
| 9    | 10   | 1    |

</center>

</div>

---

## <center class="vindent">Any idea from scientific papers?</center>

![bg right:60% 100%](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/5/5e/OLV2anotherbiblatexexample.png)

---

### Adjacency list

<div class="container">
<div class="col" style="margin-top:0%">

$\{\underbrace{\text{key}}_{\text{row ID}}: \underbrace{\text{values}}_{\substack{\text{non-zero entries'} \\ \text{column IDs}}}\}$

```markdown
{
  0:[1],
  1:[2,10],
  2:[1,3,10],
  3:[2,4,5,6],
  ...
}
```

- Useful to get ***local*** structure around a node.

</div>
<center class="col" style="font-size:24px;margin-right:2%">

|      |    0 |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |      |      |      |      |      |      |      |      |      |      |    1 |
|    1 |      |      |    1 |      |      |      |      |      |      |      |    1 |
|    2 |      |    1 |      |    1 |      |      |      |      |      |      |    1 |
|    3 |      |      |    1 |      |    1 |    1 |    1 |      |      |      |      |
|    4 |      |      |      |    1 |      |      |      |    1 |      |      |      |
|    5 |      |      |      |    1 |      |      |      |      |      |      |      |
|    6 |      |      |      |    1 |      |      |      |      |    1 |    1 |      |
|    7 |      |      |      |      |    1 |      |      |      |      |      |      |
|    8 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|    9 |      |      |      |      |      |      |    1 |      |      |      |    1 |
|   10 |    1 |    1 |    1 |      |      |      |      |      |    1 |    1 |      |

</center>
</div>


---

### Compressed Sparse Row (CSR)


<div class="container" >
<div class="col" style="flex:0.5;margin-right:5%">

Adjacency list
\{`keys`:`values`\}

```markdown
{
  0:[1],
  1:[2,10],
  2:[1,3,10],
  3:[2,4,5,6],
}
```

</div>


<div class="col" style="font-size:30px">

- *CSR = Concatenated adjacency list*.
- Consists of three 1D arrays, **indices**, **indptr**, and **data**
- **indices** concatenates `values` arrays:
  - indices = [`1`, `2,10`,`1,3,10`,`2,4,5,6`]
- **indptr** = the partition between different `values` arrays.
  - indptr = [0,1,3,6,10]
  - E.g. The `values` array of node 2 is between indptr[2] and indptr[2 + 1].
- **data** contains the values of the entries.
$$
$$
</div>
</div>

---


![bg width:100%](https://www.researchgate.net/publication/357418189/figure/fig1/AS:1106555248345089@1640834738634/The-Compressed-Sparse-Row-CSR-format-for-representing-sparse-matrices-provides-a.ppm)


---

<div class="container">
<div class="col" style="flex:0.5">

## Exercise

|     | 0   | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 1   | 1   |
| 1   | 1   | 0   | 1   | 0   |
| 2   | 1   | 1   | 0   | 1   |
| 3   | 1   | 0   | 1   | 0   |

</div>
<div class="col" style="margin-top:-5%;font-size:28px">


1. Write the adjacency list
2. Represent it by the three arrays---*indices*, *indptr* and *data*---in the CSR representation
3. Compute the degree of node 2 using the *indptr*.

Hint:
-  Adjacency list = $\{\underbrace{\text{key}}_{\text{row ID}}: \underbrace{\text{values}}_{\substack{\text{non-zero entries'} \\ \text{column IDs}}}\}$
- **indices** concatenates `values` arrays:
  - indices = [`1`, `2,10`,`1,3,10`,`2,4,5,6`]
- **indptr** = the partition between different `values` arrays.
  - indptr = [0,1,3,6,10]
  - E.g. The `values` array of node 2 is between indptr[2] and indptr[2 + 1].

</div>
</div>

---

# Python

Check out  [scipy.sparse.csr\_matrix — SciPy v1.11.2 Manual](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix)


```python
from scipy import sparse

src = [0,2,3,4,5]
trg = [5,3,1,5,6]
entry_values = [1,3,1,4,3]
A=sparse.csr_matrix((entry_values, (src, trg)), shape=(7,7))

A # 7x7 *sparse* matrix (CSR format)

A @ A # You can take its product just like a matrix
```

---

- **Compressed Sparse Column format (CSC)**:
  - Consists of *indices*, *indptr*, *data* (same as CSR)
  - *data* is the values of non-zero entries (same as CSR)
  - *indptr* is a pointer for *indices* (same as CSR)
  - *indices* = IDs of non-zero ***row IDs***
  - Equivalent to a *CSR representation of the transposed matrix*

- Implemented in `scipy` 😉

---

- **Pros 🙂**
  - Space efficient
    - Only takes $2m$ values, where $m$ is the number of non-zero entries.
  - Time efficient
    - Matrix product scales *linearly* by $m$ for sparse matrix 🚀
    - Dense matrix scales with $n^2$ ($n$ = \# of nodes).
  - Efficient format for parallel computing

## What are the *cons 🤔?*

---

- **Cons 🥲**
  - Changes to the network structure are expensive.
    - E.g., Adding/deleting an edge requires to compile from scratch.
  - CSR is slow in column slicing, e.g.,
    ```
    A[1, :] # Row slicing is fast
    A[:, 1] # Column slicing is slow
    ```
  - CSC is slow in *row* slicing

---

- **Edge table**
  - 🙂 Portable & Space efficient. 🥲 Inconvenient for computing
- **Adjacency matrix**
  - 🙂 Convenient for computing and math. 🥲 Space inefficient.
- **Adjacency list**
  - 🙂 Space efficient. Efficient access to *local* structure. 🥲 Not convenient for computing *global* stats.
- **Compressed Sparse Row/Columns**
  - 🙂 Space and Time efficient. 🥲 Not flexible to changes in the structure.
- **Others**. COOrdinate, List of List, etc.
---

# Reference


### Friendship paradox
- [The Friendship Paradox - YouTube](https://www.youtube.com/watch?v=httLvVufAYs)
- [The friendship paradox! - YouTube](https://www.youtube.com/watch?v=sF1wy6OkeLE)
- [Generalized friendship paradox in complex networks: The case of scientific collaboration | Scientific Reports](https://www.nature.com/articles/srep04603)

---

### Operationalizing "social connections."

- [SocioPatterns.org](http://www.sociopatterns.org/)
- [realitycommons.media.mit.edu/realitymining.html](http://realitycommons.media.mit.edu/realitymining.html)

