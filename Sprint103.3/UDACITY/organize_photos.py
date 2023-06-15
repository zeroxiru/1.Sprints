import os

# Change the working directory to Photo_directory

def extract_place(file_name):
    return file_name.split("_")[1]

os.chdir('Photos')

list_of_photo_dir = os.listdir()
places = []
for photo_name in list_of_photo_dir:
    place = extract_place(photo_name)
    places.append(place)
print(places)

extract_place()
# file_name = "2016-11-04_Berlin_09/42/22.jpg"
# first_slice = file_name.find("_")
# first_partial_slice = file_name[first_slice + 1:]
# second_slice = first_partial_slice.find("_")
# second_partial_slice = first_partial_slice[:second_slice]
#
# print(first_slice)
# print(first_partial_slice)
# print(second_slice)
# print(second_partial_slice)





try:
    os.chdir("Berlin")
except FileNotFoundError:
    print("File is not found")


berlin_photos = os.listdir()

#
# print(list_of_photo_dir)
# print(berlin_photos)