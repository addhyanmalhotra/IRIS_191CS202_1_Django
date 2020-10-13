from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic

from .forms import BookUploadForm
from .models import BookInstance, Book, IssueRequest


def book_upload_view(request):
    context = {}

    # create object of form
    form = BookUploadForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "home.html", context)


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(available=True).count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_visits': num_visits},
    )


class IssueRequestsByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing issue requests of current user."""
    model = BookInstance
    template_name = 'lms/bookinstance_issue_requests_user.html'
    paginate_by = 10
    context_object_name = 'issuerequest_list'

    def get_queryset(self):
        return IssueRequest.objects.filter(borrower=self.request.user)


class LoanedBooksByUserListView(generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'lms/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        context = BookInstance.objects\
            .filter(issuerequest__borrower=self.request.user)\
            .filter(issuerequest__transactions__isReturned=False)

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book