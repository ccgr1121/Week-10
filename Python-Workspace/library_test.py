import unittest
class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.Library = Library()
        book=Book(6, "Harry Potter")
        Library.add(Book)

    def test_item_are_abstract(self):
        with self.assertRaises(TypeError):
            item = Item(3)
    
    def test_add_item(self):
        library=Library()
        book = Book(6, "Harry Potter")
        library.add_item(book)
        response = {6: book}
        self.assertEqual(response, library._items)

    def test_item_in_use(self):
        book=Book(6, "Harry Potter")
        book2=Book(6, "HGTTG")
        library=Library()
        library.add_item(book)
        with self.assertRaise(IdInUseException):
            library.add_item(book2)

    def test_delete_item(self):
        library = Library()
        library._items = {6: Book(6, "Harry Potter")}
        library.test_delete_item(6)
        self.assertEqual({}, library._items)