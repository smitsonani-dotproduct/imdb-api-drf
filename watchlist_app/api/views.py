# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle,
    ScopedRateThrottle,
)
from rest_framework import filters


from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from watchlist_app.api.throttling import ReviewCreateThrottle, ReviewListThrottle


class WatchListGV(generics.ListAPIView):
    serializer_class = WatchListSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["title", "platform__name"]

    # filter_backends = [filters.SearchFilter]
    # search_fields = ["title", "=platform__name"]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["avg_rating"]

    def get_queryset(self):
        return WatchList.objects.all()


class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data
        serializer = WatchListSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        payload = request.data
        serializer = WatchListSerializer(movie, data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAP(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        # serializer = StreamPlatformSerializer(
        #     platforms, many=True, context={"request": request}
        # )  # use this intialization for HyperlinkedRelatedField or HyperlinkedModelSerializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data
        serializer = StreamPlatformSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            streaming_platform = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StreamPlatformSerializer(streaming_platform)
        # serializer = StreamPlatformSerializer(
        #     streaming_platform, context={"request": request}
        # )  # use this intialization for HyperlinkedRelatedField or HyperlinkedModelSerializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            streaming_platform = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        payload = request.data
        serializer = StreamPlatformSerializer(streaming_platform, data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            streaming_platform = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    "error_message": "Not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        streaming_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############################## Model Viewsets  #############################


class StreamPlatformViewset(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


##############################  Viewsets  #############################


# class StreamPlatformViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         platform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(platform)
#         return Response(serializer.data)

#     def create(self, request):
#         payload = request.data
#         serializer = StreamPlatformSerializer(data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         payload = request.data
#         serializer = StreamPlatformSerializer(platform, data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             movie = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         movie.delete()


##############################  Concrete View Classes  #############################


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        watchlist = WatchList.objects.get(id=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, user=review_user)

        if review_queryset.exists():
            raise ValidationError(
                "You have already submitted the review for this movie!"
            )

        if watchlist.total_rating == 0:
            watchlist.avg_rating = serializer.validated_data["rating"]
        else:
            print(
                "avg rate, current rate :)",
                watchlist.avg_rating,
                serializer.validated_data["rating"],
            )
            watchlist.avg_rating = (
                watchlist.avg_rating + serializer.validated_data["rating"]
            ) / 2
        watchlist.total_rating = watchlist.total_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, user=review_user)


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user__username", "active", "rating"]

    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # permission_classes = [IsAuthenticated]

    # over-riding exising method
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "review-detail"

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # def get_queryset(self):
    #     username = self.kwargs["username"]
    #     return Review.objects.filter(user__username=username)

    def get_queryset(self):
        username = self.request.query_params.get("username")
        return Review.objects.filter(user__username=username)


##############################  Mixins + Generic views  #############################


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(
#     mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


##############################  Class-based views  #############################


# class MovieListAV(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         payload = request.data
#         serializer = MovieSerializer(data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MovieDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         payload = request.data
#         serializer = MovieSerializer(movie, data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)


##############################  Function-based view  #############################


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         payload = request.data
#         serializer = MovieSerializer(data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, pk):

#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "PUT":
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         payload = request.data
#         serializer = MovieSerializer(movie, data=payload)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         try:
#             movie = Movie.objects.get(id=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {
#                     "error_message": "Movie not found",
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
