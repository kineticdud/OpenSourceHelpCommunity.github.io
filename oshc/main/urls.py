from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/', views.about, name="about"),
    url(r'^session/', views.request_session, name="request_session"),
    url(r'^contests/', views.contests, name="contests"),
    url(r'^contest_new/', views.contest_new, name="contest_new"),
    url(r'^add_contest/', views.add_contest, name="add_contest"),
    url(r'^submit_contest/', views.submit_contest, name="submit_contest"),
    url(r'^chatsessions/', views.chat_sessions, name="chat_sessions"),
    url(r'^journey/', views.journey, name="journey"),
    url(r'^jobs/', views.jobs, name="jobs"),
]
