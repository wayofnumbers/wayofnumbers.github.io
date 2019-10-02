Title: On the Internet, Nobody Knows You Are a Dog, or AI
Slug: On-the-Internet-Nobody-Knows-You-Are-a-Dog-or-AI
Date: 2019-10-1 20:00
Category: Machine Learning
Tags: Machine Learning, NLP, Deep Fake
author: Michael Li
Summary: Explored the impact and potential solutions for deep fake comments. 

[TOC]

An inevitable slide into online community anarchy

![Photo by [Andy Kelly](https://unsplash.com/@askkell?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10944/0*-Gl0VJUpNJfYzaoq)*Photo by [Andy Kelly](https://unsplash.com/@askkell?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

I came across the following tweet today and I wanted to talk about it. It is a new paper get accepted into EMLNP about generating deep fake comments according to a title and the article. There is already a lot of discussions about the ethical implication of this. Since it is a paper developed by Chinese researchers, as a Chinese myself, I think I can probably read more into it given that I’m more in the context of the Chinese online community and what are the possible uses of this new technology.

<iframe src="https://medium.com/media/6b8386405abf878eec165990d46843fb" frameborder=0></iframe>

## Like Censoring, But More Aggressive

Generating deep fake comments is somewhat the opposite of censoring, in a bad way. Instead of blocking/removing information you **don’t want**, it generates/adds information that you do **want**. Censoring sometimes is not easy to spot, say your content is not recommended on YouTube or your tweet is hard to search on Twitter for some reason. These all happen in the background and usually done by algorithms. You don’t know exactly what happened. A lot of the times, censoring has plausible deniability. Also, nobody can censor you if you don’t put content up, so it’s passive. But deep fake comments are different. It’s more in-your-face, everybody can see it and they don’t have to wait for you to post anything to act on it. It can flood your channel or timeline and render the real message/information less obvious. Compare to censoring, which is a passive way to shaping public opinions, deep fake comments is a very aggressive way to create some ‘artificial trends’ in an effort of engineering people’s view on certain things. It could be some movie reviews, it can also be some report on social events to spin what happened. Nonetheless, the potential impact is big.

## Fine-Grained, yet Massive in Scale

![Photo by [hue12 photography](https://unsplash.com/@hue12_photography?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10944/0*0TRjNASnDgQZobcN)*Photo by [hue12 photography](https://unsplash.com/@hue12_photography?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Deep fake comments might be in the early stage of development, but it has the potential of being fine-grained in quality and massive in quantity. The recent development in NLP often leverage transfer learning in training models with fewer data and more quickly. Researchers can utilize currently [pre-trained model like the one trained on Wikipedia](https://www.kdnuggets.com/2017/11/building-wikipedia-text-corpus-nlp.html) as a base, and fine-tune more specific models to gain state-of-the-art results much quicker with fewer data. The pre-trained model already knows how English as a language work overall, just needs to learn how certain type of English is spoken (e.g. Reddit, or IMDB movie comments). Utilizing transfer learning, deep fake comments have the potential of quickly developing multiple models for many niches and achieve fine-grained quality, generating very relevant and ‘real’ comments on different areas.

Also, since it doesn’t rely on human intervention (like the ‘[50-cents Party](https://en.wikipedia.org/wiki/50_Cent_Party)’ in Chinese Internet), theoretically you can have thousands of scripts, running slightly different styled models and generating comments trying to push the same agenda. Think of how well Google’s targeted ads can do, and you’ll have an idea of how much potential this ‘targeted comments’ has. I would even go so far as claiming it could be some kind of ‘weapon’ in some sense.

In an [Internet where no one knows you are a dog](https://en.wikipedia.org/wiki/On_the_Internet,_nobody_knows_you%27re_a_dog), people stopped trusting articles since it can be crafted to convince you buying some products or pushing some agenda, but people by and large still trust comments, thinking it’s more human and more private thus more trustworthy. Now with the deep fake comments, even the comments cannot be trusted. What else on the Internet is still legit then?

## All Hope has Not Lost, Yet

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/DMlX7GV-axI" frameborder="0" allowfullscreen></iframe></center>

Having discussed all the scary indications of the deep fake comments can have. It’s not without weakness. As we all know that comments alone won’t have much influence if it cannot form a high-quality conversation. It’s the exchange of idea and emotion that really touches people. One comments, no matter how ‘real’ or ‘relevant’ it is, won’t have the optimum impact. When real people replied on the comment and expect a clever or powerful reply back, the algorithm will most likely fall short, at least for now. This is why a lot of the chatbot or ‘Siri’ like voice assistants have not gone mainstream yet. Being able to address this challenge is to say the AI has already passed the [Turing Test](https://en.wikipedia.org/wiki/Turing_test), which is a very high bar and I don’t believe we are there yet. [Google’s Duplex is currently the closest](https://towardsdatascience.com/did-google-duplex-beat-the-turing-test-yes-and-no-a2b87d1c9f58), but still not quite.

So for now, I think the algorithm could create a lot of hassle, but cannot really touch people and have a very deep impact.
> Yet.

## What Can We Do

I honestly don’t know the answer to this. We can regulate the development and publication of this kind of technology, or we can foster self-discipline like what [OpenAI was doing with their famous GPT-2 model](https://www.wired.com/story/dangerous-ai-open-source/) (a respective move and should be encouraged, though far from solving the bigger issue though).

Another way is to accept that the algorithm will be developed one way or another, and try to developed a counter-AI to detect the deep-fakes, like what [Facebook ](https://ai.facebook.com/blog/deepfake-detection-challenge/)and [Google ](https://ai.googleblog.com/2019/09/contributing-data-to-deepfake-detection.html)are doing right now.

If we can detect the deep-fake, we can censor the deep-fake, right? **Right?**

What do you think is the best way to deal with this? Please leave your comments (No Deep Fake Please!) below.

Any feedback or constructive criticism are welcomed. You can either find me on Twitter [@lymenlee](https://twitter.com/lymenlee) or my blog site [wayofnumbers.com](https://wayofnumbers.com/).
