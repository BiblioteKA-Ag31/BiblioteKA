from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from users.models import User
from .models import Book, Copy

from .serializers import BookSerializer, CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCollaborator


class BookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        return serializer.save()


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        instance_book = get_object_or_404(Book, pk=self.request.data.get("book_id"))
        serializer.save(book=instance_book)


class CopyDetailsView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    
    def notication_student_book_available(book_id, copy_id,students):
        copy = get_object_or_404(Copy, id=copy_id)
        book=get_object_or_404(Book, id= book_id)
        emails=[students.users.email for student in students]
        subject="Livro disponível para retirada. "
        message=f"O livro {copy.book} está disponível para retirada."
        recipient_list=emails
        
        # self.request.user
        #Segui a sugestãp do instrutor Alexandre:
#         Alexandre Alves
#   13h44
# Vi sobre seu /pergunta vou deixar umas instruções sobre essa parte do email:
# No momento em que um livro é devolvido, a lógica pode estar presente nessa requisição.
# Vc terá acesso a copia que pertence a um determinado livro então você buscará qual livro foi devolvido.
# Com isso basta fazer um filtro para pegar todas as informações da tabela que segue esse determinado livro.
# Ao fazer isso, você terá acesso aos usuários que seguem esse livro, tendo acesso aos seus emails.
# Com isso basta estruturar a lógica de envio de email passando a listagem dos emails captados a partir dessa filtragem.

# Assim, na lógica que eu estava fazendo , essa lista de livros seguidos pelo usuario eu conseguiria pela propria rota e pegaria essa informação por parametro?


# Alexandre Alves
#   13h47
# Isso mesmo
    


