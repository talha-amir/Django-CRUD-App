from django.db import models

class Department(models.Model):
    se = 'Software Engineering'
    cs = 'Computer Science'

    DEPARTMENTS = (
        ('se' , se),
        ('cs' ,cs)

    )

    # id = models.AutoField(max_length=2,default=se,choices=DEPARTMENTS)
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name
        


class Student(models.Model):
    SECTIONS = (
        ['A','A'],
        ['B','B'],
        ['C','C']
        )
    
    roll_number = models.CharField(max_length=20,unique=True,primary_key=True)
    name = models.CharField(max_length=20)
    section = models.CharField(max_length=1,choices=SECTIONS,default='A')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_number

        
