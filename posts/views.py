# from django.shortcuts import render
# from django.http import HttpResponse


# def index_view(request):
#     context = {
#         "name": "Alex",
#         "title": "Главная страница",
#         "my_list": [1, 2, 3],
#     }
#     return render(request, "posts/index.html", context=context)


# def contacts(request):
#     context = {
#         "title": "Контакты"
#     }
#     return render(request, "posts/contacts.html", context)


# def about(request):
#     context = {
#         "title": "Про меня"
#     }
#     return render(request, "posts/about.html", context)

# # views.py

# from django.shortcuts import render

# def view1(request):
#     some_variable = "Привет, мир!"
#     return render(request, 'template1.html', {'some_variable': some_variable})

# def view2(request):
#     items = ['Item 1', 'Item 2', 'Item 3']
#     return render(request, 'template2.html', {'items': items})

# def view3(request):
#     user = request.user
#     return render(request, 'template3.html', {'user': user})

# def view4(request):
#     some_condition = True
#     return render(request, 'template4.html', {'some_condition': some_condition})
from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context = {

    }



 

    return render(request, "posts/index.html", context=context)

def contacts(request):
    context = {
        "title": "Контакты"
    }


    assert "title" in context, "Заголовок не найден в контексте!"

    return render(request, "posts/contacts.html", context)

def about(request):
    context = {
        "title": "Про меня",
        "page_content": "",
    }

    assert "title" in context, "Заголовок не найден в контексте!"
    assert "page_content" in context, "Контент страницы не найден в контексте!"

    return render(request, "posts/about.html", context)
