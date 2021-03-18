"""Service serializers module."""

from rest_framework import serializers

from ..house.models import HouseModel
from ..service.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    """ServiceSerializer.

    Extends from ModelSerializer and convert a queryset of the Service model
    into a native python datatype.

    """

    # houses = serializers.PrimaryKeyRelatedField(
    #     queryset=HouseModel.objects.all(), many=True
    # )

    class Meta:
        """Meta.

        Inner Meta class of ServiceSerializer, it will allow to add custom
        rules to the serialized information.

        Attributes
        ----------
        exclude : str
            Fields that should be excluded in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST request.

        """

        exclude = ("houses",)

        model = ServiceModel

        read_only_fields = ("id", "created", "updated")