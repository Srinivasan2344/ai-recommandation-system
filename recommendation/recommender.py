import pickle

model = pickle.load(open("models/model.pkl", "rb"))
encoder = pickle.load(open("models/encoder.pkl", "rb"))

course_map = {
    "Python": ["Python", "Data Science", "Machine Learning"],
    "Java": ["Java", "Spring Boot", "Microservices"],
    "SQL": ["SQL", "Power BI", "Data Analytics"],
    "R": ["R", "Statistics", "Data Visualization"],
    "Go": ["Go", "Cloud Computing", "Microservices"],
    "Swift": ["Swift", "iOS Development", "Mobile Apps"],
    "Ruby": ["Ruby", "Web Development", "Rails"]
}

def get_recommendations(student_id):
    return ["Python", "Data Science", "Machine Learning"]