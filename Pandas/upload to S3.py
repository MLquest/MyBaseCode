###uploading to S3###########

import tinys3

conn = S3Connection('AKIAIFYVRTPS5VYAIR3Q', 'mv7gUewHbY1omVKmiteRQVLTWnAGOybSdSthM6wP')
conn = tinys3.Connection('AKIAIFYVRTPS5VYAIR3Q', 'mv7gUewHbY1omVKmiteRQVLTWnAGOybSdSthM6wP',tls=True)
f = open('C:/Users/vijay/Downloads/test.csv','rb')
conn.upload('C:/Users/vijay/Downloads/test.csv',f,'vjs3website')
