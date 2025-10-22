from django.db import models

class EbenEats(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

# ADD THIS TO YOUR EXISTING models.py
class CashTransaction(models.Model):
    student_name = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Simple text fields - no complex SQL
    payment_breakdown = models.TextField(blank=True)  # "2x $10 notes, 3x $1 coins"
    change_returned = models.TextField(blank=True)    # "1x $5 note, 2x 25c coins"
    
    def calculate_change(self):
        return self.amount_paid - self.amount_due
    
    def __str__(self):
        return f"{self.student_name} - ${self.amount_due}"

# That's it! Just one simple model.