import os
import shutil
import random

# Define the paths
source_folder = "User Name"
test_folder = "test"
train_folder = "train"
validation_folder = "validation"

# Define the number of images for each category, this is the default that used in VisioAccelerAI
num_test_images = 20
num_train_images = 180
num_validation_images = 50

# List all image files in the source folder
image_files = [f for f in os.listdir(source_folder) if f.endswith(".jpg")]

# Shuffle the list to randomize the selection
random.shuffle(image_files)

# Copy images to test folder
for img in image_files[:num_test_images]:
    img_path = os.path.join(source_folder, img)
    xml_path = os.path.join(source_folder, img.replace(".jpg", ".xml"))
    shutil.copy(img_path, test_folder)
    shutil.copy(xml_path, test_folder)

# Copy images to train folder
for img in image_files[num_test_images:num_test_images+num_train_images]:
    img_path = os.path.join(source_folder, img)
    xml_path = os.path.join(source_folder, img.replace(".jpg", ".xml"))
    shutil.copy(img_path, train_folder)
    shutil.copy(xml_path, train_folder)

# Copy images to validation folder
for img in image_files[num_test_images+num_train_images:num_test_images+num_train_images+num_validation_images]:
    img_path = os.path.join(source_folder, img)
    xml_path = os.path.join(source_folder, img.replace(".jpg", ".xml"))
    shutil.copy(img_path, validation_folder)
    shutil.copy(xml_path, validation_folder)
