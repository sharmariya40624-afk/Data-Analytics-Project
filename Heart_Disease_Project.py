import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv("Heart_Disease_Prediction.csv")

#Remove extra spaces from column names
df.columns = df.columns.str.strip()

print(df.columns)

#1. Bar Chart Heart Disease Count
df["Heart Disease"].value_counts().plot(kind="bar")
plt.title("Heart Disease : Presence vs Absence")
plt.xlabel("Condition")
plt.ylabel("Number of Patients")
plt.show()

#2. Age Distribution
plt.hist(df["Age"])
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#3. Age vs Cholesterol
plt.scatter(df["Age"], df["Cholesterol"])
plt.title("Age vs Cholesterol")
plt.xlabel("Age")
plt.ylabel("Cholesterol Level")
plt.show()

#4. Max Heart Rate
plt.hist(df["Max HR"])
plt.title("Maximum HR Distribution")
plt.xlabel("Max HR")
plt.ylabel("Count")
plt.show()