# Visio_DPPT (Visio_Data Pre-Processing Tools)

## The following branches are the modified pre-processing tools used by VisioAccelerAI.
VisioAccelerAI is a capstone project. Its main goal is to deploy a facial recognition system on an FPGA board to enhance the computational capability of the model for a real-time attendance monitoring system. This repository contains the tools used to prepare datasets before training the model that will be deployed on the FPGA.

## Cloning certain branches:
- Install Git in your machine.
- In your terminal (cmd, powershell, Git Bash *recommended) put this command:
- git clone -b "name of the branch" https://github.com/Ze-r000/Visio_DPPT.git
- Just follow the steps from the README section of each branches.

## IMPORTANT!
- Install Anaconda for Windows/Ubuntu/Linux, it depends on what machine did you use for Data Augmentation. It is important to segregate Python libraries for specific use, that's why we use this Anaconda.
- https://www.anaconda.com/download

## After Installation 
- I recommend to integrate your Git Bash terminal to your Anaconda environment to be default. I prefer to use Git Bash all the time for managing Python environment.
- Instruction: https://kshitijkutumbe.medium.com/configuring-git-bash-with-anaconda-for-enhanced-data-science-workflow-bae60db2eeb1
  
# Visio_Augmentor
- This branch is used to augment the collected data using the Python library 'Augmentor.' Feel free to explore the other functions of this library. For now, script.py is used to augment several datasets for the project and follow the steps in the main branch of the Visio_Augmentor.

# Visio_Labelling-Automation
- This branch is used to automate the annotation process compared to manual labeling. It can also be used to automatically label the collected data from the images you currently have. Please follow the steps in the Visio_Labelling-Automation branch. 

# Visio_Dataset-Splitter
- This branch is used to split the datasets to train, test, validation. Follow the steps in the Visio_Dataset-Splitter branch.

##### Working as of 02/06/24
