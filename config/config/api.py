from rest_framework import routers
from rental import views as rental_views


router = routers.DefaultRouter()

router.register('friends/', rental_views.FriendViewset)
router.register('belongings/', rental_views.BelongingViewset)
router.register('borroweds/', rental_views.BorrowedViewset)
router.register('newclient/', rental_views.NewClientViewset)

