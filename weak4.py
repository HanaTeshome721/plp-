def read_and_write_file():
    try:
       
        input_file = input("Enter the name of the file to read: ")

       
        with open(input_file, "r") as f:
            content = f.read()

        modified_content = content.upper()

       
        output_file = input("Enter the name of the new file to write: ")

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f" File has been successfully read and written to '{output_file}'.")

    except FileNotFoundError:
        print(" Error: The file you entered does not exist.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()
