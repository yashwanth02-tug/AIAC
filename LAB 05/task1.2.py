import hashlib

def anonymize_email(email):
    # Hash the email to anonymize it
    return hashlib.sha256(email.encode()).hexdigest()

def collect_and_save_student_details():
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    email = input("Enter student email: ").strip()

    # Anonymize email
    anon_email = anonymize_email(email)

    # Optionally, mask the name (e.g., initials only)
    masked_name = name[0] + "***" if name else "N/A"

    # Save to file
    with open("students.txt", "a") as f:
        f.write(f"Name: {masked_name}, Age: {age}, Email Hash: {anon_email}\n")

    print("Student details saved (anonymized).")

# Example usage:
collect_and_save_student_details()
