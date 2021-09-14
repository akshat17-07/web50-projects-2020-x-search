from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util

import random
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        return render(request, "encyclopedia/edit.html", {'error': "404 Not Found"})

    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            return render(request, "encyclopedia/edit.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})

def createpage(request):

    if request.method == "POST":

        # taking value from the form
        name= request.POST.get("name").strip()
        contant = request.POST.get("contant").strip()

        # checking if the entry isvalid
        if name in util.list_entries() or name == "" or contant == "":
            return render(request, "encyclopedia/createpage.html", {
            "name": name,
            "contant": contant,
            "error": "information is invalid"
             })

        else:
            util.save_entry(name, contant)
            return redirect(pages, name=name)

    return render(request, "encyclopedia/createpage.html", {
        "name": "",
        "contant":"",
        "error": ""
    })

def pages(request, name):
    page = util.get_entry(name)

    if page == None:
        return render(request, "encyclopedia/createpage.html", {
            "name": name,
            "contant":"",
            "error": "Page not found, you could create one"
        })

    else:
        contant = markdown2.markdown(page)
        return render(request, "encyclopedia/pages.html", {
        "title": name,
        "contant": contant
        })


"""
def random(request):
    pages = util.list_entries()

    # taking a random page
    num = random.randint(0,len(pages)-1)
    print("encyclopedia/"+pages(num)+".html")

    return render(request,"encyclopedia/"+pages(num)+".html")
"""
