Title: Tweaking Pelican Elegant Theme
Slug: Tweak-Pelican-Elegant-Theme
Date: 2018-02-24 20:00
Category: Tools
Tags: Pelican, Blog, Github, Theme
author: Michael Li
Summary: My notes on how to tweak a Pelican theme, in this article, Elegant.

[TOC]

![Elegant]({static}/images/Elegant.png)

Pelican has a lot of themes, developed by the community and shared on its official GitHub repo [here](https://github.com/getpelican/pelican-themes). [Pelican Themes](http://www.pelicanthemes.com/) also offer some previews of them so you can have a good idea of what to expect. 
Some themes are really easy to setup and configure, others need some efforts. The [Elegant](http://oncrashreboot.com/elegant-best-pelican-theme-features) them is the latter. For most of the themes, to make it work, you just need to add define the 'THEME' variable, like so:
```python
'THEME' = 'theme/themename'
```
For Elegant, it's way more than that, and it's a good thing. Elegant packed a lot of great features and thorough considerations to the reader. And that's why I choose it as the theme for my site. Good things come with a price they say. So let's find out. 

Search
-----
Search is useful when you have a lot of articles. All serious blog need to have it. To use it, add 'tipue_search' and 'sitemap' to your plugins and it will automatically be enabled. 

About Me and My Project
-----
Elegant's home page layout put the blogger himself front and center with 'About Me' and the 'My Project' at the top, followed with 'Recent Posts'. To use them, you need to set the 'LANDING_PAGE_ABOUT' and 'PROJECTS' variables in the ``pelicanconf.py``. 

jQuery Issue
-----
I've enabled all the nice features, like search, collasible comments, collasible comments. But they all won't work on Chrome because it's considered 'unsafe scripts'. After some digging, it turns out the site is using HTTPS, while the original theme's template uses HTTP to load the jQuery that did all these nice features. Once I replaced the HTTP with its HTTPS counterpart, everything works like a charm. 

Table of Contents
-----
Took me some time to get table of contents to work. Firstly 'extract_toc' plugin needs to be added into the 'PLUGINS' variable. Then 'markdown' Python module needs to be installed and configured for it to work as the Elegant website instructions. But after all this, it still didn't work. Turns out, you need to add ``[TOC]`` in the Markdown file, after all the meta data, to actually add the table of contents into your post. After I did that, everything works. 

Conclusion
-----
Install and tweaking a Pelican theme isn't that hard. Look into the static folder for CSS, tweak them if you want, or add custom CSS of your own and load them in the template. Then go into the template folder to check the html files. With basic HTML/CSS/Javascripts knowledge, you already can achieve a lot on tweaking any theme of your liking. 