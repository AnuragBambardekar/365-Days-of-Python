# Neural Network

## Building blocks: Neurons
- Neurons are the basic unit of a neural network.
- A neuron takes inputs, does some math with them and produces one output.

![Alt text](https://victorzhou.com/a74a19dc0599aae11df7493c718abaf9/perceptron.svg)

- Each input is multiplied by a weight: <br>
$x_1 \rightarrow x_1 \ast w_1$ <br>
$x_2 \rightarrow x_2 \ast w_2$

- Next, all the weighted inputs are added together with a bias b: <br>
$(x_1 \ast w_1) + (x_2 \ast w_2) + b$

- Finally, the sum is passed through an activation function: <br>
$y = f(x_1 \ast w_1 + x_2 \ast w_2 + b)$

The activation function is used to turn an unbounded input into an output that has a nice, predictable form. A common;y used activation function is the sigmoid function.

The sigmoid function only outputs numbers in the range (0,1). 

## A Simple 2-input Neuron
$w = [0,1]$ <br>
$b=4$ <br>

$w = [0,1]$ is just a way of writing $w_1 = 0$, $w_2 = 1$ in vector form. 

Now, let's give the neuron an input of $x = [2,3]$. We'll use the dot product to write things more concisely: <br>
$(w \cdot x) + b = ((w_1 \ast x_1) + (w_2 \ast x_2)) + b$
$= 0 \ast 2 + 1 \ast + 4$
$= 7$
$y = f(w \cdot x + b) = f(7) = 0.999$

The neuron outputs 0.999 given the inputs $x=[2,3]$. That's it. This process of passing inputs forward to get an output is known as *feedforward*.

## Combining Neurons into a Neural Network
- A Neural Network is nothing more than a bunch of neurons connected together.
![Alt text](https://victorzhou.com/77ed172fdef54ca1ffcfb0bba27ba334/network.svg)

- This network has 2 inputs, a hidden layer with 2 neurons ($h_1 and h_2$), and an output layer with 1 neuron ($o_1$)
- Notice that the inputs for $o_1$ are the outputs from $h_1$ and $h_2$ - that's what makes this a network.

`A hidden layer is any layer between the input (first) layer and output (last) layer. There can be multiple hidden layers!`

- Let's use the network pictured above and assume all neurons have the same weights $w = [0,1]$, the same bias $b = 0$, and the same sigmoid activation function. Let $h_1, h_2, o_1$ denote the outputs of the neurons they represent.

What happens if we pass in the input $x = [2,3]$ ?

$h_1 = h_2 = f(w \cdot x + b)$
$=f((0 \ast 2) + (1 \ast 3) + 0)$ <br>
$=f(3)$ <br>
$= 0.9526$ <br>

$o_1 = f(w \cdot [h_1,h_2]+b)$ <br>
$=f((0 \ast h_1) + (1 \ast h_2) + 0)$ <br>
$=f(0.9526)$ <br>
$=0.7216$

The output of the neural network for input $x = [2,3]$ is 0.7216.

*A neural network can have any number of layers with any number of neurons in those layers. The basic idea stays the same: feed the input(s) forward through the neurons in the network to get the output(s) at the end.*

## Training a Neural Network

| Name | Weight (lb) | Height (in) | Gender
|----------|----------|----------|----------|
| Alice | 133 | 65 | F |
| Bob | 160 | 72 | M |
| Charlie | 152 | 70 | M |
| Diana | 120 | 60 | F |

Let's train our network to predict someone's gender given their weight and height:

![Alt text](https://victorzhou.com/965173626f97e1e6b497a136d0c14ec1/network2.svg)

We'll represent Male with a $0$ and Female with a $1$, and we'll also shift the data to make it easier to use:

| Name | Weight (minus 135) | Height (minus 66) | Gender
|----------|----------|----------|----------|
| Alice | -2 | -1 | 1 |
| Bob | 25 | 6 | 0 |
| Charlie | 17 | 4 | 0 |
| Diana | -15 | -6 | 1 |

*Normally, we shift by the mean*

### Loss
- Before we train our network, we first need a way to quantify how "good" it's doing so that it can try to do "better". That's what the loss is.
- We'll use the Mean Squared Error (MSE) loss:

$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{true} - y_{pred})^2 $

- n is the number of samples, which is 4 (Alice, Bob, Charlie, Diana)
- y represents the variable being predicted, which is Gender
- $y_{true}$ is the true value of the variable (the "correct answer"). For example, $y_{true}$ for Alice would be 1 (Female).
- $y_{pred}$ is the predicted value of the variable. It's whatever our network outputs.

$(y_{true} - y_{pred})^2$ is known as the squared error. Our loss function is simply taking the average over all squared errors (hence the name mean squared error). The better our predictions are, the lower our loss will be.

**Better predictions = Lower loss**

**Training a network = trying to minimize its loss**

- Let's say our network always outputs 0 - in other words, it's confident all humans are Male. Our loss would be:

$MSE = \frac{1}{4} (1 + 0 + 0 + 1) = 0.5$

- We now have a clear goal: minimize the loss of the neural network. We know we can change the network's weights and biases to influence its predictions, but how do we do so in a way that decreases loss?

The mean squared error loss (for Alice) is just Alice's squared error:

$MSE = \frac{1}{1} \sum_{i=1}^{1} (y_{true} - y_{pred})^2$ <br>
$=(y_{true} - y_{pred})^2$ <br>
$=(1-y_{pred})^2$ <br>

Another way to think about loss is a function of weights and biases.

![Alt text](https://victorzhou.com/27cf280166d7159c0465a58c68f99b39/network3.svg)

Then, we can write loss as a multivariable function: <br>
$L(w_1,w_2,w_3,w_4,w_5,w_6,b_1,b_2,b_3)$

- Partial derivatives are used to tweak $w_1$ to see how loss $L$ changes if we changed up $w_1$

- Skipping over the calculus...

- We now have all the tools needed to train a Neural Network. We'll use an optimization algorithm called Stochastic Gradient Descent (SGD) that tells us how to change our weights and biases to minimize loss. It's basically just this update equation:

$w_{1} \leftarrow w_{1} - \eta \frac{\partial L}{\partial w_1}$

where, $\eta$ is a constant called the learning rate that controls how fast we train. All we're doing is subtracting $\eta \frac{\partial L}{\partial w_1}$ from $w_1$:

- If $\frac{\partial L}{\partial w_1}$ is positive, $w_1$ will decrease, which makes $L$ decrease.
- If $\frac{\partial L}{\partial w_1}$ is negative, $w_1$ will increase, which makes $L$ decrease.

If we do this for every weight and bias in the network, the loss will slowly decrease and our network will improve.

## Our training process will look like this:

1. Choose one sample from our dataset. This is what makes it stochastic gradient descent - we only operate on one sample at a time.
2. Calculate all the partial derivatives of loss with respect to weights or biases.
3. Use the update equation to update each weight and bias.
4. Go back to step 1.

