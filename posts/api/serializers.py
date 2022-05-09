# notes .. put classes in alphebetical order .. easier for other coders to find a class .. created order will be mark with a number 

from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):                   # serialzer for the post create (3) 
	class Meta:
		model = Post 
		fields = [
			# 'id',
			'title',
			# 'slug',
			'content',
			'publish'
		]


class PostDetailSerializer(ModelSerializer):               # serializer for the post detial (2)
	class Meta:
		model = Post 
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'publish'
		]

class PostListSerializer(ModelSerializer):                   # serialzer for the post list (1) 
	class Meta:
		model = Post 
		fields = [
			'user',
			'id',
			'title',
			'slug',
			'content',
			'publish'
		]


