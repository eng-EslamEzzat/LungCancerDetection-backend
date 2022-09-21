from rest_framework import serializers
from .models import CancerModel
from django.core.files.storage import default_storage
from .deep_model import get_classification

class CancerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancerModel
        fields = ['image', 'result']

        extra_kwargs = {
            'result': {
                'required': False
            },
        }

    def to_representation(self, instance):
        data = super(CancerModelSerializer, self).to_representation(instance)
        res = data.get('result')
        if not res:
            case = CancerModel.objects.latest('id')
            img_url = default_storage.path(str(case.image))
            result = get_classification(img_url)
            case.result = result
            case.save()
            return {**data, "result": result}
        return {**data}
