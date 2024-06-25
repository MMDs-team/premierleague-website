from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ..models import Sponsor
from ..serializers.sponsor_serializers import SponsorSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_sponsors(request):
    sponsors = Sponsor.objects.all()
    serializer = SponsorSerializer(sponsors, many=True)
    return Response(serializer.data)