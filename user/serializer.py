from rest_framework import fields, serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# for adding custom claims e.g username or email etc.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token =  super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token



# user registeration model serializer
class RegisterSerilazer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required= True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    # registrations fields validations
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            # raise proper validation error when password doesn't match
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs


    # creation of user while registering fields
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user