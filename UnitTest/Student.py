#!/user/bin/python
#encoding=utf-8

class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        pass

    def get_grade(self):
        if(self.__score > 100 or self.__score < 0):
            raise ValueError("value:%s"%self.__score)
        if(self.__score >=80 and self.__score<=100):
            return 'A'
        if(self.__score >=60 and self.__score<80):
            return 'B'
        if(self.__score >=0 and self.__score<60):
            return 'C'
           
        
