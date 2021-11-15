from rest_framework import serializers

from segments.models import User, UserTag, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserTagSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tag = TagSerializer(read_only=True)

    class Meta:
        model = UserTag
        fields = '__all__'

    def filter(self, query):
        user_tag = UserTag.objects.filter(query)
        return UserTagSerializer(user_tag, many=True).data[0:]