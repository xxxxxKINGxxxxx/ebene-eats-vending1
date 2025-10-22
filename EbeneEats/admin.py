from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CashTransaction  # ADD THIS LINE

# ADD THIS CLASS
class CashTransactionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'transaction_date', 'amount_due', 'amount_paid', 'change_display')
    list_filter = ('transaction_date', 'student_name')
    search_fields = ('student_name',)
    
    def change_display(self, obj):
        return f"${obj.calculate_change()}"
    change_display.short_description = 'Change'

# REGISTER THE MODEL
admin.site.register(CashTransaction, CashTransactionAdmin)
