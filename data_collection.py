# -*- coding: utf-8 -*-

import glassdoor_scraper as gs 
import pandas as pd 

path = "/Users/davidadarkwah/Desktop/Data Science Projects/ds_salary_proj-master/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)