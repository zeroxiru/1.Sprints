def read_file(file_name):
    try:
        with open(file_name,'r') as file_obj:
            data = file_obj.read()
            return data
    except FileExistsError:
        print("File not found")
    except Exception as e:
        print(f'got and error: {e}')

def main():
    try:
        filename = input("Enter the File name to read data:")
        data = read_file(filename)
        print("\n File Content")
        print(data)
    except Exception as e:
        print(f"An error occurd:{e}")


if __name__ == "__main__":
    main()
