# The Sparks Foundation Projects

### Graduate Rotational Internship Program (GRIP)
### August 2021 to October 2021
### Author: Teghpreet Singh Mago

## Project 1 : Prediction using Supervised Machine Learning

### 1. Problem defintion

Predict the percentage of an student based on the no. of study hours. This is a simple linear regression task as it involves just 2 variables.

### 2. Dataset Source

Data can be found at http://bit.ly/w-data

### 3. Evaluation

If we can reach 95% accuracy at predicting, we'll be successful at the project.

### 4. Libraries and Features

For this project, we will import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, warnings, sklearn and sklearn.ensemble from RandomForestRegressor

## Project 2 : Color Identification in Images

### 1. Problem defintion

Implement an image color detector which identifies all the colors in an image or video.

### 2. Libraries and Features

For this project, We need sklearn for KMeans algorithm, matplotlib.pyplot for plotting graphs, numpy to work with arrays, cv2 to work with image data, collections to use Counter to count values, rgb2lab to convert RGB values and deltaE_cie76 to calculate similarity between colors

Using this application, one can input a valid location of an image and obtain the image in different filters.(The image location that we entered here was italy.jpg)

The application can also be used to plot the colours in an image into a pie chart with different colours plotted against their standard colour codes. 

Using this application, one can also input a valid location of an image folder and classify different images by colour.(The image folder that we entered here was nature)

To classify images based on their colours, we have created a dictionary COLORS and used the hexcodes of four basic/primary colurs: RED, BLUE, GREEN, YELLOW. We can also use other secondary colours by extracting their hexcodes. 
