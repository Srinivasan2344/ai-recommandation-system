import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("data/student.csv")

df["target"] = [
    "Advanced AI",
    "Java Developer",
    "Data Scientist",
    "Python Basics",
    "ML Engineer",
    "Advanced AI",
    "Java Developer",
    "Data Scientist",
    "Python Basics",
    "ML Engineer"

]

target_map = {
    "Advanced AI": 0,
    "Java Developer": 1,
    "Data Scientist": 2,
    "Python Basics": 3,
    "ML Engineer": 4,
    "Other": 5,
    "Go Developer": 6,
    "iOS Developer": 7,
    "Web Developer": 8

}

df["target"] = df["target"].map(target_map)

X = df[[
    "experience",
    "skill_match",
    "certifications",
    "education_score",
    "interview_score"
]]

y = df["target"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

pickle.dump(model, open("models/model.pkl", "wb"))

print("Model trained successfully")