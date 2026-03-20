from django.shortcuts import render, get_object_or_404
from .models import Project

from .models import Project, Slider
from .models import Project, Slider

def home(request):
    projects = Project.objects.all()[:6]
    sliders = Slider.objects.all()

    print(sliders)   # 👈 DEBUG (important)

    return render(request, 'home.html', {
        'projects': projects,
        'sliders': sliders
    })

def project_list(request):
    type_filter = request.GET.get('type')
    if type_filter:
        projects = Project.objects.filter(project_type=type_filter)
    else:
        projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            'your@email.com',
            ['your@email.com'],
        )

    return render(request, 'contact.html')


from django.shortcuts import render, redirect
from .models import Project

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
    return render(request, 'dashboard.html', {'projects': projects})

def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('dashboard')

from .models import Contact
from django.shortcuts import render, redirect

def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        success = True

    return render(request, 'contact.html', {'success': success})
