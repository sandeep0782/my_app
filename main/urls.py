"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Index),
    path('dashboard', views.DashBoard, name = 'dashboard'),

    path('view_activity', views.View_Activity, name = 'view_activity'),
    path('add_activity/', views.Change_Activity, name = 'add_activity'),
    path('change_activity/<int:pid>/', views.Change_Activity, name = 'change_activity'),
    path('delete_activity/<int:id>/', views.Delete_Activity, name = 'delete_activity'),

    path('live_calender', views.Live_Calender, name = 'live_calender'),

    path('calender/cal_home/<int:pid>/', views.cal_home, name = 'cal_home'), 
    
    path('view_calender', views.View_Calender, name = 'view_calender'),
    path('add_calender/', views.Change_Calender, name = 'add_calender'),
    path('change_calender/<int:pid>/', views.Change_Calender, name = 'change_calender'),
    path('delete_calender/<int:pid>/', views.Delete_Calender, name = 'delete_calender'),

    path('view_season', views.View_Season, name = 'view_season'),
    path('add_season/', views.Change_Season, name = 'add_season'),
    path('change_season/<int:pid>/', views.Change_Season, name = 'change_season'),

    path('view_quality', views.View_Quality, name = 'view_quality'),
    path('add_quality/', views.Change_Quality, name = 'add_quality'),
    path('change_quality/<int:pid>/', views.Change_Quality, name = 'change_quality'),
    path('delete_quality/<int:id>/', views.Delete_Quality, name = 'delete_quality'),
    
    path('view_drop', views.View_Drop, name = 'view_drop'),
    path('add_drop/', views.Change_Drop, name = 'add_drop'),
    path('change_drop/<int:pid>/', views.Change_Drop, name = 'change_drop'),


    path('view_buyer', views.View_Buyer, name = 'view_buyer'),
    path('add_buyer/', views.Change_Buyer, name = 'add_buyer'),
    path('change_buyer/<int:pid>/', views.Change_Buyer, name = 'change_buyer'),

    path('view_supplier', views.View_Supplier, name = 'view_supplier'),
    path('add_supplier/', views.Change_Supplier, name = 'add_supplier'),
    path('change_supplier/<int:pid>/', views.Change_Supplier, name = 'change_supplier'),

    path('view_travel', views.View_Travel, name = 'view_travel'),
    path('add_travel/', views.Change_Travel, name = 'add_travel'),
    path('change_travel/<int:pid>/', views.Change_Supplier, name = 'change_travel'),

    path('view_otb', views.View_Otb, name = 'view_otb'),
    path('add_otb/', views.Change_Otb, name = 'add_otb'),
    path('change_otb/<int:pid>/', views.Change_Otb, name = 'change_otb'),

    path('view_assortment', views.View_Assortment, name = 'view_assortment'),
    path('view_assortment_buyer', views.View_Assortment_Buyer, name = 'view_assortment_buyer'),
    path('add_assortment/', views.Change_Assortment, name = 'add_assortment'),
    path('import_assortment/', views.Import_Assortment, name = 'import_assortment'),
    path('change_assortment/<int:pid>/', views.Change_Assortment, name = 'change_assortment'),
    path('delete_assortment/<int:id>/', views.Delete_Assortment, name = 'delete_assortment'),

    path('change_techpack/<int:pid>/', views.Change_Techpack, name = 'change_techpack'),
    path('add_techpack/', views.Change_Techpack, name = 'add_techpack'),

    path('view_article_type', views.View_Article_Type, name = 'view_article_type'),
    path('add_article_type/', views.Change_Article_Type, name = 'add_article_type'),
    path('change_article_type/<int:pid>/', views.Change_Article_Type, name = 'change_article_type'),

    path('view_department', views.View_Department, name = 'view_department'),
    path('add_department/', views.Change_Department, name = 'add_department'),
    path('change_department/<int:pid>/', views.Change_Department, name = 'change_department'),

    path('view_gender', views.View_Gender, name = 'view_gender'),
    path('add_gender/', views.Change_Gender, name = 'add_gender'),
    path('change_gender/<int:pid>/', views.Change_Gender, name = 'change_gender'),

    path('view_active_vendor', views.View_Active_Vendor, name = 'view_active_vendor'),
    path('add_vendor_request/', views.Change_Vendor_Request, name = 'add_vendor_request'),
    path('change_vendor_request/<int:pid>/', views.Change_Vendor_Request, name = 'add_vendor_request'),
    path('delete_vendor_request/<int:id>/', views.Delete_Vendor_Request, name = 'delete_vendor_request'),
    
    
    path('change_vendor_form/<int:pid>/', views.Change_Vendor_Form, name = 'change_vendor_form'),
    
    path('login_to_wms', views.login_to_wms),
    
    path('view_order', views.View_Order, name = 'view_order'),
    path('add_order/', views.Change_Order, name = 'add_order'),
    path('change_order/<int:pid>/', views.Change_Order, name = 'change_order'),
    path('delete_order/<int:id>/', views.Delete_Order, name = 'delete_order'),
    path('view_order_details/<int:id>/', views.View_Order_Details, name = 'view_order_details'),

    path('print_preview/<int:id>/', views.print_preview, name='print_preview'),
    
    path('pi', views.Generate_Pi, name='pi'),
    path('view_pi', views.View_Pi, name='view_pi'),
    
    path('book_create', views.book_create, name='book_create'),
    
    path('view_image', views.View_Image, name='view_image'),
    path('add_image/', views.Change_Image, name = 'add_image'),
    path('change_image/<int:pid>/', views.Change_Image, name='change_image'),
    path('delete_image/<int:id>/', views.Delete_Image, name = 'delete_image'),
  
  
    path('view_discussion', views.View_Discussion, name = 'view_discussion'),
    path('add_discussion/', views.Change_Discussion, name = 'add_discussion'),
    path('change_discussion/<int:pid>/', views.Change_Discussion, name = 'change_discussion'),
    path('delete_discussion/<int:id>/', views.Delete_Discussion, name = 'delete_discussion'),
    
    path('view_details/<int:id>/', views.View_Details, name = 'view_details'),
    path('add_details/<int:id>/', views.Add_Details, name = 'Add_details'),
    path('close_request/<int:id>/', views.Close_Request, name = 'close_request'),
    
    path('read_pdf/', views.read_pdf, name = 'read_pdf'),
    
    path('upload_file', views.upload_file, name='upload_file'),



   
] 