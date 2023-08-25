from django.shortcuts import render
from django.contrib import messages
from .models import UserProfile, Extracurricular

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		extracurricular = Extracurricular.objects.filter(is_active=True)
	
		context["extracurricular"] = extracurricular
		return context
	
class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you for your message! I will be in touch soon.')
		return super().form_valid(form)
	
class ExtracurricularView(generic.ListView):
	model = Extracurricular
	template_name = "main/extracurricular.html"
	paginate_by = 6

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)
	
class ExtracurricularDetailView(generic.DetailView):
	model = Extracurricular
	template_name = "main/extracurricular-detail.html"