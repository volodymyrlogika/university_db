import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Ім'я")
        age = input("Вік")
        major = input("Спеціальність:")

        # Додавання нового студента
        cursor.execute('''
            INSERT INTO students (name, age, major) 
                        VALUES(?,?,?)''',(name, age, major))
        conn.commit()
        
    elif choice == "2":
        # Додавання нового курсу
        course_name = input("Назва курсу:")
        instructor = input("Викладач:")

        cursor.execute('''
            INSERT INTO courses (course_name, instructor) 
                        VALUES(?,?)''',(course_name, instructor))
        conn.commit()

    elif choice == "3":
        # Показати список студентів
        cursor.execute('''
            SELECT name FROM students''')
        students = cursor.fetchall()
        if students:
            print("Список студентів:")
            for student in students:
                print(student[0])

    elif choice == "4":
        # Показати список курсів
        pass
    elif choice == "5":
        # Зареєструвати студента на курс
        student_id = input("Введіть ID студента:")
        course_id = input("Введіть ID курсу:")
        cursor.execute('''
            INSERT INTO student_courses (student_id, course_id) 
                        VALUES(?,?)''',(student_id, course_id))
        conn.commit()

    elif choice == "6":
        # Показати студентів на конкретному курсі
        course_id =  input("Введіть ID курсу:")
        cursor.execute('''SELECT students.id, students.name FROM students, student_courses
                       WHERE students.id = student_courses.student_id AND student_courses.course_id = ?                  
                        ''', (course_id))
        
        students_on_course = cursor.fetchall()
        print(students_on_course)

    elif choice == "7":
        break
    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")


conn.close()