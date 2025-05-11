# Project: Analysis of the Iris Dataset 
Author: Mariane McGrath

# **Overview**

This project explores the **Iris Dataset**, one of the most well-known datasets in machine learning and statistics. It includes Python-based data exploration, visualisation, and statistical analysis of the dataset's features, offering insights into class separability and relationships between variables. 

My Jupyter Notebook (analysis.ipynb) includes statistical summaries, visualisations, and correlation analyses.

# **Problem Statement**

 - Research the data set
 - Write documentation and code in Python to investigate it

**The project includes the following:**
 - Dataset research was done online and summarised in the README.
 - A download of the dataset to the repository
 - A program called "analysis.py" that:
     1. Outputs a summary of each variable to a single text file.
     2. Saves a histogram of each variable to .png files.
     3. Outputs a scatterplot of each pair of variables.
     4. Performs any other analysis the author finds appropriate.

 - Source: https://vlegalwaymayo.atu.ie/pluginfile.php/1496518/mod_label/intro/Project%202025.pdf?time=1744985662891

## Objectives

1. Load and explore the Iris dataset to understand its structure and features.
2. Visualise the data to identify patterns, relationships, and class separability.

# Software Utilised
 - Python
 - Jupyter Notebook
 - Pandas
 - NumPy
 - Matplotlib
 - Seaborn
 - Scikit-learn
 - VSCode
 - cmder

### How to run

1. Clone the repository from GitHub.
2. Navigate to the project directory.
 - **git clone** https://github.com/marianemcgrath/pands_project.git
 - **cd pands_project**

**Repository:** [pands_project](https://github.com/marianemcgrath/pands_project)
**Notebook:** [`analysis.ipynb`](https://github.com/marianemcgrath/pands_project/blob/main/analysis.ipynb)

3. For the Python code used in this project, without mark-up cells, execute `analysis.py` using your preferred Python environment (e.g. VS Code).
 - The code will perform the following actions:
   a. Outputs the data summary to a text (.txt) file
   b. Saves images into (.png) files
   
# About the Iris Dataset

The Iris Dataset was introduced by the British statistician Ronald Fisher in 1936, and it is considered an essential resource in statistics and machine learning.

Comprising measurements of **sepal length, sepal width, petal length, and petal width** from 150 iris flowers—50 each from three distinct species: **Iris setosa, Iris versicolor, and Iris virginica**.

![alt text](https://miro.medium.com/v2/resize:fit:720/format:webp/0*11IwZmSKXw77eYz5)

Fisher used this dataset to illustrate linear discriminant analysis (LDA), a method for classifying data based on various input features. The clear distinctions among the classes in the Iris Dataset make it suitable for demonstrating how simple statistical models can be used to classify data effectively.

The Iris Dataset continues to be used for educational purposes in machine learning, benchmarking algorithms, and visualising analytical techniques such as principal component analysis (PCA) and clustering. Its clear and versatile nature makes it a key resource in data science education.

 - Source: https://www.geeksforgeeks.org/iris-dataset/(About the Iris Dataset)
 - Source: https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c(Exploring the Iris Dataset)
 - Source: https://www.ibm.com/think/topics/linear-discriminant-analysis#:~:text=Linear%20discriminant%20analysis%20(LDA)%20is,helps%20optimize%20machine%20learning%20models (About Linear Discriminant Analysis)
 - Source: https://www.statisticssolutions.com/discriminant-analysis/#:~:text=Discriminant%20analysis%20aims%20to%20create,terms%20of%20the%20predictor%20variables ((About Linear Discriminant Analysis)
 
## Investigation of the dataset

**Part I - Data loading, summary and statistical analysis**

1. Data Loading and Initial Exploration
 - Loads the Iris dataset from scikit-learn
 - Converts it to a pandas DataFrame
 - Adds the species names as a categorical column
 - Prints the raw data and DataFrame for initial inspection

2. Statistical Analysis
 - Generates descriptive statistics for all features (describe())
 - Provides species-specific statistics by grouping data by species
 - Calculates correlation matrices:
   a. Overall correlation between features
   b. Species-specific correlations

**Part II - Data Visualisation**

3. The script produces several high-quality visualisations:
   
   a. Histograms - For all four features (sepal length/width, petal length/width)
   
   b. Boxplots - Feature-specific boxplots grouped by species
   
   c. Heatmap - Visualises feature correlations
   
   d. Scatterplots - for Petal length vs. width, and Sepal length vs. width
   
   e. Pairplot - To investigate feature relationships
   
4. The Findings:

**Data Overview**
 - The dataset contains 150 samples of iris flowers, each with four features (sepal length, sepal width, petal length, petal width) and a target species (setosa, versicolor, virginica).
 - All features are numerical (measured in cm).

**Descriptive Statistics**
**Overall Summary:**

 - Sepal length ranges from 4.3 to 7.9 cm (mean: 5.84 cm).
   
 - Sepal width ranges from 2.0 to 4.4 cm (mean: 3.05 cm).
   
 - Petal length ranges from 1.0 to 6.9 cm (mean: 3.76 cm).
   
 - Petal width ranges from 0.1 to 2.5 cm (mean: 1.20 cm).

 By Species:
 
 - Setosa: Distinctly smaller petals (mean length: 1.46 cm, width: 0.24 cm) but wider sepals (mean width: 3.42 cm).
   
 - Versicolor: Intermediate measurements (e.g., petal length: 4.26 cm, width: 1.33 cm).
   
 - Virginica: Largest petals (mean length: 5.55 cm, width: 2.03 cm) and longest sepals (mean length: 6.59 cm).

**Correlation Analysis**
**Overall Correlation:**

 - Petal length and width are highly correlated (0.96).
   
 - Sepal length is moderately correlated with petal dimensions (~0.87 with petal length, 0.82 with petal width).
   
 - Sepal width shows weak or negative correlations with other features (-0.37 with petal length).

By Species:

 - Correlations vary by species. For example, in setosa, sepal width and length are positively correlated (0.74), whereas in virginica, the correlation is weaker (0.46).

**Visualisations**
 - Histograms: All features except sepal width are roughly normally distributed. Sepal width shows a slight bimodal distribution.
   
 - Boxplots: a. Setosa has distinctly smaller petals and wider sepals than the other species.
   
             b. Virginica has the largest petals and longest sepals, with some overlap with versicolor.

 - Scatterplots: a. Petal dimensions separate setosa from the other two species, with versicolor and virginica showing some overlap.

                 b.Sepal dimensions show more overlap between species, though setosa tends to have wider sepals.

 - Pairplot: Reinforces that petal measurements are better discriminators between species than sepal measurements.
   
 - Heatmap: Visually confirms the strong correlation between petal length/width and the weak correlation involving sepal width.

**Key Insights**

 - Species Differentiation: Petal features are more effective than sepal features for distinguishing species, especially setosa.

 - Outliers: Few outliers exist (e.g., one virginica sample has a notably small petal width).

 - Measurement Patterns: Virginica tends to be larger overall, while setosa is compact with small petals and wide sepals.
   
# **References**
Including markup cells and code development.

**Introduction**

**Part 1**

**Part 2**

