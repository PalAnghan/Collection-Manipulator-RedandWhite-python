#Collection Manipulator

print("Welcome to the Student Data Organizer!")
student=[]

while True:

    print("\nSelect Option: ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice_num = int(input("Enter your choice: "))

    match choice_num :

        case 1:
            print("\nEnter student deatils: ")
            stu_id = int(input("student ID: "))
            stu_name = input("Name: ")
            stu_age = int(input("Age: "))
            stu_grade = input("Grade: ")
            stu_b_date = input("Date of Birth (YYYY-MM-DD): ")
            stu_subjects = input("Subjects (comma-separated): ")

            subject_set = set(stu_subjects.split(","))
            
            student_info = (stu_id, stu_b_date)
            
            student_data = {
                "ID": stu_id,
                "Name": stu_name,
                "Age": stu_age,
                "Grade": stu_grade,
                "DOB": stu_b_date,
                "Subjects": subject_set
            }
            student.append(student_data)

            print("\nStudent added successfully!")

        case 2:
            print("\n---Display All Studnet---")

            if len(student) == 0:
                print("NO STUDENTS RECORD FOUND")
            else:
               for s in student:
                   """
                    print(f"Student ID : {s['ID']}")
                    print(f"Name       : {s['Name']}")
                    print(f"Age        : {s['Age']}")
                    print(f"Grade      : {s['Grade']}")
                    print(f"DOB        : {s['DOB']}")
                    print(f"Subjects   : {', '.join(s['Subjects'])}")
                    print("-" * 30)"""
                   
                   print(f"Student ID : {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Grade: {s['Grade']} | DOB: {s['DOB']} | Subjects: {s['Subjects']}")


        case 3:
            print("\n---Update Student Information---")

            update_id = int(input("Enter Student ID to update: "))

            for s in student:

                if s["ID"] == update_id:


                    s["Age"] = int(input("Enter new Age: "))
                    s["Grade"] = input("Enter new Grade: ")

                    new_subject = input("Enter new Subjects (comma-separated): ")
                    s["Subjects"] = set(new_subject.split(","))

                    print("Student updated successfully!")
                    break

                else:
                    print("Student ID not found.")


        case 4:
            print("\n---Delete Student---")

            delete_id = int(input("Enter Student ID to Delete: "))

            for i in range(len(student)):
                
                if student[i]["ID"] == delete_id:

                    del student[i]
                    
                    print("Student ID Deleted successfully!")
                    break
                
                else:
                    print("Student ID Not Found!")
                    
        case 5:
            print("\n---Display Subjects Offered---")

            display_subject = set()

            for s in student:
                display_subject.update(s["Subjects"])
            print(display_subject)
             

        case 6:
            print("\nExit the program!")
            break

        case _:
            print("\nINVALID NUMBER!")
        
