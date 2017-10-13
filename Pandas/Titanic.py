##################Titanic Survival########################

import pandas as pd
import numpy as np

#########################

### Prediction 1###
#df=pd.read_csv('C:/Users/vijay/Desktop/ML/Pandas/test.csv')

df=pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')

print df [['PassengerId','Sex','Age']]

df ['survey']= df.Sex.map( lambda x : 1  if x =='female'   else  1) 


print  df[['Sex','survey']]


###Prediction 1 - Alternate###
#  predictions = {}
  #  df = pandas.read_csv(file_path)
    #for passenger_index, passenger in df.iterrows():
      #  passenger_id = passenger['PassengerId']
      
        # Your code here:
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        #if passenger['Sex'] == 'male':
          #         predictions[passenger_id] = 0
        #else :
                    
          #          predictions[passenger_id] = 1
        
    #return predictions

###Prediction 2 ###
df = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')
predictions = {}
for p_index,passenger in df.iterrows():
                           passenger_id =passenger['PassengerId']
                           if   ( passenger['Sex'] == 'female' ) or  (passenger['Pclass'] == 1 and passenger['Age'] < 18 and passenger['Age']  > 1   ):
                               predictions[passenger_id] = 1
                           else:
                               predictions[passenger_id] = 0

out= pd.DataFrame({'pred':predictions})

print out.loc[792]

###Prediction 3 ###






                           
