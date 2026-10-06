from django.db import models
from django.contrib import admin 
class service_DB(models.Model):
    Vehicle_No=models.CharField(primary_key=True)
    Customer_Name=models.CharField(max_length=20)
    Mobile_No=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField()
    Date=models.DateField()
    Service_Name=models.CharField()
    Attender_Name=models.CharField()
class service_DBAdmin(admin.ModelAdmin):
    list_display=["Vehicle_No","Customer_Name","Mobile_No","Email","Address","Date","Service_Name","Attender_Name"]