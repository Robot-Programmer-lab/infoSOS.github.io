print("Welcome to file_converter!")
print()
file_name = input("Input your file name: ")

file = open(file_name)
file_data = list(file.read())
file.close()

for i in range(len(file_data)):
    if (file_data[i] == "\n"):
        file_data[i] = "<br>"
    
new_file_name = f"programm_output_file"

file = open(new_file_name, "a")

converted_file_data = "".join(file_data)

file.write(str(converted_file_data))
file.close()


print(f"Programm name result file = {new_file_name}")
print("Result file data: ")

file = open(new_file_name)
file_data = file.read()
print()

print(file_data)

print()


print("Programm stop")
