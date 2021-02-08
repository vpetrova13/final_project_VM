# Final project 
## Overview of the project
As part of Data Analysis course at Code Clan, I had to answer the client's questions through analysing the provided data. The client was the Scottish wildlife organisation which aims to protect animals. 

The organisation was primarily interested in wildlife injuries' trends by region, times of year, types of animals and in all combinations with each other. Also, they were interested in total call volume for advice calls and what was the trend in the provided data. Finally, they have asked to predict how this might look for 2021 including call volumes.


## Raw data and Challenges
Raw data contained free text data and there were no numbers at all. It covered the last three years: 2018, 2019 and 2020 (up to May). There were 4 main columns: description of call, region, time of when a call was reported and animal type. **Description column contained a sensitive data** and so it was removed after the cleaning step. It also contained 2-5 extra unnamed columns and after the first data exploration, it was discovered to contain a shifted data because of excess text in call description column. 
#### How I tackled this problem can be seen in [data_cleaning_scripts](data_cleaning_scripts/data_cleaning.ipynb)

## Plots

## Forecasting

## Summary of Insights
* Glasgow has the most injuries reported. Edinburgh is only the 4th one.
* All regions have seasonality in injuries reported - summer time. And summer’s 2019 peak is lower than in summer 2018.
* Birds (wild bird, fledgling and gull) have been mostly reported to have injuries. 
* By around two times more injuries of foxes reported in Glasgow than in any other region. 
* Some animals have increased injuries at summer time (birds, wild rabbit and hedgehog)
* Advice calls have peaks at summer and lower volume of calls in summer 2019.
* Seasonal Naive is good for short period prediction. Prophet is good for long term period prediction.
* It picks up the general trend which is a decreasing one. 
* Though only 2 seasons of data.
* Rescue is the second reason for calls after injuries.






 


