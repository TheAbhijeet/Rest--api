from rest_framework import generics
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,  HyperlinkedIdentityField
from blog.models import Post,User, Comment, Category, Page, Post,  user_actions
# from .serializers import PostSerializer

class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
           
        )

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'parent',
            'description',

        )

class Userserilaizer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Pageserilaizer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
class PageCreateSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'title',
            'content',
            'slug',

        )


class UserCreateSerializer(ModelSerializer):
    # posts = HyperlinkedIdentityField(view_name='user-posts')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email'
        )

class UserActionserializer(ModelSerializer):
    class Meta:
        model = user_actions
        fields= '__all__'

class CreateUserActionserializer(ModelSerializer):
    class Meta:
        model = user_actions
        fields= '__all__'

# class Categoryserializer(ModelSerializer):

#     class Meta:
#         model = Category
#         fields = '__all__'


# class TagSerializerField(serializers.ListField):
#     child = serializers.CharField()

#     def to_representation(self, data):
#         return data.values_list('name', flat=True)

# class TagSerializer(ModelSerializer):
#     tags = TagSerializerField()

#     def create(self, validated_data):
#         tags = validated_data.pop('tags')
#         instance = super(TagSerializer, self).create(validated_data)
#         instance.tags.set(*tags)
#         return instance