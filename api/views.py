from django.http.response import JsonResponse
from api.models import CancerModel
from api.serializers import CancerModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.

class CancerModelViewSet(viewsets.ModelViewSet):
    queryset = CancerModel.objects.all()
    serializer_class = CancerModelSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


## make an api without using RestAPI framework
# def detect_cancer(request):
#     if request.method == "POST":
#         try:
#             img = request.FILES['image']
#             img_name = default_storage.save(img.name, img)
#             img_url = default_storage.url(img_name)
#             data = {
#                 'image': img_url,
#                 'result': "under developing"
#             }
#             return JsonResponse(data, sate = False)
#         except:
#             return JsonResponse({"'image' field required"})
#     return JsonResponse({"Invalid Request": "only POST request allowed"})
