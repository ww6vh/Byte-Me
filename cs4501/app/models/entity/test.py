from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from entity.models import Computer, User, Review

class UserTestCase(TestCase):
    
    def setUp(self):
        pass
    
    def test_createSuccess(self):
        response = self.client.post('/api/v1/user/create/', {'username': 'fred', 'password': 'pass', 'email': 'jz7zb@virginia.edu'})
        self.assertEquals(response.status_code, 200)

    def test_createFail(self):
        response = self.client.post('/api/v1/user/create/', {'username': 'fred', 'password': 'pass'})
        self.assertEquals(response.status_code, 404)
        
    def test_deleteSuccess(self):
        self.client.post('/api/v1/user/create/', {'username': 'fred', 'password': 'pass', 'email': 'jz7zb@virginia.edu'})
        response = self.client.get('/api/v1/user/delete/1')
        self.assertEquals(response.status_code, 301)
    
    def test_deleteFail(self):
        response = self.client.get('/api/v1/user/delete/100')
        self.assertEquals(response.status_code, 301)
        
    def test_getSuccess(self):
        self.client.post('/api/v1/user/create/', {'username': 'fred', 'password': 'pass', 'email': 'jz7zb@virginia.edu'})
        response = self.client.get('/api/v1/user/1')
        self.assertEquals(response.status_code, 301)
        
    def test_getFail(self):
        response = self.client.get('/api/v1/user/100')
        self.assertEquals(response.status_code, 301)
        
    def test_updateSuccess(self):
        self.client.post('/api/v1/user/create/', {'username': 'fred', 'password': 'pass', 'email': 'jz7zb@virginia.edu'})
        response = self.client.post('/api/v1/user/1/', {'username': 'bob', 'password': 'pass123', 'email': 'bob@virginia.edu'})
        self.assertEquals(response.status_code, 200) 
    
    def test_updateFail(self):
        response = self.client.post('/api/v1/user/100/', {'username': 'bob', 'password': 'pass123'})
        self.assertEquals(response.status_code, 200) 
        
    def tearDown(self):
        pass
    
class ComputerTestCase(TestCase):
    
    def setUp(self):
        pass
    
    def test_createSuccess(self):
        response = self.client.post('/api/v1/computer/create/', {'make': 'HP', 'model': 'Spectre', 'condition': 'new', 'description': 'really cool'})
        self.assertEquals(response.status_code, 200)

    def test_createFail(self):
        response = self.client.post('/api/v1/computer/create/', {'make': 'HP', 'model': 'Spectre', 'condition': 'new'})
        self.assertEquals(response.status_code, 404)
        
    def test_deleteSuccess(self):
        self.client.post('/api/v1/computer/create/', {'make': 'HP', 'model': 'Spectre', 'condition': 'new', 'description': 'really cool'})
        response = self.client.get('/api/v1/computer/delete/1')
        self.assertEquals(response.status_code, 301)
    
    def test_deleteFail(self):
        response = self.client.get('/api/v1/computer/delete/100')
        self.assertEquals(response.status_code, 301)
        
    def test_getSuccess(self):
        self.client.post('/api/v1/computer/create/', {'make': 'HP', 'model': 'Spectre', 'condition': 'new', 'description': 'really cool'})
        response = self.client.get('/api/v1/computer/1')
        self.assertEquals(response.status_code, 301)
        
    def test_getFail(self):
        response = self.client.get('/api/v1/computer/100')
        self.assertEquals(response.status_code, 301)
        
    def test_updateSuccess(self):
        self.client.post('/api/v1/computer/create/', {'make': 'HP', 'model': 'Spectre', 'condition': 'new', 'description': 'really cool'})
        response = self.client.post('/api/v1/computer/1/', {'make': 'Apple', 'model': 'Macbook', 'condition': 'used', 'description': 'awesome'})
        self.assertEquals(response.status_code, 200) 
    
    def test_updateFail(self):
        response = self.client.post('/api/v1/computer/100/', {'make': 'Apple', 'model': 'Macbook'})
        self.assertEquals(response.status_code, 200) 
        
    def tearDown(self):
        pass
    
    
class ReviewTestCase(TestCase):

    def setUp(self):
        pass
    
    def test_createSuccess(self):
        response = self.client.post('/api/v1/review/create/', {'rating': 10, 'description': 'great'})
        self.assertEquals(response.status_code, 200)

    def test_createFail(self):
        response = self.client.post('/api/v1/review/create/', {'rating': 10})
        self.assertEquals(response.status_code, 404)
        
    def test_deleteSuccess(self):
        self.client.post('/api/v1/review/create/', {'rating': 10, 'description': 'great'})
        response = self.client.get('/api/v1/review/delete/1')
        self.assertEquals(response.status_code, 301)
    
    def test_deleteFail(self):
        response = self.client.get('/api/v1/review/delete/100')
        self.assertEquals(response.status_code, 301)
        
    def test_getSuccess(self):
        self.client.post('/api/v1/review/create/', {'rating': 10, 'description': 'great'})
        response = self.client.get('/api/v1/review/1')
        self.assertEquals(response.status_code, 301)
        
    def test_getFail(self):
        response = self.client.get('/api/v1/review/100')
        self.assertEquals(response.status_code, 301)
        
    def test_updateSuccess(self):
        self.client.post('/api/v1/review/create/', {'rating': 10, 'description': 'great'})
        response = self.client.post('/api/v1/review/1/', {'rating': 1, 'description': 'bad'})
        self.assertEquals(response.status_code, 200) 
    
    def test_updateFail(self):
        response = self.client.post('/api/v1/review/100/', {'rating': 5})
        self.assertEquals(response.status_code, 200) 
        
    def tearDown(self):
        pass
    