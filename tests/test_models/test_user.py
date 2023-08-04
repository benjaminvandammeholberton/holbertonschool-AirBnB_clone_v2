from tests.test_models.test_base_model import test_basemodel
from models.user import User

class test_User(test_basemodel):
    def setUp(self):
        super().setUp()
        self.name = "User"
        self.value = User

    def test_first_name(self):
        new = self.value()
        self.assertIsInstance(new.first_name, str)

    def test_last_name(self):
        new = self.value()
        self.assertIsInstance(new.last_name, str)

    def test_email(self):
        new = self.value()
        self.assertIsInstance(new.email, str)

    def test_password(self):
        new = self.value()
        self.assertIsInstance(new.password, str)
