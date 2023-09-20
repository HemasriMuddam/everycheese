import pytest
from everycheese.cheeses.models import Cheese
from everycheese.cheeses.tests.factories import CheeseFactory
# Connects our tests with our database
pytestmark = pytest.mark.django_db
def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name