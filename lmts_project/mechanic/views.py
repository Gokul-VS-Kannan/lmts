from django.shortcuts import render,redirect,get_object_or_404
from owner.models import Customuser
from.models import Mechdetails,Mechstatus,Approvedservice,Service
from vehicle.models import Issue
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def mech_reg(request):
    return render(request,'mech_reg.html')

def mech_login(request):
    return render(request,'mech_login.html')

def mechdetails(request):
    if request.method == "POST":
        full_name=request.POST['name']
        profile_pic =request.FILES['Image']
        user_name=request.POST['uname']
        password=request.POST['pwd']
        age=request.POST['age']
        phone_number=request.POST['num']
        email =request.POST['email']
        address =request.POST['address']
        skill=request.POST['skill']

        # # Check if 'image' key is present in request.FILES
        # if 'image' in request.FILES:
        #     profile_pic = request.FILES['image']
        # else:
        #     profile_pic = None

        user=Customuser.objects.create_user(
            username=user_name,
            password=password,
            is_admin=False,
            is_driver=False,
            is_user=False,
            is_mechanic=True,
            )
        
        Mechdetail=Mechdetails(
            fullname=full_name,
            profilepic=profile_pic,
            username=user,
            age=age,
            mobile=phone_number,
            email=email,
            address=address,
            skill=skill,
            )

        user.save()
        Mechdetail.save()
        
        return render(request,'mech_login.html')
    else:
        return render(request,'mech_reg.html')
    
def mechlogin(request):
    if request.method =="POST":
        usname = request.POST['username']
        pswd = request.POST['password']
        print(usname)
        print(pswd)
        user =  Customuser.objects.get(username=usname)
        print(user)
        user = authenticate(request, username=usname, password=pswd)
        print(user)

        #  retrieves the associated mechanicdtails
        if user is not None and user.is_mechanic:  # check if the user is mechanic
            # using instance for retriving
            mech_detail = Mechdetails.objects.get(username=user)
            # check the mechanic is approved or not befor login
            if mech_detail.is_approved:
                login(request, user)
                return render(request,'mech_dash.html')
            # if mechanic is not approved
            else:
                login(request, user)
                return render(request,'mech_waitlist.html')
        # if invalid login occure
        else:
            return render(request,'mech_login.html')
    else:
        return render(request,'mech_login.html')
         
def mechlogout(request):
    logout(request)
    return redirect('home')

@login_required
def mech_dash(request):
    return render(request,'mech_dash.html')

@login_required
def mech_contact(request):
    return render(request,'mech_contact.html')

@login_required
def mech_about(request):
    return render(request,'mech_about.html')

@login_required
def mechprofile(request):
    profile=Mechdetails.objects.get(username=request.user)
    return render(request,'mech_profile.html',{'profile':profile})

@login_required
def mecheditprofile(request):
    return render(request,'mech_profile_edit.html')

@login_required
def editmech(request):
    if request.method == 'POST':

        fullname = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('phnnum')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profilepic = request.FILES.get('Image')
        skill = request.POST.get('skill')

        mech=Mechdetails.objects.get(username=request.user)

        # Get the old values
        old_fullname = mech.fullname
        old_age = mech.age
        old_mobile = mech.mobile
        old_email = mech.email
        old_address = mech.address
        old_profilepic = mech.profilepic
        old_skill = mech.skill

        # Update the driver object with the new values
        mech.fullname = fullname if fullname else old_fullname
        mech.age = age if age else old_age
        mech.mobile = mobile if mobile else old_mobile
        mech.email = email if email else old_email
        mech.address = address if address else old_address
        mech.profilepic = profilepic if profilepic else old_profilepic
        mech.skill = skill if skill else old_skill

        #save updated driver object 
        mech.save(update_fields=[
            'fullname',
            'age',
            'email',
            'mobile',
            'address',
            'profilepic',
            'skill',
        ])  
        
        return redirect('mechanic:mechprofile')
    else:
        return render(request,'mech_dash.html') 
    
@login_required
def mechusername(request):
    return render(request,'mech_edit_username.html')

@login_required
def mech_user(request):
    if request.method == "POST":
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')

        if not new_username:
            return redirect('mechanic:mech_user')
        
        try:
            # Get the current user
            user = Customuser.objects.get(username=request.user)

            # Update the username in the Customuser model
            user.username = new_username
            user.save()
        
            # Check if the password is not empty
            if new_password:
                # Update the password
                user.set_password(new_password)
                user.save()
                return render(request,'mech_login.html')
            
            return render(request,'mech_login.html') 
        
        except Exception as e:
            print(e)
            return render(request,'mech_edit_username.html')  
    return render(request, 'mech_edit_username.html') 

@login_required
def mechstat(request):
    return render(request,'mech_status.html')

@login_required
def mech_status(request):
    if request.method == "POST":
        name=request.POST['name']
        date=request.POST['date']
        time=request.POST['time']
        status=request.POST['status']

        # Get the currently logged-in user
        user = request.user

        # Create a new Mechstatus object associated with the user
        Mechstat = Mechstatus(
            name=name,
            username=user,
            date=date,
            time=time,
            attendance=status,
            )

        Mechstat.save()

        return render(request,'mech_status_sucess.html')
    
@login_required
def mechserv(request):
    # Get details of issue reported
    issue = Issue.objects.all()
    return render(request,'mech_service.html',{'issue':issue})

@login_required
def ser_approve(request):
    if request.method == 'POST':
        # Assuming the ID of the issue to be approved is sent as a form parameter
        issue_id = request.POST.get('issue_id')

        # Retrieve the issue from the old table
        issue = get_object_or_404(Issue, id=issue_id)

        # Get the current user
        current_user = request.user 

        # Create a new instance in the ApprovedService table
        approved_service = Approvedservice.objects.create(
            username=current_user,
            vehicleid=issue.vehicleid,
            registration=issue.registration,
            category=issue.category,
            cc=issue.cc,
            complaint=issue.complaint,
            date=issue.date
        )

        # Delete the issue from the Issue table
        issue.delete()

        return redirect('mechanic:mechserv')

@login_required
def acpt_serv(request):
    status = Approvedservice.objects.filter(username=request.user)
    return render(request,'mech_accept_service.html',{'status':status})

@login_required
def serv_rec(request):
    return render(request,'mech_service_update.html')

@login_required
def serv_update(request):
    if request.method == "POST":
        vehicleid=request.POST['veid']
        registration=request.POST['reg']
        category=request.POST['cat']
        cc=request.POST['cc']
        complaint=request.POST['issue']
        service=request.POST['sdetail']
        service_date=request.POST['sdate']
        delivery_date=request.POST['deldate']

        # Get the current user
        current_user = request.user

        service_detail=Service(
            username=current_user,
            vehicleid=vehicleid,
            registration=registration,
            category=category,
            cc=cc,
            complaint=complaint,
            service=service,
            service_date=service_date,
            delivery_date=delivery_date,
            )
        service_detail.save()

        return render(request,'mech_dash.html')
    
@login_required
def mechdelete(request):
    if request.method =="POST":
        user=request.user

        try:
            mech_detail=Mechdetails.objects.get(username=user)

            mech_stat=Mechstatus.objects.filter(username=user)

            mech_apvdser=Approvedservice.objects.filter(username=user)

            mech_ser=Service.objects.filter(username=user)

            mech_detail.delete()
            
            mech_stat.delete()

            mech_apvdser.delete()

            mech_ser.delete()

            user.delete()

            return redirect('home')

        except Exception as e:
            print(e)
            return render(request,'mech_dash.html')