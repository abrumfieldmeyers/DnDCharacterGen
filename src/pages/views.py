from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home_view(req,*args, **kwargs):
    userName = req.user
    # resp = f"<h1>hello {userName}"
    # return HttpResponse(resp) # send a piece of HTML
    return render(req, "home.html", {}) # 3rd param is a dict of params to pass in

def contact_view(req,*args, **kwargs):
    userName = req.user
    resp = f"hello {userName}\n"
    ln = random.randint(3,10)
    nums = []
    for i in range(ln):
        nums.append(random.randint(1,100))
    ctx = {
        "user": resp,
        "number": ln,
        "nums": nums,

    }
    # return HttpResponse(resp) # send a piece of HTML
    return render(req, "contact.html", ctx)

def about_view(req,*args, **kwargs):
    my_context = {
        "my_text": "this is my text",
        "my_num": 123,
        "my_list":[1,2,3]
    }
    return render(req, "about.html", my_context)