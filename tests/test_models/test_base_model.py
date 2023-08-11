#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        tmp = BaseModel()
        n_list = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp.to_dict():
            n_list.append(key)
        self.assertEqual(n_list, check_list)

        # call instance with arguments
        tmp_wa = BaseModel(name='segun', age=23, time='now')
        n_list_wa = []
        check_list_wa = [
                'id', 'created_at', 'updated_at',
                'name', 'age', 'time', '__class__'
                ]
        for key in tmp_wa.to_dict():
            n_list_wa.append(key)
        self.assertEqual(n_list_wa, check_list_wa)

    def test_save(self):
        tmp = BaseModel()
        up_time = tmp.updated_at
        tmp.save()
        nw_time = tmp.updated_at
        self.assertNotEqual(up_time, nw_time)
        self.assertIsInstance(nw_time, datetime)


if __name__ == '__main__':
    unittest.main()
