from django.shortcuts import render
from .models import project

# Create your views here.
def project_list(request, projects=None):
    project = projects.objects.all()
    print(project)
    context = {'project':project}
    return render(request, 'project.html', context)

def project_detail(request, project_id, projects=None):
    project = projects.objects.get(id=1)
    print(project)
    context = {'project':project}
    return render(request, 'project.html', context) 