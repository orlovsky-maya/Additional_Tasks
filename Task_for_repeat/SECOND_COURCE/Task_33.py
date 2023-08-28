with (open('grades.txt', 'r', encoding='utf=8') as file):
    students = [st.strip().split() for st in file.readlines()]
    counter = 0
    for student in students:
        if int(student[1]) >= 65 and int(student[2]) >= 65 and int(student[3]) >= 65:
            counter += 1


print(counter)

