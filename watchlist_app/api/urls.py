from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_detail
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAP,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    StreamPlatformViewset,
)

# urlpatterns = [
#     path("list/", view=movie_list, name="movie-list"),
#     path("<int:pk>", view=movie_detail, name="movie-detail"),
# ]

# urlpatterns = [
#     path("list/", view=MovieListAV.as_view(), name="movie-list"),
#     path("<int:pk>", view=MovieDetailAV.as_view(), name="movie-detail"),
# ]

router = DefaultRouter()
router.register("stream", viewset=StreamPlatformViewset, basename="streamplatform")

urlpatterns = [
    path("watch/list/", view=WatchListAV.as_view(), name="watch-list"),
    path("watch/<int:pk>/", view=WatchDetailAV.as_view(), name="watch-detail"),
    path("", include(router.urls)),
    # path(
    #     "stream/list/",
    #     view=StreamPlatformListAP.as_view(),
    #     name="streamplatform-list",
    # ),
    # path(
    #     "stream/<int:pk>/",
    #     view=StreamPlatformDetailAV.as_view(),
    #     name="streamplatform-detail",
    # ),
    # path("watch/review/list", view=ReviewList.as_view(), name="reviews-list"),
    path(
        "watch/<int:pk>/review/create",
        view=ReviewCreate.as_view(),
        name="review-create",
    ),
    path("watch/<int:pk>/review/", view=ReviewList.as_view(), name="review-list"),
    path(
        "watch/review/<int:pk>/",
        view=ReviewDetail.as_view(),
        name="review-detail",
    ),
]
