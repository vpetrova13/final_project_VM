#load libraries
library(synthpop)
library(tidyverse)
library(lubridate)

#read original clean data 
original_data <- read_csv("synthetic_wildlife.csv")
original_data <- original_data  %>% 
  mutate(CALL_REGION = as.factor(CALL_REGION)) %>% 
  mutate(CA_ANIMAL_TYPE = as.factor(CA_ANIMAL_TYPE)) %>% 
  mutate(reason_for_call = as.factor(reason_for_call)) %>% 
  mutate(type_of_calls = as.factor(type_of_calls)) %>% 
  select(CALL_SAVED_TIME, everything()) %>% 
  mutate(CALL_SAVED_TIME = as.factor(CALL_SAVED_TIME)) 

#examine my data
codebook.syn(original_data)

#create synthetic data
synthetic_data <- syn(original_data, visit.sequence = (1:ncol(original_data)))
summary(synthetic_data)

#initial comparison
compare(synthetic_data, original_data, stat = "counts")

#write synthetic data
#write.syn(synthetic_data,file = "synthetic_wildlife", filetype = "csv")
