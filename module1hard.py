# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний
# балл каждого ученика, поэтому вам предстоит
# автоматизировать этот процесс":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
studentsList = list(students)
print(studentsList)
studentsList.sort()
print(studentsList)

# Надо проходить по колекциям циклом, но мы их не проходили
dictStudent = {studentsList[0]:(sum(grades[0]) / len(grades[0])),
               studentsList[1]:(sum(grades[1]) / len(grades[1])),
               studentsList[2]:(sum(grades[2]) / len(grades[2])),
               studentsList[3]:(sum(grades[3]) / len(grades[3])),
               studentsList[4]:(sum(grades[4]) / len(grades[4]))}
print(dictStudent)

