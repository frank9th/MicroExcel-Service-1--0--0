
from django.urls import path, include 
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

	#path('', include(Routers.urls)), 
	#path('index', views.index, name="index" ),
    #path('', views.upload_file, name="upload_file" ),
    path('file_upload', views.file_upload, name="file_upload" ),
    path('', views.file_list, name="file_list" ),
    #path('budget.html', views.budget, name="budget" ),
    #path('excel_files.html', views.excel_files, name="excel")
    path('excel_files.html/<int:pk>', views.excel_files, name="excel_file"),
    #path('form_item.html', views.form_item, name="form_item") 

]


# this should be used only on developement mode and not on production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    