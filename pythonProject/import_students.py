import pymongo
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME
from file_config import TEXT_FILE_PATH

def import_students_data():
    # Establish connection to MongoDB
    client = pymongo.MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    students_data = {}

    # Read data from the text file
    with open(TEXT_FILE_PATH, 'r') as file:
        for line in file:
            # Split the line into fields using pipe as the separator
            fields = line.strip().split('|')

            student_id = fields[0]

            # Check if the student already exists in the dictionary
            if student_id in students_data:
                # If the student exists, append the new subject to the subjects list
                students_data[student_id]["subjects"].append({
                    "subjectId": fields[4],
                    "subjectName": fields[5],
                    "marks": int(fields[6])
                })
            else:
                # If the student doesn't exist, create a new entry in the dictionary
                students_data[student_id] = {
                    "studentId": student_id,
                    "firstName": fields[1],
                    "lastName": fields[2],
                    "age": int(fields[3]),
                    "subjects": [
                        {
                            "subjectId": fields[4],
                            "subjectName": fields[5],
                            "marks": int(fields[6])
                        }
                    ]
                }

    # Insert student data into MongoDB
    for student_data in students_data.values():
        collection.insert_one(student_data)

    # Close the MongoDB connection
    client.close()

if __name__ == "__main__":
    # Call the import function
    import_students_data()
