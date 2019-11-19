# (Dataset Exploration Title)
## by (your name here)


## Dataset

The data consists of information regarding 113937 Prosper loans, including ('ListingKey', 'ListingNumber', 'ListingCreationDate', 'CreditGrade', 'Term', 'LoanStatus'...), the data can be found [here]( https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv), the data is not clean, after gathering and assessing the data I've done this steps to clean up the data
- Fix columns names: remove the spaces and the brackets.
- Fix missing values for our variables of interest: for Occupation and EmploymentStatus I will replace the null values with 'Other' and for BorrowerState column I'm going to drop rows with null values, and for ProsperRating_Alpha I'm going to fill the null values with values from CreditGrade, fill null values for the loans originated after July 2009 using ProsperRating_Alpha.
- Change data type from string to category for categorical features.
- Change data type from string to DateTime for DateTime features.


## Summary of Findings

In the exploration, I found that
- Professional is the most counted occupation for Prosper users.
- The majority of Prosper users are employed.
- The number of users that are Homeowners is greater than the number of users that are Not-homeowners.
- Most of the users are from California.
- Most counted income ranges Prosper users are '25-49,9' and '50-74,9' followed by '75-99,9' and '+100'
- A high proportion of the loans are completed (About 70%).
- Prosper Rating is normally distributed and centered around "C" in the middle dividing loans with lower risk and loans with higher risk.
- There is a high positive correlation between ('BorrowerAPR', 'BorrowerRate', 'LenderYield', 'EstimatedLoss', 'EstimatedReturn') and a high negative correlation between those variables and ProsperRating_numeric.
- For the majority of states, the proportion of homeowners is greater than the proportion of not homeowners.
- For the majority of Occupations, the proportion of homeowners is higher or approximately equal to the proportion of not-homeowners.
- While the risk increases (rate decreases) the proportion of Completed loans decreases and the proportion of Chargedoff and Defaulted loans increases.
- While the income range is getting higher the proportion of completed loans is getting higher.
- The rate of completion for (Employed, self-employed and retired) borrowers is greater than the rate of completion for not employed borrowers.
- For the loans with a high rating, the number is homeowners is higher than the number of not-homeowner and for loans with a low rating, the number of not-homeowners is higher.
- Retired users have the highest rate followed by the employed users.
- Retired and Employed users are having lower risque on average.
- People with high IncomeRange are likely to complete the loans.

## Key Insights for Presentation

For the presentation, in the first part, I focus on the characteristics of Prosper users (Who is using prosper?)
I start by introducing their employment status, followed by their occupations, then the homeownership and finally their income range, 

Afterward, I introduce the Loan Status variable to see how loans tend to end in general, then I use a barplot to see how Prosper rating is distributed, after that I start combining the loan status with the features seen previously to see how the loans tend to end based on the characteristics of the users (Did Prosper users successfully accomplished their debts?)
lastly, I plot Prosper Rating and Homeownership by Loan Status using different types of plots (boxplot, violin plot, and line plot) just to consolidate the previous findings.

I polished most of the plots by adding an appropriate title, legend, and labels for X and Y axes
