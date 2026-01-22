from django.shortcuts import render,redirect,get_object_or_404
from vehicle.models import Vehicle,Issue,Complaint
from.models import Driverdetails,Driverentry,Driverstatus
from owner.models import Customuser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def driver_reg(request):
    return render(request,'driver_reg.html')

def drivdetails(request):
    if request.method == "POST":
        full_name=request.POST['name']
        profile_pic =request.FILES['Image']
        user_name=request.POST['uname']
        password=request.POST['pwd']
        age=request.POST['age']
        phone_number=request.POST['phnnum']
        email =request.POST['email']
        address =request.POST['address']
        license_no =request.POST['dlno']

        #  Check if 'image' key is present in request.FILES
        # if 'Image' in request.FILES:
        #     profile_pic = request.FILES['Image']
        # else:
        #     profile_pic = None

        #Create a new user 
        user=Customuser.objects.create_user(
            username=user_name,
            password=password,
            is_admin=False,
            is_mechanic=False,
            is_driver=True,
            is_user=False,
            )
        
        # Create Driverdetails instance
        Drivdetail=Driverdetails(
            fullname=full_name,
            profilepic=profile_pic,
            username=user,
            age=age,
            mobile=phone_number,
            email=email,
            address=address,
            license_no=license_no,
            )

        # Save both the user and driver details
        user.save()
        Drivdetail.save()
        
        return render(request,'driver_login.html')
    else:
        return render(request,'driver_reg.html')
    
def driver_login(request):
    return render(request,'driver_login.html')

def drivlogin(request):
    if request.method =="POST":
        usname = request.POST['username']
        pswd = request.POST['password']
        
        user =  Customuser.objects.get(username=usname)
       
        user = authenticate(request, username=usname, password=pswd)
        
        #  retrieves the associated driverdtails
        if user is not None and user.is_driver: # Check if the user is a driver
            # using instance for retriving
            driv_detail = Driverdetails.objects.get(username=user)
            print(driv_detail)
            # check the driver is approved or not befor login
            if driv_detail.is_approved:
                login(request, user)
                return render(request,'driver_dash.html')
            # if driver is not approved
            else:
                login(request, user)
                return render(request,'driver_waitlist.html')
        # if invalid login occure
        else:
            return render(request,'driver_login.html')
        
    else:
        return render(request,'driver_login.html')
    
def drivlogout(request):
    logout(request)
    return redirect('home')

@login_required
def driver_dash(request):
    return render(request,'driver_dash.html')

@login_required
def driv_contact(request):
    return render(request,'driver_contact.html')

@login_required
def driv_about(request):
    return render(request,'driver_about.html')

@login_required
def driv_contact(request):
    return render(request,'driver_contact.html')

@login_required
def driv_about(request):
    return render(request,'driver_about.html')

@login_required
def drivprofile(request):
    profile=Driverdetails.objects.get(username=request.user)
    return render(request,'driver_profile.html',{'profile':profile})  

@login_required
def driveditprofile(request):
    return render(request,'driver_profile_edit.html')

@login_required
def editdriv(request):
    if request.method == 'POST':

        fullname = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('phnnum')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profilepic = request.FILES.get('Image')
        license_no = request.POST.get('dlno')

        driver=Driverdetails.objects.get(username=request.user)

        # Get the old values
        old_fullname = driver.fullname
        old_age = driver.age
        old_mobile = driver.mobile
        old_email = driver.email
        old_address = driver.address
        old_profilepic = driver.profilepic
        old_license_no = driver.license_no

        # Update the driver object with the new values
        driver.fullname = fullname if fullname else old_fullname
        driver.age = age if age else old_age
        driver.mobile = mobile if mobile else old_mobile
        driver.email = email if email else old_email
        driver.address = address if address else old_address
        driver.profilepic = profilepic if profilepic else old_profilepic
        driver.license_no = license_no if license_no else old_license_no

        #save updated driver object 
        driver.save(update_fields=[
            'fullname',
            'age',
            'email',
            'mobile',
            'address',
            'profilepic',
            'license_no',
        ])  
        
        return redirect('driver:drivprofile')
    else:
        return render(request,'driver_dash.html') 

@login_required
def drivusername(request):
    return render(request,'driver_edit_username.html')

@login_required
def driv_user(request):
    if request.method == "POST":
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')
        if not new_username:
            return redirect('driver:driv_user')
    
        try:
            # Get the current user
            user = Customuser.objects.get(username=request.user)

            # Update the username in the Customuser model
            user.username = new_username
            user.save()

            # Update the username in related models (if any)
            # Driverdetails.objects.filter(username=request.user).update(username=new_username)
            # Driverstatus.objects.filter(username=request.user).update(username=new_username)
            # Driverentry.objects.filter(username=request.user).update(username=new_username)

            # Check if the password is not empty
            if new_password:
                # Update the password
                user.set_password(new_password)
                user.save()
                return render(request,'driver_login.html')  
            return render(request,'driver_login.html')
        except Exception as e:
            print(e)
            return render(request,'driver_edit_username.html')  
    return render(request, 'driver_login.html') 

@login_required
def drivstat(request):
    return render(request,'driver_status.html')

@login_required
def driv_status(request):
    if request.method == "POST":
        name=request.POST['name']
        date=request.POST['date']
        time=request.POST['time']
        status=request.POST['status']

        # Get the currently logged-in user
        user = request.user

        # Create a new Driverstatus object associated with the user
        Drivstat = Driverstatus(
            name=name,
            username=user,
            date=date,
            time=time,
            attendance=status,
            )

        Drivstat.save()

        return render(request,'driver_staus_sucess.html')
    
# display vehicle details
@login_required
def vehicle_details(request):
    vehicle_details = Vehicle.objects.all()
    return render(request, 'vehicle_details.html', {'vehicle_details': vehicle_details})

# vehicle selection procedure
@login_required
def drivvehicle(request):
    # simply render the page for entering details
    return render(request,'driver_selection.html')

@login_required
def vehicle_selection(request):
    if request.method == 'POST':
        user = request.user
        vehicle_id = request.POST.get('veid')
        date = request.POST.get('date')

        # Check if the vehicle with the entered ID exists
        vehicle = get_object_or_404(Vehicle, vehicleid=vehicle_id)

        # Create a new Driverentry instance and populate its fields
        driver_entry = Driverentry.objects.create(
            username=user,
            vehicleid=vehicle.vehicleid,
            registration=vehicle.registration,
            category=vehicle.category,
            cc=vehicle.cc,
            date=date,
            )

        return render(request,'vehicle_sucess.html')
    
@login_required
def drivdelete(request):
    if request.method == "POST":
        user=request.user

        try:
            driv_detail=Driverdetails.objects.get(username=user)

            driv_stat=Driverstatus.objects.filter(username=user)

            driv_entry=Driverentry.objects.filter(username=user)

            driv_issue=Issue.objects.filter(user=user)

            driv_comp=Complaint.objects.filter(user=user)

            driv_detail.delete()

            driv_stat.delete()

            driv_entry.delete()

            driv_issue.delete()

            driv_comp.delete()

            user.delete()

            return redirect('home')
        
        except Exception as e:
            print(e)
            return render(request,'driver_dash.html')