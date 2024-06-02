# Visio_Automation-of-Labeling (Version-2)
- This branch is used to automate the annotation process compared to manual labeling. It can also be used to automatically label the collected data from the images you currently have. Please follow the steps in the Visio_Labelling-Automation branch. 

# Create Virtual Environment in Anaconda (Git Terminal)
- conda create --name Visio_Labeling python=3.6
- conda activate Visio_Labeling

# Installing Dependencies
- pip install -r requirements.txt

# Now! You're Ready to Label your Datasets.
- Follow the steps depends on your purpose.
  
## For Real-Time Data Gathering with Automation Labeling
- Note: This script is used to gather data in real time using your webcam, at the same time it automates your labeling process.
- python caffe_face_detection_webcam_no_time.py --name "your_name_here"

## For Images only 
- Note: Don't execute this, this command is only used after the data augmentation process.
- python caffe_face_detection_multiple-images.py --name "your_name_here" --images "path/of/your/images"

## For Video only
- Note: This script is used for mp4 video.
- python caffe_face_detection_video.py --name "your_name_here" --video "path/of/your/video.mp4"

# Termination
- press "q" 
