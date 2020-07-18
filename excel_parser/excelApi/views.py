from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.shortcuts import  get_object_or_404
from django.core.files.storage import FileSystemStorage 
from .forms import FileForm 
from .models import File
import pandas as pd 
import json
# Create your views here.



def file_list(request):
	files = File.objects.all()
	return render(request, ['file_list.html', 'index.html', 'excel_files.html'],  {'files' : files})


def file_upload(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# this is where we can now do somthing with the form 
			return redirect('file_list')
	else:
		form = FileForm()
		return render(request,'file_upload.html', {'form' : form})



def excel_files(request,pk):
    #get an instance of the file here... so i can access any of it's fields...
    file = get_object_or_404(File,pk=pk)
    
    #where name_of_file is the name of the field on ur model
    #file_path = file.name
    file_path = file.xlsx 

    try:
       
        # reading the excel file
        excel_data_df = pd.read_excel(file_path, usecols = "B:G",encoding='utf-8' )


        final_data = excel_data_df.to_json(orient = "table", index=None)
        #final_data = data2.to_dict(orient = "records")
        return render(request, ['excel_files.html', 'index.html'], {'final_data': final_data})

    except KeyError:
        print("failed")


