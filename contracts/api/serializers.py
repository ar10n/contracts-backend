from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Claim, Client, Contract, Manufacturer, Product, Region, Company, Shipment


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    company = CompanySerializer()
    region = RegionSerializer()
    products = ProductSerializer(many=True)

    claims = ClaimSerializer(many=True)
    shipments = ShipmentSerializer(many=True)

    class Meta:
        model = Contract
        fields = "__all__"


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
