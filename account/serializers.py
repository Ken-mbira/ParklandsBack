from rest_framework import serializers
from django.contrib.auth.models import Group

from account.models import Account

class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        groups = Group(many=True)
        fields = '__all__'
        read_only_fields = ['is_active','is_superuser','is_admin']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        """Defines what to do once a request having the new user data arrives
        """
        account = Account(email = self.validated_data['email'], username = self.validated_data['username'],profile_pic = self.validated_data['profile_pic'])
        account.set_password(self.validated_data['password'])

        account.save()
        return account