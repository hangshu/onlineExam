from django.conf.urls import patterns, include, url
from InstantTest.views import sign_in, sign_out, index, add_question, view_question, edit_question, delete_question, add_paper

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineTest.views.home', name='home'),
    # url(r'^OnlineTest/', include('OnlineTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', sign_in),
    url(r'^signout/$', sign_out),
    url(r'^teacherhome/$', index),
    url(r'^addquestion/$', add_question),
    url(r'^viewquestion/$', view_question),
    url(r'^editquestion/', edit_question),
    url(r'^deletequestion/$', delete_question),
    url(r'^addpaper/$', add_paper),
)
