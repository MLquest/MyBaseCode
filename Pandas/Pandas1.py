##########Pandas############

import pandas as pd
import numpy
#########

##############


d=pd.DataFrame({'age': pd.Series([22,38,26,35],index=['a','b','c','d']),'fare': pd.Series([7.25,71.83,8.05],index=['a','b','d']) ,'name': pd.Series(['Braund','Cummings','Vijay','Mani'],index=['a','b','c','d'])  })

print d.loc['c'] ### Passing the Index

print d ['age']
print d [['age','fare']]


print  d['age'] >30 ##returns the boolean value

print  d[d['age'] >30]  ## returns the actual datafarmes which matches the filter criteria

print d['name'][d['age'] >30]

print [d['age']>30]


##########################




countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 0]

oly=pd.DataFrame({'country_name':countries,'gold':gold, 'silver':silver,'bronze':bronze})


print oly['country_name']



print oly[(oly.gold > 0)  & (oly.silver > 0) & (oly.bronze >0)]




###Acess by index

print oly.loc[1]

print oly

year=[2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012]

foo=pd.DataFrame( {'year':  year,
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]})

print foo['year']
print foo.year
print foo[['year','team']]
print foo.loc[3]
print foo.iloc[3]
print foo[3:6]


print foo[(foo.wins > 10) & (foo.team=="Packers")]

###################################################


d={'one': pd.Series([1,2,3],index=['a','b','c']), 'two': pd.Series([1,2,3,4],index=['a','b','c','d'])}

df=pd.DataFrame(d)

print df

print df.apply(numpy.mean)

print df.two.map(lambda x :x >=1) ## to apply the transformation on a specific cols use map

print df [ (df.one  ==2)]

print df.applymap(lambda x:x >1) ##to apply the transformation on all cols use applymap


print  oly[['gold','silver','bronze']][(oly.gold > 0)  & (oly.silver > 0) & (oly.bronze >0)].apply(numpy.mean)

