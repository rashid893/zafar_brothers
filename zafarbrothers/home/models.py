from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

class CompanyBooking(models.Model):
    Company_Bookings = models.CharField(max_length=50)
    customer_order_number = models.CharField(max_length=50)
    builty_number = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    booking_price = models.DecimalField(max_digits=19, decimal_places=2)
    vehicle_number = models.CharField(max_length=20)
    drivers_name = models.CharField(max_length=100)
    drivers_id = models.CharField(max_length=50)
    drivers_mobile = models.CharField(max_length=15)
    pending_at_company = models.CharField(max_length=15)
    product = models.CharField(max_length=255)
    bank_payment_slip_number = models.CharField(max_length=50, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    name_of_the_bank = models.CharField(max_length=100, blank=True, null=True)
    zafar_and_brothers_bank_account_number = models.CharField(max_length=50)
    target_bank_account = models.CharField(max_length=50)
    warehouse_booking = models.CharField(max_length=50, blank=True, null=True)
    invoice_picture = models.ImageField(upload_to='media', blank=True, null=True)
    status = models.CharField(max_length=50)
    tons = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ordered_total_bags = models.IntegerField()
    remaining_bags = models.IntegerField(blank=True, null=True)
    diversion_bags = models.IntegerField(blank=True, null=True)
    customer_innovoice_number = models.IntegerField(blank=True, null=True)
    per_bag_price=models.CharField(max_length=122,blank=True, null=True)
    Diversion_Party = models.CharField(max_length=50,blank=True, null=True)





############# modeule2 #######33333

from django.db.models import Max

class Deal(models.Model):
    trader_name = models.CharField(max_length=255,null=True,blank=True)
    system_generated_bilty_number = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    deal_price = models.DecimalField(max_digits=20, decimal_places=2)
    vehicle_number = models.CharField(max_length=20)
    drivers_name = models.CharField(max_length=255)
    drivers_id = models.CharField(max_length=20)
    stock_location = models.CharField(max_length=255)
    delivered_status = models.CharField(max_length=20)
    drivers_mobile = models.CharField(max_length=15)
    tons = models.DecimalField(max_digits=25, decimal_places=2)
    ordered_bags = models.IntegerField()
    pending_ordered_bags = models.IntegerField()
    delivered_bags = models.IntegerField(blank=True, null=True)
    dispatched = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    bank_payment_slip_number = models.FileField(upload_to='media')
    payment_type = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_expected_date = models.DateField()
    bank_name = models.CharField(max_length=255)
    zafar_and_brothers_account_number = models.CharField(max_length=255)
    target_trader_account = models.CharField(max_length=255)
    warehouse_booking = models.CharField(max_length=255)
    fare_paid_by = models.CharField(max_length=20,null=True,blank=True)
    invoice_picture = models.ImageField(upload_to='media')
    freight_paid = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(max_length=20)

@receiver(pre_save, sender=Deal)
def update_bilty_number(sender, instance, **kwargs):
    if not instance.system_generated_bilty_number:
        # Generate serial number and update bilty number
        instance.serial_number = Deal.objects.count() + 1

        # Check if the date is not None
        if instance.date:
            date_str = instance.date.strftime('%Y%m%d')
        else:
            # Use the current date if instance.date is None
            date_str = datetime.now().strftime('%Y%m%d')

        instance.system_generated_bilty_number = f"{instance.trader_name}{date_str}-{instance.serial_number}"
####### moduel3 #######################

class Module3(models.Model):
    trader_name = models.CharField(max_length=255,null=True,blank=True)
    system_generated_bilty_number = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    deal_price = models.DecimalField(max_digits=20, decimal_places=2)
    deal_freight = models.CharField(max_length=20)
    third_party_name = models.CharField(max_length=255)
    thrid_party_paid_fare = models.CharField(max_length=255)
    paid_by_self = models.CharField(max_length=255)
    owner_transport_fare = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=20)
    drivers_name = models.CharField(max_length=255)
    drivers_id = models.CharField(max_length=20)
    stock_location = models.CharField(max_length=255)
    delivered_status = models.CharField(max_length=20)
    drivers_mobile = models.CharField(max_length=15)
    tons = models.DecimalField(max_digits=25, decimal_places=2)
    ordered_total_bags = models.IntegerField()
    pending_ordered_bags_at_traders_area = models.IntegerField()
    delivered_bags = models.IntegerField(blank=True, null=True)
    dispatched = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    bank_payment_slip_number = models.FileField(upload_to='media')
    payment_type = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_expected_date = models.DateField()
    bank_name = models.CharField(max_length=255)
    zafar_and_brothers_account_number = models.CharField(max_length=255)
    target_trader_account = models.CharField(max_length=255)
    warehouse_booking = models.CharField(max_length=255)
    fare_paid_by = models.CharField(max_length=20,null=True,blank=True)
    invoice_picture = models.ImageField(upload_to='media')
    freight_paid = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(max_length=20)

@receiver(pre_save, sender=Module3)
def update_bilty_number(sender, instance, **kwargs):
    if not instance.system_generated_bilty_number:
        # Generate serial number and update bilty number
        instance.serial_number = Module3.objects.count() + 1

        # Check if the date is not None
        if instance.date:
            date_str = instance.date.strftime('%Y%m%d')
        else:
            # Use the current date if instance.date is None
            date_str = datetime.now().strftime('%Y%m%d')

        instance.system_generated_bilty_number = f"{instance.trader_name}{date_str}-{instance.serial_number}"

class Module4(models.Model):
    trader_name = models.CharField(max_length=255,null=True,blank=True)
    product_name=models.CharField(max_length=255)
    stock_in=models.CharField(max_length=122)
    stock_out=models.CharField(max_length=122)
    per_bag_price=models.CharField(max_length=122)
    total_tons = models.DecimalField(max_digits=25, decimal_places=2)
    number_of_bags = models.IntegerField()
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    stock_out_price=models.CharField(max_length=122)
    remaining_stock_price=models.CharField(max_length=122)
    profit=models.CharField(max_length=122)




class Product(models.Model):
    product_list_fertilizer = models.CharField(max_length=100)


class Trader(models.Model):
    trader = models.CharField(max_length=255)



