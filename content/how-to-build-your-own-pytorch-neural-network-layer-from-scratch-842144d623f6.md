Title: How to Build Your Own PyTorch Neural Network Layer from Scratch
Slug: how-to-build-your-own-pytorch-neural-network-layer-from-scratch-842144d623f6
Date: Wed Jan 29 15:21:13 CST 2020
Category: Machine Learning
Tags: Machine Learning, Artificial Intelligence
author: Michael Li
Summary: How to Build Your Own PyTorch Neural Network Layer from Scratch
[TOC]

And learn a thing or two about weight initialization

![](https://cdn-images-1.medium.com/max/4000/1*oLcN6Vlpa-PrxnRYJGnXDQ.png)

This is actually an assignment from [Jeremy Howard](undefined)’s [fast.ai course](https://www.fast.ai/2019/01/24/course-v3/), lesson 5. I’ve showcased [how easy it is to build a Convolutional Neural Networks from scratch](https://towardsdatascience.com/build-a-fashion-mnist-cnn-pytorch-style-efb297e22582) using PyTorch. Today, let’s try to delve down even deeper and see if we could write our own nn.Linear module. Why waste your time writing your own PyTorch module while it’s already been written by the devs over at Facebook?

Well, for one, you’ll gain a deeper understanding of how all the pieces are put together. By comparing your code with the PyTorch code, you will gain knowledge of why and how these libraries are developed.

Also, once you’re done, you’ll have more confidence in implementing and using all these libraries, knowing how things work. There will be no myth to you.

And last but not least, you’ll be able to modify/tweak these modules should the situation require. And this is the difference between a noob and a pro.

OK, enough of the motivation, let’s get to it.

### Simple MNIST one layer NN as the backdrop

First of all, we need some ‘backdrop’ codes to test whether and how well our module performs. Let’s build a very simple one-layer neural network to solve the good-old MNIST dataset. The code (running in Jupyter Notebook) snippet below:

<iframe src="https://medium.com/media/ebfff9b2780b077023072e413883bade" frameborder=0></iframe>

![](https://cdn-images-1.medium.com/max/2000/1*p2sKZABskEsunz6WcZdf7A.png)

These codes are quite self-explanatory. We used the [fast.ai](https://github.com/fastai) library for this project. Download the MNIST pickle file and unzip it, transfer it into a PyTorch tensor, then stuff it into a fast.ai DataBunch object for further training. Then we created a simple neural network with only one Linear layer. We also write our own update function instead of using the torch.optim optimizers since we could be writing our own optimizers from scratch as the next step of our PyTorch learning journey. Finally, we iterate through the dataset and plot the losses to see whether and how well it works.

### First Iteration: Just make it work

All PyTorch modules/layers are extended from thetorch.nn.Module.

    class myLinear(nn.Module):

Within the class, we’ll need an __init__ dunder function to initialize our linear layer and a forward function to do the forward calculation. Let’s look at the __init__ function first.

We’ll use the PyTorch official document as a guideline to build our module. From the document, an nn.Linear module has the following attributes:

![](https://cdn-images-1.medium.com/max/2198/1*eDRvelSa-3eugiKZ2X_fdw.png)

So we’ll get these three attributes in:

    def __init__(self, **in_features, out_features, bias=True**):
            super().__init__()
           ** self.in_features = in_features
            self.out_features = out_features
            self.bias = bias**

The class also needs to hold weight and bias parameters so it can be trained. We also initialize those.

![](https://cdn-images-1.medium.com/max/2028/1*bxuSixoCvOkpt9HijP_4Mg.png)

           ** self.weight** = torch.nn.Parameter(torch.randn(out_features, in_features))
           ** self.bias** = torch.nn.Parameter(torch.randn(out_features))

Here we used torch.nn.Parameter to set our weight and bias, otherwise, it won’t train.

Also, note that we used [torch.rand](https://pytorch.org/docs/stable/torch.html#torch.randn)n instead of what’s described in the document to initialize the parameters. This is not the best way of doing weights initialization, but our purpose is to get it to work first, we’ll tweak it in our next iteration.

OK, now that the __init__ part is done, let’s move on to forward function. This is actually the easy part:

    def forward(self, input):
            _, y = input.shape
            if y != self.in_features:
                sys.exit(f'Wrong Input Features. Please use tensor with {self.in_features} Input Features')
            **output = input @ self.weight.t() + self.bias
            return output**

We first get the shape of the input, figure out how many columns are in the input, then check whether the input size match. Then we do the matrix multiplication (Note we did a transpose here to align the weights) and return the results. We can test whether it works by giving it some data:

    my = myLinear(20,10)
    a = torch.randn(5,20)
    my(a)

We have a 5x20 input, it goes through our layer and gets a 5x10 output. You should get results like this:

![](https://cdn-images-1.medium.com/max/2816/1*uz_Hb4rul6pYs0bMIcTEBQ.png)

OK, now go back to our neural network codes and find the Mnist_Logistic class, change self.lin = nn.Linear(784,10, bias=True) to self.lin = myLinear(784, 10, bias=True). Run the code, you should see something like this plot:

![](https://cdn-images-1.medium.com/max/2000/1*IdvjAdDwEwhgLw0hRi2zwg.png)

As you can see it doesn’t converge quite well (around 2.5 loss with one epoch). That’s probably because of our poor initialization. Also, we didn’t take care of the bias part. Let’s fix that in the next iteration. The final code for **iteration 1** looks like this:

<iframe src="https://medium.com/media/b7f8cb6179f2fbcf782d4557998676e8" frameborder=0></iframe>

### Second iteration: Proper weight initialization and bias handling

We’ve handled __init__ and forward, but remember we also have a bias attribute that if False, will not learn additive bias. We have not implemented that yet. Also, we used torch.nn.randn to initialize the weight and bias, which is not optimum. Let’s fix this. The updated __init__ function looks like this:

    def __init__(self, in_features, out_features, bias=True):
            super().__init__()
            self.in_features = in_features
            self.out_features = out_features
            self.bias = bias
            **self.weight = torch.nn.Parameter(torch.Tensor(out_features, in_features))
            if bias:
                self.bias = torch.nn.Parameter(torch.Tensor(out_features))
            else:
                self.register_parameter('bias', None)**

    **        self.reset_parameters()**

First of all, when we create the weight and bias parameters, we didn’t initialize them as the last iteration. We just allocate a regular Tensor object to it. The actual initialization is done in another function reset_parameters(*will explain later*).

For bias, we added a condition that if True, do what we did the last iteration, but if False, will use register_parameter(‘bias’, None) to give it None value. Now for reset_parameter function, it looks like this:

    def reset_parameters(self):
            **torch.nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))**
            if self.bias is not None:
                **fan_in, _ torch.nn.init._calculate_fan_in_and_fan_out(self.weight)
                bound = 1 / math.sqrt(fan_in)
                torch.nn.init.uniform_(self.bias, -bound, bound)**

The above code is taken directly from PyTorch source code. What PyTorch did with weight initialization is called kaiming_uniform_. It’s from a paper [Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification — He, K. et al. (2015)](https://arxiv.org/pdf/1502.01852.pdf).

![](https://cdn-images-1.medium.com/max/2000/1*cq0NDktwlKPtWQ2OrhL67Q.png)

What it actually does is by initializing weight with a normal distribution **with mean 0 and variance bound**, it avoids the issue of **vanishing/exploding gradients** issue(*though we only have one layer here, when writing the Linear class, we should still keep MLN in mind*).

Notice that for self.weight, we actually give the a a value of math.sqrt(5) instead of the math.sqrt(fan_in) , this is explained in [this GitHub issue](https://github.com/pytorch/pytorch/issues/15314) of PyTorch repo for whom might be interested.

Also, we can add some extra_repr string to the model:

    def extra_repr(self):
            return 'in_features={}, out_features={}, bias={}'.format(
                self.in_features, self.out_features, self.bias is not None
            )

The final model looks like this:

<iframe src="https://medium.com/media/014b75ca4e4dd27b1212b432a0397871" frameborder=0></iframe>

Rerun the code, you should be able to see this plot:

![](https://cdn-images-1.medium.com/max/2000/1*6nUlBO7nIt9t2E0xrfgP-w.png)

We can see it converges much faster to a 0.5 loss in one epoch.

### Conclusion

I hope this helps you clear the cloud on these PyTorchnn.modules a bit. It might seem boring and redundant, but sometimes the fastest( and shortest) way is the ‘boring’ way. Once you get to the very bottom of this, the feeling of knowing that there’s nothing ‘more’ is priceless. You’ll come to the realization that:
> # Underneath PyTorch, there’s no trick, no myth, no catch, just rock-solid Python code.

Also by writing your own code, then compare it with official source code, you’ll be able to see where the difference is and learn from the best in the industry. How cool is that?

Found this article useful? Follow me ([Michael Li](https://medium.com/u/72c98619a048?source=post_page-----dbe7106145f5----------------------)) on Medium or you can find me on Twitter [@lymenlee](https://twitter.com/lymenlee) or my blog site [wayofnumbers.com](https://wayofnumbers.com/). You could also check out my most popular articles below!
[**“This is CS50”: A Pleasant Way to Kick Off Your Data Science Education**
*Why CS50 is especially good to solidify your software engineering foundation*towardsdatascience.com](https://towardsdatascience.com/this-is-cs50-a-pleasant-way-to-kick-off-your-data-science-education-d6075a6e761a)
[**Two Sides of the Same Coin: Jeremy Howard’s fast.ai vs Andrew Ng’s deeplearning.ai**
*How Not to ‘Overfit’ Your AI Learning by Taking Both fast.ai and deeplearning.ai courses*towardsdatascience.com](https://towardsdatascience.com/two-sides-of-the-same-coin-fast-ai-vs-deeplearning-ai-b67e9ec32133)
[**What You Need to Know About Netflix’s ‘Jupyter Killer’: Polynote 📖**
*It’s about time Jupyter Notebook has its worthy competitor*towardsdatascience.com](https://towardsdatascience.com/what-you-need-to-know-about-netflixs-jupyter-killer-polynote-dbe7106145f5)
