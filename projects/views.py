from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

from .models import Project, Slider, Contact


# =========================================================
# HOME PAGE
# =========================================================

def home(request):
    projects = Project.objects.all()[:6]
    sliders = Slider.objects.all()

    print(sliders)   # DEBUG

    return render(request, 'home.html', {
        'projects': projects,
        'sliders': sliders
    })


# =========================================================
# PROJECT LIST
# =========================================================

def project_list(request):
    type_filter = request.GET.get('type')

    if type_filter:
        projects = Project.objects.filter(
            project_type=type_filter
        )
    else:
        projects = Project.objects.all()

    return render(request, 'project_list.html', {
        'projects': projects
    })


# =========================================================
# PROJECT DETAIL
# =========================================================

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(request, 'project_detail.html', {
        'project': project
    })


# =========================================================
# ADMIN DASHBOARD
# =========================================================

def dashboard(request):

    if request.method == "POST":

        name = request.POST.get('name')
        location = request.POST.get('location')
        project_type = request.POST.get('project_type')
        status = request.POST.get('status')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Project.objects.create(
            name=name,
            location=location,
            project_type=project_type,
            status=status,
            description=description,
            image=image
        )

        return redirect('dashboard')

    projects = Project.objects.all()

    return render(request, 'dashboard.html', {
        'projects': projects
    })


# =========================================================
# DELETE PROJECT
# =========================================================

def delete_project(request, id):

    project = Project.objects.get(id=id)

    project.delete()

    return redirect('dashboard')


# =========================================================
# CONTACT FORM
# =========================================================
def contact(request):

    if request.method == "POST":

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        # ==========================================
        # SAVE MESSAGE TO DATABASE
        # ==========================================

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # ==========================================
        # EMAIL SUBJECT
        # ==========================================

        email_subject = f"New Website Enquiry - {name}"

        # ==========================================
        # EMAIL MESSAGE
        # ==========================================

        email_message = f"""
You have received a new enquiry from the NavArka website.

----------------------------------------
CONTACT DETAILS
----------------------------------------

Name: {name}
Email: {email}
Phone: {phone}

----------------------------------------
MESSAGE
----------------------------------------

{message}

----------------------------------------
Submitted through:
https://navarka.in/contact/
----------------------------------------
"""

        # ==========================================
        # SEND EMAIL
        # ==========================================

        send_mail(
            email_subject,
            email_message,
            "info@navarka.in",
            ["info@navarka.in"],
            fail_silently=False,
        )

        # ==========================================
        # REDIRECT AFTER SUCCESSFUL SUBMISSION
        # ==========================================

        return redirect('/contact/?sent=1')

    # ==========================================
    # NORMAL PAGE LOAD
    # ==========================================

    success = request.GET.get('sent') == '1'

    return render(request, 'contact.html', {
        'success': success
    })
# =========================================================
# PARTNER WITH US
# =========================================================

def partner(request):

    return render(request, "partner.html")