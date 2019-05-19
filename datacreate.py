import csv
import random
import pandas as pd
myFile = open('train_data.csv', 'w')  
with myFile:  
    myFields = ['Temperature','Rainfall','Humidity','Moisture','Crop']
    writer = csv.DictWriter(myFile, fieldnames=myFields)    
    writer.writeheader()
    for i in range(0,2000):    
        writer.writerow({'Temperature' : random.randint(21,27),'Rainfall':random.randint(175,350), 'Humidity':random.randint(60,80),'Moisture':random.randint(383,430),"Crop":"Rice"})
        writer.writerow({'Temperature' : random.randint(13,16),'Rainfall':random.randint(60,150), 'Humidity':random.randint(75,90),'Moisture':random.randint(450,650),"Crop":"Tomato"})
        writer.writerow({'Temperature' : random.randint(21,24),'Rainfall':random.randint(30,100), 'Humidity':random.randint(50,60),'Moisture':random.randint(400,450),"Crop":"Wheat"})
        writer.writerow({'Temperature' : random.randint(5,27),'Rainfall':random.randint(39,50), 'Humidity':random.randint(60,70),'Moisture':random.randint(380,430),"Crop":"Barley"})
        writer.writerow({'Temperature' : random.randint(18,26),'Rainfall':random.randint(80,120), 'Humidity':random.randint(30,40),'Moisture':random.randint(300,400),"Crop":"chile"})
data = pd.read_csv("train_data.csv")
print(data)
