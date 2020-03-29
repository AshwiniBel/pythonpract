#count the number of Students in individual Class
from collections import Counter
classes = (
        ('V',1),
        ('V',2),
        ('VI',1),
        ('VI',2),
        ('VI',3),
        ('VII',1),
        ('VII',2),
)

students = Counter(class_name for class_name, no_students in classes)
print(students)