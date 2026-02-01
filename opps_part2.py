class Student:
    def __init__(self):
        self.name = "Alice"
        self.math_score = 85
        self.science_score = -5
        self.history_score = 92
        self.english_score = -10

student = Student()
dict = vars(student)
for key, value in dict.items():
    if isinstance(value, int) and value < 0:
        print(value)
        setattr(Student.__init__,key,0)
    
        
    
x= getattr (Student.__init__, 'science_score')
y= getattr (Student.__init__, 'english_score')
print(x)
print(y)