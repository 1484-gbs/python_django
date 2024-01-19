from rest_framework import routers
from api.views.employeeViewSet import EmployeeViewSet

router = routers.DefaultRouter()
router.register("employee", EmployeeViewSet)
