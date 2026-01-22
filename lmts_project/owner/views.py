from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from driver.models import Driverdetails,Driverentry,Driverstatus
from mechanic.models import Mechdetails,Service,Approvedservice,Mechstatus
from user.models import Orderdetails,Userdetails
from vehicle.models import Complaint,Vehicle
from django.contrib.auth.decorators import login_required
# Create your views here.


def admin_login(request):
    return render(request,'owner_login.html')

def admlogin(request):
    username=request.POST['uname']
    pswd=request.POST['pwd']
    user=authenticate(request,username=username,password=pswd)

    if user is not None:
        login(request,user)
        if user.is_superuser:
            return render(request,'owner_dash.html')
        else:
            return render(request,"owner_login.html",{'msg':"You Are Not An Admin"})
    else:
        return render(request,"owner_login.html",{'msg':"You Details Doesn't Exist/Check Your Username And Password"})
    
def adlogout(request):
    logout(request)
    return redirect('home')

@login_required
def owner_dash(request):
    return render(request,'owner_dash.html')

@login_required
def own_contact(request):
    return render(request,'owner_contact.html')

@login_required
def own_about(request):
    return render(request,'owner_about.html')

@login_required
def driv_owner_dash(request):
    return render(request,'owner_dash_driver.html')

@login_required
def mech_owner_dash(request):
    return render(request,'owner_dash_mech.html')

@login_required
def user_owner_dash(request):
    return render(request,'owner_dash_user.html')

@login_required
def driv_info(request):
    # Get only drivers whose is_approved field is False
    driver = Driverdetails.objects.filter(is_approved=False)

    return render(request,'driver_details.html',{'driver':driver})

@login_required
def driv_approve(request):
    if request.method =="POST":
        username_id = request.POST.get('username')
        # Get the driver instance based on the username
        driver = Driverdetails.objects.get(username_id=username_id)

        # Update the is_approved field to True
        driver.is_approved = True

        # Save the changes to the database
        driver.save()

        return redirect('owner:driv_info')

@login_required
def driv_deny(request):
    if request.method == "POST":
        username_id = request.POST.get('username')
        # get the driver instance based on username
        driver = Driverdetails.objects.get(username_id=username_id)

        # delete the driver
        driver.delete()

        return redirect('owner:driv_info')

@login_required
def driv_apvd(request):
    # Get only drivers whose is_approved field is True
    driver = Driverdetails.objects.filter(is_approved=True)

    return render(request,'driver_approved.html',{'driver':driver})

@login_required
def stat_driver(request):
    return render(request,'driver_stat.html')

@login_required
def statviewdriv(request):
    if request.method == "POST":
        date = request.POST['date']

        # get details from mechstatus table
        status=Driverstatus.objects.filter(date=date)

        return render(request,'driver_display_stat.html',{'status':status})

@login_required
def driv_work(request):
    return render(request,'driver_work.html')

@login_required
def viewvehicle(request):
    if request.method == "POST":
        date = request.POST['date']

        # get details from mechstatus table
        entry=Driverentry.objects.filter(date=date)

        return render(request,'driver_display_vehicle.html',{'entry':entry})

@login_required
def mech_info(request):
    # Get only mechanic whose is_approved field is False
    mech=Mechdetails.objects.filter(is_approved=False)

    return render(request,'mech_details.html',{'mech':mech})

@login_required
def mech_approve(request):
    if request.method =="POST":
        username_id = request.POST.get('username')
        # Get the MECHANIC instance based on the username
        mechanic = Mechdetails.objects.get(username_id=username_id)

        # Update the is_approved field to True
        mechanic.is_approved = True

        # Save the changes to the database
        mechanic.save()

        return redirect('owner:mech_info')
    
@login_required
def mech_deny(request):
    if request.method == "POST":
        username_id = request.POST.get('username')

        # Get the mechanic instace based on the username
        mechanic = Mechdetails.objects.get(username_id=username_id)

        # delete the mechanic
        mechanic.delete()

        return redirect('owner:mech_info')
    
@login_required
def mech_apvd(request):

    # Get only mechanic whose is_approved field is True
    mech=Mechdetails.objects.filter(is_approved=True)

    return render(request,'mech_approved.html',{'mech':mech})

@login_required
def stat_mech(request):
    return render(request,'mech_stat.html')

@login_required
def statviewmech(request):
    if request.method == "POST":
        date = request.POST['date']

        # get details from mechstatus table
        status=Mechstatus.objects.filter(date=date)

        return render(request,'mech_display_stat.html',{'status':status})

@login_required
def maintenance(request):
    # Get details of issue reported
    complaint = Complaint.objects.all()
    return render(request,'vehicle_issue_list.html',{'complaint':complaint})

@login_required
def serviceapproval(request):
    # Get details of issue reported
    complaint = Approvedservice.objects.all()
    return render(request,'accepted_service.html',{'complaint':complaint})

@login_required
def histmain(request):
    # Get details of service records
    history = Service.objects.all()
    return render(request,'service_history.html',{'history':history})

@login_required
def userinfo(request):

    # Get all the user details from userdetail table
    user = Userdetails.objects.all()

    return render(request,'user_details.html',{'user':user})

@login_required
def orderapproval(request):
    # get only order details whose is_approved and is_denied fields are both false
    order=Orderdetails.objects.filter(is_approved=False,is_denied=False)

    return render(request,'order_details.html',{'order':order})

@login_required
def order_approve(request):
    if request.method == "POST":
        id = request.POST.get('id')
        # Get the OrderAdmin instance based on the order_id
        order = Orderdetails.objects.get(id=id)
        

        # Update the is_approved field to True
        order.is_approved = True

        # Save the changes to the database
        order.save()

        return redirect('owner:orderapproval')

@login_required
def order_apvd(request):

    # get all approved orders
    order = Orderdetails.objects.filter(is_approved=True)

    return render(request,'order_approved.html',{'order':order})

@login_required
def order_deny(request):
    if request.method == "POST":
        id = request.POST.get('id')
        # Get the OrderAdmin instance based on the order_id
        order = Orderdetails.objects.get(id=id)
        
        # Update the is_denied field to True
        order.is_denied = True

        # Save the changes to the database
        order.save()

        return redirect('owner:orderapproval')

@login_required
def denyed_order(request):

    # get all approved orders
    order = Orderdetails.objects.filter(is_denied=True)

    return render(request,'order_deny.html',{'order':order})

