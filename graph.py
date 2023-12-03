import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Read the .testlog file into a list of lines
with open('optdigits.test.csv_mart_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()

# Split each line into columns based on the delimiter
data = [re.split(r'\s+', line.strip()) for line in lines]

# Create a DataFrame using pandas
mart = pd.DataFrame(data)

with open('optdigits.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()

# Split each line into columns based on the delimiter
data = [re.split(r'\s+', line.strip()) for line in lines]

# Create a DataFrame using pandas
robustlogit = pd.DataFrame(data)


# Errors for both method
errors_mart=mart[2].to_numpy().astype(int)
errors_robustlogit=robustlogit[2].to_numpy().astype(int)




x_values = np.arange(1, len(errors_mart) + 1)

# Plot the graph
plt.plot(x_values, errors_mart,  linestyle='-', color='b', label='MART')
plt.plot(x_values, errors_robustlogit, linestyle='-', color='r', label='Robust LogitBoost')
# Add labels and title
plt.xlabel('Iterations')
plt.ylabel('Errors')
plt.title('Graph of Iterations vs Error')


# Add legend
plt.legend()

# Show the plot
plt.savefig('graph.png') 
# plt.show()


