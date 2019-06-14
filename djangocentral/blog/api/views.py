from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveUpdateDestroyAPIView,
    RetrieveAPIView
)
from django.shortcuts import get_list_or_404
from rest_framework.permissions import(
	IsAuthenticatedOrReadOnly
)
from .serializers import (
	PostSerializer,
    PostCreateSerializer,
    # TagSerializer,
    Userserilaizer,
    Commentserializer,
    CommentCreateserializer,
    UserCreateSerializer,
    Pageserilaizer,
    PageCreateSerializer,
    # UserCreateSerializer,
    UserActionserializer,
    CreateUserActionserializer

)
from blog.models import Post, Comment, User, Page, user_actions
from .permissions import AdminOrAuthorCanEdit, IsOwnerOrReadOnly

#### user serializer 
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserilaizer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserCreateSerializer


##### Post serializer

class PostCreateView(CreateAPIView):
	serializer_class = PostCreateSerializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)



class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsOwnerOrReadOnly,)

class PostDetailView(RetrieveAPIView):
	lookup_field = 'id'
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostURDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'id'
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsOwnerOrReadOnly,)

class PostDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorPostView(APIView):

	@staticmethod
	def get(request, username):
		posts = get_list_or_404(Post, author__username=username)
		post_data = PostSerializer(posts, many=True)
		return Response(post_data.data)

#### Comment serializer


class CommentListView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = Commentserializer
	permission_classes = (IsOwnerOrReadOnly,)

class CommentCreateView(CreateAPIView):
	serializer_class = CommentCreateserializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)


### Page Serializer 

class PageListView(ListAPIView):
    queryset = user_actions.objects.all()
    serializer_class = Pageserilaizer
    
    def perform_create(self, serializer):
            serializer.save(author=self.request.user)

class CreateUserAction(CreateAPIView):
	serializer_class = CreateUserActionserializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)
## useraction serializer
class UserActionListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = UserActionserializer

    def perform_create(self, serializer):
            serializer.save(author=self.request.user)

