# Feature
# What the application must do
# Register students
# Collect a student's ID, name, age, and course
# View students
# Display all registered students in a readable format
# Search
# Find a student using their ID
# Update records
# Change a student's name, age, or course
# Delete records
# Remove a student after confirming the action
# Record scores
# Add assessment scores and calculate averages
# Grade students
# Assign grades based on defined score ranges
# Save and load
# Store records in a JSON file and reload them on startup
# Export records
# Export student information and scores to CSV
# Fetch external data
# Use a public HTTP API to retrieve relevant supplementary information
# Handle errors
# Deal with invalid inputs, missing files, duplicate IDs, and failed API requests


while True:
    print("=====STUDENT MANGEMENT SYSTEM=====")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Records")
    print("5. Delete Records")
    print("6. Record Scores")
    print("7. View Grades")
    print("8. Export Records to CSV")
    print("9. Fetch External Data")
    print("10. Exit")

    choice = input("Choose an Option:")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass
    elif choice == "8":
        pass
    elif choice == "9":
        pass
    elif choice == "10":
        print("--------------")
        print("Adios!")
        print("--------------")
        break
    else:
        print("-----------------------------")
        print("Invalid Choice. Try Again!")
        print("-----------------------------")