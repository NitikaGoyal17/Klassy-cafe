from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length= 200,null=True)
    email= models.EmailField(null=True)
    phone= models.IntegerField(null=True)
    number_guests= models.IntegerField(null= True)
    date = models.DateField(null=True)
    time = models.CharField(max_length= 200,null=True)
    message= models.CharField(max_length= 200,null=True)

    def __str__(self):
        return self.name

