Shopping Dataset for Marketing Purposes
Data Science 1 with R (STAT 301-1) - Final Project
Author: Sophie Langaigne
Date: December 10, 2025
Project Overview

This project analyzes consumer shopping behavior patterns using the Shopping Behavior Dataset from Kaggle. The analysis explores relationships between demographics, purchasing patterns, product preferences, and seasonal trends to provide actionable marketing insights. This project combines data science techniques with marketing analytics to understand factors influencing consumer behavior.





Repository Structure
final-project-1-sophielangaigne2027-hash/
├── README.md                           # Project overview and setup
├── .gitignore                          # Git ignore rules
├── final-project.qmd                   # Main Quarto analysis document
├── final-project.html                  # Rendered HTML report
│
├── data/
│   └── raw/
│       └── shopping_behavior_updated.csv  # Original dataset (3,900 obs, 18 vars)
│
├── plots/                              # Generated visualizations
│   ├── data.completeness.chart.png
│   ├── distribution.purchase.amount.png
│   ├── boxplot.purchase.amount.png
│   ├── frequency.items.purchased.png
│   ├── distribution.customer.age.png
│   ├── item.purchases.by.season.png
│   ├── discount.usage.payment.method.png
│   ├── revenue.across.age.groups.subscription.status.png
│   ├── us.states.by.number.purchase.png
│   ├── number.purchases.by.gender.png
│   ├── gender.shopping.by.state.png
│   └── purchase.frequency.customers.png
│
└── docs/
    └── analysis-summary.md             # Key findings summary
    
Dataset Description
Source: Shopping Behavior Dataset from Kaggle
Dimensions: 3,900 observations with 18 variables

Variables:
Categorical (11): Customer ID, Payment Method, Promo Code Used, Discount Applied, Shipping Type, Subscription Status, Season, Color, Size, Location, Category
Numeric (4): Age, Previous Purchases, Purchase Amount (USD), Review Rating
Additional (3): Gender, Item Purchased, Frequency of Purchases

Data Quality: Complete dataset with no missing values

Project Context
This analysis was completed as part of the Data Science 1 with R (STAT 301-1) course and integrates with the Integrated Marketing Certificate Program curriculum. 
The project demonstrates practical applications of R programming, statistical analysis, and data visualization in marketing analytics. 

Key Research Questions

How do demographic factors (age, gender, location) influence purchasing behavior?
What seasonal patterns exist in product purchases?
How do subscription status and discount usage affect customer value?
What are the regional variations in shopping preferences?
How does purchase frequency relate to customer satisfaction?

Overarching: What are the best ways to increase sales?

Getting Started
Prerequisites
Download the following library,
tidyverse, dplyr, readr, naniar, knitr, scales, maps

Link: https://github.com/stat301-1-2025-fall/final-project-1-sophielangaigne2027-hash.git
cd final-project-1-sophielangaigne2027-hash


Major Findings

1. Purchase Distribution

Purchase amounts uniformly distributed from $10-100
50% of purchases fall between $40-80
No significant clustering around specific price points

2. Product Preferences

Top items: Pants (185), Jewelry (182), Blouses (180)
Clear seasonal patterns in clothing purchases
Accessories maintain consistent popularity year-round

3. Demographics Insights

Customer ages range 18-73 with consistent distribution (~200 per age group)
Peak age ranges: late 20s to mid-30s and mid-50s to late 50s
Male customers represent 68% of purchases (2,652 vs 1,248 female)

4. Geographic Patterns

Top states: Montana, California, Idaho
No strong regional clustering
Significant cross-gender shopping variations in only 4 states (Idaho, Minnesota, Mississippi, Georgia)

5. Customer Value

55+ age group generates highest revenue ($82M)
Subscription customers contribute disproportionately more revenue
Medium (M) size accounts for most purchases across all colors

6. Discount & Payment Behavior

60% of transactions occur without discounts
Discount usage consistent across payment methods (~40%)
Debit card users show slightly higher discount usage (45%)

7. Loyalty Patterns

Purchase frequency evenly distributed (539-584 customers per frequency)
Every 3-month shoppers show highest satisfaction (3.77 rating)
Quarterly shoppers least satisfied despite larger numbers

Analysis Workflow

Data Loading & Cleaning - Import dataset, handle missing values
Univariate Analysis - Distribution of key variables
Bivariate Analysis - Relationships between variables
Geographic Analysis - State-level patterns and regional variations
Segmentation - Customer groups by behavior and demographics


Visualizations
The project includes 12 main visualizations:
Data completeness assessment
Purchase amount distributions (histogram & boxplot)
Item frequency analysis
Age distribution
Color and size preferences
Seasonal purchase patterns
Payment method analysis
Age group revenue by subscription
Geographic heat map
Gender purchase patterns
State-level gender differences
Customer loyalty by frequency

Language: R 4.0+
IDE: RStudio
Document Format: Quarto (QMD → HTML)
Packages: tidyverse, ggplot2, dplyr, knitr
Visualization: ggplot2, maps
Statistical Analysis: Base R, chi-squared tests

Marketing Recommendations and Conclusions

Target 55+ subscribers - highest revenue generation
Focus on Montana, California, Idaho - top purchasing states
Expand Medium size production in top colors (Teal, Violet, Olive)
Implement frequency-based promotions for every-3-month shoppers
Increase discount targeting - 60% purchase without discounts
Address quarterly customer satisfaction - lowest ratings
Investigate male-dominated purchasing - potential female market opportunity


Author Information
Sophie Langaigne
Northwestern University
Data Science Major and Integrated Marketing Certificate Program

References
Grandmaster07. (n.d.). Shopping Behaviour Dataset. Kaggle. Retrieved December 10, 2025, from https://www.kaggle.com/datasets/grandmaster07/shopping-behaviour-dataset/data
R Core Team. (2024). R: A language and environment for statistical computing. R Foundation for Statistical Computing.
