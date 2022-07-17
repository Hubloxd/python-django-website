from django.urls import path

from .views import QuestionList, QuestionDetails, vote, QuestionResults

app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', QuestionList.as_view(), name='polls'),
    # /polls/1/
    path('<int:pk>/', QuestionDetails.as_view(), name='details'),
    # /polls/1/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
    # /polls/1/results/
    path('<int:pk>/results/', QuestionResults.as_view(), name='results'),
]
