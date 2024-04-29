from django.shortcuts import render
from .models import CompanyBooking,Deal,Module3,Module4,Product,Trader
from django.contrib import messages
from datetime import datetime


# def moduel1products(request):
#     data=Product.objects.all()
#     print("cccccccccccccccccccc",data)
#     return render(request,'module1.html',{'data':data})
def moduelproducts(request):
    data = Product.objects.all()
    # print("cccccccccccccccccccc", data)
    return data

def modueltrade(request):
    trade = Trader.objects.all()
    # print("cccccccccccccccccccc", trade)
    return trade
# Create your views here.
def home(request):
    return render(request,'home.html')

def views_data_module1(request):

    if request.method=="POST":
       
       data=request.POST.get('client')
       data=CompanyBooking.objects.filter(Company_Bookings=data)
       print("here data ",data)
       return render(request,'view_entreis1.html',{'data':data})

    return render(request,'view_entreis1.html')

def views_data_module2(request):

    if request.method=="POST":
       
       data=request.POST.get('client')

       data=Deal.objects.filter(trader_name=data)
       print("here data ",data)
       return render(request,'view_entries2.html',{'data':data})

    return render(request,'view_entries2.html')

def views_data_module3(request):

    if request.method=="POST":
       
       data=request.POST.get('client')
       data=Module3.objects.filter(trader_name=data)
       print("here data ",data)
       return render(request,'view_entries3.html',{'data':data})

    return render(request,'view_entries3.html')


def views_data_module4(request):

    if request.method=="POST":
       
       data=request.POST.get('client')
       data=Module4.objects.filter(trader_name=data)
       print("here data ",data)
       return render(request,'view_entries4.html',{'data':data})

    return render(request,'view_entries4.html')




from django.contrib import messages
from .models import CompanyBooking

def module1(request):
    data = moduelproducts(request)
    if request.method == 'POST':
        company_bookings = request.POST.get('client')
        manual_bilty = request.POST.get('manual_bilty')
        customer_order_number = request.POST.get('customer_order_number')
        booking_price = request.POST.get('booking_price')
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        drivers_mobile = request.POST.get('drivers_mobile')
        pending_at_company = request.POST.get('pending_at_company')
        product = request.POST.get('product')
        products_bank_payment_slip_number = request.POST.get('products_bank_payment_slip_number')
        payment_amount = request.POST.get('payment_amount')
        order_amount = request.POST.get('order_amount')
        name_of_the_bank = request.POST.get('name_of_the_bank')
        zafar_and_brothers_bank_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_bank_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        invoice_picture = request.FILES.get('invoice_picture')
        status = request.POST.get('reach_return')
        tons = request.POST.get('tons')
        ordered_total_bags = request.POST.get('ordered_total_bags')
        diversion_bags = request.POST.get('diversion_bags')
        customer_innovoice_number = request.POST.get('customer_innovoice_number')
        print("ccccccccccccccccccccccccc",customer_innovoice_number)
        per_bag_price = request.POST.get('per_bag_price')
        Dcompany_bookings = request.POST.get('dclient')
        
        # Convert diversion_bags and ordered_total_bags to integers
        if diversion_bags:
            try:
                diversion_bags = int(diversion_bags)
            except ValueError:
                diversion_bags = None
        else:
            diversion_bags = None

        if ordered_total_bags:
            try:
                ordered_total_bags = int(ordered_total_bags)
            except ValueError:
                ordered_total_bags = None
        else:
            ordered_total_bags = None

        # Calculate remaining_bags if ordered_total_bags and diversion_bags are not None
        if ordered_total_bags is not None and diversion_bags is not None:
            remaining_bags = ordered_total_bags - diversion_bags
        else:
            remaining_bags = None

        # Convert customer_innovoice_number to integer
        

        # Create a CompanyBooking object and save it to the database
        company_booking = CompanyBooking(
            Company_Bookings=company_bookings,
            builty_number=manual_bilty,
            customer_order_number=customer_order_number,
            booking_price=booking_price,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            drivers_mobile=drivers_mobile,
            pending_at_company=pending_at_company,
            product=product,
            bank_payment_slip_number=products_bank_payment_slip_number,
            payment_amount=payment_amount,
            order_amount=order_amount,
            name_of_the_bank=name_of_the_bank,
            zafar_and_brothers_bank_account_number=zafar_and_brothers_bank_account_number,
            target_bank_account=target_bank_account,
            warehouse_booking=warehouse_booking,
            invoice_picture=invoice_picture,
            status=status,
            tons=tons,
            ordered_total_bags=ordered_total_bags,
            diversion_bags=diversion_bags,
            customer_innovoice_number=customer_innovoice_number,
            per_bag_price=per_bag_price,
            Diversion_Company_Bookings= Dcompany_bookings,
            remaining_bags=remaining_bags
        )
        company_booking.save()
        messages.success(request, 'Data added successfully')
        return render(request, 'module1.html', {'data': data})
    else:
        return render(request, 'module1.html', {'data': data})

        # Redirect to a success page or return a success message
  
    return render(request,'module1.html', {'data': data})
from datetime import datetime
from .models import Deal  # Replace 'Deal' with your actual model





def module2(request):
    data = moduelproducts(request)
    trade = modueltrade(request)
    if request.method == 'POST':
        trader_name = request.POST.get('client')
       
        deal_price = request.POST.get('deal_price')
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        stock_location = request.POST.get('stock_location')
        delivered_status = request.POST.get('delevery')
        drivers_mobile = request.POST.get('drivers_mobile')
        tons = request.POST.get('tons')
        ordered_bags = request.POST.get('ordered_total_bags')
        pending_ordered_bags = request.POST.get('pending_at_company')
        delivered_bags = request.POST.get('deliveredbags')
        dispatched = request.POST.get('dispatchedStatus')
        product = request.POST.get('product')
        bank_payment_slip_number = request.FILES.get('products_bank_payment_slip_number')
        payment_type = request.POST.get('paymentType')
        payment_amount = request.POST.get('payment_amount')
        order_total_amount = request.POST.get('order_amount')
        payment_expected_date = request.POST.get('expec_date')
        bank_name = request.POST.get('name_of_the_bank')
        zafar_and_brothers_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_trader_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        fare_paid_by = request.POST.get('fareedby')
        invoice_picture = request.FILES.get('invoice_picture')
        freight_paid = request.POST.get('freight-paid')
        status = request.POST.get('reach_return')
        print("xxxxxxxxxxxxxxxxxxxxx",trader_name,freight_paid)
           # Check if the payment type is "Hawala" and get the payment details
        if payment_type == 'Hawala':
            payment_type  = request.POST.get('paymentDetails')
            print("hereeeeeeeeeeeeee is hawala ",payment_type )
        else:
            payment_type =payment_type 

        
        
       
        deal = Deal(
            trader_name=trader_name,
          
            deal_price=deal_price,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            stock_location=stock_location,
            delivered_status=delivered_status,
            drivers_mobile=drivers_mobile,
            tons=tons,
            ordered_bags=ordered_bags,
            pending_ordered_bags=pending_ordered_bags,
            delivered_bags=delivered_bags,
            dispatched=dispatched,
            product=product,
            bank_payment_slip_number=bank_payment_slip_number,
            payment_type=payment_type,
            payment_amount=payment_amount,
            order_total_amount=order_total_amount,
            payment_expected_date=payment_expected_date,
            bank_name=bank_name,
            zafar_and_brothers_account_number=zafar_and_brothers_account_number,
            target_trader_account=target_trader_account,
            warehouse_booking=warehouse_booking,
            fare_paid_by=fare_paid_by,
            invoice_picture=invoice_picture,
            freight_paid=freight_paid,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module2.html',{'data': data,'trade':trade}) # Redirect to the same page or another page
    else:
        return render(request, 'module2.html',{'data': data,'trade':trade})
 
 ################ MODULE 3 #############################################33



def module3(request):

    if request.method == 'POST':
        trader_name = request.POST.get('client')
       
        deal_price = request.POST.get('deal_price')
        deal_freight = request.POST.get('deal-freight')
        third_party_name = request.POST.get('third_party_name')
        third_party_paid_fare = request.POST.get('third_party_paid_fare')
        paid_by_self = request.POST.get('paid_by-self')
        owner_transport_fare = request.POST.get('owner_transport_fare')

        
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        stock_location = request.POST.get('stock_location')
        delivered_status = request.POST.get('delevery')
        drivers_mobile = request.POST.get('drivers_mobile')
        tons = request.POST.get('tons')
        ordered_bags = request.POST.get('ordered_total_bags')
        pending_ordered_bags = request.POST.get('pending_at_company')
        delivered_bags = request.POST.get('deliveredbags')
        dispatched = request.POST.get('dispatchedStatus')
        product = request.POST.get('product')
        bank_payment_slip_number = request.FILES.get('products_bank_payment_slip_number')
        payment_type = request.POST.get('paymentType')
        payment_amount = request.POST.get('payment_amount')
        order_total_amount = request.POST.get('order_amount')
        payment_expected_date = request.POST.get('expec_date')
        bank_name = request.POST.get('name_of_the_bank')
        zafar_and_brothers_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_trader_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        fare_paid_by = request.POST.get('fareedby')
        invoice_picture = request.FILES.get('invoice_picture')
        freight_paid = request.POST.get('freight-paid')
        status = request.POST.get('reach_return')
        print("xxxxxxxxxxxxxxxxxxxxx",trader_name,freight_paid)
           # Check if the payment type is "Hawala" and get the payment details
        if payment_type == 'Hawala':
            payment_type  = request.POST.get('paymentDetails')
            print("hereeeeeeeeeeeeee is hawala ",payment_type )
        else:
            payment_type =payment_type 

        
        
       
        deal = Module3(
            trader_name=trader_name,
          
            deal_price=deal_price,
            deal_freight=deal_freight,
            third_party_name=third_party_name,
            thrid_party_paid_fare=third_party_paid_fare,
            paid_by_self=paid_by_self,
            owner_transport_fare=owner_transport_fare,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            stock_location=stock_location,
            delivered_status=delivered_status,
            drivers_mobile=drivers_mobile,
            tons=tons,
            ordered_total_bags=ordered_bags,
            pending_ordered_bags_at_traders_area =pending_ordered_bags,
            delivered_bags=delivered_bags,
            dispatched=dispatched,
            product=product,
            bank_payment_slip_number=bank_payment_slip_number,
            payment_type=payment_type,
            payment_amount=payment_amount,
            order_total_amount=order_total_amount,
            payment_expected_date=payment_expected_date,
            bank_name=bank_name,
            zafar_and_brothers_account_number=zafar_and_brothers_account_number,
            target_trader_account=target_trader_account,
            warehouse_booking=warehouse_booking,
            fare_paid_by=fare_paid_by,
            invoice_picture=invoice_picture,
            freight_paid=freight_paid,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module3.html') # Redirect to the same page or another page
    else:
        return render(request, 'module3.html')
    


#####################   MODULE 4  #############################
    



def module4(request):
    if request.method == 'POST':
        trader_name = request.POST.get('client')
        product_name = request.POST.get('product_name')
        stock_in = request.POST.get('stock_in')
        stock_out = request.POST.get('stock_out')
        per_bag_price = request.POST.get('per_bag_price')
        total_tons = request.POST.get('total_tons')
        number_of_bags = request.POST.get('number_of_bags')
        total_price = request.POST.get('total_price')
        stock_out_price = request.POST.get('stock_out_price')
        remaining_stock_price = request.POST.get('remaining_stock_price')
        profit = request.POST.get('profit')

        # Create a Module4 object and save it to the database
        module4_instance = Module4(
            trader_name=trader_name,
            product_name=product_name,
            stock_in=stock_in,
            stock_out=stock_out,
            per_bag_price=per_bag_price,
            total_tons=total_tons,
            number_of_bags=number_of_bags,
            total_price=total_price,
            stock_out_price=stock_out_price,
            remaining_stock_price=remaining_stock_price,
            profit=profit
        )
        module4_instance.save()

        # Redirect to a success page or another view
        messages.success(request, 'Data added successfully')
        return render(request, 'module4.html')  

    return render(request, 'module4.html')


    

