from rest_framework import serializers
from myapp.models import Register


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = Register

        fields = [
            'id',
            'name',
            'email',
            'password',
            'phone',
            'address',
            'role'
        ]