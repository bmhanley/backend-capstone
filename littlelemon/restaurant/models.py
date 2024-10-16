from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(6)
    BookingDate = models.DateField()
    
    def __str__(self): 
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   Price = models.DecimalField(max_digits=10, decimal_places=2, null=False) 
   Inventory = models.SmallIntegerField(5)

   def __str__(self):
      return self.Title