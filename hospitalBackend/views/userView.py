from cgitb import lookup
from rest_framework import generics, status
from rest_framework.response import Response

#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario


class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer()
    #permision_classes = (IsAuthenticated,)

    def list(self, request):
            print("Get a todos los Usuarios")
            queryset = self.get_queryset()
            serializer = UsuarioSerializer(queryset, many=True)
            return Response(serializer.data)


class UsuarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer()
    lookup_field = 'id'         #caompo con el que se realiza la busqueda de objetos
    lookup_url_kwarg = 'pk'     #nombre dado a la url en argumento

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        """ if valid_data['user_id' != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            print("PUT a Usuario")
            """ if valid_data['user_id' != kwargs['pk']:
                stringResponse = {'detail':'Unauthorized Request'}
                return Response(stringResponse, status=status.HTTP_401UNAUTHORIZED) """
            return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
                print("DELETE a Usuario")
                """ if valid_data['user_id' != kwargs['pk']:
                    stringResponse = {'detail':'Unauthorized Request'}
                    return Response(stringResponse, status=status.HTTP_401UNAUTHORIZED) """
                return super().delete(request, *args, **kwargs)


    

    

