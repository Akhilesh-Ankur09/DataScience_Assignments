# Week 4 – Real-World Data Analysis: Air Quality in India

## Objective
The objective of this assignment is to apply data science techniques learned in previous weeks to a real-world, large-scale dataset related to a current public health and environmental problem. This week focuses on structured data loading, cleaning, manipulation, feature engineering, and visualization using Python.

## Dataset Description
The dataset used in this project is sourced from Kaggle and contains city-level daily air quality measurements across India. It includes major air pollutants and Air Quality Index (AQI) values collected over multiple years.

### Key Attributes
- City
- Date
- PM2.5, PM10
- NO, NO2, NOx, NH3
- CO, SO2, O3
- Benzene, Toluene, Xylene
- AQI
- AQI_Bucket

The dataset contains real-world challenges such as missing values and inconsistent pollutant availability, making it suitable for applied data analysis.



## Steps Performed

### 1. Data Loading & Inspection
- Loaded the dataset using Pandas
- Inspected schema, data types, and missing values
- Verified dataset size and structure

### 2. Data Cleaning
- Converted date column to datetime format
- Removed rows with missing critical identifiers (City, Date)
- Preserved missing pollutant values to maintain data integrity
- Sorted data for time-series consistency

### 3. Feature Engineering
- Extracted Year, Month, Day, and Day of Week
- Encoded AQI severity levels numerically
- Calculated city-level average AQI
- Created a pollutant availability indicator per record

### 4. Data Visualization
Generated insight-driven visualizations:
- AQI severity distribution
- Yearly AQI trend
- Top 10 most polluted cities by average AQI
- Monthly AQI pattern

All plots are saved in the `outputs/figures` directory.

## Tools & Libraries Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Pathlib

## Key Learnings
- Handling real-world datasets with missing and noisy data
- Applying structured data cleaning decisions
- Creating meaningful engineered features
- Visualizing trends for analytical storytelling
- Maintaining professional project structure and version control

## Conclusion
This Week 4 assignment demonstrates the application of core data science concepts on a real-world environmental dataset, showcasing analytical reasoning, clean coding practices, and reproducible workflows.
# Data Science Assignments

This repository contains my weekly Data Science assignments, structured to demonstrate progressive learning from Python fundamentals to real-world data analysis using industry-standard tools and practices.

Each week focuses on building specific competencies in data handling, analysis, and problem-solving.

---



