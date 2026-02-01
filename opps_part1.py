class Student:
    student_count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.student_count +=1

    @classmethod
    def get_total_enrolled(cls):
        return f"Total students: {cls.student_count} "
    
    @staticmethod
    def clean_name(name):
        return name.strip().capitalize()
    
    def display_profile(self):
        print ("Name :", self.name, " score:", self.score)

s1 = Student ('Alice',100)
s2 = Student ('Bob',50)

print(Student.get_total_enrolled())
formatted_name = Student.clean_name ("john")
print(formatted_name)
s1.display_profile()