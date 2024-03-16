import os
import cv2
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_images_from_folder(folder):
    images = []
    labels = []
    for class_folder in os.listdir(folder):
        class_path = os.path.join(folder, class_folder)
        if os.path.isdir(class_path):
            for filename in os.listdir(class_path):
                img_path = os.path.join(class_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    images.append(img)
                    labels.append(class_folder)  # Use class folder name as label

    # Convert string labels to integer labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)

    return images, labels

# Assuming you have a 'training' folder with subfolders for each class
training_folder = './flower_photos/train'
images, lbls = load_images_from_folder(training_folder)

# Feature extraction using PCA to limit the number of features
num_features = 80  # Specify the desired number of features
pca = PCA(n_components=num_features)

# Assuming 'images' is a list of images
features = []
for img in images:
    img = cv2.resize(img, (224, 224))  # Adjust size if needed
    img = img.flatten()  # Flatten the image
    features.append(img)

# Apply PCA
features = pca.fit_transform(features)

# Normalize feature vectors using StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Create a DataFrame with features and labels
columns = [f'feature_{i}' for i in range(num_features)]
df = pd.DataFrame(features, columns=columns)
df['label'] = lbls  # Add labels column

# Reorder columns to place 'label' at the 0th column
df = df[['label'] + columns]

# Save DataFrame to CSV
df.to_csv('./data/flower_photos_80.test.csv', index=False)
