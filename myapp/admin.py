from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')  # แสดงชื่อ, จำนวนสินค้า และราคาสินค้าในตาราง
    fields = ('name', 'description', 'quantity', 'price')  # แสดงฟิลด์ในหน้าเพิ่ม/แก้ไขไอเท็ม

admin.site.register(Item, ItemAdmin)
