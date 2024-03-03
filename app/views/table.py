from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views import View
from django.contrib import messages
from app.models import Place, Table
from app.forms import PlaceForm


# class PlaceView(View):
#     template_name = "table/places.html"
#     form_class = PlaceForm
    
#     def get(self, request):
#         places = Place.objects.all()
        
#         return render(request, self.template_name, {"places": places})
    
#     def place_create(self, request):
        
#         if request.method == "POST":
#             form = PlaceForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "The place created succesfully")
#             else:
#                 messages.error(request, "oops!!! something went wrong while creating") 
#         return render(request, "table/place_create.html", {"form":self.form_class})
        
class PlaceView(ListView):
    template_name = "table/places.html"
    model = Place
    context_object_name = "places"
    

class PlaceCreateView(View):
    template_name = "table/place_create.html"
    form_class = PlaceForm
    
    def post(self, request):
        if request.method =="POST":
            form = PlaceForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Place created succesfully")
            else:
                messages.error(request, "oops something went wrong while creating")
        form = self.form_class
        return render(request, self.template_name, {"form":form})