def collect_and_save_student_details(filename="students.txt"):
    # Prompt the user to enter the student's name
    name = input("Enter student name: ")
    # Prompt the user to enter the student's age
    age = input("Enter student age: ")
    # Prompt the user to enter the student's email
    email = input("Enter student email: ")
    # Open the file in append mode and write the student details
    with open(filename, "a") as file:
        file.write(f"Name: {name}, Age: {age}, Email: {email}\n")
    # Notify the user that the details have been saved
    print("Student details saved.")

# Example usage:
# collect_and_save_student_details()