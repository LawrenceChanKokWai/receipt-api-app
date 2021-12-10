from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    # TODO: Test Create User With Email Successful return. Creating User email and password,
    #  Returning the user model of objects and create user using the defined created email and password.
    #  ** AssertEqual the user model object against the created email of Equal and password of True.
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # TODO: Test New User Email on Normalized.
    #  Creates a email variable. Creates user. assertEqual that the user email is all in lower case.
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    # TODO: Test A invalid new email:
    def test_new_invalid_email(self):
        """Test creating user with no email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser("testsuperuser@gmail.com", "superuser123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
