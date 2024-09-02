import os
import random
import shutil

# Directories
dataset_dir = os.path.join(os.path.dirname(__file__), 'Dataset', 'images')
train_dir = os.path.join(os.path.dirname(__file__), 'Processed_Dataset', 'Training_Dataset')
val_dir = os.path.join(os.path.dirname(__file__), 'Processed_Dataset', 'Validation_Dataset')
test_dir = os.path.join(os.path.dirname(__file__), 'Processed_Dataset', 'Test_Dataset')

# Create directories if they don't exist
for directory in [train_dir, val_dir, test_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Get all image filenames
image_filenames = [f for f in os.listdir(dataset_dir) if f.endswith('.png')]

# Shuffle the images
random.shuffle(image_filenames)

# Calculate the number of images for each set
num_images = len(image_filenames)
train_size = int(0.70 * num_images)
val_size = int(0.10 * num_images)
test_size = num_images - train_size - val_size

# Split the images
train_images = image_filenames[:train_size]
val_images = image_filenames[train_size:train_size + val_size]
test_images = image_filenames[train_size + val_size:]

# Function to copy images to respective directories
def copy_images(images, source_dir, target_dir):
    for image in images:
        source_path = os.path.join(source_dir, image)
        target_path = os.path.join(target_dir, image)
        shutil.copyfile(source_path, target_path)

# Copy images to train, val, and test directories
copy_images(train_images, dataset_dir, train_dir)
copy_images(val_images, dataset_dir, val_dir)
copy_images(test_images, dataset_dir, test_dir)

print("Dataset split completed.")
