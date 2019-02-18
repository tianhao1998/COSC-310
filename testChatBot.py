import unittest
class KnownValues(unittest.TestCase):
    def test_getvalue(self):
        result=chatBot.getValue('major')
        expected ='math'
        self.assertEqual(expected,result)

