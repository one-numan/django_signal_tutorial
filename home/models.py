from django.db import models

# Create your models here.
class Car(models.Model):
    car_name=models.CharField(max_length=30,null=False)
    car_launch_data=models.DateField(null=True,blank=True)
    last_modified=models.DateTimeField(auto_now=True) #last Modification
    created_at = models.DateTimeField(auto_now_add=True) # Add a Car Entries


    def __str__(self):
        return F"Car Name : {self.car_name}   | Launch Date : {self.car_launch_data}"
    


    