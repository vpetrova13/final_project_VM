#load libraries
library(synthpop)
library(tidyverse)

#read original clean data 
original_data <- read_csv("wildlife_clean.csv")
original_data <- original_data %>% 
  select(-X1) %>% 
  mutate(CALL_REGION = as.factor(CALL_REGION)) %>% 
  mutate(CA_ANIMAL_TYPE = as.factor(CA_ANIMAL_TYPE)) %>% 
  mutate(reason_for_call = as.factor(reason_for_call)) %>% 
  mutate(type_of_calls = as.factor(type_of_calls)) %>% 
  select(CALL_SAVED_TIME, everything())

#examine my data
codebook.syn(original_data)

#create synthetic data
synthetic_data <- syn(original_data, visit.sequence = (2:5))

summary(synthetic_data)

#initial comparison
compare(synthetic_data, original_data, stat = "counts")

#write synthetic data
write.syn(synthetic_data,file = "synthetic_wildlife", filetype = "csv")
