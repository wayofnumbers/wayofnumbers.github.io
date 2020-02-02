Title: How to Port Your Medium Articles to Personal Blog with a Simple Bash Script
Slug: how-to-port-your-medium-articles-to-personal-blog-with-a-simple-bash-script-4422aa7b9be
Subtitle: ‘Quick and Dirty’ Blogging Automation
Date: Sat Feb  1 20:17:31 CST 2020
Category: Machine Learning
Tags: Machine Learning, Artificial Intelligence
author: Michael Li
Summary: How to Port Your Medium Articles to Personal Blog with a Simple Bash Script
[TOC]

![Photo by [Annie Spratt](https://unsplash.com/@anniespratt?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/15904/0*lwNGcCCG8j0H_5mz)*Photo by [Annie Spratt](https://unsplash.com/@anniespratt?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Medium is a great publication platform. It has good exposure, quality content, readers that really appreciate good articles and a neat and easy to use UI. It’s especially great for writers that just start their journey.

As good as it is, having your own blog outside of Medium is still not a bad idea. It enables you to have another channel you can totally own to communicate with your readers. And who knows, no company can last forever, what if Medium got acquired by some other company or something even worse happen. You can still sleep well at night knowing you won’t lose all your articles.

I built [my own](https://wayofnumbers.com/) using [Pelican](https://github.com/getpelican/pelican), a Python-based [static site generator](https://en.wikipedia.org/wiki/Static_web_page). I wrote an [article](https://towardsdatascience.com/my-experience-migrating-my-blog-from-github-pages-to-netlify-92ff6c85fb04) explaining the whole process. For every Medium article, I need to copy the URL, run some command to transfer it into Markdown file, then generate the blog site using Pelican. It is simple, but not as simple as I like it to be. So this is a great opportunity for some quick and dirty Bash script to come for the rescue. Let’s see what we can do.

## Structure the Script

Before start writing the script, it helps to structure out what we want to accomplish, makes it easier to write quality code. Basically, we need to:

1. Put all article URLs into one text file manually(plan to automate this part too in the future, using some scraping framework maybe)

1. Read every line of the file, and for each line.

1. Extract the title and subtitle

1. Use the title and subtitle to create meta-data needed for Pelican to turn the Markdown file into a post.

1. Run Pelican command to generate the static site.

1. Push the site to GitHub and trigger Netlify’s auto-build

1. Profit.

## Let’s Write the Code

![Photo by [Shahadat Rahman](https://unsplash.com/@hishahadat?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10368/0*wZqyc6jNLf1vwg3o)*Photo by [Shahadat Rahman](https://unsplash.com/@hishahadat?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

First of all, define our variables:

    #!/bin/bash 
    # Define variables
    filename='articles.txt'
    n=1

The structure the loop to read every line of the text file:

    # Read in file and do processing on each one
    while read line; do 
        # reading each line
        n=$((n+1)) 
        slug=$(echo $line | sed 's/https:\/\/towardsdatascience.com\///' )  # get slug from URL 
        FILE="$HOME/wayofnumbers.github.io/content/$slug.md"   # generate Markdown file name from slug 
        mediumexporter $line > $FILE   # convert medium article to markdown file    
        # some processing ...
    done < $filename

We used the sed command to remove the first part of the URL: [https://towardsdatascience.com/](https://towardsdatascience.com/) so the rest could be used as our slug. For example, [https://towardsdatascience.com/9-things-i-learned-from-blogging-on-medium-for-the-first-month-2bace214b814](https://towardsdatascience.com/9-things-i-learned-from-blogging-on-medium-for-the-first-month-2bace214b814) turns into [9-things-i-learned-from-blogging-on-medium-for-the-first-month-2bace214b814](https://towardsdatascience.com/9-things-i-learned-from-blogging-on-medium-for-the-first-month-2bace214b814), perfect for a slug. Here we also uses the slug to create the filename for the MarkDown file. Then we use mediumexporter to transfer URL into the Markdown file. You can find out more about mediumexporter [here](https://medium.com/@macropus/export-your-medium-posts-to-markdown-b5ccc8cb0050).

Now that we have the Markdown file, let’s fill in the processing code we want:

    # Processing the markdown file 
        tail -n +2 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"  # remove the first line 
        fl=$(head -n 1 $FILE) # put first line (title) into fl 
        firstline=$(echo $fl | sed 's/# //') # Remove '# ' 
        tail -n +3 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"  # remove the first line 
        subtitle=$(head -n 1 $FILE) # put first line (subtitle) into subtitle 
        tail -n +2 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"  # remove the first two line

These lines are rather self-explanatory. Now we have firstline variable as the title and subtitle variable as the subtitle, we are now ready to construct the Markdown file meta-data for Pelican:

    # handle metadata for Pelican  
    meta="
    Title: $firstline
    Slug: $slug
    Subtitle: $subtitle
    Date: $(date)
    Category: Machine Learning
    Tags: Machine Learning, Artificial Intelligence
    author: Michael Li
    Summary: $firstline
    [TOC]
    "

You can refer to Pelican’s document [here](https://docs.getpelican.com/en/stable/content.html#file-metadata) for more information about the meta-data format. Simply put, the Markdown file doesn’t need to specifically write the title and subtitle, as long as we specify the title and subtitle field in our meta-data, Pelican will automatically generate them for you in the post, with specific styles per the theme you choose.

![](https://cdn-images-1.medium.com/max/2400/0*WUqf8uBnOPArexxL)

With the correct meta-data, now we can finally update the Markdown and get it ready for site generation:

    { echo -n "$meta"; cat $FILE; } >$FILE.new # sticth meta-data and article content together 
    mv $FILE{.new,} 
    head -n -8 $FILE > $FILE.new # Remove medium's recommended articles
    mv $FILE{.new,}
    done < $filename  # don't forget to enclose the loop.

All my Medium articles have several recommendations for further readings. I removed those for my blog(the last line of code above). Now that the Markdown file is ready, time to generate the site and push it to the server:

    # push to server
    cd $HOME/wayofnumbers.github.io
    pelican content -s publishconf.py 
    git add .
    git commit -m "fix"
    git push origin dev

## Conclusion

So there you go. This script only works on Pelican static site generator, but the gist of it can be applied to any of your blogging platforms. I hope you learned a thing or two. And happy blogging/coding!
