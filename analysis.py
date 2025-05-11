# Iris Dataset Project
# by Mariane McGrath

# Analysis of the Iris Data set - This script performs Exploratory data analysis (EDA) on the Iris dataset.

#===============================================================================
#  Importing Libraries
#===============================================================================

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

#===============================================================================
#  Loading the Iris Data set
#===============================================================================

# Now, we will load the iris dataset from Sklearn and convert it into a Pandas DataFrame
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['Species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

#===============================================================================
# Iris DataFrame
#===============================================================================

# Now, we'll take a look at the first and last 5 rows of the data in a nice way
# Below we can see the data
print (iris)

#------------------------
# Data Overview
#------------------------
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
# Iris Data Summary 
# ===============================================================================       

# We'll take a look at the summary of the data
print (iris_df.describe())

# And we'll also take a look at the summary of the data grouped by species
describe_species = iris_df.groupby('Species').describe().transpose()

#===============================================================================
# Iris Data Summary Text File
#===============================================================================       

summary_path = "iris_analysis_summary.txt"

# 1. Overall summary
overall_summary = iris_df.describe()

# 2. Per-species summary
species_summary = iris_df.groupby("Species").describe().T

# 3. Overall correlation matrix
overall_corr = iris_df.drop("Species", axis=1).corr(method="pearson")

# 4. Per-species correlation matrices
per_species_corr = {}
for species in iris_df['Species'].unique():
    sub_df = iris_df[iris_df['Species'] == species].drop("Species", axis=1)
    per_species_corr[species] = sub_df.corr(method="pearson")

# ------------------------
# Write to Text File
# ------------------------

with open(summary_path, "w") as f:
    f.write("Iris Dataset Analysis Summary\n")
    f.write("=" * 40 + "\n\n")

    # Overall summary
    f.write("1. Overall Summary Statistics\n")
    f.write("-" * 35 + "\n")
    f.write(overall_summary.to_string())
    f.write("\n\n")

    # Per-species summary
    f.write("2. Summary Statistics by Species\n")
    f.write("-" * 35 + "\n")
    f.write(species_summary.to_string())
    f.write("\n\n")

    # Overall correlation
    f.write("3. Correlation Matrix (All Species Combined)\n")
    f.write("-" * 35 + "\n")
    f.write(overall_corr.to_string())
    f.write("\n\n")

    # Per-species correlation
    f.write("4. Correlation Matrices by Species\n")
    f.write("-" * 35 + "\n")
    for species, corr in per_species_corr.items():
        f.write(f"\n{species.capitalize()}:\n")
        f.write(corr.to_string())
        f.write("\n")

print(f"Full analysis written to '{summary_path}'")

#===============================================================================  
# Iris Histograms per Feature
#===============================================================================

# We have to plot a histogram for each feature
# We'll set the style of the plot, including the colour, sixe and how many bins (bars)
iris_df.hist(figsize=(12, 12), bins=12, color='lightblue', edgecolor='black')

# Now we'll add a title
plt.suptitle('Histogram of Features')

# then we'll add a title to the x-axis
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

# We start by creating a figure, and set the size to 12 by 10
plt.figure(figsize=(12, 10))

# Then, we'll loop through each feature in the iris dataset (sepal length, sepal width, etc.). 'enumerate' helps us keep track of which plot
# we're on (i=0 for first, i=1 for second, etc.)
for i, col in enumerate(iris.feature_names):
    # We will create a subplot in a grid(2 rows, 2 columns)
    plt.subplot(2, 2, i+1)
    # For the current feature, using the 'Species' column to group the data
    # The 'palette' selection keeps the colour similar throughout the project
    sns.boxplot(data=iris_df, x='Species', y=col, palette='pastel')
    
    # Let's add a title to each plot
    plt.title(f"{col} by Species")
    # We will the x-axis label, because it would just say "Species" too many times
    plt.xlabel('')
        # And then add "cm" to the y-axis since all measurements are in centimeters
    plt.ylabel('cm')

# Now, we'll add some the spacing between plots, so they don't overlap
plt.tight_layout()

# Save boxplots as a PNG image file
plt.savefig('iris_boxplots.png', bbox_inches='tight')  # bbox_inches prevents cutting off labels

# Let's show them plots
plt.show()

#===============================================================================  
# Iris Heatmaps per Features
#===============================================================================

# We will create a heatmap to show how iris features relate to each other
# 'coolwarm' makes high values red (warm) and low values blue (cool) - Chose this instead of Pastel as it was too confusing to read
plt.imshow(iris_corr, cmap='coolwarm', interpolation='nearest')

# We'll add the feature names to the x and y axes
# and a rotation of 45 degree' tilts so the labels don't overlap
plt.xticks(range(len(iris.feature_names)), iris.feature_names, rotation=45)
plt.yticks(range(len(iris.feature_names)), iris.feature_names)

# Then, we'll add a color bar to show what the colors mean
# The label shows us correlation strength
plt.colorbar(label='Correlation level')

# We will give our heatmap a title
plt.title('Correlation Between Iris Features')

# And, we'll add the correlation numbers to each box in the heatmap, to make it easier to read
# The :.2f means we'll show just 2 decimal places
for i in range(len(iris.feature_names)):
    for j in range(len(iris.feature_names)):
        plt.text(j, i, f'{iris_corr.iloc[i, j]:.2f}', 
                ha='center', va='center', color='black')

# Save the heatmap as a PNG image file
plt.savefig('iris_heatmap.png', bbox_inches='tight')  # bbox_inches prevents cutting off

# Finally, let's show the heatmap
plt.show()

#===============================================================================  
# Iris Scatterplot per Species
#===============================================================================  

# First, we will create a canvas for our plots, 12x6
plt.figure(figsize=(12, 6))

# FIRST PLOT (LEFT SIDE): PETAL MEASUREMENTS
# We will want the first of two side-by-side plots
# Below we establish how we want it to loo, the first plot will be on the 1st row, of 2 columns, position 1
plt.subplot(1, 2, 1)                
# Then, we will create a scatterplot of petal length vs width.
sns.scatterplot(data=iris_df, x='petal length (cm)', y='petal width (cm)', hue='Species', palette='pastel')
# Add add a title the plot
plt.title('Petal Length vs Width by Species')
# And add labels to our axes 
plt.xlabel('Petal Length (cm)')   
plt.ylabel('Petal Width (cm)')   
# We'll add grid lines to make it easier to read the values
plt.grid()

# SECOND PLOT (RIGHT SIDE): SEPAL MEASUREMENTS
# Now we'll make the second plot (position 2)
plt.subplot(1, 2, 2)
# This scatterplot will show sepal measurements instead of petals
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='Species', palette='pastel')
# Let's add similar labels for this plot
plt.title('Sepal Length vs Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.grid()

# We will adjust spacing to avoid overlap
plt.tight_layout()

# Then we'll save the scatter plots as a PNG image file
# bbox_inches makes sure all labels are visible
plt.savefig('iris_scatterplots.png', bbox_inches='tight')  

# Finally, we show the plots
plt.show()

#===============================================================================  
# Iris Pairplots
#===============================================================================      

# We will create pairplot, to show us all possible relationships between features
# Using seaborn's pairplot function, and setting the hue to 'Species' to colour the points by species
# diag_kind='kde' makes the diagonal plots show kernel density estimates
# markers=["o", "s", "D"] sets different markers for each species
sns.pairplot(iris_df, hue='Species', diag_kind='kde', markers=["o", "s", "D"], palette="pastel")

# We will add a big title at the top of our pairplot, and adding y=1.02 moves the title up so it doesn't overlap
plt.suptitle('Pairplot of Iris Dataset', y=1.02)

# Then, we'll save the pairplot as a PNG file
plt.savefig('iris_pairplot.png')

# Finally, we'll show the plot
plt.show()

#===============================================================================
# Please note that the references to all the code used througout this project is listed directly on the Jupyter Notebook and the ReadMe file.
#===============================================================================