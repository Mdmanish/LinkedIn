from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_profile'

urlpatterns = [
    path('profile', views.profile_page, name='profile_page'),
    path('editprofile/<id>', views.edit_profile, name='edit_profile'),
    path('uploadpic', views.upload_pic, name="upload_pic"),
    path('uploadcoverpic', views.upload_cover_pic, name="upload_cover_pic"),
    path('search', views.search, name='search'),
    path('search_profile/<str:username>',
         views.search_profile, name='search_profile'),
    path('followers', views.followers, name='followers'),
    path('experienceform',
         views.experience_form, name="experience_form"),
    path('educationform',
         views.education_form, name="education_form"),
    path('certificateform',
         views.certificate_form, name="certificate_form"),
    path('skillsform', views.skills_form, name="skills_form"),
    path('languageform',
         views.language_form, name="language_form"),
     path('experienceform/<id>',
         views.experience_form, name="experience_form"),
    path('educationform/<id>',
         views.education_form, name="education_form"),
    path('certificateform/<id>',
         views.certificate_form, name="certificate_form"),
     path('message/<str:username>',views.message,name="message"),
     path('checkview/<str:username>', views.checkview, name="checkview"),
     path('send', views.send, name="send"),
     path('all_messages/<str:username>', views.get_all_messages, name="all_messages")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
