from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.ListHomeView.as_view(), name='home'),
    path('about/', views.TemplateAboutView.as_view(), name='about'),
    path('communication/', views.ListComView.as_view(), name='communication'),
    path('communication/<int:pk>/detail/', views.DetailComView.as_view(), name='communication_detail'),
    path('communication/create/', views.CreateComView.as_view(), name='communication_create'),
    path('communication/<int:com_id>/comment/', views.CreateCommentView.as_view(), name='comment'),
    path('communication/<int:pk>/delete/', views.DeleteComView.as_view(), name='communication_delete'),
    path('communication/<int:pk>/update/', views.UpdateComView.as_view(), name='communication_update'),
    path('official/', views.ListOfficialView.as_view(), name='official'),
]