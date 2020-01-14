from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import questionnaire, user, question_link

router = routers.DefaultRouter()
router.register(r'users',  user.UserViewSet, basename='users')
router.register(
    r'questionnaires',
    questionnaire.QuestionnaireViewSet,
    basename='questionnaires'
)

nested_router = routers.NestedDefaultRouter(
    router, r'questionnaires', lookup="questionnaire"
)
nested_router.register(
    r'questions',
    question_link.QuestionLinkViewSet,
    base_name='questions'
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(nested_router.urls)),
]
