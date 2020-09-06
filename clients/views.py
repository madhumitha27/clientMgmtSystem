from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin  # New
from django.contrib.auth.models import User

from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.views.generic import ListView , DetailView

from .forms import CommentForm , VechicleForm , VechicleCreateForm
from .models import models , VechicleByCust
from .models import Client , Comment
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render , redirect , get_object_or_404


class ClientListView ( LoginRequiredMixin , ListView ) :
    model = Client
    template_name = 'client_list.html'
    def get_queryset ( self ) :
        if self.request.user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter ( author=self.request.user)

class ClientDetailView ( LoginRequiredMixin , DetailView ) :
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView ( LoginRequiredMixin , UpdateView ) :
    model = Client
    fields = ('name' , 'notes' , 'address' , 'city' , 'state' , 'zipcode' , 'email' , 'cell_phone' , 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView ( LoginRequiredMixin , DeleteView ) :
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy ( 'client_list' )

class ClientCreateView ( LoginRequiredMixin , CreateView ) :
    model = Client
    template_name = 'client_new.html'
    fields = ('name' , 'notes' , 'address' , 'city' , 'state' , 'zipcode' , 'email' , 'cell_phone' , 'acct_number')
    login_url = 'login'

    def form_valid ( self , form ) :
        form.instance.author = self.request.user
        return super ( ).form_valid ( form )

def change_password ( request ) :
    if request.method == 'POST' :
        form = PasswordChangeForm ( data=request.POST , user=request.user )
        if form.is_valid ( ) :
            form.save ( )
            return redirect ( 'login' )
    else :
        form = PasswordChangeForm ( user=request.user )
        args = {'form' : form}
        return render ( request , 'change_password.html' , args )

class CommentCreateView ( LoginRequiredMixin , CreateView ) :
    model = Comment
    form_class = CommentForm
    template_name = 'comment_new.html'
    login_url = 'login'

    def form_valid ( self , form ) :
        pk = self.kwargs.get ( "pk" )
        cc=Client.objects.filter(id=pk)
        form.instance.client_id=pk
        form.instance.author_id = self.request.user.id
        return super ( ).form_valid ( form )

class VehicleUpdateView ( LoginRequiredMixin , UpdateView ) :
    model = VechicleByCust
    form_class = VechicleForm
    template_name = 'vehicle_edit.html'
    success_url = reverse_lazy ( 'client_list' )


class VehicleDeleteView ( LoginRequiredMixin , DeleteView ) :
    model = VechicleByCust
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy ( 'client_list' )


class VehicleCreateView ( LoginRequiredMixin , CreateView ) :
    model = VechicleByCust
    template_name = 'vehicle_new.html'
    form_class = VechicleCreateForm
    login_url = 'login'
    success_url = reverse_lazy ( 'client_list' )

    def form_valid ( self , form ) :
        pk = self.kwargs.get ( "pk" )
        cc = Client.objects.filter ( id=pk )
        form.instance.client_id = pk
        return super ( ).form_valid ( form )