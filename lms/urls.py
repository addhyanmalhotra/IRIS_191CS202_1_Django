from django.conf.urls.static import static
from django.urls import path

from library import settings
from lms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('issue/', views.IssueRequestsByUserListView.as_view(), name='my-requests'),
    path('issue/<int:bi_id>', views.issuebook, name='raiseIr')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
