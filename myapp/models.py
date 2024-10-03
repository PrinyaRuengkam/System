from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='ไม่มีคำอธิบาย')  # เพิ่มค่าเริ่มต้น
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
