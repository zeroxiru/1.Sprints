
employees = [
    ["John Doe", "Software Engineer", "Front-end"],
    ["James Smith", "Jr. Software Engineer", "Databases"],
    ["Rohan", "Software Engineer", ["Front-end", "UI/UX"]]
]
james_enterprise = employees[1][2]
employees[1][2] = "Sr. databases"
emp_rohan = employees[2]
print(emp_rohan)
print(employees)
