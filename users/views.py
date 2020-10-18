from django.shortcuts import render, redirect

from welcome.models import Item, Bid

#forms
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm

from django.contrib import messages

# generic views
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from datetime import datetime
import pytz



# user manager
def register(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "users/signup.html",context)

@login_required
def profile(request):
    if request.method =="POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            redirect("welcome:index")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/view_profile.html', context)
class MyItemListView(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'users/my_items.html'
    context_object_name = 'items'
    def get_queryset(self):
        user = self.request.user
        new_context = Item.objects.filter(user = user).order_by('-date_end')
        return new_context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'currentTime': datetime.now(),
        })
        return context
class BidCreateView(LoginRequiredMixin,CreateView):
    model = Bid
    fields = ['price']
    def form_valid(self, form):
        form.instance.item = Item.objects.get(id=self.kwargs.get('pk'), date_end__gt =datetime.now(pytz.UTC))
        form.instance.user = self.request.user
        form.instance.date_and_time = datetime.now(pytz.UTC)
        return super().form_valid(form)
class MyBidListView(LoginRequiredMixin, ListView):
	model = Bid
	template_name = 'users/my_bids.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		myBids = Bid.objects.filter(user = self.request.user).order_by('-date_and_time')
		context.update({
			'myBids': myBids,
		})
		return context
