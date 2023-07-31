from rest_framework import generics, status
from .models import Book, Subject, Author
from .serializers import BookSerializer, AuthorSerializer, SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK
from .exceptions import InvalidAuthorID


# AUTENTICAÇÃO

class CustomAuthToken(ObtainAuthToken):
    @staticmethod
    def post(request, *args, **kwargs):
        # Chama o método post da classe ObtainAuthToken para obter a resposta original
        response = super(CustomAuthToken, CustomAuthToken).post(
            request, *args, **kwargs)

        # Verifica se o login foi bem-sucedido e se o token foi retornado na resposta original
        if 'token' in response.data:
            # Modifica a resposta para incluir apenas o token, removendo outros dados
            token = Token.objects.get(key=response.data['token'])
            return Response({'token': token.key}, status=HTTP_200_OK)

        # Se não encontrar o token na resposta original, retorna a resposta sem modificação
        return response


obtain_auth_token = CustomAuthToken.as_view()


# BOOKS

# Responsável pela criação do Book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_id = self.request.data.get('author_id')
        if author_id and not Author.objects.filter(pk=author_id).exists():
            raise InvalidAuthorID()

        serializer.save()

# Rsponsável pela listagem dos Books


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Responsável por expor um book de acordo com os métodos http do permitidos (GET, PUT e DELETE)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# AUTHORS

# Responsável por expor um Author de acordo com os métodos http permitidos (GET e DELETE)
@api_view(['GET', 'DELETE'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({"error": "Autor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Responsável por expor uma lista de Authors


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# SUBJECTS

# Responsável por expor um Subject de acordo com os métodos http do cliente permitidos (GET e DELETE)
@api_view(['GET', 'DELETE'])
def subject_detail(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response({"error": "Assunto não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Responsável por expor umA lista de Subjects


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Responsável por expor uma lista de Books filtrados por sua relação com determinado Subject (subject_id)


class BooksBySubjectAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Book.objects.filter(booksubjects__subject_id=subject_id)

# Responsável por expor uma lista de Books filtrados por sua relação com determinado Author (author_id)


class BooksByAuthorAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Book.objects.filter(author_id=author_id)
