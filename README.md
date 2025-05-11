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

3. For the Python code used in this project, execute `analysis.py` using your preferred Python environment (e.g. VS Code).
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
    - Overall correlation between features
    - Species-specific correlations

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
   
 - Boxplots: - Setosa has distinctly smaller petals and wider sepals than the other species.
             - Virginica has the largest petals and longest sepals, with some overlap with versicolor.
   
   ![alt text](https://github.com/marianemcgrath/pands_project/blob/main/iris_boxplots.png)

 - Scatterplots: - Petal dimensions separate setosa from the other two species, with versicolor and virginica showing some overlap.

                 - Sepal dimensions show more overlap between species, though setosa tends to have wider sepals.

 - Pairplot: Reinforces that petal measurements are better discriminators between species than sepal measurements.

  ![alt text](https://github.com/marianemcgrath/pands_project/blob/main/iris_pairplot.png)
   
 - Heatmap: Visually confirms the strong correlation between petal length/width and the weak correlation involving sepal width.

**Key Insights**

 - Species Differentiation: Petal features are more effective than sepal features for distinguishing species, especially setosa.

 - Outliers: Few outliers exist (e.g., one virginica sample has a notably small petal width).

 - Measurement Patterns: Virginica tends to be larger overall, while setosa is compact with small petals and wide sepals.
   
# **References**

Here is a summary of the sources used to complete this project. Additional links are in the Jupyter NB.

## 1. Loading and Preparing the Iris Dataset
**Loading the Iris Dataset:**
- [scikit-learn: load_iris()](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [StackOverflow: load_iris() in Python](https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python)

**Converting to Pandas DataFrame:**
- [StackOverflow: Convert scikit-learn dataset to Pandas](https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset)

**Displaying Data:**
- [GeeksforGeeks: Display DataFrame in Table Style](https://www.geeksforgeeks.org/display-the-pandas-dataframe-in-table-style/)
- [Analytics Vidhya: head() and tail() Functions](https://www.analyticsvidhya.com/blog/2023/07/head-and-tail-functions/)
- [DataCamp: Python DataFrame Size](https://www.datacamp.com/tutorial/python-dataframe-size)

## 2. Basic Statistics & Data Summarisation
**Descriptive Statistics:**
- [UCD: Mean and Standard Deviation](https://www.ucd.ie/msc/t4media/Mean%20and%20Standard%20Deviation.pdf)
- [LibreTexts: Basic Statistics Definitions](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/13%3A_Statistics_and_Probability_Background/13.01%3A_Basic_statistics-_mean_median_average_standard_deviation_z-scores_and_p-value)
- [W3Schools: describe() in Python](https://www.w3schools.com/python/pandas/ref_df_describe.)

**Grouped Analysis:**
- [DataBrewer: Group Data in Pandas](https://www.databrewer.co/python-data-wrangling/group-data)
- [PythonSpot: Pandas groupby()](https://pythonspot.com/pandas-groupby/)
- [StackOverflow: groupby() with describe()](http://stackoverflow.com/questions/69201770/is-there-any-way-to-groupby-a-df-in-pandas-and-then-add-a-column-of-values-from)

## 3. Correlation Analysis
**Correlation Basics:**
- [GeeksforGeeks: Exploring Correlation](https://www.geeksforgeeks.org/exploring-correlation-in-python/)
- [Real Python: Correlation in Python](https://realpython.com/numpy-scipy-pandas-correlation-python/)

**Correlation Matrix & Heatmaps:**
- [Hacker's Realm: Iris Dataset Correlation](https://www.hackersrealm.net/post/iris-dataset-analysis-using-python)
- [GeeksforGeeks: Pandas corr()](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/)
- [BuiltIn: How to Read a Correlation Matrix](https://builtin.com/data-science/correlation-matrix)
- [W3Schools: Correlation Matrix](https://www.w3schools.com/datascience/ds_stat_correlation_matrix.asp)
- [SciCoding: Correlation Matrices in Python](https://scicoding.com/how-to-use-correlation-matrices-in-python/)
- [Medium: Heatmap Analysis](https://medium.com/@kulkarni.madhwaraj/heatmap-analysis-using-python-seaborn-and-matplotlib-f6f5d7da2f64)

**Heatmap Visualisation:**
- [Atlassian: Heatmap Guide](https://www.atlassian.com/data/charts/heatmap-complete-guide)
- [Tableau: What is a Heatmap?](https://www.tableau.com/visualization/what-is-heat-map-and-highlight-table)
- [FullStory: Why Use Heatmaps?](https://www.fullstory.com/blog/heatmap/)
- [Matplotlib: Annotated Heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)
- [GeeksforGeeks: imshow() Heatmap](https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/)

## 4. Histograms & Box Plots
**Histograms:**
- [Pandas Docs: DataFrame.hist()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)
- [Statistics by Jim: Histograms Explained](https://statisticsbyjim.com/basics/histograms/)

**Box Plots:**
- [Chartio: What is a Box Plot?](https://chartio.com/resources/tutorials/what-is-a-box-plot/)
- [Tableau: Box-and-Whisker Plot](https://www.tableau.com/chart/what-is-box-and-whisker-plot)
- [Mokkup.ai: Box Plot Limitations](https://www.mokkup.ai/blogs/what-is-a-box-plot-and-when-to-use-it/)
- [Atlassian: Box Plot Guide](https://www.atlassian.com/data/charts/box-plot-complete-guide)
- [Medium: Iris Dataset Boxplots](https://medium.com/@hfahmida/eda-for-iris-dataset-with-boxplots-violin-plots-heatmap-pairwise-plots-535275b4c2a0)
- [Rowan Nicholls: Boxplots in Python](https://rowannicholls.github.io/python/graphs/ax_based/boxplots_significance.html)
- [YouTube: Box Plots Explained](https://www.youtube.com/watch?v=KwqWuRvt7XQ)
- [Medium: Customising Boxplots](https://medium.com/data-science/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643)

## 5.Scatter Plots & Pair Plots
**Scatter Plots:**
- [Tableau: What is a Scatter Plot?](https://www.tableau.com/chart/what-is-scatter-plot)
- [Atlassian: Scatter Plot Uses](https://www.atlassian.com/data/charts/what-is-a-scatter-plot)
- [Indeed: Scatter Plot Guide](https://www.indeed.com/career-advice/career-development/a-guide-to-scatter-plots)
- [scikit-learn: Iris Scatter Plot](https://scikit-learn.org/1.3/auto_examples/datasets/plot_iris_dataset.html)
- [Medium: Visualising Data with Scatterplots](https://medium.com/@elumavictoria/introduction-1e1310086438)

**Pair Plots:**
- [GeeksforGeeks: seaborn.pairplot()](https://www.geeksforgeeks.org/python-seaborn-pairplot-method/)
- [GeeksforGeeks: Pairplot in Matplotlib](https://www.geeksforgeeks.org/pairplot-in-matplotlib/)
- [Whizlabs: Pair Plot Limitations](https://www.whizlabs.com/labs/exploring-pair-plots/)
- [Stats StackExchange: Interpreting Pair Plots](https://stats.stackexchange.com/questions/636112/how-to-interpret-pairplots)
- [Analytics Vidhya: Pair Plots in ML](https://www.analyticsvidhya.com/blog/2024/02/pair-plots-in-machine-learning/)
- [scikit-learn: Kernel Density Estimates](https://scikit-learn.org/stable/modules/density.html)
- [scikit-learn: PCA Iris Plot](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

## 6. General EDA & Tutorials on Iris Dataset
- [Medium: Uni-variate EDA on Iris](https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)
- [YouTube: Iris Classification (EDA)](https://www.youtube.com/watch?v=dlFScQLOtoY)

## 7. Helper Tools & Functions
- [GeeksforGeeks: pandas iloc](https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/)
- [Write to a text .txt file in Python](https://www.youtube.com/watch?v=6jsCbjQB3y0)
- [DeepSeek AI: Code Debugging](https://chat.deepseek.com) (Prompt-based help included in Jupyter NB by author)

