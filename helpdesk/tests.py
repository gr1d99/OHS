from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from accounts.models import UserProfile


class TestLogin(TestCase):
    """
    This test case tests whether special system users such as
    the administrator and the system manager context are different
    from the rest of the normal users context.
    """

    def setUp(self):
        administrator = UserProfile.objects.create_superuser(
            'test_admin',
            'test_admin@gmail.com',
            'testadminpassword',
        )

        student = UserProfile.objects.create_user(
            'student',
            'student@gmail.com',
            'studentpassword'
        )

        self.administrator = administrator
        self.student = student

    def test_admin_in_index_view(self):
        c = Client()
        login_admin = c.login(username='test_admin', password='testadminpassword')
        self.assertEqual(login_admin, True)
        response = c.get('/')
        request = response.context['request']
        self.assertEqual(request.user.is_superuser, True)
        self.assertEqual(self.administrator, request.user)

    def test_student_in_index_view(self):
        c = Client()
        student_login = c.login(username='student', password='studentpassword')
        self.assertEqual(student_login, True)
        response = c.get('/')
        request = response.context['request']
        self.assertEqual(request.user.is_superuser, False)
        self.assertEqual(self.student, request.user)