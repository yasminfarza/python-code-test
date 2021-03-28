import unittest
from core import least_common_ancestor


class TestLca(unittest.TestCase):

    def test_node_6_7(self):
        """ Test create for node 6 & 7 """
        self.assertEqual(least_common_ancestor.lca(
            least_common_ancestor.root, 6, 7).data, 3)

    def test_node_3_7(self):
        """ Test create for node 3 & 7 """
        self.assertEqual(least_common_ancestor.lca(
            least_common_ancestor.root, 3, 7).data, 3)


if __name__ == '__main__':
    unittest.main()
