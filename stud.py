groupmates = [
    {
        "name": "Мария",
        "surname": "Гуслякова",
        "exams": ["Философия","ИС","АиГ"],
        "marks": [4,5,3]
    },
    
    {
        "name": "Даниил",
        "surname": "Иванов",
        "exams": ["История","ИКТ","Физика"],
        "marks": [5,5,5]
    },
    
    {

        "name": "Максим",
        "surname": "Петров",
        "exams": ["КТП","ЭЭиС","Психология"],
        "marks": [4,5,5]
    },
    
    {
        "name": "Анастасия",
        "surname": "Сидорова",
        "exams": ["Информатика","АиГ","КТП"],
        "marks": [4,5,4]
    }]

def print_students(students):
 print(u"Имя".ljust(15), u"Фамилия".ljust(10),
u"Экзамены".ljust(30), u"Оценки".ljust(20))
 for student in students:
     print(student["name"].ljust(15),
student["surname"].ljust(10), str(student["exams"]).ljust(30),
str(student["marks"]).ljust(20))
print_students(groupmates)
