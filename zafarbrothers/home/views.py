from django.shortcuts import render
from .models import CompanyBooking,Deal,Module3,Module4,Product,Trader,StockInData,StockOut
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
    #data = moduelproducts(request)
    trade = modueltrade(request)

    if request.method=="POST":
       
       data=request.POST.get('client')
       data=Module4.objects.filter(customer_account_name =data)
       print("here data ",data)
       return render(request,'view_entries4.html',{'data':data})

    return render(request,'view_entries4.html')



def views_data_module6(request):
    #data = moduelproducts(request)
    trade = modueltrade(request)

    if request.method=="POST":
       
       data=request.POST.get('client')
       data=StockOut.objects.filter(customer_account=data)
       print("here data ",data)
       return render(request,'view_entries6.html',{'data':data})

    return render(request,'view_entries6.html')





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
       # ordered_total_bags = request.POST.get('ordered_total_bags')
        diversion_bags = request.POST.get('diversion_bags')
        customer_innovoice_number = request.POST.get('customer_innovoice_number')
       
        per_bag_price = request.POST.get('per_bag_price')
        Diversion_Party= request.POST.get('dclient')
        ordered_total_bags = int(request.POST.get('ordered_total_bags', 0))
        print("ordered_total_bags:", ordered_total_bags)
        # Retrieve ordered_total_bags from the request
        ordered_total_bags = int(request.POST.get('ordered_total_bags', 0))

        # Fetch the first StockInData object
        stock_in_data = StockInData.objects.first()

        if stock_in_data is not None:
            # Print the initial values
            print(f"Before Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}, ordered_total_bags={ordered_total_bags}")

            # Update the total_bags_in_Warehouse field by adding ordered_total_bags to the existing value
            stock_in_data.total_bags_in_Warehouse += ordered_total_bags

            # Save the updated object back to the database
            stock_in_data.save()

            # Print the updated values
            print(f"After Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}")
        else:
            # If no records found, create a new instance of StockInData and set total_bags_in_Warehouse to ordered_total_bags
            stock_in_data = StockInData.objects.create(total_bags_in_Warehouse=ordered_total_bags)

            # Print a message
            print("No records found. Created new record.")

            # Print the initial and updated values
            print(f"Before Update: total_bags_in_Warehouse={ordered_total_bags}, ordered_total_bags={ordered_total_bags}")
            
       
        
   
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
            Diversion_Party=Diversion_Party,
            remaining_bags=remaining_bags
        )
        company_booking.save()
        messages.success(request, 'Data added successfully')
        return render(request, 'module1.html', {'data': data})
    else:
        return render(request, 'module1.html', {'data': data})

        # Redirect to a success page or return a success message
  
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
        # ordered_bags = request.POST.get('ordered_total_bags')
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
        diversion_bags = request.POST.get('diversion_bags')
        per_bag_price = request.POST.get('per_bag_price')
        Diversion_Party = request.POST.get('dclient')
        print("cccccccccccccccpp",diversion_bags)
        ordered_bags = int(request.POST.get('ordered_total_bags', 0))

        # Fetch the first StockInData object
        stock_in_data = StockInData.objects.first()

        if stock_in_data is not None:
            # Print the initial values
            print(f"Before Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}, ordered_total_bags={ ordered_bags}")

            # Update the total_bags_in_Warehouse field by adding ordered_total_bags to the existing value
            stock_in_data.total_bags_in_Warehouse +=  ordered_bags

            # Save the updated object back to the database
            stock_in_data.save()

            # Print the updated values
            print(f"After Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}")
        else:
            # If no records found, create a new instance of StockInData and set total_bags_in_Warehouse to ordered_total_bags
            stock_in_data = StockInData.objects.create(total_bags_in_Warehouse=ordered_bags)

            # Print a message
            print("No records found. Created new record.")

            # Print the initial and updated values
            print(f"Before Update: total_bags_in_Warehouse={ordered_bags}, ordered_total_bags={ordered_bags}")
            
       

        # Convert diversion_bags and ordered_total_bags to integers
        if diversion_bags:
            try:
                diversion_bags = int(diversion_bags)
            except ValueError:
                diversion_bags = None
        else:
            diversion_bags = None

        if ordered_bags:
            try:
                ordered_bags = int(ordered_bags)
            except ValueError:
                ordered_bags = None
        else:
            ordered_bags = None

        # Calculate remaining_bags if ordered_total_bags and diversion_bags are not None
        if ordered_bags is not None and diversion_bags is not None:
            remaining_bags = ordered_bags - diversion_bags
        else:
            remaining_bags = None

        # Check if the payment type is "Hawala" and get the payment details
        if payment_type == 'Hawala':
            payment_type = request.POST.get('paymentDetails')
            print("hereeeeeeeeeeeeee is hawala ", payment_type)
        else:
            payment_type = payment_type

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
            per_bag_price=per_bag_price,
            diversion_bags=diversion_bags,
            Diversion_Party=Diversion_Party,
            remaining_bags=remaining_bags,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module2.html', {'data': data, 'trade': trade})  # Redirect to the same page or another page
    else:
        return render(request, 'module2.html', {'data': data, 'trade': trade})




 ################ MODULE 3 #############################################33



def module3(request):
    data = moduelproducts(request)
    trade = modueltrade(request)

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
        #ordered_bags = request.POST.get('ordered_total_bags')
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
        diversion_bags = request.POST.get('diversion_bags')
        per_bag_price = request.POST.get('per_bag_price')
        Diversion_Party = request.POST.get('dclient')
      
        status = request.POST.get('reach_return')
      
        print("xxxxxxxxxxxxxxxxxxxxx",trader_name,freight_paid)
        ordered_bags = int(request.POST.get('ordered_total_bags', 0))

        # Fetch the first StockInData object
        stock_in_data = StockInData.objects.first()
        

        if stock_in_data is not None:
            # Print the initial values
            print(f"Before Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}, ordered_total_bags={ ordered_bags}")

            # Update the total_bags_in_Warehouse field by adding ordered_total_bags to the existing value
            stock_in_data.total_bags_in_Warehouse +=  ordered_bags

            # Save the updated object back to the database
            stock_in_data.save()

            # Print the updated values
            print(f"After Update: total_bags_in_Warehouse={stock_in_data.total_bags_in_Warehouse}")
        else:
            # If no records found, create a new instance of StockInData and set total_bags_in_Warehouse to ordered_total_bags
            stock_in_data = StockInData.objects.create(total_bags_in_Warehouse=ordered_bags)

            # Print a message
            print("No records found. Created new record.")
        
        
        # Convert diversion_bags and ordered_total_bags to integers
        if diversion_bags:
            try:
                diversion_bags = int(diversion_bags)
            except ValueError:
                diversion_bags = None
        else:
            diversion_bags = None

        if ordered_bags:
            try:
                ordered_bags = int(ordered_bags)
            except ValueError:
                ordered_bags = None
        else:
            ordered_bags = None

        # Calculate remaining_bags if ordered_total_bags and diversion_bags are not None
        if ordered_bags is not None and diversion_bags is not None:
            remaining_bags = ordered_bags - diversion_bags
        else:
            remaining_bags = None

            # Print the initial and updated values
          


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
            per_bag_price=per_bag_price,
            diversion_bags=diversion_bags,
            Diversion_Party=Diversion_Party,
            remaining_bags=remaining_bags,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module3.html', {'data': data, 'trade': trade})
       
    else:
         return render(request, 'module3.html', {'data': data, 'trade': trade})
       
    


#####################   MODULE 4  #############################
from datetime import datetime
from .models import Module4
from datetime import datetime
from .models import Module4



# def generate_order_number_m4(customer_account_name):
#     current_date = datetime.now().strftime('%Y%m%d')  # Use datetime.now() directly
#     order_count = Module4.objects.count() + 1
#     serial_number = f"{order_count:00d}"
#     order_number = f"{customer_account_name}_{current_date}_{serial_number}"
#     return order_number


from datetime import datetime
from .models import Module4
from .models import Module4

def generate_order_number_m4(customer_account_name):
    # Count entries where customer_account_name is not None
    customer_entries_count = Module4.objects.exclude(customer_account_name__isnull=True).count()

    # Calculate the new order count based on customer entries count
    order_count = customer_entries_count + 1
    
    # Format serial number with leading zeros (if needed)
    serial_number = f"{order_count}"  # No leading zeros
    
    # Construct the order number
    order_number = f"{customer_account_name}_{serial_number}"
    
    return order_number


   


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Module4, Trader, StockInData
#from .utils import generate_order_number  # Assuming you have this utility function

def module4(request):
    trade = Trader.objects.all()
    
    if request.method == 'POST':
        stock_in = request.POST.get('stock_in')
        client = request.POST.get('client')
        product_name = request.POST.get('product_name')
        number_of_bags = request.POST.get('number_of_bags')
        per_bag_price = request.POST.get('per_bag_price')
        description = request.POST.get('description')
        credit = request.POST.get('credit')
        debit = request.POST.get('debit')

        if not stock_in or not client or not product_name or not number_of_bags or not per_bag_price or not description or not credit or not debit:
            messages.error(request, 'All fields are required.')
            return redirect('module4')

        try:
            stock_in = int(stock_in)
            number_of_bags = int(number_of_bags)
            per_bag_price = float(per_bag_price)
            credit = float(credit)
            debit = float(debit)
        except ValueError:
            messages.error(request, 'Stock In, Number of Bags, Per Bag Price, Credit, and Debit must be numbers.')
            return redirect('module4')

        stock_in_data = StockInData.objects.first()
        if stock_in_data:
            if stock_in > stock_in_data.total_bags_in_Warehouse:
                print("Stockout exceeds warehouse stock:", stock_in_data.total_bags_in_Warehouse)
                messages.error(request, 'Stockout exceeds the total bags in warehouse.')
                return redirect('module4')

        # Update warehouse stock
        stock_in_data.total_bags_in_Warehouse -= stock_in
        stock_in_data.save()

        balance = credit - debit

        # Generate order number
        order_number = generate_order_number_m4(client)

        Module4.objects.create(
            stock_in=stock_in,
            customer_account_name=client,
            product_details=product_name,
            per_bag_price=per_bag_price,
            description=description,
            customer_order_number=order_number,
            credit=credit,
            debit=debit,
            balance=balance,
        )

        messages.success(request, 'Data added successfully.',{'trade': trade})
        return redirect('module4')

    return render(request, 'module4.html', {'trade': trade})

def query_module4(request):
    if request.method == 'POST':
        data = request.POST['client']
        model = Module4.objects.filter(customer_order_number=data)
        return render(request, 'querym4.html', {'model': model})
    return render(request, 'querym4.html')

from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from .models import Module4

def entry_module4(request):
    if request.method == 'POST':
        customer_order_number = request.POST.get('client')
        description = request.POST.get('description')
        credit = float(request.POST.get('credit', 0))  # Convert to float, default to 0 if empty
        debit = float(request.POST.get('debit', 0))    # Convert to float, default to 0 if empty

        print("Customer Order Number:", customer_order_number)

        # Get the latest balance for the given customer order number
        latest_transaction = Module4.objects.filter(customer_order_number__startswith=customer_order_number).order_by('-date_time').first()

        if latest_transaction:
            previous_balance = float(latest_transaction.balance)  # Convert to float if it's a string
            # Create new customer order number
            if '_' in latest_transaction.again_customer_order_number:
                base_order_number, latest_order_index = latest_transaction.again_customer_order_number.rsplit('_', 1)
                new_order_index = int(latest_order_index) + 1
                new_customer_order_number = f"{base_order_number}_{new_order_index}"
            else:
                new_customer_order_number = f"{customer_order_number}_1"
        else:
            previous_balance = 0
            new_customer_order_number = customer_order_number

        # Calculate new balance
        new_balance = previous_balance + credit - debit

        # Create new transaction
        Module4.objects.create(
            customer_order_number=customer_order_number,
            again_customer_order_number=new_customer_order_number,
            description=description,
            credit=credit,
            debit=debit,
            balance=new_balance,
            date_time=datetime.now()  # Ensure you have this field in your model
        )
        messages.success(request, 'Data Added Successfully')
        return render(request, 'querym4.html')

    return render(request, 'querym4.html')



from datetime import datetime
#####################################################################################################################
# def generate_order_number(customer_account_name):
#     # Get the current date in YYYYMMDD format
#     current_date = datetime.datetime.now().strftime('%Y%m%d')

#     # Count the total number of orders to generate a serial number
#     order_count = StockOut.objects.count() + 1

#     # Format the serial number to be three digits, e.g., 001, 002, etc.
#     serial_number = f"{order_count:03d}"

#     # Combine the customer account name, current date, and serial number
#     order_number = f"{customer_account_name}_{current_date}_{serial_number}"

#     return order_number

def generate_order_number(customer_account_name):
    current_date = datetime.now().strftime('%Y%m%d')  # Use datetime.now() directly
    order_count = StockOut.objects.count() + 1
    serial_number = f"{order_count:00d}"
    order_number = f"{customer_account_name}_{current_date}_{serial_number}"
    return order_number














from django.shortcuts import render, redirect
from django.contrib import messages
from decimal import Decimal
from .models import StockOut, Trader, Product, StockInData, Module6Stockretail, Module4

def module6_stockout(request):
    # Fetch product and trader data
    data = moduelproducts(request)
    trade = modueltrade(request)
    if request.method == 'POST':
        # Retrieve form data
        stockout = request.POST.get('stockout')
        client = request.POST.get('client')
        product = request.POST.get('product')
        description = request.POST.get('description')
        per_bag_price = request.POST.get('per_bag_price')
         
        if stockout and client and product and per_bag_price:
            # Convert to appropriate data types
            try:
                stockout = int(stockout)
                per_bag_price = Decimal(per_bag_price)
            except ValueError:
                messages.error(request, 'Stockout and Price Per Bag must be numbers.')
                return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
          
            # Retrieve the first StockInData record
            stock_in_data = StockInData.objects.first()
            if stock_in_data:
                if stockout > stock_in_data.total_bags_in_Warehouse:
                    print("Stockout exceeds warehouse stock:", stock_in_data.total_bags_in_Warehouse)
                    messages.error(request, 'Stockout exceeds the total bags in warehouse.')
                    return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
                
                product_average = Module6Stockretail.objects.filter(product=product).first()
                if product_average:
                    profit_per_bag = per_bag_price - product_average.average_price_per_bag
                    print("Average price after calculation:", product_average.average_price_per_bag)
                    
                    # Update the total bags in the warehouse
                    stock_in_data.total_bags_in_Warehouse -= stockout
                    stock_in_data.save()
                    
                    stock_out_total_amount = stockout * per_bag_price
                    total_profit = profit_per_bag * stockout

                    # Update the average price in Module6Stockretail
                    product_average.average_price_per_bag = per_bag_price
                    product_average.save()

                    order_number = generate_order_number(client)

                    # Create StockOut record
                    
                    StockOut.objects.create(
                        stock_out=stockout,
                        customer_account=client,
                        product=product,
                        description=description,
                        stock_out_price_per_bag=per_bag_price,
                        customer_order_number=order_number,
                        stock_out_total_amount=stock_out_total_amount,
                        profit_per_bag=profit_per_bag,
                        total_profit=total_profit,
                       
                    )
                    messages.success(request, 'Stock out information saved successfully!')
                        
                    return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
            
                    
                    # return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
                else:
                    messages.error(request, 'No product average price found for the selected product.')
                    return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
            else:
                messages.error(request, 'No stock in data found.')
                return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})
        else:
            messages.error(request, 'Please fill out all required fields.')

    return render(request, 'module6_stockout.html', {'data': data, 'trade': trade})

# from django.db.models import Sum
# from django.utils import timezone
# from .models import CompanyBooking, Deal, Module3

# def get_dap_stock_data():
#     start_date = timezone.make_aware(datetime(2024, 1, 1))
#     end_date = timezone.now()
    
#     # Aggregate total amount and total bags for CompanyBooking
#     company_booking_aggregate = CompanyBooking.objects.filter(
#         product='SONA UREA P',
#         date__range=[start_date, end_date]
#     ).aggregate(
#         total_amount=Sum('order_amount'),
#         total_bags=Sum('ordered_total_bags')
#     )
    
#     # Aggregate total amount and total bags for Deal
#     deal_aggregate = Deal.objects.filter(
#         product='SONA UREA P',
#         date__range=[start_date, end_date]
#     ).aggregate(
#         total_amount=Sum('order_total_amount'),
#         total_bags=Sum('ordered_bags')
#     )
    
#     # Aggregate total amount and total bags for Module3
#     module3_aggregate = Module3.objects.filter(
#         product='SONA UREA P',
#         date__range=[start_date, end_date]
#     ).aggregate(
#         total_amount=Sum('order_total_amount'),
#         total_bags=Sum('ordered_total_bags')
#     )
    
#     # Sum the total amounts and total bags from all sources
#     total_amount = (
#         (company_booking_aggregate['total_amount'] or 0) +
#         (deal_aggregate['total_amount'] or 0) +
#         (module3_aggregate['total_amount'] or 0)
#     )
    
#     total_bags = (
#         (company_booking_aggregate['total_bags'] or 0) +
#         (deal_aggregate['total_bags'] or 0) +
#         (module3_aggregate['total_bags'] or 0)
#     )
    
#     # Calculate average price per bag
#     if total_bags > 0:
#         average_price_per_bag = total_amount / total_bags
#     else:
#         average_price_per_bag = 0
    
#     return {
#         'total_amount': total_amount,
#         'total_bags': total_bags,
#         'average_price_per_bag': average_price_per_bag
#     }

# # Example usage
# dap_stock_data = get_dap_stock_data()
# print(dap_stock_data)


from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from django.contrib import messages

from .models import CompanyBooking, Deal, Module3, Module6Stockretail, Product  # Import your models

def product_average():
    # Fetch all products
    products = Product.objects.all()
   

    start_date = timezone.make_aware(datetime(2024, 1, 1))
    end_date = timezone.now()
    results = []

    for product in products:
        product_data = product.product_list_fertilizer
        
        # Filter and aggregate data for CompanyBooking
        company_booking_data = CompanyBooking.objects.filter(
            product=product_data,
            date__range=[start_date, end_date]
        ).aggregate(
            total_amount=Sum('order_amount'),
            total_bags=Sum('ordered_total_bags')
        )
        
        # Filter and aggregate data for Deal
        deal_data = Deal.objects.filter(
            product=product_data,
            date__range=[start_date, end_date]
        ).aggregate(
            total_amount=Sum('order_total_amount'),
            total_bags=Sum('ordered_bags')
        )
        
        # Filter and aggregate data for Module3
        module3_data = Module3.objects.filter(
            product=product_data,
            date__range=[start_date, end_date]
        ).aggregate(
            total_amount=Sum('order_total_amount'),
            total_bags=Sum('ordered_total_bags')
        )
        
        # Sum the total amounts and total bags from all sources
        total_amount = (
            (company_booking_data['total_amount'] or 0) +
            (deal_data['total_amount'] or 0) +
            (module3_data['total_amount'] or 0)
        )
        
        total_bags = (
            (company_booking_data['total_bags'] or 0) +
            (deal_data['total_bags'] or 0) +
            (module3_data['total_bags'] or 0)
        )
        
        # Calculate average price per bag
        if total_bags > 0:
            average_price_per_bag = total_amount / total_bags
        else:
            average_price_per_bag = 0
        
        # Save or update the data in Module6Stockretail
        module6_stock, created = Module6Stockretail.objects.get_or_create(
            product=product_data,
            defaults={'average_price_per_bag': average_price_per_bag}
        )
        if not created:
            module6_stock.average_price_per_bag = average_price_per_bag
            module6_stock.save()

        results.append({
            'product': product_data,
            'total_amount': total_amount,
            'total_bags': total_bags,
            'average_price_per_bag': average_price_per_bag
        })
    

product_average()