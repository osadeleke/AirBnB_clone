#!/usr/bin/python3
"""Test Case Module for BaseModel Module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Class for Base Model
    """
    def test_init_no_arg(self):
        """Tests instance creation with no arguments
        """
        tmp = BaseModel()
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
        tmp_wa = BaseModel(name='segun', age=23, time='now')
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
        tmp_args = BaseModel(13, "new", "anything", 34.50)
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
        tmp_args_kwargs = BaseModel("every", "new", 23, name="segun", age=12)
        list_ak = []
        check_list = [
                'id', 'created_at', 'updated_at',
                'name', 'age', '__class__'
                ]
        for key in tmp_args_kwargs.to_dict():
            list_ak.append(key)
        self.assertEqual(list_ak, check_list)

    def test_str(self):
        tmp_str = BaseModel()
        s_name = type(tmp_str).__name__
        s_id = tmp_str.id
        s_dict = str(tmp_str.__dict__)
        output = "[{}] ({}) {}".format(s_name, s_id, s_dict)
        self.assertEqual(str(tmp_str), output)

    def test_save(self):
        """Tests the save method
        """
        obj = BaseModel()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertLess(first_update, second_update, "Error")

    def test_to_dict(self):
        """Tests to_dict method with empty argument on instance call
        """
        tmp_dict = BaseModel()
        check_dict = {}
        check_dict['id'] = tmp_dict.id
        check_dict['created_at'] = tmp_dict.created_at.isoformat()
        check_dict['updated_at'] = tmp_dict.updated_at.isoformat()
        check_dict['__class__'] = type(tmp_dict).__name__
        self.assertEqual(tmp_dict.to_dict(), check_dict)

    def test_to_dict_kwargs(self):
        """Tests to_dict method with kwargs argument on instance call
        """
        tmp_dict = BaseModel(name="Black Genius", user="10thcode")
        check_dict = {}
        check_dict['id'] = tmp_dict.id
        check_dict['created_at'] = tmp_dict.created_at.isoformat()
        check_dict['updated_at'] = tmp_dict.updated_at.isoformat()
        check_dict['user'] = tmp_dict.user
        check_dict['__class__'] = type(tmp_dict).__name__
        check_dict['name'] = tmp_dict.name
        self.assertEqual(tmp_dict.to_dict(), check_dict)

    def test_to_dict_args(self):
        """Tests to_dict method with args argument on instance call
        """
        tmp_dict = BaseModel(10, "something")
        check_dict = {}
        check_dict['id'] = tmp_dict.id
        check_dict['created_at'] = tmp_dict.created_at.isoformat()
        check_dict['updated_at'] = tmp_dict.updated_at.isoformat()
        check_dict['__class__'] = type(tmp_dict).__name__
        self.assertEqual(tmp_dict.to_dict(), check_dict)


if __name__ == '__main__':
    unittest.main()
