Title: Setup Data Science Blog with Pelican + GitHub Pages 
Slug: Setup-Pelican-1
Date: 2018-02-14 20:00
Category: Tools
Tags: Pelican, Data Science, Blog, Github, Jupyter Notebook, Disqus, Google Analytics
author: Michael Li
Summary: My notes on how to setup Data Science blog using Pelican static site generater and GitHub Pages.

[TOC]

![Coding Background]({static}/images/coding.png)

First of all, this is by no means a thorough tutorial. I've followed Dataquest's blog post: [Building a data science portfolio: Making a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/) to get this one setup. Here are some insights and hiccups that may be helpful to others who want to do the same thing.

## Static sites and static sites generator

If you have never experienced the web development world, static site might be a new word to you. Actually it's quite simple, it's just plan web-site with HTML files, CSS sheets and Javascript files. These file never changes unless you make them, thus the word 'static'. The 'dynamic' site, on the other hand, use database and complex post-end technology to 'dynamically' generate these HTML/CSS/Javascripts files. It's much harder to develop and maintain. 
But I don't want that complexity you say. I just want to write something and post them and make them look neat. Then, my friend, look no further than a static site. Good news to us, there are a lot of static sites generators out there that can help us do the heavy-lifting of developing a website. 
The static sites generators come with many flavors, [Jekyell(based on Ruby)](https://jekyllrb.com/), [Pelican(based on Python](https://blog.getpelican.com/) are too popular one. Since I'm more familiar with Python. I decided to use Pelican to build my data science blog.

The beautiful thing here is, since Pelican is written in Python, it's quite easy to make it work with Jupyter Notebook, which is a huge bonus for data science. This means you can write your blog posts using Jupyter Notebook, leverage all the powerful snippets, data visualization and code executing it has and roll all those into your post, with ease.

## Install Pelican

Usually install Pelican will be easy, but if we also want to support Jupyter Notebook it will be harder. Many python modules will need to be installed using **pip**. 

Here is a list I used:
```bash
Markdown==2.6.6    # Markdown support
pelican==3.6.3     # Pelican itself
jupyter>=1.0       # Jupyter Notebook
ipython>=4.0       # iPython
nbconvert>=4.0     #
beautifulsoup4     # not sure why we need pharsing here, maybe manipulating codes
ghp-import==0.4.1  #handle git branches
matplotlib==1.5.1  #data visualization
```

Once all are installed, run:

```bash
pelican-quickstart
```

Answer couple of questions and the backbone of your site is up. To make the Jupyter Notebook part work, we will need this Pelican plugin (yes, Pelican support plugins!): [Pelican-ipynb](https://github.com/danielfrg/pelican-ipynb). 
Once installed, activate the plugin in your `pelicanconf.py`. This is your dot file, and you'll be dealig with it a lot later on. 
Add these into the bottom:

```python
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
```

## Write Post
Well this is the easier part. Just put your Jupyter Notebook file into the `'content'` folder. Also, for each post, we'll need a meta file to include some meta data of the post. The meta file should have the extension: `.ipynb-meta`. Here is an example:

```
Title: First Post
Slug: first-post
Date: 2016-06-08 20:00
Category: posts
Tags: python firsts
author: Vik Paruchuri
Summary: My first post, read it to find out.
```

It's quite easy to figure out what they are so I won't bother explain here. When done, save. 

## Generating HTML
Exit out of content folder, and run `pelican content` to generate the HTML. Enter `output` again and run:

```bash
python -m pelican.server
```

Then visit: `localhost:8000` to see your new site. 

## Putting it on GitHub Pages

Create a GitHub Page is simple and there are many tutorials out there. Once created, edit your `SITEURL` in `publishconf.py` file, make it into `https://username.github.io`, substitute `username` with your site name. 

--------------------------

Run `pelican content -s publishconf.py` to generate the real stuff. 

Run `ghp-import output -b master` to import everything into the `output` folder to the `master` branch. 

Run `git push origin master` to push changes to GitHub repo. 

----------------------------

## Themes
There are a lot of [themes](https://github.com/getpelican/pelican-themes) to choose from. What you need to do is to configure your `pelicanconf.py` file and assign the theme name. Some themes may need to install extra Python modules or have access to other services to work. But overall the process is straight forward.

## Google Analytics
Pelican have Google Analytics support out of the box. Register the site on GA, then get the `UA-XXXXxxxxx` id, put it into the `pelicanconf.py` file and you're golden. 

## Disqus
Disqus support come out of the box too. Register the site on Disqus, get your **shortname** correct, and put into `pelicanconf.py` and you should be good too. Some turorial suggest put into `publishconf.py`, well mine only works on `pelicanconf.py` so use your own judgement. 

## SEO
Basic SEO can be achieved using **sitemap** plugin. Search for it and put into `pelicanconf.py`, it will work automatically.

## Conclusion
Overall the process is not hard at all. Once everything is set. Just focus on putting in solid content using Jupyter Notebook. Enjoy coding, visualizing and writing!
