import pymongo
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME
from file_config import TEXT_FILE_PATH

def import_students_data():
    # Establish connection to MongoDB
    client = pymongo.MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Read data from the text file
    with open(TEXT_FILE_PATH, 'r') as file:
        for line in file:
            # Split the line into fields using pipe as the separator
            fields = line.strip().split('|')

            # Create a dictionary for the student data
            student_data = {
                "studentId": fields[0],
                "firstName": fields[1],
                "lastName": fields[2],
                "age": int(fields[3]),
                "subjects": [
                    {
                        "subjectId": fields[4],
                        "subjectName": fields[5],
                        "marks": int(fields[6])
                    },
                    # Add more subjects if needed
                ]
            }

            # Insert the student data into MongoDB
            collection.insert_one(student_data)

    # Close the MongoDB connection
    client.close()

if __name__ == "__main__":
    # Call the import function
    import_students_data()
