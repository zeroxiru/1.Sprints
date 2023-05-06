def convert_kph_to_mph(kph):
    mph = kph * 0.6214
    return mph

def display_speed_table(strt_spped, end_speed, inrement):

    for kph in range (strt_spped, end_speed, inrement):
        mph = convert_kph_to_mph(kph)
        print(f"{kph} km per hour = {mph: .3f} mph")

def print_table_header():
    print("KPH\t MPH")
    print("---------------")


# def Generate_spped_table(strt_spped, end_speed, inrement):
#     for speed_in_kph in range(strt_spped, end_speed, inrement):
#         mph = convert_kph_to_mph(speed_in_kph)
#         print(speed_in_kph, "/t", format(mph,".2f"))
#display_speed_table()


def main():
    print_table_header()
   # Generate_spped_table(60,130,5)
#print(convert_kph_to_mph(100))
    display_speed_table(60,130,5)

if __name__ == '__main__':
    main()