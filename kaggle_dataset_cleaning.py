import csv
import pandas as pd

df = pd.read_csv('Smartphone_Usage_Productivity_Dataset_50000.csv')

print(df.columns)
print(df["Device_Type"])
print(df.isnull().sum())

df= df.drop_duplicates(subset="User_ID")

df["User_ID"]=df["User_ID"].astype(str)

df["Age"]=df["Age"].astype(int)

df["Gender"] = df["Gender"].astype(str)

df["Occupation"]=df["Occupation"].astype(str)

df["Device_Type"]=df["Device_Type"].astype(str)

df["Daily_Phone_Hours"]=df["Daily_Phone_Hours"].astype(float)

df["Social_Media_Hours"] = df["Social_Media_Hours"].astype(float)

df["Work_Productivity_Score"]=df["Work_Productivity_Score"].astype(float)

df["Sleep_Hours"]=df["Sleep_Hours"].astype(float)

df["Stress_Level"]=df["Stress_Level"].astype(float)

df["App_Usage_Count"]=df["App_Usage_Count"].astype(float)

df["Caffeine_Intake_Cups"] = df["Caffeine_Intake_Cups"].astype(int)

df["Weekend_Screen_Time_Hours"]=df["Weekend_Screen_Time_Hours"].astype(float)

df.dropna(subset=['User_ID',"Age",'Gender', 'Occupation', 'Device_Type',
       'Daily_Phone_Hours', 'Social_Media_Hours', 'Work_Productivity_Score',
       'Sleep_Hours', 'Stress_Level', 'App_Usage_Count',
       'Caffeine_Intake_Cups', 'Weekend_Screen_Time_Hours'], inplace=True)

df["User_ID"]=df["User_ID"].str.lower().str.strip()

df["Gender"]=df["Gender"].str.lower().str.strip()

df["Occupation"]=df["Occupation"].str.lower().str.strip()

df["Device_Type"]=df["Device_Type"].str.lower().str.strip()

df=df[df["Daily_Phone_Hours"].between(0, 24)]
df=df[df["Sleep_Hours"].between(0,16)]

df["Device_Type"]=df["Device_Type"].replace({
    "IOS":"Iphone",
    "Android":"Android Phone",
})