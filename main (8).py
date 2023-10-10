'''
Implement a function called sort_students that takes a list of stident bject as input and sorts the
list based on their CGPA (Cumulative Grate point Average) in descending order.Each student object
has the following attributes:name(string),roll_number(string),and cgpa(float).Test the function
write different input lists of students.
'''
 
class student:
  
 def __init__(self,name,roll_number,cgpa ):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa


def sort_students(student_List):
  #Sort the list of students in descending order of CGPA
    sorted_students = sorted(student_List,
       key=lambda           students: students.cgpa,
      reverse=True)
  # syntax - lambda arg:exp
    return sorted_students


#Example usage:
students = [
  student("Hari","A123",7.8),
  student("Srikanth","A124",8.9),
  student("Saumya","A125",9.1),
  student("Mahidhar","A126",9.9),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
   print("Name: {},Roll Number: {}, CGPA: {}".format(student.name,
                                    student.roll_number,
                      student.cgpa))