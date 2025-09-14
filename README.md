# Ex02 Django ORM Web Application
## Date: 13-09-2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<WhatsApp Image 2025-09-13 at 09.37.14_63f9a718.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
from django.db import models

class car(models.Model):
    id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=15)
    model=models.CharField(max_length=30)
    year=models.DateField()
    price=models.IntegerField()
    type=models.CharField(max_length=10)

from django.contrib import admin
from . models import car

admin.site.register(car)
class carAdmin(admin.ModelAdmin):
    list_display=('id','barnd','model','year','price')    
```
## OUTPUT
<img width="1920" height="1200" alt="Screenshot 2025-09-13 110521" src="https://github.com/user-attachments/assets/516fbb3e-3b09-4f5c-abeb-8b104b1c0cb9" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
