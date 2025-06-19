#Task1
dict_students = {'Raghav': 54, 'Ayush': 62, 'Priya': 77, 'Alice': 93}
dict_name = input("Enter student's name: ")
dict_marks = dict_students.get(dict_name)
if dict_marks is not None:
    print(f"{dict_name}'s marks: {dict_marks}")
else:
    print("Student not found")


#Task2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", my_list)
extracted_first_five = my_list[0:5]
print("Extracted first five elements:", extracted_first_five)
reversed_extracted_elements = extracted_first_five[::-1]
print("Reversed extracted elements:", reversed_extracted_elements)