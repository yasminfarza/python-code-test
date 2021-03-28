import unittest
from core.object_depth import print_depth


class TestDictDepth(unittest.TestCase):

    def test_depth_with_object(self):
        """
        Test create for print nested dictionary keys
        and python object with depth
        """

        class Person(object):

            def __init__(self, first_name, last_name, father):
                self.first_name = first_name
                self.last_name = last_name
                self.father = father

        person_a = Person('User', '1', None)
        person_b = Person('User', '2', person_a)

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            }
        }

        res = print_depth(a)
        output = 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\nfirst_name 4\nlast_name 4\nfather 4\nfirst_name 5\nlast_name 5\nfather 5'

        self.assertMultiLineEqual(res, output)


if __name__ == '__main__':
    unittest.main()
