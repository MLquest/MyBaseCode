##################Aadhaar data ####################

import pandas as pd

import pandasql as sql


df=pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/aadhaar_data.csv')

df.rename(columns = lambda x :  x.replace(' ','_').lower(),inplace=True)

####Above command replace the colum name ex: enrolment agency to enrolment_agency


query="""select state, sum(Aadhaar_generated)   from df  group by state limit 50 ; """

query1="""select  sum(case when gender='M' then 1 else 0 end) as  male,

sum(case when gender='F' then 1 else 0 end)  as fem
from df  where age > 50 ; """

query2 = """

select gender ,sum(Aadhaar_generated) from df  where age > 50 group by gender ;
"""

print sql.sqldf(query,locals())

print sql.sqldf(query1,locals())

print sql.sqldf(query2,locals())


