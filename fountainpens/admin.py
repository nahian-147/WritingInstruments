from django.contrib import admin
from .models import FountainPen, Nib ,NibSize, NibColor, NibPoint, InkReserviorType, InkReservior, Brand

admin.site.register(FountainPen)
admin.site.register(Nib)
admin.site.register(NibSize)
admin.site.register(NibColor)
admin.site.register(NibPoint)
admin.site.register(InkReserviorType)
admin.site.register(InkReservior)
admin.site.register(Brand)