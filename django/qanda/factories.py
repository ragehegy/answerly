
from unittest.mock import patch
import factory

from .models import Question
from user.factories import UserFactory

from .service.elasticsearch import Elasticsearch
from unittest.mock import patch

class QuestionFactory(factory.django.DjangoModelFactory):
    title = factory.sequence(lambda n: 'Question # %d' %n)
    question = 'What is it about?'
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Question

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        with patch('qanda.service.elasticsearch.Elasticsearch'):
            return super()._create(model_class, *args, **kwargs)
