from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.

 
# this Class will add new item and show all item
class useradd(TemplateView):
    template_name='add-show.html'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=User.objects.all()
        context={'abc':fm, 'stu':stud}
        return context

    def post(self, request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['name']
            ue=fm.cleaned_data['email']
            up=fm.cleaned_data['password']
            reg=User(name=un, email=ue, password=up)
            reg.save()
        return HttpResponseRedirect('/')

        


# this function will add new item and show all item

class userupdate(View):
    def get(self, request, id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)    
        return render(request, 'update.html', {'form':fm})
    
    def post(self, request, id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        # return render(request, 'update.html', {'form':fm})
        return HttpResponseRedirect('/')


# This Class will delete data
 
class deletedata(RedirectView):
    url='/' 
    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs)
        # print(kwargs['id'])
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    


