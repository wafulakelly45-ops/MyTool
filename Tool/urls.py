from django .urls import path
from. import views

urlpatterns =[
    
    path("data/",views.data, name="data"),  # path to user info like the email  and username
    path("login", views.login_view, name="login"), # login view
    path("logout", views.logout_view, name="logout"),# logout view
    path("<int:tool_id>", views.tool, name="tool"), #  view to a single object
    path("add/",views.add ,name="add"),  # path to add new tools
    path("", views.index, name="index"), # this the path to the  main page
   
]