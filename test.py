import unittest
from tasks.task1 import Dictionary
from tasks.task2 import get_total
from tasks.task3 import word_creator

class TestDictionary(unittest.TestCase):
    def test_newentry_and_look(self):
        d = Dictionary()
        d.newentry('Apple', 'A fruit that grows on trees')
        self.assertEqual(d.look('Apple'), 'A fruit that grows on trees')
        self.assertEqual(d.look('Banana'), "Can't find entry for Banana")
        
class TestGetTotal(unittest.TestCase):
    def test_get_total(self):
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        self.assertEqual(get_total(costs, ['socks', 'shoes'], 0.09), 70.85)
        self.assertEqual(get_total(costs, ['socks', 'banana'], 0.09), 5.45)
        self.assertEqual(get_total(costs, [], 0.09), 0.0)


class TestWordCreator(unittest.TestCase):
    def test_word_creator(self):
        self.assertEqual(word_creator(['yoda', 'best', 'has']), 'yes')
        self.assertEqual(word_creator([]), '')
        self.assertEqual(word_creator(['a']), 'a')


if __name__ == '__main__':
    unittest.main()