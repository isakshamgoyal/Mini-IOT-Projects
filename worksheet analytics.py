
import pandas as pd
import matplotlib.pyplot as plt



colnames=["Timestamp","Email Address",'Name','Age','genre','Limitless','DDLJ','Annabelle','3 idiots','hours','movies']
db=pd.read_csv("Worksheet (Responses) - Form Responses 1.csv", names=colnames, header=None)

db.drop(["Timestamp","Email Address"],axis=1, inplace=True)
db.drop(0, axis=0, inplace=True)


#Plotting Movie Frequency  
movies=db['movies']

movie=[]

for i in movies:
    for key in i.split(','):
        key=key.strip()
        movie.append(key.lower())
        
mov = pd.DataFrame(movie)
count = mov[0].value_counts()
count = pd.DataFrame(count[:10])

plt.bar(count.index, count[0], align='center')

#Plotting Genre
genres = db['genre']

genre = []

for i in genres:
    for key in i.split(','):
        key = key.strip()
        if key is not "":    
            genre.append(key.lower())
        
gen = pd.DataFrame(genre)
count = gen[0].value_counts()
count = pd.DataFrame(count[:11])

plt.bar(count.index, count[0], align='center')   
plt.pie(count.values, labels= count.index, autopct='%1.1f%%')  

#Plotting Hours wrt age group 17-29
hours = db[(db['Age']=='17-29')]['hours']

hour_count = hours.value_counts()
hour_count = pd.DataFrame(hour_count)

fig = plt.figure()
plt.pie(hour_count.values, labels= hour_count.index, autopct='%1.1f%%')  
fig.suptitle('Age 17-29', fontsize = 20)
