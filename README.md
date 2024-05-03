# Hazard Detection in Self-driving Vehicles
Link to presentation slides [here.](https://github.com/mattwyz/CS-766-Project/blob/main/Presentation_Slides.pdf)\
Link to Github repository [here.](https://github.com/mattwyz/CS-766-Project)

# Motivation and Problem Statement
Every year there are more electric and self driving vehicles on the roads, and an important part of these vehicles is ensuring the occupants and other drivers' safety.
A major part of this safety guarantee comes in the form of reliable hazard detection and taking possible preventative measures based on that data.
For our project we wanted to explore how this hazard detection can be completed through the means of computer vision using machine learning.\
\
We set out to make a simple model that could classify multiple different types of hazards from input images, and we later explored using an established model and a 
large dataset to achieve more hazard and road feature identification for both images and video inputs.
# Methodology
## Dataset and Preprocessing
For our project we used two different datasets for our individual classification and identification models.\
\
For our classification model we used a dataset found on [Kaggle](https://www.kaggle.com/datasets/virenbr11/pothole-and-plain-rode-images/data) which included 740
images of roads with and without potholes that were scraped from google. Before training, we removed the images that had poor quality or did not accurately match their corresponding labels.
Then we found and added around 100 images into the dataset in order to create a new class of hazard. When we had the images, we preprocessed them using Keras by resizing and scaling the images for ease of computing.\
\
For our indentification model, we used the [BDD100K](https://www.vis.xyz/bdd100k/) which includes 70,000 images for training, 10,000 images for validation, and 20,000 images for testing.
Then, using the [FiftyOne](https://docs.voxel51.com/) library, we converted the dataset to be compatible with the YOLO architechural model, which consisted of storing the coordinates of the images, along with other data
in a text file for each image.

## Model Architecture 
Classification 
The VGG16 architecture was developed by NK. Simonyan and A. Zisserman from the University of Oxford in 2014. It was described in their paper "Very Deep Convolutional Networks for Large-Scale Image Recognition." In the VGG16 architecture, images pass through sequential layers that include two convolutional layers followed by a max-pooling layer, continuing with more convolutions and pooling until reaching the fully connected layers. The convolutional layers primarily use small 3×3 filters, with a stride of 1 and padding to preserve spatial resolution, alongside 2×2 max-pooling layers with a stride of 2.

![](./VGG1.png)


# Results
## Classification 

## Detection (Yolov8)


# Demonstrations

https://drive.google.com/file/d/1IW957dk0qJjIovECwUIXdjqxlTxDkt-K/view?resourcekey

# References
