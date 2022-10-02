from rest_framework import generics, status
from rest_framework.response import Response

#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.medicoSerializer import MedicoSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.medico import Medico


class MedicoListCreateView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer()
    #permision_classes = (IsAuthenticated,)

    def list(self, request):
            print("Get a todos los Medico")
            queryset = self.get_queryset()
            serializer = MedicoSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
            print("Post a Medico")
            print(request.data)
            usuarioData = request.data.pop('usuario')
            serializerU = UsuarioSerializer(data=usuarioData)
            serializerU.is_valid(raise_exception=True)
            usuario = serializerU.save()
            enfData = request.data
            enfData.update({"usuario":usuario.id})
            serializerEnf = MedicoSerializer(data=enfData)
            serializerEnf.is_valid(raise_exception=True)
            serializerEnf.save()
            return Response(status=status.HTTP_201_CREATED)
            
    """tokenData = {
                "username":request.data["username"],
                "password":request.data["password"]
                }
    tokenSerializer = TokenObtainPairSerializer(data=tokenData)

    tokenSerializer.is_valid(raise_exception=True)
    return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)"""




class MedicoRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer()
    lookup_field = 'id'         #caompo con el que se realiza la busqueda de objetos
    lookup_url_kwarg = 'pk'     #nombre dado a la url en argumento

    def get(self, request, *args, **kwargs):
        print("GET a Medico")
        """ if valid_data['user_id' != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Medico")
        """ if valid_data['user_id' != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        print("DELETE a Usuario")
        """ if valid_data['user_id' != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)


    

    