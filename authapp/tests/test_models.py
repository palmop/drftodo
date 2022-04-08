from rest_framework.test import APITestCase
from authapp.models import UserApp

class TestModel(APITestCase):

    def test_creates_userapp(self):
        user = UserApp.objects.create_user(
            username='palmonaz',
            email='paolo.palmonari@gmail.com',
            password='sirtss.P'
        )
        self.assertIsInstance(user, UserApp)
        self.assertFalse(user.is_staff, False)
        self.assertEqual(user.username, 'palmonaz')
        self.assertEqual(user.email, 'paolo.palmonari@gmail.com')


    def test_creates_superuser(self):
        user = UserApp.objects.create_superuser(
            username='superpalmonaz',
            email='superpaolo.palmonari@gmail.com',
            password='sirtss.P'
        )
        self.assertIsInstance(user, UserApp)
        self.assertTrue(user.is_staff, True)
        self.assertTrue(user.is_superuser, True)
        self.assertEqual(user.username, 'superpalmonaz')
        self.assertEqual(user.email, 'superpaolo.palmonari@gmail.com')

    def test_raise4username(self):
        self.assertRaises(ValueError,
            UserApp.objects.create_superuser,
            username=None,
            email='superpaolo.palmonari@gmail.com',
            password='sirtss.P'
            )

    
    def test_raise4email(self):
        self.assertRaises(ValueError,
            UserApp.objects.create_user,
            username="palmonaz",
            email=None,
            password='sirtss.P'
            )
    

    def test_raise_value_error4username(self):
        with self.assertRaisesMessage(ValueError, "username mandatory"):
                UserApp.objects.create_user(
                    username=None,
                    email='superpaolo.palmonari@gmail.com',
                    password='sirtss.P')
                
                
