from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [

	path('', auth_views.LoginView.as_view(template_name = 'registration/login.html'),name = 'login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('familytour/appointment.html',views.app_new,name = 'app_new'),
	path('familytour/',views.familytour , name = "familytour"),
	path('card1/',views.card1, name = "card1"),
	path('graph/',views.graph, name = "graph"),
	path('religioustour/appointment.html',views.app_new,name = 'app_new'),
	path('religioustour/',views.religioustour , name = "religioustour"),
	path('solotrip/appointment.html',views.app_new,name = 'app_new'),
	path('solotrip/',views.solotrip , name = "solotrip"),
	path('adventuretour/appointment.html',views.app_new,name = 'app_new'),
	path('adventuretour/',views.adventuretour , name = "adventuretour"),
	path('homepage/',views.homepage,name = 'homepage'),
	path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
	path('appointment/',views.app_new,name = 'app_new'),
	path('about/',views.about,name = 'about'),
	path('gallery/',views.gallery,name = 'gallery'),
	path('pie_chart',views.pie_chart,name = 'pie_chart'),
	path('pie_chart/data/', views.chart_data, name='chart_data'),
	path('column_chart/', views.column_chart, name='column_chart')
	
]
