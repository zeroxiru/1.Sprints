import json


with open("grades.json", "r") as fileobj:
    data = json.loads(fileobj.read())

    analysis_data = []
    for student in data:
        name = student["name"]
        average = sum(student["grades"]) / len(student["grades"])
        lowest_grade = min(student["grades"])
        highest_grade = max(student["grades"])
        print(f"Name: {name} \n Average: {average}\n Highest: {highest_grade} \n Lowest {lowest_grade}")

    # Create a dictionary with the analysis data for the current student
    analysis_dict = {
        "name": name,
        "avg": average,
        "highest": highest_grade,
        "lowest": lowest_grade
    }

    # Append the analysis dictionary to the analysis_data list
    analysis_data.append(analysis_dict)

# Save the analysis_data to a JSON file
with open("grades_analysis.json", "w") as fileobj:
    json.dump(analysis_data, fileobj)