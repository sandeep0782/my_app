from sqlite3 import IntegrityError
from django.db import IntegrityError
from django.contrib import messages
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import requests
from main.forms import *
from .models import *
import pandas as pd
from . utils import *
import datetime
import csv
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from . choice import STATE_CHOICES
from django.db.models import Avg, Sum, Count
# Create your views here.


def Index(request):
    d={}
    return render(request, 'new.html', d)

def DashBoard(request):
    buyer = Department.objects.all()
    om = Order_Management.objects.all()
    d = {"om":om, 'buyer':buyer}
    return render(request, 'hop/index.html', d)

# def CalenderHome(request):
#     department = Department.objects.all()
#     activity = Activity.objects.all()
#     season = Season.objects.all()
#     buyer = UserProfile.objects.filter(user_role = 2, user_type=1)
#     drop = Drop.objects.all()
#     calender = None
#     if request.method =='POST':
#         calender = Calender.objects.all()

#     d = {'season':season, 'buyer':buyer, 'drop':drop, 'calender':calender, 'department':department}
#     return render(request, 'calender/calender_dashboard.html', d)


def View_Order(request):
    order = Order.objects.filter( )
    d = {'order':order}
    return render(request, 'order/view_order.html', d)


def Change_Order(request, pid=None):
    buyer = UserProfile.objects.all()
    season = Season.objects.all()
    drop = Drop.objects.all()
    quality = Quality.objects.all()
    order = None
    today = date.today()
    BookFormSet = formset_factory(BookForm, extra=10)
    if pid:
        order = Order.objects.get(id=pid)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        formset = BookFormSet(request.POST, prefix = 'departments', instance=order)
        
        if formset.is_valid() and form.is_valid():
            pro = form.save()
            pro.order_date = today
            pro.save()
            
            for form in formset:
                if form.cleaned_data:
                    form.save()        
            messages.info(request, 'Order added Successfully')
            return redirect('view_order')
        else:
            messages.info(request, form.errors)
    else:
        
        formset = BookFormSet(prefix= "departments")
        
    d = {'order': order, 'buyer':buyer, 'season':season, 'drop':drop, 'quality':quality, 'formset':formset}
    return render(request, 'order/change_order_sandeep.html', d)

def View_Order_Details(request, id):
    order_detail = OrderDetails.objects.filter(order=id )
    d = {'order_detail':order_detail}
    return render(request, 'order/view_order_details.html', d)

def Delete_Order(request, id):
    order = Order.objects.filter(id = id)
    order.delete()
    return redirect('view_order')

def print_preview(request, id):
    pi = Order.objects.filter(id = id)
    d = {'pi': pi}
    return render(request, 'pi.html', d)


def View_Activity(request):
    activity = Activity.objects.all()
    d = {'activity':activity}
    return render(request, 'gtm/activity/view_activity.html', d)

def Delete_Activity(request, id):
    activity = Activity.objects.filter(id = id)
    try:
        activity.delete()
    except IntegrityError as e:
        messages.info(request, 'Cannot Delete as this Activity is associated with calender')
        return redirect('view_activity')
    
def Change_Activity(request, pid=None):
    buyer = Department.objects.all()
    activity = None
    if pid:
        activity = Activity.objects.get(id=pid)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Activity added Successfully')
            return redirect('view_activity')
        else:
            messages.info(request, form.errors)
    d = {'activity': activity, 'buyer':buyer}
    return render(request, 'gtm/activity/change_activity.html', d)



def View_Discussion(request):
    discussion = Discussion.objects.all()
    d = {'discussion':discussion}
    return render(request, 'discussion/view_discussion.html', d)

def Delete_Discussion(request, id):
    discussion = Discussion.objects.filter(id = id)
    discussion.delete()
    return redirect('view_discussion')

def Change_Discussion(request, pid=None):
    discussion = None
    if pid:
        discussion = Discussion.objects.get(id=pid)
    if request.method == "POST":
        form = DiscussionForm(request.POST, instance=discussion)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'discussion added Successfully')
            return redirect('view_discussion')
        else:
            messages.info(request, form.errors)
    d = {'discussion': discussion, }
    return render(request, 'discussion/change_discussion.html', d)


def View_Details(request, id):
    detail = Details.objects.filter(detail=id)
    d = {'detail':detail}
    return render(request, 'discussion/view_details.html',d)

def Add_Details(request, id):
    d = Discussion.objects.get(id=id)
    if request.method=="POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            pro=form.save()
            pro.detail = d
            pro.start_date = date.today()
            pro.save()
            messages.success(request, "Configured proprly")
            return redirect('view_discussion')  # Redirect to success page or any other view
    else:
        form = DetailForm()
    return render(request, 'discussion/change_details.html')

def Close_Request(request, id):
    detail = Details.objects.get(id = id)
    discussion = Discussion.objects.filter(name = detail)
    print(detail)
    # discussion.dis_status
    # discussion.save()
    return redirect('view_discussion')

# @login_required(login_url='login')
# @admin_only
def Change_Calender(request, pid=None):
    buyer = Buyer.objects.all()
    season = Season.objects.all()
    drop = Drop.objects.all()
    activity = Activity.objects.all()
    order_type = Order_Type.objects.all()
    calender = None
    s_date = request.POST.get('start_date')
    e_date = request.POST.get('end_date')
    if pid:
        calender = Calender.objects.get(id=pid)
    if request.method == "POST":
        form = CalenderForm(request.POST, instance=calender)
        if form.is_valid():
            if e_date>=s_date:
                pro = form.save()
                pro.save()
                messages.info(request, 'Calendar Created Successfully')
                return redirect('view_calender')
            else:
              messages.info(request,"Wrong End Date. Please Choose Proper End Date") 
        else:
            messages.info(request, form.errors)
    d = {'calender': calender, 'buyer':buyer, 'season':season, 'drop':drop, 'activity':activity, 'order_type':order_type}
    return render(request, 'gtm/calender/change_calender.html', d)


# @login_required(login_url='login')
# @admin_only
def View_Calender(request):
    buyer = None
    try:
        buyer = Buyer.objects.get(user = request.user)
    except:
        pass
    user = request.user
    calender = Calender.objects.filter()
    d = {'calender':calender}
    return render(request, 'gtm/calender/view_calender.html', d)


def cal_home(request, pid):
    from datetime import datetime, timedelta
    d1 = datetime.now().date()
    d2 = datetime.now().date()
    stdate = datetime(d1.year, d1.month, d1.day, 10)+timedelta(days=1)
    stdate2 = datetime(d1.year, d1.month, d1.day, 10)+timedelta(days=1)
    end1 = (stdate + timedelta(hours=1))

    end2 = (stdate2 + timedelta(hours=1))

    listofemail = []
    
    startdate = []
    enddate = []
    subjectlist =  []
    # messagelist = []
    activity = Activity.objects.get(id=pid)
    calender = Calender.objects.filter(activity_name=activity)
    
    
    for buyer in calender:
        
        
        listofemail.append(str(buyer.buyer.user.email))
        # listofemail.append(str(buyer.buyer.user.email))
        subjectlist.append(buyer.activity_name.name)
        d = buyer.start_date
        stdate = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
        
        startdate.append(stdate.isoformat())
        e = buyer.end_date
        endate = datetime(e.year, e.month, e.day, 10)+timedelta(days=1)
        enddate.append(endate.isoformat())
        
        
    # response = create_event(listofemail, subjectlist, startdate, enddate)
    # myresponse = get_calendar_service()
    # myresponse = main()
    # print(myresponse)
    # return HttpResponse('Careated successfully')
    return render(request, 'calender/main.html', locals())

def Live_Calender(request):
    calender = Calender.objects.all()
    d = {'calender':calender}
    return render(request, 'gtm/live_calender.html', d)

def Delete_Calender(request, id):
    calender = Calender.objects.filter(id = id)
    calender.delete()
    return redirect('view_calender')


def View_Season(request):
    season = Season.objects.all()
    d = {'season':season}
    return render(request, 'master/view_season.html', d)

def Change_Season(request, pid=None):
    buyer = Department.objects.all()
    season = None
    if pid:
        season = Season.objects.get(id=pid)
    if request.method == "POST":
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Activity added Successfully')
            return redirect('view_season')
        else:
            messages.info(request, form.errors)
    d = {'season': season, 'buyer':buyer}
    return render(request, 'master/change_season.html', d)

def View_Quality(request):
    quality = Quality.objects.all()
    d = {'quality':quality}
    return render(request, 'master/view_quality.html', d)

def Change_Quality(request, pid=None):
    quality = None
    if pid:
        quality = Quality.objects.get(id=pid)
    if request.method == "POST":
        form = QualityForm(request.POST, instance=quality)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Quality added Successfully')
            return redirect('view_quality')
        else:
            messages.info(request, form.errors)
    d = {'quality': quality}
    return render(request, 'master/change_quality.html', d)

def Delete_Quality(request, id):
    quality = Quality.objects.filter(id = id)
    quality.delete()
    return redirect('view_quality')


def View_Drop(request):
    drop = Drop.objects.all()
    d = {'drop':drop}
    return render(request, 'master/view_drop.html', d)

def Change_Drop(request, pid=None):
    buyer = Department.objects.all()
    drop = None
    if pid:
        drop = Drop.objects.get(id=pid)
    if request.method == "POST":
        form = DropForm(request.POST, instance=drop)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Drop added Successfully')
            return redirect('view_drop')
        else:
            messages.info(request, form.errors)
    d = {'drop': drop, 'buyer':buyer}
    return render(request, 'master/change_drop.html', d)


def View_Buyer(request):
    buyer = Buyer.objects.all()
    d = {'buyer':buyer}
    return render(request, 'master/view_buyer.html', d)

def Change_Buyer(request, pid=None):
    buyer = None
    if pid:
        buyer = Buyer.objects.get(id=pid)
    if request.method == "POST":
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Buyer added Successfully')
            return redirect('view_buyer')
        else:
            messages.info(request, form.errors)
    d = {'buyer': buyer}
    return render(request, 'master/change_buyer.html', d)


def View_Supplier(request):
    supplier = Supplier.objects.all()
    d = {'supplier':supplier}
    return render(request, 'master/view_supplier.html', d)

def Change_Supplier(request, pid=None):
    supplier = None
    if pid:
        supplier = Buyer.objects.get(id=pid)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Supplier added Successfully')
            return redirect('view_supplier')
        else:
            messages.info(request, form.errors)
    d = {'supplier': supplier}
    return render(request, 'master/change_supplier.html', d)


def View_Department(request):
    department = Department.objects.all()
    d = {'department':department}
    return render(request, 'master/view_department.html', d)

def Change_Department(request, pid=None):
    department = None
    if pid:
        department = Department.objects.get(id=pid)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Department added Successfully')
            return redirect('view_department')
        else:
            messages.info(request, form.errors)
    d = {'department': department}
    return render(request, 'master/change_department.html', d)


def View_Gender(request):
    gender = Gender.objects.all()
    d = {'gender':gender}
    return render(request, 'master/view_gender.html', d)

def Change_Gender(request, pid=None):
    gender = None
    if pid:
        gender = Gender.objects.get(id=pid)
    if request.method == "POST":
        form = GenderForm(request.POST, instance=gender)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Gender added Successfully')
            return redirect('view_gender')
        else:
            messages.info(request, form.errors)
    d = {'gender': gender}
    return render(request, 'master/change_gender.html', d)


def View_Travel(request):
    travel = Travel.objects.all()
    d = {'travel':travel}
    return render(request, 'travel/view_travel.html', d)

def Change_Travel(request, pid=None):
    travel = None
    s_date = request.POST.get('start_date')
    e_date = request.POST.get('end_date')
    if pid:
        travel = Travel.objects.get(id=pid)
    if request.method == "POST":
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            if e_date>=s_date:
                pro = form.save()
                pro.save()
                messages.info(request, 'Trip Added Successfully')
                return redirect('view_travel')
            else:
              messages.info(request,"End Date cannot be less thatn the Start Date") 
        else:
            messages.info(request, form.errors)
    d = {'travel': travel}
    return render(request, 'travel/change_travel.html', d)


def View_Otb(request):
    buyer = Buyer.objects.all()
    otb = OTB.objects.filter()

    # otb= OTB.objects.all().aggregate(Sum('amount'))

    d = {'otb':otb, 'buyer':buyer}
    return render(request, 'otb/view_otb.html', d)

def Change_Otb(request, pid=None):
    otb = None
    buyer = Buyer.objects.all()
    season = Season.objects.all()
    drop = Drop.objects.all()
    article_type = Article_Type.objects.all()
    if pid:
        otb = OTB.objects.get(id=pid)
    if request.method == "POST":
        form = OTBForm(request.POST, instance=otb)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'OTB Added Successfully')
            return redirect('view_otb')
        else:
            messages.info(request, form.errors)
    d = {'otb': otb, 'buyer':buyer, 'season':season, 'drop':drop, 'article_type':article_type}
    return render(request, 'otb/change_otb.html', d)


def View_Article_Type(request):
    article_type = Article_Type.objects.all()
    d = {'article_type':article_type}
    return render(request, 'master/view_article_type.html', d)

def Change_Article_Type(request, pid=None):
    article_type = None
    gender = Gender.objects.all()
    if pid:
        article_type = Article_Type.objects.get(id=pid)
    if request.method == "POST":
        form = ATForm(request.POST, instance=article_type)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Article Type Added Successfully')
            return redirect('view_article_type')
        else:
            messages.info(request, form.errors)
    d = {'article_type': article_type, 'gender':gender}
    return render(request, 'master/change_article_type.html', d)


def View_Assortment(request):
    assortment = Assortment.objects.all()
    d = {'assortment':assortment}
    return render(request, 'assortment/view_assortment.html', d)

def View_Assortment_Buyer(request):
    assortment = Assortment.objects.all()
    d = {'assortment':assortment}
    return render(request, 'buyer/view_assortment_buyer.html', d)

def Change_Techpack(request, pid=None):
    techpack = None
    if pid:
        techpack = Assortment.objects.get(id=pid)
    if request.method == "POST":
        form = TechpackForm(request.POST, request.FILES, instance=techpack)
        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'Techpack Updated Successfully')
            return redirect('view_assortment_buyer')
        else:
            pass
            # messages.info(request, form.errors)
    d = {'techpack': techpack}
    return render(request, 'buyer/upload_techpack.html', d)

def Change_Assortment(request, pid=None):
    buyer = Buyer.objects.all()
    season = Season.objects.all()
    drop = Drop.objects.all()
    gender = Gender.objects.all()
    article_type = Article_Type.objects.all()
    domimp = Domimp.objects.all()
    offonn = Onoff.objects.all()
    wwnww = Wwnww.objects.all()
    order_type = Order_Type.objects.all()
    fabric_type = Fabric_Type.objects.all()
    assortment = None
    if pid:
        assortment = Assortment.objects.get(id=pid)
    if request.method == "POST":
        form = AssortmentForm(request.POST, instance=assortment)
        if form.is_valid():
            pro = form.save()
            pro.assortment_date = date.today()
            pro.save()
            messages.info(request, 'OTB Added Successfully')
            return redirect('view_assortment')
        else:
            messages.info(request, form.errors)
    d = {'assortment': assortment, 'buyer':buyer, 'season':season, 'drop':drop, 'gender':gender, 'article_type':article_type, 'domimp':domimp, 'offonn':offonn, 'wwnww':wwnww, 'order_type':order_type,'fabric_type':fabric_type}
    return render(request, 'assortment/change_assortment.html', d)


def Delete_Assortment(request, id):
    assortment = Assortment.objects.filter(id = id)
    assortment.delete()
    return redirect('view_assortment')


def Import_Assortment(request):
    response = None
    if request.method == 'POST':
        try:
            bulk = request.FILES['file']
            df = pd.read_csv(bulk, encoding="ISO-8859-1")
            response = import_assortment_fn(request, df)
        except ValueError:
            messages.info(request,"Please select proper format")
            return redirect('import_assortment')
        if response:
            return response
        else:
            return redirect('view_assortment')
    return render(request, 'assortment/import_assortment.html')

def cal_home(request, pid):
    from datetime import datetime, timedelta
    d1 = datetime.now().date()
    d2 = datetime.now().date()
    stdate = datetime(d1.year, d1.month, d1.day, 10)+timedelta(days=1)
    stdate2 = datetime(d1.year, d1.month, d1.day, 10)+timedelta(days=1)
    end1 = (stdate + timedelta(hours=1))

    end2 = (stdate2 + timedelta(hours=1))

    listofemail = []
    
    startdate = []
    enddate = []
    subjectlist =  []
    # messagelist = []
    activity = Activity.objects.get(id=pid)
    calender = Calender.objects.filter(activity_name=activity)
    
    
    for buyer in calender:
        listofemail.append(str(buyer.activity_name.department_name.email))
        # listofemail.append(str(buyer.buyer.user.email))
        subjectlist.append(buyer.activity_name.name)
        d = buyer.start_date
        stdate = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
        
        startdate.append(stdate.isoformat())
        e = buyer.end_date
        endate = datetime(e.year, e.month, e.day, 10)+timedelta(days=1)
        enddate.append(endate.isoformat())
        
        
    # response = create_event(listofemail, subjectlist, startdate, enddate)
    # myresponse = get_calendar_service()
    # myresponse = main()
    # print(myresponse)
    # return HttpResponse('Careated successfully')
    return render(request, 'gtm/calender/main.html', locals())


def View_Active_Vendor(request):
    avl = Vendor.objects.all()
    d = {'avl':avl}
    return render(request, 'vendor/active_vendor_list.html', d)

def View_Non_Active_Vendor(request):
    avl = Vendor.objects.all()
    d = {'avl':avl}
    return render(request, 'vendor/non_active_vendor_list.html', d)

def Change_Vendor_Request(request, pid=None):
    vendor_request = None
    factory_request = None
    factory = Factory.objects.all()
    brand = Buyer.objects.all()
    if pid:
        try:
            vendor_request = Vendor.objects.get(id=pid)
        except Vendor.DoesNotExist:
            pass
        try:
            factory_request = Factory.objects.get(id=pid)
        except Factory.DoesNotExist:
            pass
        
    if request.method == "POST":
        form = VendorForm (request.POST, request.FILES, instance=vendor_request)

        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'New Vendor Onboarding request is placed Successfully')
            return redirect('view_active_vendor')
            
        else:
            # pass
            messages.info(request, form.errors)
    
    d = {'brand':brand,'vendor_request':vendor_request,'factory_request':factory_request,'state':STATE_CHOICES, 'city':CITY_CHOICES, 'MASTER_CATEGORY':MASTER_CATEGORY, 'REGION':REGION, 'FACTORY_TYPE':FACTORY_TYPE, 'factory':factory}
    return render(request, 'vendor/new_vendor_request.html',d)

def Delete_Vendor_Request(request, id):
    request = Vendor.objects.get(id = id)
    try:
        request.delete()
    except IntegrityError as e:
        messages.info(request, 'Cannot Delete as this Activity is associated with calender')
    return redirect('view_active_vendor')


def Change_Vendor_Form(request, pid=None):
    vendor_request = None
    factory_request = None
    factory = Factory.objects.all()
    brand = Buyer.objects.all()
    if pid:
        try:
            vendor_request = Vendor.objects.get(id=pid)
        except Vendor.DoesNotExist:
            pass
        try:
            factory_request = Factory.objects.get(id=pid)
        except Factory.DoesNotExist:
            pass
        
    if request.method == "POST":
        form = VendorForm (request.POST, request.FILES, instance=vendor_request)

        if form.is_valid():
            pro = form.save()
            pro.save()
            messages.info(request, 'New Vendor Onboarding request is placed Successfully')
            return redirect('view_active_vendor')
            
        else:
            # pass
            messages.info(request, form.errors)
    
    d = {'brand':brand,'vendor_request':vendor_request,'factory_request':factory_request,'state':STATE_CHOICES, 'city':CITY_CHOICES, 'MASTER_CATEGORY':MASTER_CATEGORY, 'REGION':REGION, 'FACTORY_TYPE':FACTORY_TYPE, 'factory':factory}
    return render(request, 'vendor/new_vendor_request.html',d)


def login_to_wms(username, password):
    login_url = 'https://your-wms-api.com/login'
    credentials = {'username': username, 'password': password}
    response = requests.post(login_url, json=credentials)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print("Failed to login to the WMS.")
        return None

def Generate_Pi(request):
    today = date.today()
    print(today)
    if request.method =="POST":
        if request.POST.get("singlecheckbox"):
            id = request.POST.get("singlecheckbox")
            l = len(str(id))
            # print(l)
            idd = id[0:l-1]
            present = idd.split(",")
            li=[]
            dataa = Order.objects.all()
            for i in dataa:
                li.append(i.id)
            ab = list(set(li)-set(present))
            abbb = list(set(present)-set(li))
            new_pi = Order.objects.filter(id__in = abbb)
            total_value = new_pi.aggregate(total_value=Sum('value'))['total_value'] or 0
            pi = Pi.objects.create(pi_date = today, value = total_value)
            
    return redirect(('view_pi'))
    
def View_Pi(request):
    pi = Pi.objects.all()
    d = {'pi':pi}
    return render(request, 'pi/view_pi.html', d)



from django.shortcuts import render, redirect
from . forms import BookForm

def book_create(request):
    BookFormSet = formset_factory(BookForm, extra=10)
    if request.method == 'POST':
        formset = BookFormSet(request.POST, prefix = 'departments')
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    form.save()
            return redirect('view_order')  # Replace with your URL name
    else:
        
        formset = BookFormSet(prefix= "departments")

    return render(request, 'order/new.html', {'formset': formset})


def Change_Image(request, pid=None):
    image = None
    if pid:
        image = Image.objects.get(id=pid)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            pro = form.save()
            pro.date = date.today()
            pro.save()
            messages.info(request, 'Image Updated Successfully')
            return redirect('view_image')
        else:
            pass
            # messages.info(request, form.errors)
    d = {'image': image}
    return render(request, 'image/change_image.html', d)


def View_Image(request):
    image = Image.objects.all()
    d = {'image':image}
    return render(request, 'image/view_image.html', d)

def Delete_Image(request, id):
    image = Image.objects.filter(id = id)
    image.delete()
    return redirect('view_image')





from PyPDF2 import PdfFileReader, PdfReader
import re

def read_pdf(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded file
            pdf_file = request.FILES['file']

            # Check if the uploaded file is a PDF
            if pdf_file.name.endswith('.pdf'):
                # Open and read the PDF file
                pdf_reader = PdfReader(pdf_file)
                num_pages = len(pdf_reader.pages)  # Use getNumPages() instead of numPages

                ###### Extract text from each page
                extracted_text = ''
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    extracted_text += page.extract_text()  # Use extract_text() instead of extractText()

    #             # Render extracted text in a response
    #             return HttpResponse(extracted_text)
    #         else:
    #             return HttpResponse('Uploaded file is not a PDF.')
    # else:
    #     form = UploadFileForm()
        
        ##### Define specific words to capture
            specific_words = ['LOGISTIC', 'Claims']

            # Use regex to find specific words in the extracted text
            captured_words = []
            for word in specific_words:
                matches = re.findall(r'\b{}\b'.format(word), extracted_text, flags=re.IGNORECASE)
                captured_words.extend(matches)

            # Render captured words in a response
            if captured_words:
                response_text = 'Captured words: {}'.format(', '.join(captured_words))
            else:
                response_text = 'No specific words found.'

            return HttpResponse(response_text)

        else:
            return HttpResponse('Uploaded file is not a PDF.')

    else:
        form = UploadFileForm()

    return render(request, 'new.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
import io



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            output = process_file(file)
            
            # Ensure the response is set up correctly for file download
            response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=processed_file.xlsx'
            return response
    else:
        form = UploadFileForm()
    return render(request, 'upload_excel.html', {'form': form})
