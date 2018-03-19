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
	url(r'^category/(?P<category_name>[\w\-]+)/$',
		views.show_category, name='show_category'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
	url(r'^submit_comment/$',views.submit_comment,name='submit_comment'),
	url(r'^update_comment_feat/$', views.update_comment_feat, name='update_comment_feat'),
	url(r'^update_post_feat/$', views.update_post_feat, name='update_post_feat'),
	url(r'^post/#(?P<post_id>[\w\-]+)/$',views.show_post,name='show_post'),
	url(r'^post/(?P<postID>[\w\-]+)/$',views.post,name='post'),
	url(r'search/$', views.search, name='search'),
	url(r'^profile_registration', views.register_profile, name='register_profile'),

	#the navtabs
	url(r'^myContents/(?P<username>[\w\-]+)/$',views.myContents,name='myContents'),
	url(r'^myComments/(?P<username>[\w\-]+)/$',views.myComments,name='myComments'),
	url(r'^settings/$',views.settings,name='settings'),
	url(r'^uploadContent/$',views.uploadContent,name='uploadContent'),
	# url(r'^uploadContent/(?P<categoryName>[\w\-]+)/$',views.uploadContent,name='uploadContent'),
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
	# url(r'^register/$', views.register, name='register'),
	# url(r'^login/$', views.user_login, name='login'),
	# url(r'^restricted/', views.restricted, name='restricted'),
	# url(r'^logout/$', views.user_logout, name='logout'),
	]
