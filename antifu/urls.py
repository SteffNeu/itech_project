from django.conf.urls import url
#from django.conf.urls import include
from antifu import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
	url(r'^contactUs/$', views.contactUs, name='contactUs'),
	url(r'^personalHelp/$', views.personalHelp, name='personalHelp'),
	url(r'^faq/$', views.faq, name='FAQ'),
	# url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
	# url(r'^register/$', views.register, name='register'),
	# url(r'^login/$', views.user_login, name='login'),
	# url(r'^restricted/', views.restricted, name='restricted'),
	# url(r'^logout/$', views.user_logout, name='logout'),
	]
