import json, csv, requests


class Student:
    def __init__(self, student_id, name, age, course, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.score = score


class Student_manager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        with open("students.json", "r") as file:
            load = json.load(file)

        students = []

        for data in load:
            one_student = Student(
                data["studentid"],
                data["name"],
                data["age"],
                data["course"],
                data["score"]
            )
            students.append(one_student)

        return students

    def register_student(self):
        self.student_id = input("Enter StudentID: ")
        for student in self.students:
            if student.student_id == self.student_id:
                print("-----------------------------")
                print("StudentID Already Exists!")
                print("-----------------------------")
                return False
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter Student Age: "))
        if self.age <= 0:
            print("-------------")
            print("Invalid Age!")
            print("-------------")
            return False
        self.course = input("Enter Student Course: ")
        self.score = None
        one_student = Student(
            self.student_id,
            self.name,
            self.age,
            self.course,
            self.score
        )

        return one_student

    def record_scores(self):
        studentid = input("Enter StudentID: ")
        found = False
        for student in self.students:
            if student.student_id == studentid:
                found = True
                print(f"Student Name: {student.name}")
                add_score = float(input("Enter Score: "))
                if add_score < 0 or add_score > 100:
                    print("---------------------------------")
                    print("Score must be between 0 and 100.")
                    print("---------------------------------")
                    return False
                student.score = add_score
                print("--------------")
                print("Score Added!")
                print("--------------")
        if not found:
            print("-------------------------------")
            print("Search doesn't match records.")
            print("-------------------------------")
            return False

        self.student_data = []
        for student in self.students:
            student_dict = {
                "studentid": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "score": student.score
            }
            self.student_data.append(student_dict)

        with open("students.json", "w") as file:
            json.dump(self.student_data, file)

    def save_students(self):
        new_student = self.register_student()
        if new_student:
            self.students.append(new_student)
            print("----------------------------------")
            print("Student Registered Successfully!")
            print("----------------------------------")

        self.student_data = []
        for student in self.students:
            student_dict = {
                "studentid": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "score": student.score
            }
            self.student_data.append(student_dict)
        with open("students.json", "w") as file:
            json.dump(self.student_data, file)

    def view_students(self):
        if not self.students:
            print("-----------------")
            print("No Student Found")
            print("-----------------")
            return False

        print("====STUDENTS====")
        for student in self.students:
            print("----------------------")
            print(f"StudentID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Course: {student.course}")
            print(f"Score: {student.score}")
        print("----------------------")

    def search_students(self):
        studentid = input("Enter StudentID: ")
        found = False
        for student in self.students:
            if student.student_id == studentid:
                found = True
                print("----------------------------")
                print("RECORD FOUND")
                print("----------------------------")
                print(f"StudentID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Course: {student.course}")
                if student.score == None:
                    print("Score: Not recorded")
                else:
                    print(f"Score: {student.score}")
                print("----------------------------")

        if not found:
            print("------------------------------")
            print("Search doesn't match records.")
            print("------------------------------")

    def update_records(self):
        studentid = input("Enter StudentID: ")
        found = False
        for student in self.students:
            if student.student_id == studentid:
                found = True
                print("------------------------")
                print("CURRENT RECORD")
                print("------------------------")
                print(f"StudentID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Course: {student.course}")
                if student.score == None:
                    print("Score: Not recorded.")
                else:
                    print(f"Score: {student.score}")
                print("------------------------")
                while found:
                    print("1. Update Name")
                    print("2. Update Age")
                    print("3. Update Course")
                    decision = input("Choose an option: ")
                    if decision == "1":
                        new_name = input("Enter new name: ")
                        student.name = new_name
                        print("-----------------")
                        print("Record Updated.")
                        print("-----------------")
                        self.student_data = []
                        for student in self.students:
                            student_dict = {
                                "studentid": student.student_id,
                                "name": student.name,
                                "age": student.age,
                                "course": student.course,
                                "score": student.score
                            }
                            self.student_data.append(student_dict)
                        with open("students.json", "w") as file:
                            json.dump(self.student_data, file)
                        break
                    if decision == "2":
                        new_age = int(input("Enter new age: "))
                        student.age = new_age
                        print("----------------")
                        print("Record Updated.")
                        print("----------------")
                        self.student_data = []
                        for student in self.students:
                            student_dict = {
                                "studentid": student.student_id,
                                "name": student.name,
                                "age": student.age,
                                "course": student.course,
                                "score": student.score
                            }
                            self.student_data.append(student_dict)
                        with open("students.json", "w") as file:
                            json.dump(self.student_data, file)
                        break
                    if decision == "3":
                        new_course = input("Enter new course: ")
                        student.course = new_course
                        print("----------------")
                        print("Record Updated.")
                        print("----------------")
                        self.student_data = []
                        for student in self.students:
                            student_dict = {
                                "studentid": student.student_id,
                                "name": student.name,
                                "age": student.age,
                                "course": student.course,
                                "score": student.score
                            }
                            self.student_data.append(student_dict)
                        with open("students.json", "w") as file:
                            json.dump(self.student_data, file)
                        break

        if not found:
            print("------------------------------")
            print("Search doesn't match records.")
            print("------------------------------")

    def delete_records(self):
        studentid = input("Enter StudentID: ")
        found = False
        for student in self.students:
            if student.student_id == studentid:
                found = True
                print(f"StudentID: {student.student_id}")
                print(f"Student Name: {student.name}")
                while found:
                    decision = input("Press Enter⏎ to delete record or C to cancel: ")
                    if decision == "":
                        self.students.remove(student)
                        self.student_data = []
                        for student in self.students:
                            student_dict = {
                                "studentid": student.student_id,
                                "name": student.name,
                                "age": student.age,
                                "course": student.course,
                                "score": student.score
                            }
                            self.student_data.append(student_dict)
                        with open("students.json", "w") as file:
                            json.dump(self.student_data, file)
                        print("-----------------------------")
                        print("Student Deleted Sucessfully.")
                        print("-----------------------------")
                        break
                    if decision.lower() == "c":
                        print("-----------------")
                        print("Delete Canceled.")
                        print("-----------------")
                        break
        if not found:
            print("-------------------------------")
            print("Search doesn't match records.")
            print("-------------------------------")


    def view_grades(self):
        print("====STUDENT GRADES====")
        for student in self.students:
            print('--------------------')
            print(f"Student name: {student.name}")

            if student.score is None:
                print("Score: Not recorded.")
                print("Grade: Not available.")
            else:
                print(f"Score: {student.score}")

                if 100 >= student.score >= 70:
                    print("Grade A")
                elif 69 >= student.score >= 60:
                    print("Grade B")
                elif 59 >= student.score >= 50:
                    print("Grade C")
                elif 49 >= student.score >= 45:
                    print("Grade D")
                elif 44 >= student.score >= 0:
                    print("Grade F")
        print('--------------------')

    def export_csv(self):
        with open("students.csv", "w") as file:
            content = csv.writer(file)
            content.writerow(["StudentID", "Name", "Age", "Course", "Score"])
            for student in self.students:
                content.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.course,
                    student.score
                ])
                            

student_obj = Student_manager()

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

    choice = input("Choose an Option: ")

    if choice == "1":
        student_obj.save_students()
    elif choice == "2":
        student_obj.view_students()
    elif choice == "3":
        student_obj.search_students()
    elif choice == "4":
        student_obj.update_records()
    elif choice == "5":
        student_obj.delete_records()
    elif choice == "6":
        student_obj.record_scores()
    elif choice == "7":
        student_obj.view_grades()
    elif choice == "8":
        student_obj.export_csv()
    elif choice == "9":
        pass
    elif choice == "10":
        print("---------")
        print("Adios!")
        print("---------")
        break
    else:
        print("-----------------------------")
        print("Invalid Choice. Try Again!")
        print("-----------------------------")


