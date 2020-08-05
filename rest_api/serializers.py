from rest_framework import serializers,fields
from . import models


class SerializeProject(serializers.ModelSerializer):

	# created_by = serializers.StringRelatedField(many=True)

	class Meta:
		model = models.Project
		fields = ('id','project_name','created_at','created_by')



class SerializeClient(serializers.ModelSerializer):



	class Meta:
		model = models.Client
		fields = ('id','client_name','created_at','created_by','projects')
		extra_kwargs = {'projects': {'read_only': True}}
