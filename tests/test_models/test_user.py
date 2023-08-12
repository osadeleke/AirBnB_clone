#!/usr/bin/python3
"""Test Case Module for User Module
"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test Class for Base Model
    """
    def test_init_no_arg(self):
        """Tests instance creation with no arguments
        """
        tmp = User()
        n_list = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp.to_dict():
            n_list.append(key)
        self.assertEqual(n_list, check_list)

    def test_init_kwargs_args(self):
        """Tests instance creation with kwargs arguments
        """
        tmp_wa = User(name='segun', age=23, time='now')
        n_list_wa = []
        check_list_wa = [
                'id', 'created_at', 'updated_at',
                'name', 'age', 'time', '__class__'
                ]
        for key in tmp_wa.to_dict():
            n_list_wa.append(key)
        self.assertEqual(n_list_wa, check_list_wa)

    def test_init_args_args(self):
        """Tests instance creation with args arguments
        """
        tmp_args = User(13, "new", "anything", 34.50)
        nlist_args = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp_args.to_dict():
            nlist_args.append(key)
        self.assertEqual(nlist_args, check_list)

    def test_init_args_and_kwargs(self):
        """Tests instance creation with args and kwargs
        """
        tmp_args_kwargs = User("every", "new", 23, name="segun", age=12)
        list_ak = []
        check_list = [
                'id', 'created_at', 'updated_at',
                'name', 'age', '__class__'
                ]
        for key in tmp_args_kwargs.to_dict():
            list_ak.append(key)
        self.assertEqual(list_ak, check_list)

    def test_str(self):
        tmp_str = User()
        s_name = type(tmp_str).__name__
        s_id = tmp_str.id
        s_dict = str(tmp_str.__dict__)
        output = "[{}] ({}) {}".format(s_name, s_id, s_dict)
        self.assertEqual(str(tmp_str), output)


if __name__ == '__main__':
    unittest.main()
