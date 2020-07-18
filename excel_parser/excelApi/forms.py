from django import forms 
from .models import File

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ["name", "sector", "xlsx"]


'''
class FileForm2(forms.Form):
    name = forms.CharField(label='File_name')
    sector = forms.CharField(label='Sector_name')
    xlsx= forms.FielField(label='file_xlsx')
 '''   
   