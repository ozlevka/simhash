# -*- coding: utf-8 -*-
from unittest import main, TestCase
from elasticsearch import Elasticsearch


CLIENT = Elasticsearch()


class TestElastic(TestCase):

    def test_1(self):
        self.assertEqual(2,2, "2 always equals to 2")