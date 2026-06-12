# COVID-19 Data Analyzer

## Project Overview

COVID-19 Data Analyzer is a Python-based Data Analytics project that collects real-time COVID-19 statistics from a public API, performs data cleaning, exploratory data analysis (EDA), feature engineering, and generates visual insights using Matplotlib.

The project helps identify the most affected countries, analyze death and recovery rates, classify countries based on risk levels, and visualize trends through charts.

---

## Problem Statement

COVID-19 generated massive amounts of global health data, making it difficult to manually analyze cases, deaths, and recoveries across countries.

This project automates data collection, processing, analysis, and visualization to extract meaningful insights from COVID-19 statistics.

---

## Features

* Fetch real-time COVID-19 data using API
* Convert JSON data into CSV format
* Perform Exploratory Data Analysis (EDA)
* Calculate Death Rate
* Calculate Recovery Rate
* Classify countries by Risk Level
* Visualize:

  * Top 10 Countries by Cases
  * Top 10 Countries by Deaths
  * Top 10 Countries by Death Rate
  * Top 10 Countries by Recovery Rate
  * Cases vs Deaths Scatter Plot
  * Risk Distribution Pie Chart

---

## Technologies Used

* Python
* Pandas
* Requests
* Matplotlib

---

## Project Structure

```text
COVID-19-Data-Analyzer/
│
├── Data/
│   ├── covid_data.csv
│   └── cleaned_covid_data.csv
│
├── src/
│   ├── fetch_response.py
│   ├── csv_analysis.py
│   ├── EDA.py
│   └── visualization.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd COVID-19-Data-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Fetch Data

```bash
python src/fetch_response.py
```

### Step 2: Create CSV

```bash
python src/csv_analysis.py
```

### Step 3: Perform EDA

```bash
python src/EDA.py
```

### Step 4: Generate Visualizations

```bash
python src/visualization.py
```

---

## Sample Insights

* USA recorded the highest number of COVID-19 cases.
* India ranked among the most affected countries.
* Recovery rates vary significantly across countries.
* Death rates are not directly proportional to total cases.
* Most countries fall into the Low Risk category.

---

## Future Improvements

* Interactive Plotly Dashboard
* Streamlit Web Application
* Country Comparison Tool
* Automated PDF Reports
* Time-Series Analysis
* Machine Learning-Based Trend Prediction

---

## Author

Krishna

B.Tech Student | Python Developer | Data Analytics Enthusiast

GitHub: <a href="https://github.com/Devidutta3">Profile Link </a>
