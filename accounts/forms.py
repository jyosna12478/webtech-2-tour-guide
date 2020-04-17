from django import forms
from .models import Enquiry1

class EnquiryForm(forms.ModelForm):
	class Meta:
		model = Enquiry1
		fields = ('Name','Gender','dob','age','phone','Email','Category','No_of_Days','No_of_Childrens','No_of_Adults','Enquiry_message')