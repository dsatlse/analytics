## Signup Data

This is a dataset on society membership

### Data Description

```ID``` : Anonymised ID corresponding to an unique student

```product_name``` : Either ```"Give It A Go Mailing List"``` or ```"Membership"```

```purchase_date``` : Date purchased

Example row:

| ID | product_name | purchase_date|
| -- | -- | --|
| 657 | Membership | 2020-09-24 20:07:00 |


### Questions to investigate

Produce a report (Jupyter/ R / Pluto) that addresses these, and any other questions:

+ Plot cumulative membership for each year. For each year, filter memberships on or after July to get the membership for that year. 
+ When do people purchase membership?
+ Make a stacked plot of membership by month,  to see if we can see any differences in trend in each year
+ What are the trends in membership (yearly, monthly differenced) across 2017, 2018, 2019, 2020? There is probably a stastistical test for differences in trend
+ How many people who purchase Give It A Go mailing list convert to membership?
+ How many people remain members across years?

### Productionising

This could then be turned into a simple dashboard - User uploads the ```file.csv```, relevant data visualisations are displayed

### Technologies

Analysis: Python (Numpy, Pandas), R (ggplot, tidyverse), Julia

Plotting / Dashboard : Plotly, R Shiny, React.js (d3.js?)
