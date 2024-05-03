# Hazard Detection in Self-driving Vehicles
Link to presentation slides [here.](https://github.com/mattwyz/CS-766-Project/blob/main/Presentation_Slides.pdf)\
Link to Github repository [here.](https://github.com/mattwyz/CS-766-Project)

# Motivation and Problem Statement
Every year there are more electric and self driving vehicles on the roads, and an important part of these vehicles is ensuring the occupants and other drivers' safety.
A major part of this safety guarantee comes in the form of reliable hazard detection and taking possible preventative measures based on that data.
For our project we wanted to explore how this hazard detection can be completed through the means of computer vision using machine learning.\
\
We set out to make a simple model that could detect multiple different types of hazards from input images, and we later explored using an established model and a 
large dataset to achieve more hazard and road feature identification for both images and video inputs.
# Methodology
## Dataset and Preprocessing
For our project we used two different datasets for our individual detection and identification models.\
\
For our classification model we used a dataset found on [Kaggle](https://www.kaggle.com/datasets/virenbr11/pothole-and-plain-rode-images/data) which included 740
images of roads with and without potholes that were scraped from google. Before training, we removed the images that had poor quality or did not accurately match their corresponding labels.
Then we found and added around 100 images into the dataset in order to create a new class of hazard. When we had the images, we preprocessed them using Keras by resizing and scaling the images for ease of computing.

# Results
## Classification 

## Detection (Yolov8)


# Demonstrations

[Watch the video](https://drive.google.com/file/d/1IW957dk0qJjIovECwUIXdjqxlTxDkt-K/view?usp=drive_link)
