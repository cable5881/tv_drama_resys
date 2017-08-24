from rest_framework import viewsets
from meiju.models.drama import Drama
from meiju.models.drama_type import DramaType
from meiju.serializers.drama_serializer import DramaSerializer
from meiju.serializers.drama_type_serializer import DramaTypeSerializer


class DramaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer


class DramaTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = DramaType.objects.all()
    serializer_class = DramaTypeSerializer


"""
class DramaList(generics.ListCreateAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer


class DramaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer
"""

"""
class DramaList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DramaDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

"""
class DramaList(APIView):
    def get(self, request, format=None):
        dramas = Drama.objects.all()
        serializer = DramaSerializer(dramas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DramaDetail(APIView):

    def get_object(self, pk):
        try:
            return Drama.objects.get(pk=pk)
        except Drama.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        drama = self.get_object(pk)
        serializer = DramaSerializer(drama)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        drama = self.get_object(pk)
        serializer = DramaSerializer(drama, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        drama = self.get_object(pk)
        drama.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
@api_view(['GET', 'POST'])
def drama_list(request, format=None):
    if request.method == 'GET':
        dramas = Drama.objects.all()
        serializer = DramaSerializer(dramas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drama_detail(request, pk, format=None):

    try:
        drama = Drama.objects.get(pk=pk)
    except Drama.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DramaSerializer(drama)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DramaSerializer(drama, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drama.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
