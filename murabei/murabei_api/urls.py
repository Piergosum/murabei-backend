

from django.urls import path
from .views import BookCreateView
from .views import AuthorListView
from .views import BookListView
from .views import SubjectListView, BooksBySubjectAPIView
from .views import BooksByAuthorAPIView
from .views import book_detail
from .views import author_detail
from .views import subject_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # Authentication
    path('auth/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # Endpoint para obter o token
    path('auth/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  # Endpoint para renovar o token
    # Books
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/', book_detail, name='book-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    # Authors
    path('author/<int:pk>/', author_detail, name='author-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books-by-author/<int:author_id>/',
         BooksByAuthorAPIView.as_view(), name='books-by-author'),
    # Subjects
    path('subject/<int:pk>/', subject_detail, name='subject'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('books-by-subject/<int:subject_id>/',
         BooksBySubjectAPIView.as_view(), name='books-by-subject'),

]
