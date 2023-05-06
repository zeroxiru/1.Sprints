def calculate_distance(speed, time):
    distance = speed * time
    return distance

def generate_distance_report(speed, hours):
    print("Hour\tDistance Traveled")
    print("------------------------")

    for hour in range(1, hours + 1):
        distance = speed * hour
        print(f"{hour}\t{distance}")

print(calculate_distance(40, 4))
print (generate_distance_report(80, 7))


