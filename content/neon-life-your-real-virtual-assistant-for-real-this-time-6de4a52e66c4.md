Title: NEON.LIFE: Your REAL Virtual Assistant, For Real This Time?
Subtitle: The anatomy and theory-crafting of NEON.LIFE, Samsung’s new ‘Artificial Human’
Slug: neon-life-your-real-virtual-assistant-for-real-this-time-6de4a52e66c4
Date: Thu Jan 30 11:13:50 CST 2020
Category: Machine Learning
Tags: Machine Learning, Artificial Intelligence
author: Michael Li
Summary: NEON.LIFE: Your REAL Virtual Assistant, For Real This Time?
[TOC]


![](https://cdn-images-1.medium.com/max/2500/0*pbfygQlozOYzIXYx.jpg)

Anyone watched [Blade Running 2049](https://www.imdb.com/title/tt1856101/) must remember ‘Joi’, the pretty and sophisticated holographic projection of an artificial human. She speaks to you, helps you with house affairs, tells jokes to you, keeps you accompanied, and some more… just like a real human. She even has her own memory with you and developed character over time. Except, ‘she’ is not human. She is just a super complicated ‘modeling’ of a real human that can speak, act and react like one. Yet still, quite some people secretly wish that they could also have their own ‘Joi’. Well, she might not be as far away as you think. Enter [NEON](https://www.neon.life/), Samsung’s new artificial human.

![Joi from [Gfycat](https://gfycat.com/grouchyfaintesok)](https://cdn-images-1.medium.com/max/2000/0*qewd9ME91MB7hJnH.gif)*Joi from [Gfycat](https://gfycat.com/grouchyfaintesok)*

## Encounter

I was at CES 2020 show last week and walking the floor. There were many new gadgets, new technologies revealed like past years. There were also tons of displays. Small, big, huge, foldable, half-transparent, you name it. Among them, one display grabbed my attention. A life-like human stands within a display looking at me with a warm smile and also talks about something with rich gestures. What is this for? A new remote video service maybe? Intrigued, I came closer and checked. Turns out, none of these very realistic figures are human. They are called NEONs, artificial humans created in a Samsung-backed company called STAR Labs.
> *NEON, our first artificial human is here. NEON is a computationally created virtual being that looks and behaves like a real human, with the ability to show emotions and intelligence. — STAR Labs*

![From NEON.LIFE](https://cdn-images-1.medium.com/max/2000/0*4apnXkka8XrrtBaX.jpg)*From NEON.LIFE*

The look, expression, gesture are so natural I can’t really tell whether it is pre-recorded video or CGI. Look closer, it is obviously CGI, just very very ‘real’. Real in the sense of ‘human-like’ rather than ‘high-resolution’. I dug in deeper and found out that these are AI-generated CGI footage based on the pre-recorded real human video, a ‘recreation’ from human actor videos. Very much like what [James Cameron](https://www.imdb.com/name/nm0000116/?ref_=tt_ov_dr) first did it in the movie [Avatar](https://www.imdb.com/title/tt0499549/).

![Photo from [lyon.onvasortir.com](http://lyon.onvasortir.com/pourquoi-j-039ai-pas-mange-mon-pere-3873571.html)](https://cdn-images-1.medium.com/max/2000/0*1a6inxMk4U1I2xVH.jpg)*Photo from [lyon.onvasortir.com](http://lyon.onvasortir.com/pourquoi-j-039ai-pas-mange-mon-pere-3873571.html)*

But NEON didn’t stop there, it pushes things even further. These NEONs can go out-of-script and develop its own ‘personality’. It can originally generate new expressions, gestures, and reactions out of its own unique ‘personality’. These ‘personalities’ can also be trained and adapted to outside stimuli. Now, this is deeper than just mimic the facial expression! How did Samsung achieve this and what does this mean? There aren’t too many details revealed at the show. My inner Data Scientists instantly got turned on, let’s try to figure out (guess) how this is achieved and what impact it could have on our society and industry, shall we?

## Anatomy

So how did they do this? Let’s first look at what it can do. To achieve what they claimed, NEON need to do several things:

*Notes: The below parts are just my ‘educated prediction’, thus bearing no truth on how NEON actually works or created. More details of NEON has yet to be released by Samsung.*

## Physical modeling: Real-human video to CGI, cross the uncanny valley

Given some video datasets of one actor, the model needs to learn how to transfer a video into CGI footage, the more similar the better. This technology has been well developed with the rise of Avatar and performance capture. Actors get filmed with some color dots grid on their faces to record their facial expressions and transfer those facial expressions grid movements into CGI character expressions. It’s a rather mature technology. What NEON did is just a bit different. It might not have the grid as a reference but using deep learning, it’s not too hard for the deep neural networks to find the features they need for the task and it can maybe do better than a simpler model like the facial grid.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/OJ1JzYPjcj0" frameborder="0" allowfullscreen></iframe></center>

**Data Input:** video footages

**Data Output:** facial/body grid movements time series data.

## Expression modeling: Expression/Gesture projection to CGI

So from the video footage, we now have a grid movements time series data set, if we can label these data set with different expressions, we should be able to train some kind of autoencoder that can encode the CGI time-series to expression encoding, then re-generate the same CGI time-series data. Then we can look at the encoding and figure out what is smile, cry, surprise, angry, etc. This is also a solved problem. You can find one examples below:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/dCKbRCUyop8" frameborder="0" allowfullscreen></iframe></center>

**Data Input:** CGI Time-series data set

**Data Output:** Expression encoding/embedding layers

## Personality modeling: Emotion to expression

So now we can pretty much control the expression of our CGI avatar via expression encoding, the next step would be to map emotion to expression. The expression is the externalizing of emotion, but the mapping isn’t always straightforward. You would think people will laugh when they are happy, but humanity is way more complicated than that. Some outgoing people will laugh out loud while an introvert will probably just smirk subtly. What controls the mapping from emotion to expression is personality. Now how do we model personality? This requires a lot of domain knowledge(this is also what Samsung claims the part they are still working on and I think the most challenging. Cause humanity, you know…).

![](https://cdn-images-1.medium.com/max/3840/0*4kfOSTR1OQfyoXf1)

**Data Input:** Emotion Labeling (multiple labels since one expression could have multiple emotions behinds it)

**Data Output:** Expression encoding/embeddings representing the emotion for given avatar

## What Samsung Say About NEON is comprised of

From the presentation we know that NEON is actually comprised of three parts:

* Behavioral Neural Network (**Expression Model?**)

* Evolutionary Generative Intelligence (**Personality Model?**)

* Computational reality (**Physical Model?**)

Are my above assumptions true? We’ll know more in the near future, but please leave some responses if you have different ideas!

## Theorycrafting

So how do these parts fit together and form a NEON? It could work as a pipeline:

First using the video footage of one human actor to train a neural network that can generate CGI grid time-series data. This will give the ability to control the CGI avatar to be as human as possible. The neural network will inevitably learn how human gestures and human facial expressions patterns, this lays the ground for further abstraction.

With the CGI grid movement time-series data, we can train an autoencoder that can do some kind of dimensional reduction, create some middle layer encoder then regenerate the CGI. Once the regenerated CGI is similar enough to the original time-series data, we’ll get an even more abstract layer (expression encoder) of the video, expressions, and gestures. Once we have the encoder or embedding, we can play around and see which combination of weights could generate certain expressions, e.g. smile, angry, surprised, etc. We can then use these weights ( might need to do some PCA to make it more manageable) to control the expression of our avatar, make it smile, cry, etc.

To this point, the avatar’s expression could be largely controlled manually, but it’s not there yet. What’s needed is to have the avatar itself originally ‘generate’ expressions on its own, react to outside stimuli. This is where the personality model comes into play. Using the domain knowledge of phycology, emotional science, many different personality features can be developed their relationship to expression and outside stimuli can be modeled. If we use certain celebrity (say Bruce Lee) as an example, by labeling his behavior (expression) and outside stimulus (sentiment of words, gestures, etc.), we can develop a ‘personality’ model that reflects what the celebrity will react to the different sentiment with different expressions. Then we use this personality model to control the NEON’s reaction expression according to outside sentiment ( output from a sentiment classifier neural network maybe).

In the NEON official videos, there is a real-time visualization of NEON’s ‘emotion activation’ status, indicating how NEON react to outside stimulus. Pretty cool.

![NEON’s emotional map in real-time, the light bulb is where her current state is and the words are different emotional states.](https://cdn-images-1.medium.com/max/2000/1*qdaUUj1a0AmtNuoV_Erg4g.png)*NEON’s emotional map in real-time, the light bulb is where her current state is and the words are different emotional states.*

Beyond that, NEON can learn domain knowledge and provide more value. Samsung claims that they have another cloud AI platform called Spectra for that and 3rd party developers will be able to develop those ‘skills’ for NEON. Thinking Siri with a pretty face, charming voice, and can teach you Kung Fu. 😜

I have to say, even though the demo they showed on CES 2020 is far from perfect, NEON is groundbreaking. The team is thinking quite big and laid down a good foundation and framework. The computational hunger application at this moment may mean NEON can’t live on the edge, but with the fast development of 5G and better cloud platform, I believe the future potential for NEON is huge.

## Vision

![Which NEON do you want? Yoga tutor? Magician? Business assistant? Personal Photographer?](https://cdn-images-1.medium.com/max/3840/0*Bxam4hzol0C0TINZ)*Which NEON do you want? Yoga tutor? Magician? Business assistant? Personal Photographer?*

This is the part of the article where I’m allowed to go wild. Let’s see what a NEON can do:

* **Perfect NPC in gaming. **In RPG games, NPCs are usually pretty dumb. Their facial expression and reaction are so fake. NEON can change that and give gamers a very real experience.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/Vzxv-MKtXZc" frameborder="0" allowfullscreen></iframe></center>

* **Recreate your passed away loved ones or friends. **If you’ve read [this article](https://www.wired.com/story/a-sons-race-to-give-his-dying-father-artificial-immortality/) about a boy tried to create a chatbot speak exactly like his dad and kept him accompany after the old man passed away, you know what I’m talking about. NEON can go even further on this, not only the chatbot generate texts like his father, it can look like, sounds like, act as his father and even with similar ‘personality’. (maybe a bit creepy but who am I to judge…)

* **All kinds of service assistants. **Like Yoga tutor, financial planner, or just keep you company with a good personality.

* **Guidance/Helper for disabled people.**

* **Celebrity ‘copy’ for fans to adore**

* **Autism therapist**

The list can go on and on, but you get the idea. With it being an open platform, it could very well be the next big thing in tech.

## Conclusion

Usually, CES is about engineering innovations rather than science breakthrough, but I think NEON is somewhat sit in the middle. The team is still very young and I’m so excited to see what they can do in the near future and learn about their approaches. It is really a hidden gem that I felt compelled to introduce to my readers. What do you think an artificial human can do? Cannot do? Or should never do?

For more details on what’s shown on the stage of CES, you can check out this detailed video:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/lXZBmMGD7pI" frameborder="0" allowfullscreen></iframe></center>
