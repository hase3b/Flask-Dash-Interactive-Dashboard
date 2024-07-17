# Flask-Dash-Interactive-Dashboard
This repository contains a comprehensive project focused on data preparation, exploratory data analysis (EDA), and the creation of an interactive visualization dashboard using Flask and Dash. The project includes the following components:

1) Data Preparation:
  * Jupyter Notebook: A detailed notebook where the dataset is explored, cleaned, and preprocessed for a classification task. The notebook includes:
    * Dataset Exploration
    * Data Cleaning (Identifying & Removing Missing Values, & Correcting Data Types)
    * Exploratory Data Analysis (EDA)
    * Data Preprocessing (Discretization, Feature Scaling, Feature Encoding, Data Splitting)
2) Interactive Dash App:
  * **Multipage Dash App**: Built using the Flask framework, this app includes five pages:
    * About: Overview of the dataset
    * Dataset: Display of the dataset
    * Descriptive Statistics: Statistical summary of the dataset
    * Univariate Analysis: Analysis of individual variables
    * Bivariate Analysis: Analysis of relationships between variables
  * Features:
    * Multiple dropdowns and callbacks to update plots dynamically
    * Plots created using Seaborn and Plotly for interactive and visually appealing graphics
  * **Note**: The Dash app has not been hosted online but can be run locally using the provided code. It can also be easily hosted online, but this was out of the scope for this project.
3) Project Report:
  * A detailed report documenting the entire process from data preparation to the creation of the interactive dashboard. The report provides insights into the methodologies used and the results obtained.

### Repository Structure:
* Data-Preparation.ipynb: Jupyter Notebook for data preparation and EDA
* Project Report.pdf: Detailed project report
* Dashboard/: Folder containing Python scripts for the Dash web app
* Video

### How to Run:
1) Clone the repository:
   ```sh
   git clone https://github.com/hase3b/Flask-Dash-Interactive-Dashboard.git
   ```
3) Navigate to the Dashboard folder:
   ```sh
   cd Flask-Dash-Interactive-Dashboard/Dashboard
   ```
5) Run the Dash app locally:
   ```sh
   python index.py
   ```
   Open your web browser and go to http://127.0.0.1:8050/ to view the app.
   
### Future Work:
* Hosting the Dash app online for broader accessibility.
* Enhancing the app with additional analysis and visualizations.
* Integrating machine learning models for predictive analytics.
