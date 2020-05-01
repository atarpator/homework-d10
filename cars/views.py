from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Car

# Create your views here.

class index(ListView):    
    model = Car    
    context_object_name = "cars"
    template_name = "index.html" 
    paginate_by = 12

    def get_queryset(self):
        cars = super().get_queryset()
        query_dict = dict(self.request.GET.lists())
                
        maker_Q = Q(maker__icontains=query_dict.get("maker", [""])[0])
        model_Q = Q(car_model__icontains=query_dict.get("model", [""])[0])

        year_Q = Q(year__isnull=False)
        if "year" in query_dict:
            try:
                query_dict["year"] = [int(x) for x in query_dict["year"]]
                year_Q = Q(year__in=query_dict["year"])
            except ValueError:            
                pass

        transmission_Q = Q(transmission__isnull=False)
        if "transmission" in query_dict:
            try:
                query_dict["transmission"] = [int(x) for x in query_dict["transmission"]]
                transmission_Q = Q(transmission__in=query_dict["transmission"])
            except ValueError:            
                pass            

        color_Q = Q(color__icontains=query_dict.get("color", [""])[0])

        cars = cars.filter(maker_Q & model_Q & year_Q & transmission_Q & color_Q)

        return cars

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_copy = self.request.GET.copy()
        if "page" in r_copy:
            r_copy.pop("page")
        context["filter"] = r_copy.urlencode()
        return context


class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"   