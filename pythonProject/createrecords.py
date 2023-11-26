import random

def generate_student_records(n):
    records = []

    for _ in range(n):
        student_id = str(random.randint(1000000, 9999999))
        first_name = random.choice(["Alice", "Bob", "Charlie", "David", "Eva"])
        last_name = random.choice(["Smith", "Johnson", "Williams", "Jones", "Brown"])
        age = random.randint(18, 25)

        subjects = [
            {"subjectId": "001", "subjectName": "Math", "marks": random.randint(70, 100)},
            {"subjectId": "002", "subjectName": "English", "marks": random.randint(70, 100)},
            {"subjectId": "003", "subjectName": "Science", "marks": random.randint(70, 100)}
        ]

        record = f"{student_id}|{first_name}|{last_name}|{age}|"
        record += "|".join([f"{subj['subjectId']}|{subj['subjectName']}|{subj['marks']}" for subj in subjects])

        records.append(record)

    return records

def write_to_file(data, file_path):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line + '\n')

if __name__ == "__main__":
    # Specify the number of records you want
    number_of_records = 1000

    # Generate student records
    student_records = generate_student_records(number_of_records)

    # Specify the path to the output text file
    output_file_path = r"C:\StudentsData\insertrecords.txt"

    # Write records to the text file
    write_to_file(student_records, output_file_path)
