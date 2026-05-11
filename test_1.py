import unittest

from lab6_1 import Node, search, insert, delete


class TestSearch(unittest.TestCase):
    def test_search_finds_existing_value(self):
        tree = Node(5, Node(3), Node(7))
        self.assertTrue(search(tree, 3))

    def test_search_returns_false_for_missing_value(self):
        tree = Node(5, Node(3), Node(7))
        self.assertFalse(search(tree, 10))

    def test_search_on_empty_tree(self):
        self.assertFalse(search(None, 5))


class TestInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        tree = insert(None, 5)
        self.assertEqual(tree, Node(5))

    def test_insert_new_value_in_correct_position(self):
        tree = Node(5, Node(3), Node(7))
        new_tree = insert(tree, 4)
        expected = Node(5, Node(3, None, Node(4)), Node(7))
        self.assertEqual(new_tree, expected)

    def test_insert_duplicate_returns_unchanged_tree(self):
        tree = Node(5, Node(3), Node(7))
        new_tree = insert(tree, 5)
        self.assertEqual(new_tree, tree)


class TestDelete(unittest.TestCase):
    def test_delete_leaf_node(self):
        tree = Node(5, Node(3), Node(7))
        new_tree = delete(tree, 3)
        expected = Node(5, None, Node(7))
        self.assertEqual(new_tree, expected)

    def test_delete_node_with_one_child(self):
        tree = Node(5, Node(3, Node(2), None), Node(7))
        new_tree = delete(tree, 3)
        expected = Node(5, Node(2), Node(7))
        self.assertEqual(new_tree, expected)

    def test_delete_node_with_two_children(self):
        tree = Node(5, Node(3), Node(7, Node(6), Node(8)))
        new_tree = delete(tree, 7)
        expected = Node(5, Node(3), Node(8, Node(6), None))
        self.assertEqual(new_tree, expected)


if __name__ == "__main__":
    unittest.main()