from django.db import models
from django.contrib.auth.models import User

from accounts.models import UserProfile
from . choice import *

class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)


class Gender(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Article_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

class Width(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Buyer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    
# Ok #

class Quality(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    count = models.CharField(max_length=100, null=True, blank=True)
    construction = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    gsm = models.CharField(max_length=100, null=True, blank=True)
    width = models.CharField(max_length=100, null=True, blank=True)
    s_price = models.CharField(max_length=100, null=True, blank=True)
    r_price = models.CharField(max_length=100, null=True, blank=True)
    d_price = models.CharField(max_length=100, null=True, blank=True)
    moq = models.CharField(max_length=100, null=True, blank=True)
    lead_time = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
     #     return self.order_date

class Factory(models.Model):
    factory_name = models.CharField(max_length=100, null=True, blank=True)
    factory_email = models.EmailField(null=True, blank=True)
    factory_contact = models.CharField(max_length=100, null=True, blank=True)
    factory_address = models.CharField(max_length=500, null=True, blank=True)
    factory_city = models.CharField(max_length=500, choices=CITY_CHOICES, null=True, blank=True)
    factory_state = models.CharField(max_length=500, choices=STATE_CHOICES, null=True, blank=True)
    factory_pan = models.CharField(max_length=500, null=True, blank=True)
    factory_gst = models.CharField(max_length=500, null=True, blank=True)
    region = models.CharField(max_length=500, null=True, blank=True)
    master_category = models.CharField(max_length=500, null=True, blank=True)


    # def __str__(self):
    #     return self.factory_name
 

class Vendor(models.Model):
    
    vendor_name = models.CharField(max_length=100, null=True, blank=True)
    # factory_name = models.ForeignKey(Factory, on_delete=models.DO_NOTHING, null=True, blank=True)
    vendor_owner = models.CharField(max_length=100, null=True, blank=True)
    vendor_email = models.EmailField(null=True, blank=True)
    vendor_contact = models.CharField(max_length=100, null=True, blank=True)
    vendor_address = models.CharField(max_length=500, null=True, blank=True)
    vendor_city = models.CharField(max_length=500, choices=CITY_CHOICES, null=True, blank=True)
    vendor_state = models.CharField(max_length=500, choices=STATE_CHOICES, null=True, blank=True)
    vendor_pan = models.CharField(max_length=500, null=True, blank=True)
    vendor_gst = models.CharField(max_length=500, null=True, blank=True)
    factory_type = models.CharField(max_length=50, choices=FACTORY_TYPE, null=True, blank=True)
    factory_name = models.CharField(max_length=100, null=True, blank=True)
    factory_email = models.EmailField(null=True, blank=True)
    factory_contact = models.CharField(max_length=100, null=True, blank=True)
    factory_address = models.CharField(max_length=500, null=True, blank=True)
    factory_city = models.CharField(max_length=500, choices=CITY_CHOICES, null=True, blank=True)
    factory_state = models.CharField(max_length=500, choices=STATE_CHOICES, null=True, blank=True)
    factory_pan = models.CharField(max_length=500, null=True, blank=True)
    factory_gst = models.CharField(max_length=500, null=True, blank=True)
    region = models.CharField(max_length=500, null=True, blank=True)
    # audit_type = models.CharField(max_length=500, null=True, blank=True)
    # master_category = models.CharField(max_length=500, null=True, blank=True)
    # requested_on = models.DateField(null=True, blank=True)
    # requested_by = models.CharField(max_length=500, null=True, blank=True)
    # actioned_by = models.CharField(max_length=500, null=True, blank=True)
    # request_status = models.CharField(max_length=50, choices=FACTORY_TYPE, null=True, blank=True)
    # audit_form_shared = models.BooleanField(default=False)
    # audited_on = models.DateField(null=True, blank=True)
    # onboadring_status = models.BooleanField(default=False)
    # valid_till= models.BooleanField(default=False)
    # remarks = models.CharField(max_length=500, null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return self.vendor_name
    

    


class Season(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Drop(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Domimp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Fabric_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Onoff(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Order_Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Wwnww(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Ok #
class Activity(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    department_name = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name
# Ok #

class Discussion(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=6, null=True, blank=True)
    dis_status = models.CharField(max_length=100, choices=DIS_STATUS, null=True, blank=True)


    def __str__(self):
        return self.name
    
class Details(models.Model):
    detail = models.ForeignKey(Discussion, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=2000, null=True, blank=True)
    next_follow_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.detail)

# Ok #
class Calender(models.Model):
    activity_name = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.activity_name
    # Ok #

# Ok #
class Assortment(models.Model):
    options = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    inward_month = models.CharField(max_length=100, null=True, blank=True)
    content1 = models.CharField(max_length=100, null=True, blank=True)
    content2 = models.CharField(max_length=100, null=True, blank=True)
    content3 = models.CharField(max_length=100, null=True, blank=True)
    article_type = models.ForeignKey(Article_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    brand = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    domimp = models.ForeignKey(Domimp, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    fabric_type = models.ForeignKey(Fabric_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, null=True, blank=True)
    onoff = models.ForeignKey(Onoff, on_delete=models.DO_NOTHING, null=True, blank=True)
    order_type = models.ForeignKey(Order_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    wwnww = models.ForeignKey(Wwnww, on_delete=models.DO_NOTHING, null=True, blank=True)
    assortment_date = models.DateField(null=True, blank=True)
    techpack = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.options
    # Ok #


class Travel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class OTB(models.Model):
    brand = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    article_type = models.ForeignKey(Article_Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    otb_value = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Project_created_by')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Project_updated_by')
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Order_Management(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    

class Order(models.Model):
    order_date = models.DateField(null=True, blank=True)
    order_no = models.CharField(max_length=100, null=True, blank=True)
    buyer = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    buyer_del_date = models.DateField(null=True, blank=True)
    supplier_del_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    # def save(self, *args, **kwargs):
    #     self.value = int(self.quantity) * int(self.price)
    #     # self.value = get_user_model().objects.get(id=2)    #############
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.buyer)
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.order)
    

class Pi(models.Model):
    pi_date = models.DateField(null=True, blank=True)
    pi_no = models.IntegerField(null=True, blank=True, default=0) 
    order = models.OneToOneField(Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    value = models.IntegerField(blank=True, null=True)
    buyer_del_date = models.DateField(null=True, blank=True)
    supplier_del_date = models.DateField(null=True, blank=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.pi_no = self.pi_no + 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.pi_no)

class Pi_Item(models.Model):
    pi_no = models.ForeignKey(Pi, on_delete=models.DO_NOTHING, null=True, blank=True)
    item = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pi_no)


class New_Order(models.Model):
    order_date = models.DateField(null=True, blank=True)
    order_no = models.CharField(max_length=100, null=True, blank=True)
    buyer = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop = models.ForeignKey(Drop, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_qty = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    del_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.buyer)
    
class New_Order_Details(models.Model):
    
    order = models.ForeignKey(New_Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING, null=True, blank=True)
    qty = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    del_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.quality)
    
    
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
from io import BytesIO
# import StringIO 
from django.db.models.signals import post_delete
from django.dispatch import receiver
from sorl.thumbnail import ImageField, get_thumbnail


class Image(models.Model):

    date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to ='uploads/', blank=True, null=True) 

    def save(self, *args, **kwargs):
        if self.photo:
            super().save(*args, **kwargs)
            img = Img.open(self.photo.path)
            # if img.height > 700 or img.weight > 700:
            output_size = (1080,1440)
            img.thumbnail(output_size)
            img.save(self.photo.path)
#     def save(self, *args, **kwargs):
#         width = 1080
#         height = 1440
#         size = (width,height)
#         isSame = False
#         if self.image:
#             try:
#                 this = Image.objects.get(id=self.id)
#                 if this.photo==self.photo :
#                     isSame= True
#             except: pass # when new photo then we do nothing, normal case

#             # image = Img.open(StringIO.StringIO(self.photo.read()))
#             image = Img.open(BytesIO(self.image.read()))
#             (imw, imh) = image.size
#             if (imw>width) or (imh>height) :
#                 image.thumbnail(size, Img.ANTIALIAS)

#             #If RGBA, convert transparency
#             if image.mode == "RGBA":
#                 image.load()
#                 background = Img.new("RGB", image.size, (255, 255, 255))
#                 background.paste(image, mask=image.split()[3]) # 3 is the alpha channel
#                 image=background


#             output = BytesIO()
#             image.save(output, format='JPEG', quality=72)
#             output.seek(0)
#             self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output, None)

#         try:
#             this = Image.objects.get(id=self.id)
#             if this.image==self.image or isSame :
#                 self.image=this.image
#             else :
#                 this.image.delete(save=False)
#         except: pass # when new photo then we do nothing, normal case 

#         super(Image, self).save(*args, **kwargs)

# @receiver(post_delete, sender=Image)
# def photo_post_delete_handler(sender, **kwargs):
#     instance = kwargs['instance']
#     storage, path = instance.photo.storage, instance.photo.path
#     if (path!='.') and (path!='/') and (path!='photo/') and (path!='photo/.'):
#         storage.delete(path)


from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
