from django.test import TestCase


from todos.models import Todo


class AnimalTestCase(TestCase):

    def setUp(self):
        Todo.objects.all()

    def test_animals_can_speak(self):
        self.assertEqual(5, 4)
        self.assertEqual(3, 3)