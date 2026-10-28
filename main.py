# import json, csv, requests


class Student:
    def __init__(self, student_id, name, age, course, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.score = score


class Student_manager:
    pass



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


