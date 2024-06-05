from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list')
]

'''
- Assigning a view called post_list to the ROOT URL
'' : The URL pattern will match an empty string & the Django URL will ignore the domain name(e.g, 127.0.0.1:8080/) that prefix the full url path
views.post_list : This pattern will tell Django that views.post_list the right place to go if someone enters your website at the "https://127.0.0.1:8000/" address
name='post_list' : Is the name of the URL that will be used to identify the view(page)
'''