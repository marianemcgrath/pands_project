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

Source: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html (About the load.iris() function)
Source: https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset (Converting Dataset)
Source: https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python (load_iris() in Python)
Source: https://www.geeksforgeeks.org/display-the-pandas-dataframe-in-table-style/ (Display function)
Source: https://www.analyticsvidhya.com/blog/2023/07/head-and-tail-functions/ (Head () and Tail () Functions Explained with Examples and Codes)
Source: https://www.datacamp.com/tutorial/python-dataframe-size (Python DataFrame Size)
Source: https://www.ucd.ie/msc/t4media/Mean%20and%20Standard%20Deviation.pdf (Definition and use of each metric)
Source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/13%3A_Statistics_and_Probability_Background/13.01%3A_Basic_statistics-_mean_median_average_standard_deviation_z-scores_and_p-value (Basic statistics definitions)
Source: https://www.w3schools.com/python/pandas/ref_df_describe. (Describe() in Python)
Source: https://www.databrewer.co/python-data-wrangling/group-data (Describe and group by function)
Source: https://pythonspot.com/pandas-groupby/ (GROUPBY function)
Source: http://stackoverflow.com/questions/69201770/is-there-any-way-to-groupby-a-df-in-pandas-and-then-add-a-column-of-values-from (Describe function, by species)
Source: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40 (Analysis of the Iris Dataset)
Source: https://www.geeksforgeeks.org/exploring-correlation-in-python/ (Exploring correlation in Python) 
Source: https://realpython.com/numpy-scipy-pandas-correlation-python/ (Correlation With Python)
Source: https://www.hackersrealm.net/post/iris-dataset-analysis-using-python (Correlation Matrix)
Source: https://www.geeksforgeeks.org/python-pandas-dataframe-corr/ (Correlation Matrix)
Source: https://builtin.com/data-science/correlation-matrix (How to read a correlation matrix)
Source: https://www.w3schools.com/datascience/ds_stat_correlation_matrix.asp (Statistics Correlation Matrix)
Source: https://flexiple.com/python/exploratory-data-analysis-on-iris-dataset#:~:text=2.%20Relation%20between%20Variables (Plotting a histogram in Python)
Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html (Making a histogram of the DataFrame’s columns)
Source: https://statisticsbyjim.com/basics/histograms/#:~:text=Histograms%20and%20Skewed%20Distributions (Using Histograms to Understand Your Data)
Source: https://flexiple.com/python/exploratory-data-analysis-on-iris-dataset (Exploratory Data Analysis on Iris Dataset in Python - Histograms)
Source: https://chartio.com/resources/tutorials/what-is-a-box-plot/ (Boxplot definition)
Source: https://www.tableau.com/chart/what-is-box-and-whisker-plot (Boxplot use)
Source: https://www.mokkup.ai/blogs/what-is-a-box-plot-and-when-to-use-it/ (Limitations of Box Plots)
Source: https://www.atlassian.com/data/charts/box-plot-complete-guide (Best practices for using a boxplot)
Source: https://medium.com/@hfahmida/eda-for-iris-dataset-with-boxplots-violin-plots-heatmap-pairwise-plots-535275b4c2a0 (Boxplots of Features)
Source: https://rowannicholls.github.io/python/graphs/ax_based/boxplots_significance.html (Graphs in Python)
Source: https://www.atlassian.com/data/charts/box-plot-complete-guide#:~:text=A%20complete%20guide%20to%20box%20plots,-POSTED%20BY%3A%20MIKE (Understanding boxplots)
Source: https://www.youtube.com/watch?v=KwqWuRvt7XQ (Box Plots Explained)
Source: https://medium.com/data-science/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643#:~:text=Customizing%20boxplots%20to%20compare%20distributions (Comparing distributions in Boxplots)
Source: https://www.atlassian.com/data/charts/heatmap-complete-guide (A complete guide to heatmaps)
Source: https://www.tableau.com/visualization/what-is-heat-map-and-highlight-table#:~:text=Heatmaps%20work%20best%20for%20presenting,volume%20with%20color%20and%20size. (Type of Analysis)
Source: https://www.fullstory.com/blog/heatmap/#:~:text=Why%20(and%20when)%20to%20use,shown%20in%20the%20video%20below) (Why use a heatmap)
Source: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html (Annotated Heatmap)
Source: https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/ (Heatmap using imshow)
Source: https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/ (Explaining pandas' iloc)
Source: https://scicoding.com/how-to-use-correlation-matrices-in-python/ (How to use Correlation Matrices in Python - Iris Dataset)
Source: https://medium.com/@kulkarni.madhwaraj/heatmap-analysis-using-python-seaborn-and-matplotlib-f6f5d7da2f64 (Correlation values with a heatmap)
Source: https://www.tableau.com/chart/what-is-scatter-plot (Scatter plot definitions)
Source: https://www.atlassian.com/data/charts/what-is-a-scatter-plot(Use of scatter plots)
Source: https://www.indeed.com/career-advice/career-development/a-guide-to-scatter-plots (Limitations of scatter plots)
Source: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ (Relationship between Variables)
Source: https://www.youtube.com/watch?v=JGWqb5nNudE (Data Visualisation - Iris Dataset)
Source: https://scikit-learn.org/1.3/auto_examples/datasets/plot_iris_dataset.html (Scatter Plot of the Iris dataset)
Source: https://medium.com/@elumavictoria/introduction-1e1310086438 (Visualisation of the data - Scatterplots)
Source: https://www.geeksforgeeks.org/python-seaborn-pairplot-method/(seaborn.pairplot() method)
Source: https://www.geeksforgeeks.org/pairplot-in-matplotlib/ (Pairplot in Matplotlib)
Source: https://www.whizlabs.com/labs/exploring-pair-plots/ (Limitations of pair plots)
Source: https://www.youtube.com/watch?v=dlFScQLOtoY (Iris Classification (Part 1) | Data Analysis and Exploration)
Source: https://www.youtube.com/watch?v=JGWqb5nNudE (Data Visualisation - Iris Dataset)
Source: https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#:~:text=feature_names%27%2C%20%27filename%27%2C%20%27data_module%27%5D)-,Plot%20of%20pairs%20of%20features%20of%20the%20Iris%20dataset,-%23 (Pair plots)
Source: https://stats.stackexchange.com/questions/636112/how-to-interpret-pairplots (How to interpret pair plots)
Source: https://www.analyticsvidhya.com/blog/2024/02/pair-plots-in-machine-learning/ (Pair Plots in Machine Learning)
Source: https://scikit-learn.org/stable/modules/density.html (About Kernel density Estimates)
Source: https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html (Plot of pairs of features of the Iris dataset)
Source: https://www.youtube.com/watch?v=6jsCbjQB3y0 (Write to a text .txt file in Python)

