# Use Pandas for data manipulation
import pandas as pd
# Use Scikit-learn for machine learning and accessing their databases
import sklearn as skl
# We'll use NumPy for numerical operations
import numpy as np
# We'll use Matplotlib for plotting
import matplotlib.pyplot as plt
# and Seaborn for statistical data visualization
import seaborn as sns

#================================#
# Iris Dataset Analysis
#================================#
# Loading the iris dataset

# We'll use the iris dataset from sklearn
from sklearn.datasets import load_iris

# Loading the iris dataset
iris_data = load_iris()

# Converting the iris dataset to a pandas DataFrame with your column names
iris_df = pd.DataFrame(data=iris_data.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

# Adding the target variable to the DataFrame
iris_df['Species'] = iris_data.target_names[iris_data.target]

# Now let's create our summary file
with open('iris_summary.txt', 'w') as file:
    
    # Write a title
    file.write("=== Iris Flower Summary ===\n\n")
    
    # Basic information about the dataset
    file.write(f"This dataset contains {len(iris_df)} flower measurements.\n")
    file.write("There are three species of iris flowers:\n")
    for species in iris_df['Species'].unique():
        file.write(f"- {species}\n")
    file.write("\n")
    
    # Summary for each measurement
    file.write("Measurement Summaries:\n\n")
    
    measurements = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
    
    for measure in measurements:
        file.write(f"{measure} (in cm):\n")
        file.write(f"  Shortest: {iris_df[measure].min():.1f}\n")
        file.write(f"  Average: {iris_df[measure].mean():.1f}\n")
        file.write(f"  Longest: {iris_df[measure].max():.1f}\n")
        file.write("\n")
    
    # Count of each flower type
    file.write("Number of each flower type:\n")
    species_counts = iris_df['Species'].value_counts()
    for species, count in species_counts.items():
        file.write(f"- {species}: {count} flowers\n")
    file.write("\n")
    
    # Finish the file
    file.write("End of summary.")

print("Summary created successfully in 'iris_summary.txt'")

# Source: https://www.w3schools.com/python/pandas/ref_df_describe.asp

# We'll take a look at the summary of the data
print (iris_df.describe())

# Source: https://www.w3schools.com/python/pandas/ref_df_describe.asp

#=============================================#
# Histograms of each variable
#=============================================#

# We have to plot a histogram for each feature
iris.hist(figsize=(10, 10), bins=10, color='lightblue', edgecolor='black')

# Now we'll add a title
plt.suptitle('Histogram of Features')

# We'll add a title to the x-axis
plt.xlabel('Features')

# We'll add a title to the y-axis
plt.ylabel('Frequency')

# Showing the plot
plt.show()

# Source: https://flexiple.com/python/exploratory-data-analysis-on-iris-dataset#:~:text=2.%20Relation%20between%20Variables (Plotting a histogram in Python)

#=============================================#
# Scatterplot of each variable
#=============================================#

# Create a figure with 1 row and 2 columns for side-by-side plots
plt.figure(figsize=(12, 6))

# First scatter plot (left)
plt.subplot(1, 2, 1)
# Scatter plot for petal length vs petal width with different colors for each species
sns.scatterplot(x='petal length (cm)', y='petal width (cm)', hue='species', data=iris, palette='pastel')
# Add title and labels
plt.title('Petal Length vs Width by Species')
# Add labels for x and y axes
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
# Add grid for better readability
plt.grid()

# Second scatter plot (right)
plt.subplot(1, 2, 2)
# Scatter plot for sepal length vs sepal width with different colors for each species, using the same palette
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=iris, palette='pastel')
# Add title and labels
plt.title('Sepal Length vs Width by Species')
# Add labels for x and y axes
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
# Add grid for better readability
plt.grid()

# Show the plots
plt.tight_layout()  # Adjust spacing between plots
plt.show()

#=============================================#
# Statistics description to each variable
#=============================================#
# We'll take a look at the summary of the data
print(iris.describe())

# And we'll also take a look at the summary of the data grouped by species
describe_species = iris.groupby('Species').describe().transpose()

# Display the summary of the data grouped by species
print (describe_species)

# We have to plot a histogram for each feature
df.hist(figsize=(12, 12), bins=12, color='lightblue', edgecolor='black')

# Now we'll add a title
plt.suptitle('Histogram of Features')

# We'll add a title to the x-axis
plt.xlabel('Features')

# We'll add a title to the y-axis
plt.ylabel('Frequency')

# Save the histogram as a PNG file
plt.savefig('iris_histogram_features.png')

# Showing the plot
plt.show()



#=============================================#
# Pairplot of each variable
#=============================================#

# Add target names to the DataFrame
iris['target_name'] = [iris.target_names[i] for i in iris.target]
# Create a pairplot with different markers and colors
sns.pairplot(iris, hue='target_name', diag_kind='kde', markers=["o", "s", "D"], palette="pastel")
# Add titles and labels
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
# Show the plot
plt.show()

# Source: https://www.youtube.com/watch?v=dlFScQLOtoY (Iris Classification (Part 1) | Data Analysis and Exploration)
# Source: https://www.youtube.com/watch?v=JGWqb5nNudE (Data Visualisation - Iris Dataset)
# Source: https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#:~:text=feature_names%27%2C%20%27filename%27%2C%20%27data_module%27%5D)-,Plot%20of%20pairs%20of%20features%20of%20the%20Iris%20dataset,-%23