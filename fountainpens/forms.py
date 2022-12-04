from django import forms
from .models import FountainPen, Nib ,NibSize, NibColor, NibPoint, InkReserviorType, InkReservior, Brand

class FountainPenForm(forms.ModelForm):
	class Meta:
		model = FountainPen
		fields = [
            'brand',
            'pen_model',
			'color',
            'supported_nib_size',
            'nib',
			'ink_reservior'
            ]


class NibForm(forms.ModelForm):
	class Meta:
		model = Nib
		fields = [
            'nib_size',
            'nib_point',
            'nib_color',
            'nib_manufacturer']

class NibColor(forms.ModelForm):
	class Meta:
		model = NibColor
		fields = ['color_name']

class NibSize(forms.ModelForm):
	class Meta:
		model = NibSize
		fields = ['size']

class NibPoint(forms.ModelForm):
	class Meta:
		model = NibPoint
		fields = ['point']

class Brand(forms.ModelForm):
	class Meta:
		model = Brand
		fields = [
            'name',
            'origin',
            'established'
        ]

class InkReserviorType(forms.ModelForm):
	class Meta:
		model = InkReserviorType
		fields = ['reservior_type_name']

class InkReservior(forms.ModelForm):
	class Meta:
		model = InkReservior
		fields = [
            'reservior_type',
            'reservior_model_name',
            'reservior_capacity'
        ]