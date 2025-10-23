# Basic-Xray-Edge-Detection

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Results](#results)
- [Structure](#structure)

## Overview
The goal of this project is to create a functional program that lets users upload medical imaging files that are then analyzed and reproduced with highlighted edges. Throughout the project, I hope to gain more practical experience in digital image processing and apply concepts and algorithms learned in my classes.

## Tech Stack
- Python 3.11
- opencv
- tkinter
- PIL

## Usage
Simply upload an image file to see a side-by-side comparison of the original and processed images. You can also use the two sliders to change the minimum and maximum threshold values for the edge-detection algorithm. It is important to note that the same parameters will not always work the best for different images. When you are satisfied with your processed image, you can save the file onto your machine. 

## Results
Although the edge detection algorithm isn't robust and certainly doesn't meet industry standards by any means, it still serves its purpose as a basic edge detection program that lets you upload and save files. Upon completing the first version of this program, I can say I've learned a lot about the how the Canny edge detection algorithm works. I didn't implement it from scratch but I read up about the steps within the algorithm like noise reduction using a Gaussian blur function, gradient calculation, thresholding, etc. This definitely reinforced by understanding of how image processing worked mathematically and in the future, I would like to dive deeper into implementing an algorithm from scratch. Additionally, I was able to gain valuable experience creating a GUI using the tkinter library which is a skill that I will continute to utilize and improve in future projects.

## Structure
I start off by defining a default window size of 1200x600 for the app. I've writen all my functions used in the program towards the top of the file so we can easily see what is happening behind the scenes. For instance, there are a few methods dedicated just to make sure that the scaling of the images and the Canny thresholds are updated in realtime based on the window size and the slider positions, respectively. After defining all my functions, I create a frame and divide it vertically into two equally-sized grids that will contain their respective images. The left side contains the original image and the right side contains the processed image. The rest of the code defines and packs the labels, sliders, and buttons you see in the program.