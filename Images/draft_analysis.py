
# Iris Dataset Project
# by Mariane McGrath

#=================================#
# Importing Libraries
#=================================#

# Use Pandas for data manipulation
import pandas as pd

# Use Scikit-learn for machine learning and accessing their databases
import sklearn as skl

from sklearn.datasets import load_iris

# We'll use NumPy for numerical operations
import numpy as np

# We'll use Matplotlib for plotting
import matplotlib.pyplot as plt

# and Seaborn for statistical data visualization
import seaborn as sns

#=================================#
# Loading the Iris Data set
#=================================#

# Now, we will load the iris dataset from the UCI Machine Learning Repository
# The dataset is available at the following URL
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# The dataset is in CSV format, so we will use pandas to read it.
# The dataset contains 5 columns: Sepal_Length, Sepal_Width, Petal_Length, Petal_Width, and Species  
iris_columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
iris_species = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

# And we'll convert the target to names of the species, as they are represented numerically
# The species are: Iris Setosa, Iris Versicolor, and Iris Virginica
# The dataset is in CSV format, so we will use pandas to read it.
# The dataset contains 5 columns: Sepal_Length, Sepal_Width, Petal_Length, Petal_Width, and Species
iris_df = pd.read_csv(csv_url, names = iris_columns)

# Loading the iris dataset
iris = load_iris()

# Below we can see the data
print (iris)

#===============================================================================
# Iris DataFrame
#===============================================================================

# Now, we'll take a look at the first and last 5 rows of the data in a nice way
print (iris_df)

#===============================================================================
# Iris data summary of the data and per species
#===============================================================================
# We'll take a look at the summary of the data
print (iris_df.describe())

# And we'll also take a look at the summary of the data grouped by species
describe_species = iris_df.groupby('Species').describe().transpose()

# Show the summary of the data grouped by species
print(describe_species)

#===============================================================================
# Iris Correlation Matrix
#===============================================================================

# Calculate correlation matrix for numerical columns
iris_corr = iris_df.corr(numeric_only=True, method='pearson')

# Display the correlation matrix
print(iris_corr)

#===============================================================================  
# Iris Histograms per Feature
#===============================================================================
# We have to plot a histogram for each feature
iris_df.hist(figsize=(12, 12), bins=12, color='lightblue', edgecolor='black')

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

#===============================================================================  
# Iris Feature Boxplots per Species
#===============================================================================

plt.figure(figsize=(12, 10))

# First plot (top left) - Sepal Length
plt.subplot(2, 2, 1)
sns.boxplot(x='Species', hue= 'Species', y='Sepal_Length', data=iris_df, palette='pastel')

plt.title('Sepal Length by Species')
plt.xlabel('')
plt.ylabel('Length (cm)')

# Second plot (top right) - Sepal Width
plt.subplot(2, 2, 2)
sns.boxplot(x='Species', hue= 'Species', y='Sepal_Width', data=iris_df, palette='pastel')
plt.title('Sepal Width by Species')
plt.xlabel('')
plt.ylabel('Width (cm)')

# Third plot (bottom left) - Petal Length
plt.subplot(2, 2, 3)
sns.boxplot(x='Species', hue= 'Species', y='Petal_Length', data=iris_df, palette='pastel')
plt.title('Petal Length by Species')
plt.xlabel('Flower Type')
plt.ylabel('Length (cm)')

# Fourth plot (bottom right) - Petal Width
plt.subplot(2, 2, 4)
sns.boxplot(x='Species', hue= 'Species', y='Petal_Width', data=iris_df, palette='pastel')
plt.title('Petal Width by Species')
plt.xlabel('Flower Type')
plt.ylabel('Width (cm)')

plt.savefig('iris_boxplots.png')  # Added bbox_inches to prevent cutoff
plt.tight_layout()
plt.show()

#===============================================================================  
# Iris Heatmaps per Features
#===============================================================================
# Create the heatmap
plt.imshow(iris_corr, cmap='coolwarm', interpolation='nearest')

# Add feature names as labels
plt.xticks(range(len(iris.feature_names)), iris.feature_names, rotation=45)
plt.yticks(range(len(iris.feature_names)), iris.feature_names)

# Add colorbar and title
plt.colorbar(label='Correlation level')
plt.title('Correlation Between Iris Features')

# Add text for each cell
for i in range(len(iris.feature_names)):
    for j in range(len(iris.feature_names)):
        plt.text(j, i, f'{iris_corr.iloc[i, j]:.2f}', ha='center', va='center', color='black')

# Save the heatmap as a PNG file
plt.savefig('iris_heatmap.png')

# Show the plot
plt.show()

#===============================================================================  
# Iris Heatmaps per Species
#===============================================================================  

iris_df['Species'] = iris.target  # Add the target column

# Map target numbers to species names for better readability
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
# Map the target numbers to species names
iris_df['Species'] = iris_df['Species'].map(species_names)
iris_corr = iris_df.corr(numeric_only=True, method='pearson')

# Option 1: Create separate correlation heatmaps for each species
for species in iris_df['Species'].unique():  
    species_df = iris_df[iris_df['Species'] == species].drop(columns=['Species'])
    iris_corr = species_df.corr(numeric_only=True, method='pearson')
    # Create a heatmap for the current species
    plt.figure(figsize=(6, 4))
    sns.heatmap(iris_corr, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f"Feature Correlations for {species.capitalize()}")
    # Save the heatmap as a PNG file
    plt.savefig(f'iris_heatmap_{species}.png')
    
    plt.tight_layout()
    plt.show()


#===============================================================================  
# Iris Scatterplot per Species
#===============================================================================  

iris_columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

# Create a figure with 1 row and 2 columns for side-by-side plots
plt.figure(figsize=(12, 6))

# First scatter plot (left)
plt.subplot(1, 2, 1)
sns.scatterplot(x='Petal_Length', y='Petal_Width', hue='Species', data=iris_df, palette='pastel')
plt.title('Petal Length vs Width by Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.grid()

# Second scatter plot (right)
plt.subplot(1, 2, 2)
sns.scatterplot(x='Sepal_Length', y='Sepal_Width', hue='Species', data=iris_df, palette='pastel')
plt.title('Sepal Length vs Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.grid()

# Save the scatter plots as a PNG file
plt.savefig('iris_scatter_plots.png')

plt.tight_layout()  # Adjust spacing between plots
plt.show()

#===============================================================================  
# Iris Pairplots
#===============================================================================      

# Create a pairplot with different markers and colors
sns.pairplot(iris_df, hue='Species', diag_kind='kde', markers=["o", "s", "D"], palette="pastel")

# Add titles and labels
plt.suptitle('Pairplot of Iris Dataset', y=1.02)

# Save the pairplot as a PNG file
plt.savefig('iris_pairplot.png')

# Show the plot
plt.show()

THE END