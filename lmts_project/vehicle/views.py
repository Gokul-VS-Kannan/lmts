from django.shortcuts import render,redirect,get_object_or_404
from.models import Vehicle,Issue,Complaint
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def drivissue(request):
    return render(request,'vehicle_issue.html')

@login_required
def vehicleentry(request):
    return render(request,'vehicle_entry.html')

@login_required
def vehicle_entry(request):
    if request.method == 'POST':
        vehicle_id = request.POST['vid']
        registration = request.POST['vreg']
        category = request.POST['type']
        cc = request.POST['cc']

        vehicle=Vehicle(
            vehicleid=vehicle_id,
            registration=registration,  
            category=category,
            cc=cc
        )

        vehicle.save()

        return render(request,'entry_sucess.html')
    else:
        return render(request,'vehicle_entry.html')

@login_required
def vehicleissue(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('veid')
        complaint = request.POST.get('issue')
        date = request.POST.get('idate')

        # Check if the vehicle with the entered ID exists
        vehicle = get_object_or_404(Vehicle, vehicleid=vehicle_id)

        # Create a new issue instance and populate its fields
        issue_entry = Issue.objects.create(
            user=request.user,
            vehicleid=vehicle.vehicleid,
            registration=vehicle.registration,
            category=vehicle.category,
            cc=vehicle.cc,
            complaint=complaint,
            date=date,
            )

        # Create a new issue instance and populate its fields
        complaint_entry = Complaint.objects.create(
            user=request.user,
            vehicleid=vehicle.vehicleid,
            registration=vehicle.registration,
            category=vehicle.category,
            cc=vehicle.cc,
            complaint=complaint,
            date=date,
            )


        return render(request,'issue_sucess.html')

