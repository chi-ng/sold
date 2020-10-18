import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import Item, Bid

# generic views
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from bootstrap_datepicker_plus import DateTimePickerInput

from datetime import datetime
import pytz
# list views
class ItemListView(ListView):
	model = Item
	template_name = 'welcome/base.html'
	context_object_name = 'object'
	ordering = ['-date_end']
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		items = Item.objects.filter(date_end__gt = datetime.now(pytz.UTC))
		bids = []
		for item in items:
			bids_queryset = Bid.objects.filter(item = item).order_by('-price')
			if bids_queryset.exists():
				bids.append(bids_queryset.first())
		context.update({
		'items': items,
		'bids': bids,
		})
		return context
class ItemDetailView(DetailView):
	model = Item
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		item = Item.objects.get(id=self.kwargs.get('pk'))
		bid = Bid.objects.filter(item = item).order_by('-price').first()
		now = datetime.now()
		context.update({
		'item': item,
		'bid': bid,
		'currentTime': now,
		})
		return context
class ItemCreateView(LoginRequiredMixin,CreateView):
	model = Item
	fields = ['title', 'description', 'price', 'date_start', 'date_end', 'picture']
	widget=DateTimePickerInput
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	def get_form(self):
         form = super().get_form()
         form.fields['date_start'].widget = DateTimePickerInput()
         form.fields['date_end'].widget = DateTimePickerInput()
         return form












def searchItem(request):
	context = {}
	if request.method =="GET":
		query = request.GET['search']
		bids = []
		if query  =="" or query == None:
			items = Item.objects.filter(date_end__gt = datetime.now(pytz.UTC))
		else:
			items = Item.objects.filter(title__icontains = query, date_end__gt = datetime.now(pytz.UTC))

			for item in items:
				bids_queryset = Bid.objects.filter(item = item).order_by('-price')
				if bids_queryset.exists():
					bids.append(bids_queryset.first())
		context  = {
			'items': items,
			'bids': bids,
		}
	return render(request, 'welcome/base.html', context)
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item
	fields = ['title', 'description', 'price', 'date_end']

	def get_form(self):
         form = super().get_form()
         form.fields['date_end'].widget = DateTimePickerInput()
         return form
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	def test_func(self):
		item = self.get_object()
		if self.request.user == item.user:
			return True
		else:
			return False
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Item
	success_url = '/'
	def test_func(self):
		item = self.get_object()
		if self.request.user == item.user:
			return True
		else:
			return False
class ClosedItemListView(ListView):
	model = Item
	template_name = 'welcome/closed_auctions.html'
	context_object_name = 'closed_items'
	ordering = ['-date_end']
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		items = Item.objects.filter(date_end__lt = datetime.now(pytz.UTC))
		context.update({
			'items': items,
		})
		return context
