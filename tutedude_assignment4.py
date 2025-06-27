#Task1
import os
if os.path.exists('sample.txt'):
    with open('sample.txt', 'r') as file:
        line_number = 1
        for line in file:
            print(f"{line.strip()}")
            line_number += 1
else:
    print(f"Error: The file 'sample.txt' was not found.")

#Task2
import os
output_filename = "output.txt"
user_input_initial = input("Enter text to write to the file: ")
with open(output_filename, 'w') as file:
    file.write(user_input_initial + '\n')
print(f"Data successfully written to {output_filename}.")
user_input_append = input("Enter additional text to append: ")
with open(output_filename, 'a') as file:
    file.write(user_input_append + '\n')
print("Data successfully appended.")
print(f"\nFinal content of {output_filename}:")
if os.path.exists(output_filename):
    with open(output_filename, 'r') as file:
        print(file.read().strip())
else:
    print(f"Error: The file '{output_filename}' was not found.")