from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import *
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.forms.models import inlineformset_factory
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


def user_login (request):
    context ={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect (reverse('home'))
        else:
            context["error"]= "Provide valid credentials!!"
            return render (request,'user_login.html',context)

    else:
        return render (request,'user_login.html',context)
        
    return render(request, 'user_login.html')

@login_required(login_url='/crinsp/login')
def home (request):
    return render (request,'home.html')


class TestingCreateView(CreateView):
    template_name = 'testing.html'
    model = Testing
    fields = ["Testing_Date","Testing_Shift","Rolling_Mill","Rail_Section","Testing_Result",]


    def get_form(self, form_class=None):
        # next 5 lines are just for placing place holder can be removed in java script is enabled for datepicker
        if form_class is None:
            form_class = self.get_form_class()
        form = super(TestingCreateView, self).get_form(form_class)
        form.fields['Testing_Date'].widget = forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
        return form
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["Heat_Status"] = Heat_StatusFormset(self.request.POST)
        else:
            data["Heat_Status"] = Heat_StatusFormset()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        Heat_Status = context["Heat_Status"]
        user = self.request.user
        form.instance.IE_Testing = user
        
        self.object = form.save()
        if Heat_Status.is_valid():
            Heat_Status.instance = self.object
            Heat_Status.save()
        #return super().form_valid(form)
        return super(TestingCreateView, self).form_valid(form)
   
    def get_success_url(self):
        return reverse ('home')


Heat_StatusFormset = inlineformset_factory(Testing, Heat_Status, fields=('Heat_Number',), can_delete = False, extra=9)
    

@login_required(login_url='/crinsp/login')
def status (request):
   
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match= Heat_Status.objects.filter(Q(Heat_Number__iexact=srch))

            if match:
                return render (request,'status.html',{'sr':match})
            else:
                messages.error(request,'Heat Number not Tested Yet! For Trial Purpose you can enter Heat number: 123456')
        else:
            return HttpResponseRedirect('/crinsp/status')
    return render(request,'status.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })