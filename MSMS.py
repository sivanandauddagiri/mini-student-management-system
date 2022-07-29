
class Student:
    student_Dictionary = {}
    
    def __init__(self):
        self.rollno = input('\n\tEnter the student rollno: ')
        self.name = input('\n\tEnter the student name: ')
        self.phnno = input('\n\tEnter the student phnno: ')
        self.address = input('\n\tEnter the student address: ')
        student_class = input('\n\tEnter the student class[ex: 1,2,3,4,5,6,7,8,9,10]: ')
        
        
        if student_class in studentclass.classes:
            studentclass.classes[student_class].studentList.append(self)
            
        else:
            new_class = studentclass(student_class)
            new_class.studentList.append(self)
            studentclass.classes[student_class] = new_class
        
        self.student_class = studentclass.classes[student_class]
    
    
        print("\n Student added successfully")
        self.getStudent()
    
    
    
    def getStudent(self):
        print("\n---Student datails---\n")
        print("\tRoll Number : ", self.rollno)
        print("\tName : ", self.name)
        print("\tPhone Number : ", self.phnno)
        print("\tAddress : ", self.address)
        print("\tClass : ", self.student_class.name)
        print("\tSchool Name = 'Cambridge School' ")
        
    def UpdateStudent(self):
        print("\t\t select option to update student details\n")
        
        print("\t\t\t(1). To change student name\n")
        print("\t\t\t(2). To change student phone number\n")
        print("\t\t\t(3). To change student Address\n")
        print("\t\t\t(4). To change student Class\n")
        
        option = input("Enter any given option to modify:")
        print()
        
        if option in ['1','2','3','4']:
            if option == '1':
                self.name = input("\t\t\t Enter the student new name:")
                print("\n\t\t student new name updated successfully\n")
                
            elif option == '2':
                self.phnno = input("\t\t\t Enter the student new phone number:")
                print("\n\t\t student new phone number updated successfully\n")
                
            elif option == '3':
                self.address = input("\t\t\t Enter the student new address:")
                print("\n\t\t student new address updated successfully\n")
            if option == '4':
                new_class = input("\t\t\t Enter the student new class:")
                self.student_class.studentList.remove(self)
                try:
                    self.student_class = studentclass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addclass = studentclass(new_class)
                    self.student_class = addclass
                    addclass.studentList.append(self)
                    
                print("\n\t\t student new class updated successfully\n")
                    
                
            self.getStudent()
        else:
            print("\n\t\t you have choosen wrong option")
            
        
        
        
    @classmethod
    def UpdateSchoolName(cls,new_schl_name):
        cls.school_name = new_schl_name
        
        
    @classmethod
    def getTotalStudents(cls):
        return len(cls.student_Dictionary)
        
        
class studentclass:
    
    classes = {}
    def __init__(self,name):
        self.name = name
        studentclass.classes[name] = self
        self.studentList = []
        
        

def main():
    
    
    print("---Welcome to the Cambridge School Student Management System---\n")
    print("\t(1). To Get Student Details")
    print("\t(2). To Add New Student Details")
    print("\t(3). To Remove Student Details")
    print("\t(4). To Update Student Details")
    print("\t(5). To Get Number of Student in School")
    print("\t(6). To Get All Student Details")
    print("\t(7). To Get any Class Student Details")
    print("\t(8). To Update School Name")
    
    
    option = input('Enter any above given option:')
    print()
    
    
    if option == '1':
        rollno =  input("\t Enter the Roll number of a Student:")
        
        try:
            Student.student_Dictionary[rollno].getStudent()
        except:
            print("\t\t Sorry, You have entered the wrong Roll Number...")
            

        
        
    elif option == '2':
        new_student = Student()
        Student.student_Dictionary[new_student.rollno] = new_student
        
    elif option == '3':
        
        rollno = input('\t Enter the Roll number to delete the particular student details: ')
        
        try:
            student = Student.student_Dictionary.pop(rollno)
            student.student_class.studentList.remove(student)
            print('\t\t',rollno,'Student details removed successfully')
            
        except:
            print("\t\t Sorry,check ☑ You have entered the wrong Roll Number.. or No student there to delete.")

    elif option == '4':
        rollno = input("\tEnter the Roll Number of a student: ")
        print()
        try:
            Student.student_Dictionary[rollno].UpdateStudent()
        except:
            print("\n\t\t You have entered the wrong Roll number")
    
    elif option == '5':
        print('\n\t\t Total number of students in the school: ',Student.getTotalStudents())
        
        
    elif option == '6':
        if Student.student_Dictionary:
            print('\n\t\t Total number of students in the school: ',Student.getTotalStudents())
            print("\nTotal list with details\n")
            for sNo,student in enumerate(Student.student_Dictionary.values()):
                print('student-', sNo + 1 )
                student.getStudent()
                print()
        else:
            print("\tNo students are there")
        
    elif option == '7':
        try:
            students = studentclass.classes[input("\t Enter the class name:")]
            print("\nstudents of class-",students)
            print("\nTotal number of students in the class{students.name}:{len(students.studentList)}")
            print()

            for sNo,student in enumerate(students.studentList):
                print("student-",sNo+1)
                student.getStudent()
                print()
        except:
            print("\n you entered wrong class name or no students there")

        
            
        
    elif option == '8':
        new_schl_name = input("\t Enter the new school name:")
        Student.UpdateSchoolName(new_schl_name)
        print("\n School name changed successfully",new_schl_name)
        

        
        
        
if __name__ == "__main__":
    option = 'Y'
    while option == 'Y':
        main()
        
        option == input('\n Do you want to continue [Y/N ?]:')
        print()
        