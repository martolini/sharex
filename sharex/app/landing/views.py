from django.shortcuts import render
from .forms import ApplyPirateForm
from .models import Pirate

def index(request):
	modal_popup = 0
	message = None
	form_sent = 0
	if request.POST:
		form = ApplyPirateForm(request.POST)
		if form.is_valid():
			pirate = form.save()
			message = "Thank you for applying for the fleet, now it's up to the pirates to decide your destiny! You will hear from us on your email soon enough. 'Til then!".format(pirate.name)
			form_sent = 1
		else:
			modal_popup = 1
	else:
		form = ApplyPirateForm()
	num_pirates = Pirate.objects.count()
	return render(request, 'landing/index.html', {
		'form': form,
		'modal_popup': modal_popup,
		'form_sent': form_sent,
		'message': message,
		'spots_left': 97 - num_pirates,
		'questions_asked': 244,
		'war_stories_shared': 23,
		'pirates_in_line': 51 + num_pirates
		})