Title: What You Need to Know About Netflix’s ‘Jupyter Killer’: Polynote 📖
Slug: what-you-need-to-know-about-netflixs-jupyter-killer-polynote
Date: 2019-10-25 20:00
Category: Machine Learning
Tags: Machine Learning, AI, Polynote, Netflix, Jupyter Notebook
author: Michael Li
Summary: Introduced Polynote, Netflix's new open source notebook for data science research.

[TOC]

It’s about time Jupyter Notebook has its worthy competitor

![](https://cdn-images-1.medium.com/max/2490/0*MCKD9v7ezPD7yXrX)

Today, Netflix open-sourced [Polynote](http://www.polynote.org/), the internal notebook they developed, to the public. It’s not rare these days that big tech companies open sources their internal tools or services, then got popular and adopted by the industry. Amazon AWS, Facebook’s React.js, etc. are two of them. It makes sense. These big tech companies have the best engineers in the industry and more often than not they are facing the biggest challenges that will drive the development of great tools. Netflix’s Polynote could be another one of those great tools and the data science/machine learning industry does need better tools in terms of how to write code, experiment algorithms and visualize data. Here are several things you need to know about this new tool. I’ll try to keep this succinct and to the point so you can quickly read through it and be knowledgeable about the pros and cons of this new choice of our development/research environment.

### Polynote is more like a simple version of IDE rather than nicer version of a REPL

![](https://cdn-images-1.medium.com/max/2000/1*ekzSzXwlM_3FLniZ0IQD5g.png)

![](https://cdn-images-1.medium.com/max/2000/1*K2Pfk9OWcw9VmgW4Rr68Cg.png)

![](https://cdn-images-1.medium.com/max/2000/1*30lhxh_hNfdnEZdPUOmAqw.png)

![auto-completion, error indication, better text editor, LaTex support](https://cdn-images-1.medium.com/max/2000/1*Nb7HgK1vpzZK6OGccmFvJQ.png)_auto-completion, error indication, better text editor, LaTex support_

Polynote put some emphasis on making the notebook work more like an IDE or code editors like VS Code. It supports better auto-completion, linting, rich text editor, and LaTex. This might be a bit of an overstatement, but that’s the direction it is going. You can say better syntax highlighting and better auto-completion are trivial, but these little quality-of-life improvements could go a long way and make you focus more on the real tasks. BTW, most of the editing capabilities are powered by the [Monaco](https://microsoft.github.io/monaco-editor/) editor which powers the experience of Visual Studio Code, showing potential to be even better.

### Multi-language Support

![](https://cdn-images-1.medium.com/max/2000/0*oqEdsGYz4i50jLTj.gif)

Currently, it only supports Python, Scala, and SQL. You might argue that Jupyter Notebook also supports Python, R, and Julia. But how they support multi-languages is different. For Jupyter Notebook, you can only choose one language for one notebook. Whereas Polynote can support all these languages working seamlessly in one notebook. It achieves this by sharing variables between cells so different language cells can work under same context. Needless to say, this has the potential to be very powerful. With more languages it supports, a skilled data scientist can use the best language for the right tasks. It increased the skill-cap yet also raise the performance bar.

### Data Visualization and Data Awareness

In Polynote, data visualization is built-in. It means developers won’t need to write any code to visualize their data, they can just use a GUI interface and see the data the way they want. Also, developers won’t need to type in any code in order to see the value of the variable, you can just use the GUI. When code is running, there is also a progress window at the right side of the screen so you always have an idea of which part of the code is currently running.

![](https://cdn-images-1.medium.com/max/2000/0*2WOpp02MSITUTTq9.gif)

These will all add up to better data intuition.

### Configuration and dependency management built-in

Another quality-of-life improvement. Gone of the days you have to run things like:

    ! pip install packages

You can simply specify what dependencies you need for your code to run smoothly and BOOM, Polynote will set it up for you. This will result in less clutter in code. How good is that!

![](https://cdn-images-1.medium.com/max/3200/0*aUB7r2JbsRMhM39w)

## Reproducible Code

Simply put, Polynote is not using the good old REPL model for code execution. It uses its own code interpreter instead. The biggest difference is: for Jupyter Notebook that uses REPL, you can safely execute cells not in the order they are written. You can execute cell 3, then cell 2, then cell 1. It’s all up to you. This brings flexibility but decreases the sharability of the notebook. Polynote handles cell execution differently:

> By keeping track of the variables defined in each cell, Polynote constructs the input state for a given cell based on the cells that have run above it. Making the position of a cell important in its execution semantics enforces the principle of least surprise, allowing users to read the notebook from top to bottom.

It seems to be more like you are writing a script instead of a notebook. You take more notice of making sure things are in order when writing it. But you get the benefit of consistent code results and better sharability. See the animation below:

![](https://cdn-images-1.medium.com/max/2000/0*Zky40q2ZMyTr7e85.gif)

### Conclusion

We’ll see how well the industry will adopt Polynote but definitely it shows potential and making some sound decisions. One question is whether the big cloud platforms like GCP, AWS or Azure will adopt it. This is quite important because, without the support of these cloud platforms, people rely on them to do research/experiment won’t have access to Polynote and thus won’t use it.

Found this article useful? Follow me ([Michael Li](undefined)) on Medium or you can find me on Twitter [@lymenlee](https://twitter.com/lymenlee) or my blog site [wayofnumbers.com](https://wayofnumbers.com). You could also check out my most popular articles below!
[**“This is CS50”: A Pleasant Way to Kick Off Your Data Science Education**
*Why CS50 is especially good to solidify your software engineering foundation*towardsdatascience.com](https://towardsdatascience.com/this-is-cs50-a-pleasant-way-to-kick-off-your-data-science-education-d6075a6e761a)
[**Two Sides of the Same Coin: Jeremy Howard’s fast.ai vs Andrew Ng’s deeplearning.ai**
*How Not to ‘Overfit’ Your AI Learning by Taking Both fast.ai and deeplearning.ai courses*towardsdatascience.com](https://towardsdatascience.com/two-sides-of-the-same-coin-fast-ai-vs-deeplearning-ai-b67e9ec32133)
[**I finished Andrew Ng’s Machine Learning Course and I Felt Great!**
*The good, the bad, and the beautiful*medium.com](https://medium.com/datadriveninvestor/thoughts-on-andrew-ngs-machine-learning-course-7724df76320f)
