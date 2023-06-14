import os


#os.chdir("Photos")

file_name = "2016-11-04_Berlin_09/42/22.jpg"
def place_name(file_name):
    first_slice = file_name.find("_")
    first_paartial_slice = file_name[first_slice + 1:]
    second_slice = first_paartial_slice.find("_")
    second_partial_slice = first_paartial_slice[:second_slice]
    # print(second_slice)
    # print(first_paartial_slice)
    print(second_partial_slice)


place_name(file_name)

file_name_1 = "2016-11-04_Berlin_09/42/22.jpg"

def extract_place(file_name_1):
    place_name = file_name_1.split("_")[1]
    return place_name


extract_place(file_name_1)

t_1 = (1, 2, 3, 4, 5)
t_2 = (10, 9, 8, 7, 6)
def swap_numbers(t_1, t_2):
     (t_1, t_2) = (t_2, t_1)
     print(" After Swaping:")
     print(f"t_1:{t_1}")
     print(f"t_2:{t_2}")

swap_numbers(t_1, t_2)