from rest_framework.response import Response
from models import CarAd
from serializers import CarAdSerializer
from django.http import Http404
from rest_framework.views import APIView


class CarAdList(APIView):
    def get(self, request, format=None):
        car_ads = CarAd.objects.all()  # filter?
        serialized_car_ads = CarAdSerializer(car_ads, many=True)
        return Response(serialized_car_ads.data)


class CarAdDetail(APIView):

    def get_object(self, idFromSite):
        try:
            querySet = CarAd.objects.all().filter(idFromSite=idFromSite)
            if len(querySet):
                return querySet[0]
            else:
                raise CarAd.DoesNotExist
        except CarAd.DoesNotExist:
            raise Http404

    def get(self, requset, idFromSite, format=None):
        car_ad = self.get_object(idFromSite)
        serialized_car_ad = CarAdSerializer(car_ad)
        return Response(serialized_car_ad.data)
