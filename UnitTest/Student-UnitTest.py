import unittest
from Student import Student

class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart',80)
        s2 = Student('Lisa',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')
    
    def test_60_to_79(self):
        s1 = Student('Bart',79)
        s2 = Student('Lisa',60)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(),'B')

    def test_0_to_59(self):
        s1 = Student('Bart',0)
        s2 = Student('Lisa',59)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'C')

    def test_invalid(self):
        s1 = Student('Bart',-1)
        s2 = Student('Lisa',101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == "__main__":
    unittest.main()
