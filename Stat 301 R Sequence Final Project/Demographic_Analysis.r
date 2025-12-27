# Demographic Variables: Univariable Analysis

library(tidyverse)
library(dplyr)
library(readr)
library(naniar)
library(knitr)

## Age
#summary statistics
summary(shopping_dataset_clean$Age)
#explore outliers
boxplot.stats(shopping_dataset_clean$Purchase.Amount..USD.)$out


# Standard deviation and other metrics
shopping_dataset_clean %>%
  summarise(
    n = n(),
    mean_age = mean(Age, na.rm = TRUE),
    median_age = median(Age, na.rm = TRUE),
    sd_age = sd(Age, na.rm = TRUE),
    min_age = min(Age, na.rm = TRUE),
    max_age = max(Age, na.rm = TRUE),
    IQR_age = IQR(Age, na.rm = TRUE)
  )

# Create age groups
sdc <- shopping_dataset_clean %>%
  mutate(AgeGroup = case_when(
    Age < 18 ~ "Under 18",
    Age >= 18 & Age <= 24 ~ "18–24",
    Age >= 25 & Age <= 34 ~ "25–34",
    Age >= 35 & Age <= 44 ~ "35–44",
    Age >= 45 & Age <= 54 ~ "45–54",
    Age >= 55 & Age <= 64 ~ "55–64",
    Age >= 65 ~ "65+"
  ))

# Average spending by age group
sdc %>%
  group_by(AgeGroup) %>%
  summarise(avgpurchase = mean(Purchase.Amount..USD., na.rm = TRUE))

sdc_p <- sdc %>%
  group_by(AgeGroup) %>%
  summarise(total = sum(Purchase.Amount..USD., na.rm = TRUE)) %>%
  mutate(percentage = (total / sum(total)) * 100)

# @fig2 and @fig3
# show the most important parts of the distribution



## Gender
# Summary statistics
summary(as.factor(shopping_dataset_clean$Gender))

# Count and percentage by gender
shopping_dataset_clean %>%
  count(Gender) %>%
  mutate(percentage = n / sum(n) * 100)

# Average spending by gender
shopping_dataset_clean %>%
  group_by(Gender) %>%
  summarise(
    n = n(),
    mean_purchase = mean(Purchase.Amount..USD., na.rm = TRUE),
    median_purchase = median(Purchase.Amount..USD., na.rm = TRUE),
    sd_purchase = sd(Purchase.Amount..USD., na.rm = TRUE),
    min_purchase = min(Purchase.Amount..USD., na.rm = TRUE),
    max_purchase = max(Purchase.Amount..USD., na.rm = TRUE)
  ) 
# Total spending and percentage by gender
shopping_dataset_clean %>%
  group_by(Gender) %>%
  summarise(total = sum(Purchase.Amount..USD., na.rm = TRUE)) %>%
  mutate(percentage = (total / sum(total)) * 100) 

## Location
shopping_dataset_clean %>%
  count(Location) %>%
  arrange(desc(n)) %>%
  head(10)

shopping_dataset_clean %>%
  group_by(Location) %>%
  summarise(revenue = sum(Purchase.Amount..USD.)) %>%
  arrange(desc(revenue)) %>%
  head(10)

# use a map to help visualize

