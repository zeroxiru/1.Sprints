numbers = [5, -2, 10, -8, 3, -6, 0, 7, -1]
pos_num = list(filter(lambda x: x > 0, numbers))

print(pos_num)

H:\5. MasterSchool\1.Sprints\Udacity\Sprint105\Sprint105.1

import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Change the directory to the desired path
new_directory = "H:\5. MasterSchool\1.Sprints\Udacity\Sprint105\Sprint105.1"
os.chdir(new_directory)

# Verify the change
updated_directory = os.getcwd()
print("Updated working directory:", updated_directory)