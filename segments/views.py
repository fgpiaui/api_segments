# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from segments.constantes import ID, FIELD, VALUE

from segments.controllers.edit_data import EditData
from segments.controllers.query_controller import QueryController
from segments.models import Tag, User, UserTag
from segments.serializer import UserSerializer, UserTagSerializer, TagSerializer


@api_view(['POST'])
def create_user(request):
    data = request.data
    user = UserSerializer(data=data)
    if user.is_valid():
        user.save()
    
    return Response(user.data)

@api_view(['POST'])
def create_tag(request):
    data = request.data
    tag = TagSerializer(data=data)
    if tag.is_valid():
        tag.save()
    
    return Response(tag.data)


@api_view(['POST'])
def create_segments(request):
    data = request.data
    user_tag = UserTagSerializer(data=data)
    if user_tag.is_valid():
        user_tag.save()
    return Response(user_tag.data)

@api_view(['POST'])
def edit_user(request):
    data = request.data
    user = User.objects.get(id=data[ID])
    edit_data = EditData(data[FIELD], data[VALUE], user)
    user = edit_data.update()
    user = UserSerializer(data=user)
    return Response(user)

@api_view(['POST'])
def edit_tag(request):
    data = request.data
    tag = Tag.objects.get(id=data[ID])
    edit_data = EditData(data[FIELD], data[VALUE], tag)
    tag = edit_data.update()
    tag = TagSerializer(data=tag)
    return Response(tag)

@api_view(['POST'])
def edit_user_tag(request):
    data = request.data
    user_tag = UserTag.objects.get(id=data[ID])
    edit_data = EditData(data[FIELD], data[VALUE], user_tag)
    user_tag = edit_data.update()
    user_tag = UserTagSerializer(data=user_tag)
    return Response(user_tag)

@api_view(['POST'])
def delete_user(request):
    data = request.data['id']
    try:
        User.objects.filter(id=data).delete()    
        return Response({'mensagem':f'User de id {data} deletado com sucesso'})
    except Exception as e:
        return Response({'mensagem': f'Falha ao deletar user {data}, {e}'})

@api_view(['POST'])
def delete_tag(request):
    data = request.data['id']
    try:
        Tag.objects.filter(id=data).delete()
        return Response({'mensagem':f'Tag de id {data} deletado com sucesso'})
    except Exception as e:
        return Response({'mensagem': f'Falha ao deletar tag {data}, {e}'})

@api_view(['POST'])
def delete_segments(request):
    data = request.data['id']
    try:
        UserTag.objects.filter(id=data).delete()
        return Response({'mensagem':f'Segments de id {data} deletado com sucesso'})
    except Exception as e:
        return Response({'mensagem': f'Falha ao deletar segments {data}, {e}'})


@api_view(['POST'])
def filter_user_tag(request):
    data = request.data
    query_controller = QueryController(data)
    query = query_controller.execute()
    user = UserTagSerializer().filter(query)
    return Response(user)

