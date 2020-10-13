from django.urls import path

from lms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('issue/', views.IssueRequestsByUserListView.as_view(), name='my-requests'),
    #path('issue/<int:ir_id>', views.IssueRequestsByUserListView,name='raiseIr')
 #   path('issue')
]
