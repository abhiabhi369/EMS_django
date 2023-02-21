from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from Ems_app.models import Country,State,District,Constituency, Voters,WardIssues

class CountrySerailizer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class ConstiSerializer(ModelSerializer):
    class Meta:
        model = Constituency
        fields = '__all__'

class VoterSerializer(ModelSerializer):
    class Meta:
        model = Voters
        fields = '__all__'

class WardIssuesSerializer(ModelSerializer):
    class Meta:
        model = WardIssues
        fields = '__all__'

