# ENGR 571 - Project 2
![Cover_Image](coverimage.png "Simple Classification Engine")

# Problem Statement
This project aims to develop a classification algorithm that will predict the number of rings (and by extension the age) of an abalone given following the features and measurements:

![Feature Table](featuretable.png "Feature Table")
<center><img src="featuretable.png" alt="Feature Table"></center>

Since the number of rings if not a continuous value, this problem can be considered a classification problem. For simplicity, the classes were set as r<4, 5, 6, …, 21, and r>21 (20 classes in total).

A full report summary can be found in the 'docs' page. Although the results provide no new insight in light of documents that have already been written, it was an excellent exercise to build my first ever classification engine and an exciting introduction to the world data science.

This project was initially conducted to satisfy requirements for ENGR 571, Analytics in Systems Engineering. The initial project prompt was to build the "classification model of Module 10 applied to your own data set.” 

Module 10 provided a walkthrough of the training, validation, testing, and deployment of a small classification algorithm with three features, three classes, and thirty samples for each development phase. It also provided a brief analysis at the end of the system performance. 

With the available information from Module 10, an analogous system was built in a Python-based Jupyter Notebook and applied to a marine biology dataset published by the [University of California Irvine online machine learning repository](http://mlr.cs.umass.edu/ml/datasets/Abalone/). The dataset description states that the Marine Resources Division of Tasmania, Australia originally used the data in a biology study before eventually donating it to UCI in 1995. Interestingly, the documentation also reports that two papers have been published that used the data to test novel neural networks.


# What the Heck is an Abalone?
[Abalone](https://en.wikipedia.org/wiki/Abalone) are marine snails that belong to the family Haliotidae. To determine the age of an individual abalone, it must be cut and stained before the number of rings can be counted through a microscope. Since this is process is often time-consuming and tedious, other approaches involving much easier physical measurements have been proposed to estimate their age.
