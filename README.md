# IMPORTANT!
- Install Anaconda for Windows/Ubuntu/Linux, it depends on where you deploy the model. it is important to segregate python libraries for specific use.
- https://www.anaconda.com/download

# After Installation 
- I recommend to integrate your Git Bash terminal to your Anaconda environment to be default. I prefer to use Git Bash all the time for managing Python environment.
- Instruction: https://kshitijkutumbe.medium.com/configuring-git-bash-with-anaconda-for-enhanced-data-science-workflow-bae60db2eeb1
  
# Create Virtual Environment in Anaconda (Git Terminal)
- conda create --name Visio_Augmentor python=3.9.18
- conda activate Visio_Augmentor

# Install Dependencies
- cd Augmentor
- python setup.py

# Now! You're ready to augment your data
- Feel free to explore the functions of the Python 'Augmentor' library, which offers a wide range of features to augment your data.
- Change the location of your images and the output number of the images.
- python script.py --loc "put_the_location_of_the_images" --num "put_the_output_numbers_of_the_images"
