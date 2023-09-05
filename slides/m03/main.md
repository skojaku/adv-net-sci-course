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

<div style="font-size:22pt;margin-top:-5%">

1. You will start up a social networking service and want to attract popular people to promote your service. Which of the following approaches is more likely to attract popular people as users? Explain why from the perspective of the friendship paradox.
   - **Waiting list**: Anyone can sign up for a waiting list and join the service on a first-come-first-served basis.
   - **Invitation**: Users can invite a given number of new users.

2. Create the Compressed Sparse Row Format of the undirected and unweighted network shown below with three arrays `indptr`, `indices` and `data`.


<center>

![center width:300px](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/800px-6n-graf.svg.png)

</center>

</div>

---


# <center  style="margin-top:7%"> Friendship paradox </center>

#### <center style="margin-top:7%">Your friends have more friends than you do</center>
<center style="margin-top:0%">on average</center>

---

### Let's test the Friendship paradox

Average \# of friends
$$
(1 + 3 + 2 + 2)/4 = 2
$$
Average \# of friends *a friend has*
$$
(\underbrace{1}_{\text{Abby}} + \underbrace{3 +3 + 3}_{\text{Becca}} +  \underbrace{2 + 2}_{\text{Chloe}} + \underbrace{2 +2}_{\text{Deb}}) / 8 = 2.25
$$

![bg right:40% 80%](https://static01.nyt.com/images/2012/09/06/opinion/strogatz2-fig1/strogatz2-fig1-blog427.jpg)

---

# The friendship paradox is a ***mathematical*** fact

![bg right:36% 100%](https://static01.nyt.com/images/2012/09/06/opinion/strogatz2-fig1/strogatz2-fig1-blog427.jpg)

It is always true unless everyone has an equal number of friends.

**Why?**:
Popular individuals appear frequently in someone's friend list.

---

You will start up a social networking service and want to attract popular people to promote your service. Which of the following approaches is more likely to attract popular people as users? Explain why from the perspective of the friendship paradox.
   - **Waiting list**: Anyone can sign up for a waiting list and join the service on a first-come-first-served basis.
   - **Invitation**: Users can invite a given number of new users.


---


### ... and beyond an interesting piece of trivia

- Why is word-of-mouth an effective marketing strategy?

- Why can an infectious disease spread so quickly  🦠?

- Why is the snow-ball sampling biased?

---

You will start up a social networking service and want to attract popular people to promote your service. Which of the following approaches is more likely to attract popular people as users? Explain why from the perspective of the friendship paradox.
   - **Waiting list**: Anyone can sign up for a waiting list and join the service on a first-come-first-served basis.
   - **Invitation**: Users can invite a given number of new users.

**Answer**: The invitation-based approach is considered more effective as it takes advantage of the friendship paradox, which means that popular individuals are more likely to receive invitations through social contacts.

---

<center>Another trivia </center>

# **<center>Vaccinating a friend is a more effective preventive measure than vaccinating an individual.</center>**

# <center style="margin-top:80px"> Why 🤔?</center>


---

<div style="font-size:25pt;margin-top:-5%">

First of all, let's create the adjacency list:

<center>

![bg width:100% right:30%](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/800px-6n-graf.svg.png)

</center>

```
{
  1: [2,5],
  2: [1,3,5],
  3: [2,4],
  4: [3,5,6],
  5: [1,2,4],
  6: [4],
}
```

Then, create the CSR representation:
```
indices = [2,5,1,3,5,2,4,3,5,6,1,2,4,4]
indptr = [0,2,5,7,10,13,14]
data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
```

</div>

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

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

# **Advanced Topics in Network Science**

SSIE 641

Module 3

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

# <center class="vindent">Network of the Week</center>

- Find an interesting network-related work
- Write a critique about it, shared it, and discuss it.
- Share it on Brightspace, and optionally Slack (`#interesting-nets` channel)
- https://brightspace.binghamton.edu/d2l/le/251332/discussions/List

---


# <center>Data normalization</center>

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

# <center class="vindent">Data integrity</center>
...is about how well data are organized and preserved throughout its life cycle, ensuring accuracy, completeness, and consistency.

---

# <center class="vindent">Spreadsheets (Excel) considered harmful</center>

<center>

Horror stories 🙈 https://eusprig.org/research-info/horror-stories/

</center>

![bg width:80% right:50%](https://eusprig.org/wp-content/uploads/logo.jpg)

---


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

