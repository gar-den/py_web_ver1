# deals url request
# bring data from db and send to template(HTML)

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = 'index.html'

