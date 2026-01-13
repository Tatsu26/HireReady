import json

def load_questions():
    with open("backend/data/questions.json", "r") as f:
        return json.load(f)
