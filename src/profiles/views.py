from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm,RawProfileForm

# Create your views here.
def profile_detail_view(request):
    
    obj = Profile.objects.get(id=1)
    # context = {       # Hard coded example of context for an object. Better to draw from Database instead
    #     'title': obj.name,
    #     'description': obj.description,
    #     'email': obj.email,
    #     'featured':obj.featured,
    # }
    context = {
        'object':obj
    }
    return render(request,"profiles/profile_detail.html",context)

def profile_create_view(request):
    # Create a full Django form to create a new profile
    rawForm = RawProfileForm() # implied request.GET method
    if request.method == "POST":
        rawForm = RawProfileForm(request.POST)
        if rawForm.is_valid():
            Profile.objects.create(**rawForm.cleaned_data)  # **turns rawForm into args to pass in
            rawForm = RawProfileForm()
    context = {'form': rawForm}
    return render(request,"profiles/profile_create.html",context)

# def profile_create_view(request):
#     # Form for creating new profile
#     form = ProfileForm(request.POST or None)
#     if form.is_valid(): # If the form can be saved, save it, then clear out fields
#         form.save()
#         form = ProfileForm()    # Re-render the form to clear old fields

#     context = {
#         'form':form
#     }
#     return render(request,"profiles/profile_create.html",context)

# def profile_create_view(request):
#     # Handle raw HTML for profile creation form
#     context = {}
#     return render(request,"profiles/profile_create.html",context)