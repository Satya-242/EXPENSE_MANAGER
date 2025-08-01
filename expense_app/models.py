from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    paid_by = models.CharField(max_length=100, choices=[
        ('Satya', 'Satya'),
        ('Mani', 'Mani'),
        ('Kamal', 'Kamal'),
        
    ])

    def __str__(self):
        return f"{self.date} - {self.description} - ₹{self.amount}"