---
marp: true
theme: uncover
class:
  - lead
  - invert
paginate: true
backgroundColor: #011627
size: 4:3
style: |
  .vindent {
    margin-top: 5%;
  }
  .red {
    color: #c44f51
  }
  .blue {
    color: #4c72b0
  }
  section {
    font-size: 28px;
  }
  .container {
    display:flex;
  }
  .col {
    flex: 1
  }
  strong {
    color: #ffeb95;
  }
  h3 {
    color: #ffeb95;
  }
  a {
    color: #ff79c6;
  }
---

# Quiz


---


<div style="font-size:20pt;margin-top:-5%">

1. Why should we specify data types when loading data? Explain with an example.

2. We want to create a social network of students in a collage, in which each edge between two students indicates that they joined the same party, weighted by the number of parties they joined together. Let $B$ be a matrix, where $B_{ik}=1$ if student $i$ joins party $k$, and otherwise $B_{ij}=0$. Express the adjacency matrix $A$ of the student network by using B. Self-loops are allowed.

3. The weight of a self-loop edge indicates the number of parties a student joined alone. True or False.

3. If there is an edge with a large weight between two students, we can always say that the two students are friends to each other. True or False, and explain why.

</div>

---

[An alarming number of scientific papers contain Excel errors - The Washington Post](https://www.washingtonpost.com/news/wonk/wp/2016/08/26/an-alarming-number-of-scientific-papers-contain-excel-errors/?postshare=4161472211255740)

![width:600px](./excel-horror-gene.png)


---

# <center class="vindent"> One-mode projection </center>

<center style="margin-top:55px"> Probably the most commonly used network construction method </center>

---

$$
(A)_{ij} = \sum_{y} B_{ik} B_{jk}
$$

or alternatively

$$
A = B B^\top
$$

---

### <center > Two types of measurements of edges </center>

- **Direct**:
  - e.g., ask people for their friends to identify friendship ties.
- **Indirect (inferential)**:
  - e.g., consider two people having a friendship tie if they hang out together frequently.
  - *Most networks are this type*.

One-mode projection generates edges based on correlation. And correlation does not imply causation.

---

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Moreno_Sociogram_2nd_Grade.png)

### Advanced Topics in Network Science

SSIE 641

Module 4

Sadamori Kojaku

https://github.com/skojaku/adv-net-sci-course

---

### For EngiNet™ students


WARNING

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

# Revisiting previous quiz

---

2. Create the Compressed Sparse Row Format of the undirected and unweighted network shown below with three arrays `indptr`, `indices` and `data`.

<center>

![invert center width:300px](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/800px-6n-graf.svg.png)

</center>

---

<div  style="font-size:22pt;margin-top:-5%">

Adjacency list
<center style="background-color:white">

![invert bg width:100% right:30%](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/800px-6n-graf.svg.png)

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

CSR representation

```
indices = [2,5,1,3,5,2,4,3,5,6,1,2,4,4]
indptr = [0,2,5,7,10,13,14]
data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
```

Neighbors of node $i$
```python
indices[indices[i]:indices[i+1]]
```

The weigh of edges to the neighbors of node $i$
```python
data[indices[i]:indices[i+1]]
```

</div>

---

<div  style="font-size:22pt;margin-top:-5%">

CSR representation

```
indices = [2,5,1,3,5,2,4,3,5,6,1,2,4,4]
indptr = [0,2,5,7,10,13,14]
data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
```

The $k$th neighbor of node $i$
```python
i = 1
k = 2
indices[indices[i] + k]
```

The weight of the edge to the $k$th neighbor
```python
data[indices[i]+k]
```

</div>


---


# GigHub codespaces

### Please fork the course repo and open codespaces on your forked repo.

(otherwise I might go into bankruptcy 😭)

https://github.com/skojaku/adv-net-sci-course


---

# Assignment instruction

https://github.com/skojaku/adv-net-sci-course/wiki/Submitting-assignments

---

# <center class="vindent"> Data visualization </center>

<center style="margin-top:55px"> Probably the most important skill for anyone working with data </center>

---

# <center class="vindent"> Why data visualization? </center>

---

## <center class="vindent"> ... 1854, London </center>

---

<center>

# *Industorial revolution*

Rapid urbanization but no infrastructure

</center>

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Powerloom_weaving_in_1835.jpg/2880px-Powerloom_weaving_in_1835.jpg)

---

<center>

# *Nightman*

</center>

![bg right:50%](https://victorianweb.org/history/work/19.jpg)

---

<center >

# *Night soil / Cesspools*

</center>

![bg right:50%](https://constructionmanuals.tpub.com/14259/img/14259_174_1.jpg)

---

![](https://etc.usf.edu/clipart/23900/23992/leaky_drain_23992_lg.gif)

---

<center >

# *Cholera outbreak,* *1854*

127 died in three days.

</center>

![bg right:50%](https://www.sciencemuseum.org.uk/sites/default/files/styles/embedded_image/public/2019-08/king-cholera-wellcome.jpg?itok=_nFr-q_i)

---

# <center > "Miasma (bad air) theory" </center>
# <center > vs </center>
# <center > "Germ theory" </center>

---

<center >

# Henry Whitehead

</center>

![bg left:50%](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Whitehead_henry1884.jpg/220px-Whitehead_henry1884.jpg)

---

<center>

# John Snow

</center>

![bg right:50%](https://static.wikia.nocookie.net/gameofthronesfanon/images/6/66/Jon_Snow_%28Trials_and_Tribulations_of_the_Oathkeeper%29.png)

---

<center>

# John Snow

</center>

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/John_Snow.jpg/440px-John_Snow.jpg)

---

<center >

# They changed the fate of human race.

### What did they do?

</center>

---

![bg](https://media.nationalgeographic.org/assets/photos/000/276/27636.jpg)

---

![bg](pump.png)

---

> *On proceeding to the spot, ***I found that nearly all the deaths had taken place within a short distance of the [Broad Street] pump***. There were only ten deaths in houses situated ***decidedly nearer*** to another street-pump. In five of these cases the families of the deceased persons informed me that they always sent to the pump in Broad Street, as they preferred the water to that of the pumps which were nearer. In three other cases, the deceased were children who went to school near the pump in Broad Street...*

*John Snow, letter to the editor of the Medical Times and Gazette*

---

![bg](https://www.londonxlondon.com/wp-content/uploads/2023/03/John-Snow-shutterstock_2231427637.jpg)

---

# Can't we just use numbers?

![width:800px](https://miro.medium.com/v2/resize:fit:1166/1*JyDU5qgFA-S2XOFBah9YcQ.png)


---

![bg width:80%](https://1millionmonkeystyping.files.wordpress.com/2020/09/screen-shot-2020-09-12-at-8.47.58-pm.png)

---

<center>

## Anscombe's quartet

</center>

![bg width:100% right:50%](https://1millionmonkeystyping.files.wordpress.com/2020/09/screen-shot-2020-09-12-at-8.47.58-pm.png)

---

- [What data patterns can lie behind a correlation coefficient? (blog post)](https://figshare.com/articles/journal_contribution/What_data_patterns_can_lie_behind_a_correlation_coefficient_blog_post_/6945335/1)
- [Same Stats, Different Graphs - CHI 2017 - YouTube](https://www.youtube.com/watch?v=DbJyPELmhJc)

<iframe width="560" height="315" src="https://www.youtube.com/embed/DbJyPELmhJc?si=8Agx3YkY966z463F" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

<center style="margin-top:30%">

# Our visual system is a powerful pattern recognition machine

</center>

![bg width:100% right:50%](https://assetsio.reedpopcdn.com/gpu-power-ladder-all-graphics-cards-tested-1569663337391.jpg?width=1600&height=900&fit=crop&quality=100&format=png&enable=upscale&auto=webp)

---


<center >

# Networks

</center>

- nodes/edges,
- size/width
- colors
- layout
- ....

![bg width:270% right:50%](https://zkm.de/sites/default/files/styles/r17_1280/public/bild/150_years_of_nature_2019_1_c_barabasilab.png?itok=KXzZp_lX)

---


<center >

# Perception

### Why shuld we care?

</center>

---

![bg width:80%](https://nerdwisdom.files.wordpress.com/2007/09/checkershrunk001.jpg?w=403&zoom=2)

---

![bg width:80%](https://nerdwisdom.files.wordpress.com/2007/09/checkerproofshrunk002.jpg?w=422&zoom=2)

---

<center >

# \#dressgate


</center>

![bg width:100% right:50%](https://people.com/thmb/KdU_A2ey3pBkt0rJ1y7GqZPdTXQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/internet-meltdown-435-1c7e5a912b5c41268776cbc309603516.jpg)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I had to double check this using the Gimp. It is not a fake. Seeing is not believing. <a href="https://t.co/q8zHa4HIPH">pic.twitter.com/q8zHa4HIPH</a></p>&mdash; Kat Scott 🐀 (@kscottz) <a href="https://twitter.com/kscottz/status/873726218344050688?ref_src=twsrc%5Etfw">June 11, 2017</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---


![bg width:70%](https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Mountain-spring-redwhite.png/520px-Mountain-spring-redwhite.png)

---

# What is <span style="color:red">C</span><span style="color:yellow">o</span><span style="color:#0f0">l</span><span style="color:pink">o</span><span style="color:cyan">r</span>?

---

<div style="background-color:#ee0000;height:2350px;width:2350px;margin-left:-10%;margin-top:-5%;margin-bottom:-5%">
</div>

---

<div class="container">

<div class="col" style="flex:1;;margin-right:-5%;margin-left:-10%">
<center>
<div style="background-color:#ee0000;height:350px;width:350px">
<p style="padding-top:40%">Red</p>
</div>
</center>
</div>

<div class="col" style="flex:1;;margin-right:-5%;margin-left:-10">
<center>
<div style="background-color:#cc0000;height:350px;width:350px">
<p style="padding-top:40%">Red</p>
</div>
</center>
</div>

<div class="col" style="flex:1;;margin-right:-5%;margin-left:-10">
<center>
<div style="background-color:#aa0000;height:350px;width:350px">
<p style="padding-top:40%">Red</p>
</div>
</center>
</div>
</div>

---

![width:800px](https://i0.wp.com/imgs.xkcd.com/blag/satfaces_map_450.png?zoom=2)

---

# How can we quantitatively represent colors?

### Do you know any "system" to represent colors?

---

# RGB
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/The_three_primary_colors_of_RGB_Color_Model_%28Red%2C_Green%2C_Blue%29.png/440px-The_three_primary_colors_of_RGB_Color_Model_%28Red%2C_Green%2C_Blue%29.png)


---

# CMY(K)

![width:500px](https://media.geeksforgeeks.org/wp-content/uploads/20190722223850/cmy.png)


---


![left width:400px](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/The_three_primary_colors_of_RGB_Color_Model_%28Red%2C_Green%2C_Blue%29.png/440px-The_three_primary_colors_of_RGB_Color_Model_%28Red%2C_Green%2C_Blue%29.png)
![bg right width:500px](https://media.geeksforgeeks.org/wp-content/uploads/20190722223850/cmy.png)

---

![width:600px](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hsl-hsv_models.svg/1200px-Hsl-hsv_models.svg.png)

---

### Brightness: HSL
![width:500px](https://www.peko-step.com/image/img_hsv005.png)

### Brightness: HSV
![width:500px](https://www.peko-step.com/image/img_hsv003.png)

---

# Lightness

![bg width:100% right:50%](https://www.cs.unm.edu/~brayer/vision/w32.gif)

---

![bg](https://www.cs.unm.edu/~brayer/vision/sim_cont.gif)

---

# Which is lighter?

<div class="container">
<div class="col" style="flex:1;;margin-right:10%">
<center>
<div style="background-color:#adadad;height:350px;width:350px">
</div>
</center>
</div>
<div class="col" style="flex:1;;margin-right:10%">
<center>
<div style="background-color:#a8a8a8;height:350px;width:350px">
</div>
</center>
</div>
</div>

---

# Which is lighter?

<div class="container">
<div class="col" style="flex:1;;margin-right:-5%">
<center>
<div style="background-color:#adadad;height:350px;width:350px">
</div>
</center>
</div>
<div class="col" style="flex:1;">
<div style="background-color:#a8a8a8;height:350px;width:350px">
</div>
</center>
</div>
</div>

---

![bg](perception-vs-intensity-lightness.png)


---

![](https://i.insider.com/591f22f263914721008b50a5?width=1300&format=jpeg&auto=webp)

## Discussion

### <div style="margin-top:-5%">What is a problem of this map (from the perspective of human perception)?</div>

---

# <span style="color:red">H</span><span style="color:yellow">U</span><span style = "color:cyan">E</span>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/RGB_color_wheel_24.svg/220px-RGB_color_wheel_24.svg.png)

---

## Three dimensions of colors


<div class="container">
<div class="col" style="flex:1">

### Brightness

![width:200px height:200px](https://www.peko-step.com/image/img_hsv005.png)

</div>

<div class="col" style="flex:1">

### Lightness
![width:200px](https://www.cs.unm.edu/~brayer/vision/w32.gif)

</div>

<div class="col" style="flex:1">

### <span style="color:red">H</span><span style="color:yellow">U</span><span style = "color:cyan">E</span>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/RGB_color_wheel_24.svg/220px-RGB_color_wheel_24.svg.png)

</div>
</div>

---

### What is the problem of the rainbow color?

![width:900px](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-020-19160-7/MediaObjects/41467_2020_19160_Fig1_HTML.png)

![bg height:80% right:30%](https://root.cern/assets/images/RCM02.png)

---

[A Better Default Colormap for Matplotlib | SciPy 2015 | Nathaniel Smith and Stéfan van der Walt - YouTube](https://youtu.be/xAoljeRJ3lU?si=XPO_ZLBxt99eew5O)


<iframe width="560" height="315" src="https://www.youtube.com/embed/xAoljeRJ3lU?si=XPO_ZLBxt99eew5O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

![](https://hess.copernicus.org/articles/25/4549/2021/hess-25-4549-2021-avatar-web.png)


---

# Green vs Red

![](https://clipart-library.com/images/8cxKkagEi.gif)

---

<div style="font-size:150px"> 🙈 </div>

![bg width:400px](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU61eUVDef0KiN7PiVC53XPgsZ13d6BKvGYGM60nBD-s-k94jvCfG3hqALQLqWjoaFldA&usqp=CAU)

![bg width:400px](https://www.researchgate.net/publication/328771265/figure/fig4/AS:962855188824085@1606573974194/PPI-network-analysis-of-the-identified-DEGs-Red-and-green-color-represents-upregulated.png)


---

# Psychophysics

a branch of psychology on the relationships between phsyical stimulti and sensation

---

![bg width:95%](bottle-of-water01.png)

---

# Weber's law


<div style="font-size:100px">

$$
k = \frac{\Delta I}{I}
$$

</div>

- $I$: Intensity
- $\Delta I$: Changes in the intensity
- $k$: constant

(Just noticeable difference; JND)

---

# Steven's power law

---

### How many times is the larger one bigger than the smaller one (in terms of radius)?


<div class="container">
<div class="col" style="flex:1;margin-top:13%">

![width:100px right:50%](https://www.pngall.com/wp-content/uploads/13/Red-Circle.png)

</div>
<div class="col" style="flex:1">

![width:300px right:50%](https://www.pngall.com/wp-content/uploads/13/Red-Circle.png)

</div>
</div>

---

### How many times is the larger one bigger than the smaller one?


<div class="container">
<div class="col" style="flex:1;margin-top:13%;margin-right:-20%">

<center>
<div style="background-color:#f00;height:50px;width:200px;">
</div>
</center>

</div>
<div class="col" style="flex:1;margin-top:29%">

<center>
<div style="background-color:#f00;height:50px;width:600px">
</div>
</center>

</div>
</div>

---

## The larger ones are 3x bigger.

<div class="container">
<div class="col" style="flex:1;margin-top:13%">

![width:100px right:50%](https://www.pngall.com/wp-content/uploads/13/Red-Circle.png)

</div>
<div class="col" style="flex:1">

![width:300px right:50%](https://www.pngall.com/wp-content/uploads/13/Red-Circle.png)

</div>
</div>

<div class="container" style="margin-top:-20%">
<div class="col" style="flex:1;margin-top:13%;margin-right:-20%">

<center>
<div style="background-color:#f00;height:50px;width:200px;">
</div>
</center>

</div>
<div class="col" style="flex:1;margin-top:29%">

<center>
<div style="background-color:#f00;height:50px;width:600px">
</div>
</center>

</div>
</div>

---

# What did you find?

---

## Steven's power law

<div style="font-size:80px">

$$
S = I^\alpha
$$

</div>

- $S$: Sensation
- $I$: Intensity
- $\alpha$: Exponent

![bg width:100% right:55%](https://graphworkflow.files.wordpress.com/2019/09/stevens_law.png)

---

![bg width:100%](visual-hierarchy.png)

---

### What is the issue of pichart?

![width:100%](https://www.dagira.com/wp-content/uploads/2016/05/pie.jpg)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Why you should not use pie charts. <a href="https://t.co/AahWfGYU6N">pic.twitter.com/AahWfGYU6N</a></p>&mdash; Max Roser (@MaxCRoser) <a href="https://twitter.com/MaxCRoser/status/857389434756505600?ref_src=twsrc%5Etfw">April 27, 2017</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<div style="margin-top:900px;margin-left:-8%;padding-left:0px;">

# From my paper



![width:1000px](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-021-93572-3/MediaObjects/41598_2021_93572_Fig4_HTML.png?as=webp)

</div>

---

# <span style="color:f00">Pre-</span>attentative
# processing

---

# How many 5s?

# 345678904345678455678905643567890965

---

# How many 5s?

# 34<span style="color:red">5</span>67890434<span style="color:red">5</span>6784<span style="color:red">5</span><span style="color:red">5</span>67890<span style="color:red">5</span>643<span style="color:red">5</span>6789096<span style="color:red">5</span>

---

![bg ](https://media2.dallasobserver.com/dal/imager/as-fascism-rises-schindlers-list-has-become-almost-radical/u/magnum/11395917/schindlers_list_oliwia_dabrowska_courtesy_universal_pictures.jpg?cb=1642543936)

---

![bg ](https://qph.cf2.quoracdn.net/main-qimg-bc3a79a0b9c86bc90f438c70c64e8149-lq)

---


[The toll of Israeli bombs on Gaza, mapped - The Washington Post](https://www.washingtonpost.com/world/2021/06/11/gaza-damage-map-rebuilding-israel/)


---

![bg width:100%](preattentative.png)


---

![bg](https://www.cns.nyu.edu/~david/courses/perception/lecturenotes/attention/attention-slides/Slide11.jpg)

---

# Gestalt Priniple

---

### How do we know the right order of panels to read without explicit instruction?

![bg width:100% right:50%](https://qph.cf2.quoracdn.net/main-qimg-941ae8158aa5634eb93dc5326879a6b3-lq)

---


![bg width:100%](https://miro.medium.com/v2/resize:fit:2000/0*c6t0WWqxrf25XlWD.jpg)


---

![bg width:110%](https://chrisbrejon.com/wp-content/uploads/2020/08/030_gestaltTheory_0030_gestalt_principles_FHD.jpg)

---

![bg width:100%](gestalt.png)

---

# Discussion


### How do you improve this visualization?

![width:600px](https://umap-learn.readthedocs.io/en/latest/_images/basic_usage_30_1.png)

---

### Differentiate colors simultaneously along the three color dimensions

![](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fnmeth0810-573/MediaObjects/41592_2010_Article_BFnmeth0810573_Fig2_HTML.jpg?as=webp)


---

### Use predefined color maps

[ColorBrewer: Color Advice for Maps](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)

---

## Use different shapes

![](https://pressbooks.umn.edu/app/uploads/sites/41/2020/05/Pressbook_Gestalt-Principles-300x300.png)

---

# References

[Checker shadow illusion - Wikipedia](https://en.wikipedia.org/wiki/Checker_shadow_illusion)
[Same Stats, Different Graphs - CHI 2017 - YouTube](https://www.youtube.com/embed/DbJyPELmhJc?si=8Agx3YkY966z463F)
[What data patterns can lie behind a correlation coefficient? (blog post)](https://figshare.com/articles/journal_contribution/What_data_patterns_can_lie_behind_a_correlation_coefficient_blog_post_/6945335/1)

[Color coding | Nature Methods](https://www.nature.com/articles/nmeth0810-573)
[A Better Default Colormap for Matplotlib | SciPy 2015 | Nathaniel Smith and Stéfan van der Walt - YouTube](https://youtu.be/xAoljeRJ3lU?si=XPO_ZLBxt99eew5O)

[The toll of Israeli bombs on Gaza, mapped - The Washington Post](https://www.washingtonpost.com/world/2021/06/11/gaza-damage-map-rebuilding-israel/)

[How Florence Nightingale Changed Data Visualization Forever - Scientific American](https://www.scientificamerican.com/article/how-florence-nightingale-changed-data-visualization-forever/)