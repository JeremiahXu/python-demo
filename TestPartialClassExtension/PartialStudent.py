 # class partial classname(object):
from Student import Student 



# here is method extension.
def GetName(self):
    return self.name
Student.GetName = GetName
Student.GetSex = lambda self:self.name.upper()


if __name__ == "__main__":
    s1 = Student('Ann')
    print(s1.GetName())
    print(s1.GetSex())
