from django.test import Client, TestCase
from .models import *
from django.urls import reverse


# Testing the views
class TestPage(TestCase):
    def setUp(self):
        self.client = Client()
    def test_landingPage_page(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public.html')
        html=response.content.decode('utf-8');
        self.assertIn('<h1 class="learnAbout">Learn About Donation</h1>', html)
    def test_signInPage(self):
        url = reverse('loginpage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        html=response.content.decode('utf-8');
        self.assertIn('<strong>LOGIN</strong>', html)
    def test_signupPage(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        html=response.content.decode('utf-8');
        self.assertIn('<input type="password" name="conf_password"', html)
    def test_donateBloodPage(self):
        url = reverse('donateBlood')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donateBlood.html')
        html=response.content.decode('utf-8');
        self.assertIn('<th scope="col">Camp Name</th>', html)
    def test_searchBloodPage(self):
        url = reverse('searchBlood')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchBlood.html')
        html=response.content.decode('utf-8');
        self.assertIn('<th scope="col">Blood Group and Quantity</th>', html)

# Testing the views accorrding to their Status code
class PageStatus(TestCase):
    def testLandingPage(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200);
    def testLoginPage(self):
        response = self.client.get('/user/loginpage')
        self.assertEqual(response.status_code, 200);
    def testSignupPage(self):
        response = self.client.get('/user/signup')
        self.assertEqual(response.status_code, 200);
    def testDonateBlood(self):
        response = self.client.get('/user/donateBlood')
        self.assertEqual(response.status_code, 200);
    def testSearchBlood(self):
        response = self.client.get('/user/searchBlood')
        self.assertEqual(response.status_code, 200);
    def testWithoutLogin(self):
        def logout():
            response = self.client.get('/user/logout');
            self.assertEqual(response.status_code, 302);
        def bloodBankDashboard():
            response = self.client.get('/user/blood_bank_dashboard');
            self.assertEqual(response.status_code, 302);
        def bloodBankBloodCamp():
            response = self.client.get('/user/blood_bank_dashboard/blood_camp');
            self.assertEqual(response.status_code, 302);
        def bloodBankProfile():
            response = self.client.get('/user/blood_bank_dashboard/blood_bank_profile');
            self.assertEqual(response.status_code, 302);
        logout();
        bloodBankDashboard();
        bloodBankBloodCamp();
        bloodBankProfile();


class SigninTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(state_id= 72, name= 'Gujarat')
        self.city = City.objects.create(city_id= 59303, name= 'Gogodar', state= self.state)
        self.credentials = {
            'blood_bank_name': 'test4',
            'username': 'test4',
            'email': 'test4@gmail.com',
            'password': '123456',
            'contact': 1234567890,
            'address': 'test4',
            'state': self.state,
            'city': self.city,}
        User.objects.create(**self.credentials)
        
    def test_login(self):
        # get the inner html of dashboard
        data = {'username': 'test4', 'password': '123456'.encode('utf-8')}
        response = self.client.post('/user/loginUser', data = data)
        print(response);
    def updateComponent(self):
        