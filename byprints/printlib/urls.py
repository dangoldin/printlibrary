from django.conf.urls.defaults import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

print views.__file__

print dir(views)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.books, name='books'),
    # url(r'^printlib/', include('printlib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	# url(r'^books/', 'views.books', name='books')
)