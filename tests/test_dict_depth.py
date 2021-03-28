import unittest
from core.dictionary_depth import print_depth


class TestDictDepth(unittest.TestCase):

    def test_depth_with_dict(self):
        """ Test create for print nested dictionary keys with depth """

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }

        res = print_depth(a)
        output = 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3'

        self.assertMultiLineEqual(res, output)


if __name__ == '__main__':
    unittest.main()
