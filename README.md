# The_Sparks_Foundation_Task_2

## The Sparks Foundation

### GRIP January 2022 Batch

### Author: Teghpreet Singh Mago

### Task 2 : Color Identification in Images

### 1. Problem defintion

Implement an image color detector which identifies all the colors in an image or video.

### 2. Libraries and Features

For this project, We need sklearn for KMeans algorithm, matplotlib.pyplot for plotting graphs, numpy to work with arrays, cv2 to work with image data, collections to use Counter to count values, rgb2lab to convert RGB values and deltaE_cie76 to calculate similarity between colors

Using this application, one can input a valid location of an image and obtain the image in different filters.(The image location that we entered here was italy.jpg)

The application can also be used to plot the colours in an image into a pie chart with different colours plotted against their standard colour codes. 

Using this application, one can also input a valid location of an image folder and classify different images by colour.(The image folder that we entered here was nature)

To classify images based on their colours, we have created a dictionary COLORS and used the hexcodes of four basic/primary colurs: RED, BLUE, GREEN, YELLOW. We can also use other secondary colours by extracting their hexcodes. 
