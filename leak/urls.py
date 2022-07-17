from django.urls import path

from . import views



app_name = 'leak'

urlpatterns = [
    # leaks
    path('home', views.HomePage.as_view(), name='home'),
    path('c/<slug:slug>', views.CategoryLeakView.as_view(), name='category-leaks'),
    path('s/<slug:slug>', views.SubcategoryLeakView.as_view(), name='subcategory-leaks'),
    path('l/<slug:slug>', views.LeakDetail.as_view(), name='leak-detail'),


    # creation links
    path('category-create/', views.CategoryCreate.as_view(), name='category-create'),
    path('subcategory-create/<int:category_id>/', views.SubcategoryCreate.as_view(), name='subcategory-create'),
    path('leak-create/<int:category_id>/<int:subcategory_id>/', views.LeakCreate.as_view(), name='leak-create'),


    # upvote and downvote
    path('leak-upvote/<int:leak_id>', views.UpvoteLeak.as_view(), name='leak-upvote'),
    path('leak-downvote/<int:leak_id>', views.DownvoteLeak.as_view(), name='leak-downvote'),


    #constitution
    path('constitution/<int:pk>', views.ConstitutionView.as_view(), name='constitution'),
    path('edit-constitution/<int:pk>', views.ConstitutionEdit.as_view(), name='constitution-edit'),


    # citizenship
    path('citizenship-apply/<slug:slug>', views.ApplyForCitizenship.as_view(), name='citizenship-apply'),
    path('citizenship-renounce/<slug:slug>', views.RenounceCitizenShip.as_view(), name='citizenship-renounce'),


    path('add-share-count/<int:leak_id>', views.AddShareCount.as_view(), name='add-share-count'),
    # like country
    path('like-country/<int:subcategory_id>', views.LikeSubcategory.as_view(), name='like-country'),
    path('like-country/<int:subcategory_id>', views.UnLikeSubcategory.as_view(), name='unlike-country'),

]












