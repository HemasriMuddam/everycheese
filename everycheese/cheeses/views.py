from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Cheese, Rating
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import logging  # Import the logging module


# Create a logger object
log = logging.getLogger("root")


class CheeseListView(ListView):
    model = Cheese
class CheeseDetailView(DetailView):
    model = Cheese
class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness',
                'country_of_origin']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
class CheeseUpdateView(LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = [
    'name',
    'description',
    'firmness',
    'country_of_origin'
    ]
    
    action = "Update"

    def get_context_data(self, **kwargs):
        log.info("FOUND RATING!!!!!")
        ctx = super(CheeseUpdateView, self).get_context_data(**kwargs)
        _slug = self.kwargs.get("slug")
        ch = Cheese.objects.all().filter(slug = _slug).first()

        if ch ==None:
            ctx["rating"] =0
            return
        r = Rating.objects.all().filter(creator = self.request.user, cheese = ch).first()

        if r != None:
            ctx["rating"] = r.i_rating
        else:
            ctx["rating"] = 0
        return ctx
    
    
class CheeseDeleteView(DeleteView):
    model = Cheese
    action = "Delete"
    success_url = reverse_lazy('cheeses:list')  # Redirect after deletion
    template_name = 'cheeses/cheese_confirm_delete.html'  # Template for confirmation
