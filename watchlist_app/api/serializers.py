from rest_framework import serializers

# from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["watchlist"]


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source="platform.name")

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="watch-detail"
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


#############  Hyperlinked Model Serializer  ############


# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
#     watchlist = WatchListSerializer(many=True, read_only=True)

#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"


#############  Model Serializer  ############


# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ["name", "description", "active"]
#         # exclude = ["id"]

#     def get_len_name(self, object):
#         length = len(object.name)
#         return length

#     def validate(self, data):
#         # object-level validation
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title & Description should not be same")
#         return data

#     def validate_name(self, value):
#         # field-level validation
#         if len(value) < 3:
#             raise serializers.ValidationError("Name is too short!")
#         return value


#############  Serializer  ############

# def name_length(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Name is too short!")
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])  # Validators
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # instance - old values
#         # validated_data - new values
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()

#         return instance

#     def validate(self, data):
#         # object-level validation
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title & Description should not be same")
#         return data

#     # def validate_name(self, value):
#     #     # field-level validation
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value
