# Traffic

In this project, I made an AI with a neural network that will be able do determine which road sign it is given with a high accuracy based on previous experience (traning data set).

## Installing dependencies

Download an archive from [here](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip) and unpack it in this directory. It contains the neccesarry data for AI to train. Also install python dependancies like shown below. There is also available a smaller data [set](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb-small.zip) to experiment with, that just containts 3 types of road signs instead of 43.

```
pip3 install -r requirements.txt 
```

## Usage

```
pyton traffic.py
```

## Output

//////////

## Experimentation and thought process

### load_data

When working on the first function (load_data) tried going through the files and directories in the data set with os.walk that returns all directories, subdirectories and files in the specified directory, but then, when testing it's output, saw that it outputs a list of directories not in an order that I want, even though it woudn't have affected the resulted neuron network. Then I found that I can just iterate over every directory just by number and that way I will also keep track of labels/directory names.

### get_model

When I started creating the model for this project I first copied the model from the lecture, changing some values to fit my images that I am gonna pass in. When I started the program turned out that the example model wasn't right for my case, because the accuracy of the predictions from the start of the training to the end was quite low (~0.82) and the loss ws very high (~0.6). 

### Experimentation

Then I tried removing dropout layer, which resulted in improved results (~0.96 accuracy and ~0.15 loss on training sets). That was good but yielded overfitted results and because of that accuracy on testing sets was significantly lower (0.9) and the loss much higher (1.0). Then I tried changing and experimenting with the amount of dropout (you can view the results of this experimentation in the table below). Note that all values in the table are estimates and are not accurate.

| Dropout rate | Training loss | Training accuracy | Test loss | Test accuracy |
|:------------:|:-------------:|:-----------------:|:---------:|:-------------:|
|       0      |      0.15     |        0.96       |    0.7    |      0.92     |
|      0.1     |      0.3      |        0.92       |    0.35   |      0.92     |
|      0.2     |      0.25     |        0.94       |    0.32   |      0.95     |
|      0.3     |      0.33     |        0.91       |    0.29   |      0.93     |
|      0.4     |      0.57     |        0.83       |    0.4    |      0.9      |
|      0.5     |      1.2      |        0.6        |    0.6    |      0.82     |

As you can see from the table, rate of 0.2 is the one that yields the best results (the most accurate test results with the minimum loss).

Next I tried experimenting, adding the second convolutional and pooling layers, keeping the dropout layer at a rate of 0.2 as it appeared to be the most effective. Running the program for a few times (see results below), it becomes clear that inputting another convolution and pooling layers helped to improve accuracy and reduce loss in both the training and the testing sets.

| Training loss | Training accuracy | Test loss | Test Accuracy |
|:-------------:|:-----------------:|:---------:|:-------------:|
|      1.5      |        0.96       |    0.21   |      0.96     |
|      0.11     |        0.97       |    0.14   |      0.97     |
|      0.21     |        0.94       |    0.25   |      0.94     |
|      0.31     |        0.9        |    0.5    |      0.88     |
|      0.17     |        0.95       |    0.23   |      0.94     |
