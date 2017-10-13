###############New your subway data Wrangling########################
##
##
##

import pandas as pd
import numpy as ny
import pandasql

###Problem 1#######

weather_data = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv')

print weather_data ['rain']


query = """ select count(rain) from weather_data  where rain=1;


"""

print pandasql.sqldf(query.lower(),locals())


########Problem ##########

query="""
select fog, max(maxtempi) from weather_data group by fog;
"""

print pandasql.sqldf(query.lower(),locals())
