Title: OpenAI: Catch Me If You Can
Slug: openai-catch-me-if-you-can
Date: 2019-09-19 20:00
Category: Machine Learning
Tags: Machine Learning, AI, OpenAI, Gaming, Reinforcement Learning
author: Michael Li
Summary: OpenAI's multi-agent hide and seek experiments explained.

What OpenAI’s Multi-Agent Hide and Seek Break Through Means

![](https://cdn-images-1.medium.com/max/5074/1*zx1DVdwYOVJWdHURXr5qjw.png)

### Who is OpenAI?

When it comes to reinforcement learning, OpenAI is a big name. The [OpenAI Gym toolkit](https://gym.openai.com/) provides a solid foundation for a lot of ML researchers to explore and study reinforcement learning techniques. They also are known to have developed ‘[GPT-2](https://openai.com/blog/better-language-models/)’ language model. The ‘deep fake’ news the model generated is so scarily good that OpenAI refused to release the trained model, just the [code ](https://github.com/openai/gpt-2)and [paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf).

![From OpenAI.com](https://cdn-images-1.medium.com/max/2406/1*p3ZS8EKITYRCTu1_JqtwiA.png)*From OpenAI.com*

### Hide and Seek, Only This Time the Computer is Playing It

Today they release something new and equally groundbreaking: [The Multi-agent Hide and Seek](https://openai.com/blog/emergent-tool-use/). You can have a look at the short video below from their website:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/kopoLzvh5jY" frameborder="0" allowfullscreen></iframe></center>

Simply put, they designed a reinforcement agent and let it play a simple ‘Hide and Seek’ game that we all played when we were still a kid. After millions of games played with itself and the prior version of itself. Both the seeking and hiding agent developed several very effective strategies to counter each other and win.

![Basic abilities agent has to play and win the game](https://cdn-images-1.medium.com/max/2000/1*ldh0SVwH9-Z8iZWY_MGhTw.gif)*Basic abilities agent has to play and win the game*

### How to Train Your Dragon, urr… Agent

The agents develop their tactics in an adversarial way.

1. Both agents move randomly

1. Seeking agent learns to chase hiding agent.

1. Hiding agent learns to run away from seeking agent (not working)

1. Hiding agent learns to use blocks in the environment to block entrance to a small room and hide inside (It works!)

1. Seeking agent learns to use ramp blocks in the environment to jump over the wall to get inside the blocked room

1. Hiding agent learns to move ramp blocks inside the room, then block the room

1. …… the game keeps playing and more gaming mechanism is discovered and exploited, both agents getting smarter and smarter.

The seeking agent and hiding agent counter each other and at the same time grow with each other. This is a concept (相生相克 mutually reinforce and neutralize each other) very familiar to Chinese people, and can be illustrated in a simple way:

![Taichi 太极](https://cdn-images-1.medium.com/max/2000/1*w3rxOO7r5d96JdDDAYskpQ.gif)*Taichi 太极*

Philosophy aside, we did see this kind of concept appear on recent AI field quite often. Another example is the rise of [GAN (General Adversarial Network)](https://towardsdatascience.com/must-read-papers-on-gans-b665bbae3317) where a ‘generator’ and ‘discriminator’ are trained at the same time to achieve state-of-the-art results.

### The Agents Looks Cute! But Why I Still Feels a Bit Chilly on My Spine?

Agents in the game are quite cute with cartoony big heads and smiley eyes. But underneath the cuteness, what does the great results suggest? Well, just imagine, if they are not playing this cute little hide and seek game where agents giggles when get caught, rather, they are playing Doom or Quake, where blood and gores fly around when the agent gets caught. Will the bloody scene lead you to start worrying about the possible application of this model and the potential it has if weaponized? If this still seems too far away from reality, let me bring this uncomfortable imagination one step further, allow me to use three words:
> # Boston Dynamic, Drones, Skynet.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/dKjCWfuvYxQ" frameborder="0" allowfullscreen></iframe></center>

The tasks and tactics agent learned from millions of games might still seem easy. Hide, use blocks, use ramps, etc. But don’t forget that complicated and sophisticated strategy is formed with all these small pieces. One big advancement of AI recently is [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning), build new AI models on top of already trained/learned models. (Using transfer learning based on already trained [IMAGENET](http://www.image-net.org/) model, people can quickly train a fine-grained cat/dog classifier with only 100 images and 1 GPU in minutes. I explained the approach of [fast.ai](https://course.fast.ai/videos/?lesson=1) at [here](https://medium.com/datadriveninvestor/deep-learning-models-by-fast-ai-library-c1cccc13e2b3)). These basic game tactic model can be utilized in the future to build more realistic and dangerous military strategy models that can totally be applied in war.** This is not beyond our reach now. **If we put all our current AI and robotic achievements together, great/scary things can be achieved.
> When an OpenAI model agent running within a Boston Dynamics robot or killer drones, and video surveillance networks everywhere to watch your every step, if you are the hider playing this game, what is the chance of you winning?
