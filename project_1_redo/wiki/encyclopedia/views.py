from django.shortcuts import render, redirect

from . import util

import markdown2

from random import randint

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):

    if name not in util.list_entries():
        return render(request, "encyclopedia/notFound.html",{
        "name": name
        })

    # getting entry in html format
    content = markdown2.markdown(util.get_entry(name))

    # rendering the page
    return render(request, "encyclopedia/entry.html", {
    "name": name,
    "content": content
    })

def search(request):

    # taking the keyword
    keyword = request.GET.get("keyword").lower()

    # finding the words matching the keyword
    all_words = util.list_entries()
    matched_words = []

    for word in all_words:

        # appending to the word in list
        if keyword in word.lower():
            matched_words.append(word)

    return render(request, "encyclopedia/search.html" ,{
    "name": keyword,
    "entries": matched_words
    })



def random(request):

    # chosing a random page
    lname = util.list_entries()
    n = (randint(0,len(lname)-1))
    name = lname[n]

    # redirecting to the page
    return redirect(entry, name=name)

def edit(request, name):

    # editing the form
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(name, content)

        return redirect('entry', name = name)


    # getting information in normal format
    content = util.get_entry(name)

    # rendering the page
    return render(request, "encyclopedia/edit.html",{
    "name": name,
    "content": content
    })

def create(request, name=""):

    # if method is request create a page
    if request.method == "POST":

        # getting information
        name = request.POST.get("name")
        content = request.POST.get("content")

        # checking if the information is valid
        if name == "" or content== "":
            return render(request,"encyclopedia/create.html",{
            "name": name,
            "content": content,
            "error": "Information is missing"
            })

        elif name in util.list_entries():

            return render(request,"encyclopedia/create.html",{
            "name": name,
            "content": content,
            "error": "Information already exist"
            })

        # saving the information
        else:
            util.save_entry(name, content)

            # redirecting to the entry
            return redirect("entry", name = name)

    else:

        if name:
            return render(request,"encyclopedia/create.html",{
            "name": name,
            "error": "Page not found but you could create one"
            })
        # render create page
        return render(request,"encyclopedia/create.html")
