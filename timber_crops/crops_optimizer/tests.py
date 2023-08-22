from django.test import TestCase
from .views.views import home
from .models import GameMode
from decimal import Decimal

# Create your tests here.

class FoodToCropSimulationTest (TestCase):
    def setUp(self):
        # Create a test GameMode instance
        self.game_mode = GameMode.objects.create(
            name="Hard (Test Mode)", 
            food_consumption_daily_unit=2.5,
            food_consumption_percentage=100
        )

    def test_carrots_only_simulation(self):
        data = {
            "game_mode": self.game_mode.id,
            "number_of_beavers": 100,
            "carrots": "on",
            "carrots_food_ratio": 1,
            #if html checkbox is not ticked on, the "bread" field does not go through POST
            "bread_food_ratio": 1,
        }

        # Simulate a POST request
        # As it happens in the homepage, the targetted url is "empty" (see urls.py)
        response = self.client.post('', data)

        # Assert the expected results in the response
        self.assertEqual(response.status_code, 200)
        print("Value of response.content :", response.context)
        # self.assertContains(response, "Required carrot crops: 333.33")
        # Check the context values directly
        expected_carrot_crops = Decimal("333.33")
        context = response.context
        actual_carrot_crops = context['required_carrot_crops'].quantize(Decimal('0.00'))
        self.assertEqual(actual_carrot_crops, expected_carrot_crops)