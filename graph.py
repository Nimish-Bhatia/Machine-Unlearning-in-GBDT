import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Coffee Bean dataset
# Open testlog and unlearnlog files
with open('./logs/coffee_bean_images_80.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
original_error = pd.DataFrame(data)
with open('./logs/coffee_bean_images_80.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
unlearn_error = pd.DataFrame(data)

# Errors for both models
errors_original = original_error[2].to_numpy().astype(int)
errors_unlearn = unlearn_error[2].to_numpy().astype(int)
x_values = np.arange(1, len(original_error) + 1)

# Plot the graph for errors in both models
plt.plot(x_values, errors_original,  linestyle='solid', color='r', label='Original Model')
plt.plot(x_values, errors_unlearn, linestyle='solid', color='b', label='Unlearned Model')
plt.xlabel('Iterations')
plt.ylabel('Errors')
# Add labels and title
plt.title('Coffee Bean Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_coffee_bean.png') 
plt.close()

# Dog dataset
# Open testlog and unlearnlog files
with open('./logs/dog_image_85.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
original_error = pd.DataFrame(data)
with open('./logs/dog_image_85.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
unlearn_error = pd.DataFrame(data)

# Errors for both models
errors_original = original_error[2].to_numpy().astype(int)
errors_unlearn = unlearn_error[2].to_numpy().astype(int)
x_values = np.arange(1, len(original_error) + 1)

# Plot the graph for errors in both models
plt.plot(x_values, errors_original,  linestyle='solid', color='r', label='Original Model')
plt.plot(x_values, errors_unlearn, linestyle='solid', color='b', label='Unlearned Model')
plt.xlabel('Iterations')
plt.ylabel('Errors')
# Add labels and title
plt.title('Dog Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_dog.png') 
plt.close()

# Flower dataset
# Open testlog and unlearnlog files
with open('./logs/flower_photos_80.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
original_error = pd.DataFrame(data)
with open('./logs/flower_photos_80.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
unlearn_error = pd.DataFrame(data)

# Errors for both models
errors_original = original_error[2].to_numpy().astype(int)
errors_unlearn = unlearn_error[2].to_numpy().astype(int)
x_values = np.arange(1, len(original_error) + 1)

# Plot the graph for errors in both models
plt.plot(x_values, errors_original,  linestyle='solid', color='r', label='Original Model')
plt.plot(x_values, errors_unlearn, linestyle='solid', color='b', label='Unlearned Model')
plt.xlabel('Iterations')
plt.ylabel('Errors')
# Add labels and title
plt.title('Flower Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_flower.png') 
plt.close()

# Intel dataset
# Open testlog and unlearnlog files
with open('./logs/intel_image_80.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
original_error = pd.DataFrame(data)
with open('./logs/intel_image_80.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
unlearn_error = pd.DataFrame(data)

# Errors for both models
errors_original = original_error[2].to_numpy().astype(int)
errors_unlearn = unlearn_error[2].to_numpy().astype(int)
x_values = np.arange(1, len(original_error) + 1)

# Plot the graph for errors in both models
plt.plot(x_values, errors_original,  linestyle='solid', color='r', label='Original Model')
plt.plot(x_values, errors_unlearn, linestyle='solid', color='b', label='Unlearned Model')
plt.xlabel('Iterations')
plt.ylabel('Errors')
# Add labels and title
plt.title('Intel Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_intel.png') 
plt.close()

# Vehicle dataset
# Open testlog and unlearnlog files
with open('./logs/vehicle_image_72.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
original_error = pd.DataFrame(data)
with open('./logs/vehicle_image_72.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
unlearn_error = pd.DataFrame(data)

# Errors for both models
errors_original = original_error[2].to_numpy().astype(int)
errors_unlearn = unlearn_error[2].to_numpy().astype(int)
x_values = np.arange(1, len(original_error) + 1)

# Plot the graph for errors in both models
plt.plot(x_values, errors_original,  linestyle='solid', color='r', label='Original Model')
plt.plot(x_values, errors_unlearn, linestyle='solid', color='b', label='Unlearned Model')
plt.xlabel('Iterations')
plt.ylabel('Errors')
# Add labels and title
plt.title('Vehicle Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_vehicle.png') 
plt.close()