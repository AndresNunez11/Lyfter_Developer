class Student:
    def __init__(self, name, section, spanish_grade, english_grade, social_grade, science_grade ):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.average = self.average_grade()
    
    def average_grade(self):
        return (int(self.spanish_grade) + int(self.english_grade) + int(self.social_grade) + int(self.science_grade)) / 4
    


