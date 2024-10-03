# myapp/models.py
from django.db import models
import uuid
from django.utils import timezone  # เพิ่มการนำเข้า timezone

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default='ไม่มีคำอธิบาย')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่เพิ่ม
    updated_at = models.DateTimeField(auto_now=True)       # วันที่อัปเดต

    def __str__(self):
        return self.name

    def created_at_th(self):
        return timezone.localtime(self.created_at).strftime('%d/%m/%Y %H:%M')  # แปลงเป็นเวลาในโซนท้องถิ่น

    def updated_at_th(self):
        return timezone.localtime(self.updated_at).strftime('%d/%m/%Y %H:%M')  # แปลงเป็นเวลาในโซนท้องถิ่น
