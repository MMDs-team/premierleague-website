from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

from base.models import Ticket, TicketType
from base.serializers.ticket_serializers import *


@api_view(['GET'])
def get_all_tickets(request):
    ticket = Ticket.objects.all()
    serializer = TicketSerializerSimple(ticket, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def get_single_ticket(request, pk):
    try:
        ticket = Ticket.objects.get(pk = pk)
        serializer = TicketSerializerSimple(ticket, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No ticket found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_ticket(request):
    data = request.data
    user = request.user

    try:
        ticket = Ticket.objects.create(
            user = user,
            match_id = int(data['match']),
            type_id = int(data['type']),
            seat_number = data['seat_number']
        )

        serializer = TicketSerializerSimple(ticket, many=False)

        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating ticket'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancel_ticket(request, pk):
    data = request.data
    user = request.user
    ticket = Ticket.objects.filter(pk=pk).first()
    if ticket.user_id != user.id:
        Response({'detail': 'Not authorized to cancel this ticket'}, status=status.HTTP_400_BAD_REQUEST)
        
    if ticket is None: return Response({
        'detail': "ticket with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    ticket.delete()

    return Response({
        'detail': f"Ticket with id={pk} have been deleted successfully!"
    }, status.HTTP_200_OK)


@api_view(['GET'])
def get_all_ticket_type(request):
    stadiums = TicketType.objects.all()
    serializer = TicketTypeSerializer(stadiums, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def get_single_ticket_type(request, pk):
    try:
        ticket_type = TicketType.objects.get(pk = pk)
        serializer = TicketTypeSerializer(ticket_type, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No ticket_type found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def add_ticket_type(request):
    data = request.data

    try:
        ticket_type = TicketType.objects.create(
            ratio = data['ratio'],
            s_number = data['s_number'],
            e_number = data['e_number'],
            color = data['color'],
            description = data['description'],
            stadium_id = int(data['stadium']),
            html_tag_id = data['html_tag_id']
        )

        serializer = TicketTypeSerializer(ticket_type, many=False)

        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating ticket_type'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def update_ticket_type(request, pk):
    data = request.data

    try:
        ticket_type = TicketType.objects.get(pk = pk)

        if data.get('ratio') != None: ticket_type.ratio = data['ratio']
        if data.get('s_number') != None: ticket_type.s_number = data['s_number']
        if data.get('e_number')  != None: ticket_type.e_number = data['e_number']
        if data.get('color') != None: ticket_type.color = data['color']
        if data.get('description') != None: ticket_type.description = data['description']
        if data.get('stadium') != None: ticket_type.stadium = data['stadium']
        if data.get('html_tag_id') != None: ticket_type.html_tag_id = data['html_tag_id']

        ticket_type.save()

        serializer = StadiumSerializer(ticket_type, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating ticket_type'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def remove_ticket_type(request, pk):
    ticket_type = TicketType.objects.filter(pk=pk).first()
    if ticket_type is None: return Response({
        'detail': "ticket_type with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    ticket_type.delete()

    return Response({
        'detail': f"TicketType with id={pk} have been deleted successfully!"
    }, status.HTTP_200_OK)




@api_view(['GET'])
def get_user_ticket(request):
    user_id = int(request.GET.get('us', '-1'))

    user_tickets = list(Ticket.objects.filter(user_id = user_id))
    
    serializer = TicketSerializerSimple(user_tickets, many=True)

    return Response(serializer.data)