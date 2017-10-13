################# CSV Processing ##################

import pandas as pd
import numpy as ny

###########################

df =pd.read_csv('C:/Users/vijay/Desktop/ML/Pandas/Master.csv') # Base ball data

df ['nameFull'] = df ['nameFirst'] +  ' ' + df ['nameLast']

print df ['nameFull']

#df.to_csv('C:/Users/vijay/Desktop/ML/Pandas/Master_updates.csv')

############################
##Linear regression### to fill in the



print   df['weight'].fillna(ny.mean(df['weight']))


print ny.sum(df['weight'])

print ny.mean(df['weight'])
