Title: How I Migrated My Blog from GitHub Pages to Netlify
Subtitle: Things to consider when blogging as a data scientist
Slug: how-I-migrated-my-blog-from-github-pages-to-netlify
Date: 2019-09-26 20:00
Category: Machine Learning
Tags: GitHub, Pelican, Netlify, Blogging
author: Michael Li
Summary: Explained how I migrate my Pelican-based blog from GitHub Pages to Netlify

[TOC]


![Migrating Pelican site from GitHub Pages to Netlify](https://cdn-images-1.medium.com/max/4000/1*KirSA0PTL6iyG54DaSjDiw.png)*Migrating Pelican site from GitHub Pages to Netlify*

## The motivation

Today I came across [Rachel Thomas](undefined)’s story of ‘[**Why you (yes, you) should blog](https://medium.com/@racheltho/why-you-yes-you-should-blog-7d2544ac1045)**’. She brought up a great point that all data scientists should have their own blog. She further explained that blogging helps you clear your thoughts, spread knowledge and get noticed. All great points and I wholeheartedly agree. So I wanted to share my recent blogging experience and hope it can provide some insights into what it takes and why it is rewarding to do this.

## The Settlement

I’ve had my own blog for some time now. Starting my first blog post on WordPress.com, I stumbled along the way across multiple platforms, trying to find a good home for my thoughts and feelings. About a year ago, I settled on using [Pelican ](https://blog.getpelican.com/)(a Python-based static site generator) to generate my content, then host it on [GitHub Pages](https://pages.github.com/). It all works pretty well.

Python is an easy to write yet very powerful programming language. Also as a data scientist, you are very likely to live with Python every day. So among all the [static site generators](https://www.staticgen.com/), I picked Pelican, which is quite mature and regularly maintained. It also supports tons of [themes](https://github.com/getpelican/pelican-themes) and [plugins](https://github.com/getpelican/pelican-plugins). (I’ve even developed a [Pelican plugin](https://github.com/getpelican/pelican-plugins/tree/master/readtime) that calculates the article read time like Medium and get pulled into the main branch. ). It supports [Jupyter Notebooks](https://github.com/danielfrg/pelican-ipynb) which is also a plus for data scientists.

GitHub Pages is a very popular, free hosting service generously offered by [GitHub](http://github.com). It’s based on Ruby’s Jekyll framework but you don’t have to use it. This solution is totally free and somewhat easy to maintain. Once you set everything up, you only need to focus on putting content and running a simple script to push it to GitHub and it will automatically make it live. I used it to blog for a while. All seems fine.

(Note: Anyone wants to know more about how to do this, you can check this detailed [blog post](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/).)

## The Struggle

Then came the struggle. Somehow I cannot figure out how to make the SEO work. I exposed the ‘master’ branch on GitHub and also my blog site, and Google think it’s duplicate content and gave pretty bad rankings. It seems to be quite hard to get any traffic. Also as a free ‘side’ service provided by GitHub, there really isn’t a lot of features for hosting on GitHub Pages. As outlined in [this page](https://www.netlify.com/github-pages-vs-netlify/) by Netlify, it’s OK when you start blogging, but when you try to get more serious of your work, GitHub Pages just won’t cut it.

![Image Credit: Netlify.com](https://cdn-images-1.medium.com/max/2000/1*5v5qkuscnPTIJfHP_f5_1g.png)*Image Credit: Netlify.com*

## The Strife

So I decided to migrate to Netlify, which is also free, but offer way more features and if I want to scale up in the future, there are plenty of paid plans out there.

### Getting Pelican Ready

Since I already have my Pelican site ready on GitHub, most of the work is done. (If you haven’t set up Pelican site yet, you can follow this [tutorial](https://docs.getpelican.com/en/stable/quickstart.html). ) I still need to make some changes to the site so Netlify can smoothly connect to my GitHub account and pull the site to deploy.

**Dependencies:**

First of all, Netlify will need to set up the necessary dependencies so it can build my site. This requires me to provide a requirements.txt file under the site GitHub repo. To do that, I created a Python virtual environment for it:

    $ sudo apt update
    $ sudo apt install virtualenv  # install virtualenv
    $ cd ~/git/wayofnumbers.github.io/
    $ virtualenv venv -p python3.6  # create a virtualenv for Python 3.6
    $ source venv/bin/activate  # activate the virtual env

I also added venv/ in your .gitignore file so GitHub won’t sync it. Once the virtual env is ready, I installed only the necessary packages as follows:

    $ pip install -U --force-reinstall pip
    $ pip install pelican Markdown typogrify ipython beautifulsoup4 nbconvert

Now that the dependencies are all installed on my local virtual environment, I used the following command to generate the requirements.txt :

    $ pip freeze > requirements.txt

**CNAME:**

I created a CNAME file that contains my custom domain name( ‘wayofnumbers.com’) under the root folder of the repo. I also put the following lines in my pelicanconf.py file to ensure the CNAME file is copied to the root of the output directory:

    STATIC_PATHS = ['../CNAME']
    EXTRA_PATH_METADATA = {'../CNAME': {'path': 'CNAME'}}

**Plugins and Themes:**

Then it’s time to deal with plugins and themes. I copied the plugins and theme (folders) I use into the repo and set the pelicanconf.py file to point to those since on Netlify build time it needs to have access to them within the repo.

**Runtime.txt:**

Netlify needs a runtime.txt to decide which Python version to use for building the site. So I created a runtime.txt file under the root of the repo and put 3.7(Netlify supports either 3.7 or 3.5) in it.

Alright, now that the Pelican is ready, I can move on to set the Netlify up!

### Connect to Netlify

This part is actually quite easy. I registered to Netlify‘s free tier, and followed [this step-to-step guide](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/) to connect my GitHub repo. The only thing different is on ‘**Step 4: Configure Your Settings’**. Since I was using Pelican, the ‘Build command’ I used is:

    pelican content -s publishconf.py

After some failed builds due to dependencies issues, I got everything to work. Netlify automatically pulled my GitHub repo, installed the dependencies and built the site. I applied a custom domain with Google Domains and followed this link to set it up: [https://www.netlify.com/docs/custom-domains/#googledomains](https://www.netlify.com/docs/custom-domains/#googledomains). With $12 a year, it’s totally worth it.

I also turned on SSL, following [this guide.](https://www.netlify.com/docs/ssl/)

So now my site is up and running on its new home:

![My blog with ‘Elegant’ theme](https://cdn-images-1.medium.com/max/2520/1*xDKjW2Rr-NBQrnefrL5dbg.png)*My blog with ‘Elegant’ theme*

## The Thoughts

The whole migration process took me around one day. I learned quite some new stuff from it. It’s challenging but totally do-able. I encourage anyone that’s interested in treating your blogging seriously to try this out. It’s quite neat. Some people say data scientists should focus on their research and learning, I tend to wander off from time to time. Picking up some web programming tips here, getting some DevOps experience there. I found this kind of ‘digress’ actually is a bit relaxing and stimulate the other part of my brain. It’s a form of rest and relax. I felt like playing a hacking game and solving problems along the way. Having knowledge of deployment will help you in [putting your model to production](https://towardsdatascience.com/two-sides-of-the-same-coin-fast-ai-vs-deeplearning-ai-b67e9ec32133) easier and quicker. Having a blog is like having another venue to communicate with your colleagues and like-minded people out there. Can’t go wrong with that, right?

Any feedback or constructive criticism are welcomed. You can either find me on Twitter [@ lymenlee](https://twitter.com/lymenlee) or my blog site [wayofnumbers.com](https://wayofnumbers.com).
