import json

data = [
    {
        "name": "Jonathan",
        "grades": [100, 98, 33, 55]
    },
    {
        "name": "Rona",
        "grades": [99, 22]
    },
    {
        "name": "Valentin",
        "grades": [99, 99, 98, 97, 95]
    }
]

analysis_data = []
for student in data:
    name = student["name"]
    average = sum(student["grades"]) / len(student["grades"])
    lowest_grade = min(student["grades"])
    highest_grade = max(student["grades"])

    analysis_data.append({
        "name": name,
        "avg": average,
        "highest": highest_grade,
        "lowest": lowest_grade
    })

with open("grades_analysis.json", "w") as fileobj:
    json.dump(analysis_data, fileobj)
