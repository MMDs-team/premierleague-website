from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base.models import Action, ActionType
from base.serializers.action_serializers import *
import datetime


@api_view(['GET'])
def get_all_actions(request):
    actions = Action.objects.all()
    serializers = ActionSerializer(actions, many=True)
    
    return Response(serializers.data)


@api_view(['GET'])
def get_single_action(request, pk):
    action = Action.objects.filter(pk=pk).first()

    if action is None: return Response({
        'detail': "Action with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    serializer = ActionSerializer(action, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_action(request, pk):
    action = Action.objects.filter(pk=pk).first()
    if action is None: return Response({
        'detail': "Action with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    action.delete()
    return Response({
        'detail': f"Action with id={pk} have been deleted!"
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_action(request, pk):
    action = Action.objects.filter(pk=pk).first()
    if action is None: return Response({
        'detail': "Action with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)


    '''
        fields we can change: action_type, match, subject, object, 
            subject_from_home, time
    '''
    data = request.data
    if data.get('action_id') is not None: return Response({
        'detail': "You can not change the primary key!"
    }, status=status.HTTP_400_BAD_REQUEST)

    if data.get('action_type') is not None: action.action_type = int(data['action_type'])
    if data.get('match') is not None: action.match = int(data['match'])
    if data.get('subject') is not None: action.subject = int(data['subject'])
    if data.get('object') is not None: action.object = int(data['object'])
    if data.get('subject_from_home') is not None: action.subject_from_home = int(data['subject_from_home'])
    if data.get('time') is not None: 
        # 01:14:36
        hour, minute, second = int(data['time'][:2]), int(data['time'][3:5]), int(data['time'][6:])
        action.time = datetime.time(hour, minute, second)

    action.save()

    serializer = ActionSerializer(action, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_action(request):
    data = request.data
    if data.get('action_type') is None or \
        data.get('match') is None or \
        data.get('subject') is None or \
        data.get('time') is None: return Response({
            'detail': 'Some required field is missing!'
        }, status=status.HTTP_400_BAD_REQUEST)

    hour, minute, second = int(data['time'][:2]), int(data['time'][3:5]), int(data['time'][6:])
    time = datetime.time(hour, minute, second)
    action = Action(
        action_type_id = int(data['action_type']),
        match_id = int(data['match']),
        subject_id = int(data['subject']),
        time = time,
    ) if data.get('action_id') is None else Action(
        pk=int(data['action_id']),
        action_type = int(data['action_type']),
        match = int(data['match']),
        subject = int(data['subject']),
        time = time,
    )

    if data.get('object') is not None: action.object = data['object']
    if data.get('subject_from_home') is not None: action.subject_from_home = data['subject_from_home']
    action.save()

    serializer = ActionSerializer(action, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_action_types(request):
    action_types = ActionType.objects.all()
    serializers = ActionTypeSerializer(action_types, many=True)
    
    return Response(serializers.data)


@api_view(['GET'])
def get_single_action_type(request, pk):
    action_type = ActionType.objects.filter(pk=pk).first()

    if action_type is None: return Response({
        'detail': "Action type with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    serializer = ActionTypeSerializer(action_type, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_action_type(request, pk):
    action_type = ActionType.objects.filter(pk=pk).first()
    if action_type is None: return Response({
        'detail': "Action type with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    action_type.delete()
    return Response({
        'detail': f"Action type with id={pk} have been deleted!"
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_action_type(request, pk):
    action_type = ActionType.objects.filter(pk=pk).first()
    if action_type is None: return Response({
        'detail': "Action type with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)


    '''
        fields we can change: subtype, type
    '''
    data = request.data
    if data.get('action_type_id') is not None: return Response({
        'detail': "You can not change the primary key!"
    }, status=status.HTTP_400_BAD_REQUEST)

    if data.get('subtype') is not None: action_type.subtype = data['subtype']
    if data.get('type') is not None: action_type.type = data['type']

    action_type.save()

    serializer = ActionTypeSerializer(action_type, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_action_type(request):
    data = request.data
    if data.get('subtype') is None or \
        data.get('type') is None: return Response({
            'detail': 'Some required field of request is missing!'
        }, status=status.HTTP_400_BAD_REQUEST)

    action_type = ActionType() if data.get('action_type_id') is None else ActionType(pk=int(data['action_type_id']))
    action_type.subtype = data['subtype']
    action_type.type = data['type']
    action_type.save()

    serializer = ActionTypeSerializer(action_type, many=False)
    return Response(serializer.data)