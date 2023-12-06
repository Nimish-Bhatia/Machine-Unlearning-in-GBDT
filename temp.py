import os
import shutil
from sklearn.model_selection import train_test_split

def delete_files_with_extension_recursive(folder_path, target_extension):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(target_extension):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Specify the folder path
folder_path = './data/dog-breeds/'

# Specify the target extension to delete (in this case, "Zone.Identifier")
target_extension = 'Zone.Identifier'

# Call the function to delete files with the specified extension
delete_files_with_extension_recursive(folder_path, target_extension)

def train_test_split_per_class(class_folder, output_train_folder, output_test_folder, test_size=0.2, random_state=42):
    class_name = os.path.basename(class_folder)

    # List all images in the current class folder
    images = [f.path for f in os.scandir(class_folder) if f.is_file()]

    # Split the images into train and test sets
    train_images, test_images = train_test_split(images, test_size=test_size, random_state=random_state)

    # Create output folders if they don't exist
    os.makedirs(os.path.join(output_train_folder, class_name), exist_ok=True)
    os.makedirs(os.path.join(output_test_folder, class_name), exist_ok=True)

    # Copy the train images to the output train folder
    for train_image in train_images:
        shutil.copy(train_image, os.path.join(output_train_folder, class_name, os.path.basename(train_image)))

    # Copy the test images to the output test folder
    for test_image in test_images:
        shutil.copy(test_image, os.path.join(output_test_folder, class_name, os.path.basename(test_image)))

# Specify the main dataset folder
dataset_folder = './data/dog-breeds'

# Specify the output folders for the train and test sets
output_train_folder = './data/dog-train'
output_test_folder = './data/dog-test'

# Create the output folders if they don't exist
os.makedirs(output_train_folder, exist_ok=True)
os.makedirs(output_test_folder, exist_ok=True)

# List all class folders in the dataset
class_folders = [f.path for f in os.scandir(dataset_folder) if f.is_dir()]

# Perform train-test split for each class
for class_folder in class_folders:
    train_test_split_per_class(class_folder, output_train_folder, output_test_folder)