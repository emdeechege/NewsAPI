import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('cnn','CNN.','View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN','https://www.nytimes.com/2018/08/31/sports/tennis/us-open-results.html')

    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))

# isinstance:::: Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false.
