# -*- coding: utf-8 -*-
from unittest import main, TestCase
from elasticsearch import Elasticsearch
from elastic import ElasticOperations


CLIENT = Elasticsearch()


class TestElastic(TestCase):

    def test_hebrew_text_tokenize(self):
        text = "שלום אדון עולם של אני"
        op = ElasticOperations(CLIENT)
        res = op.tokenize_text(text)
        self.assertEquals(len(res), 2, "Tokenize is incorrect for this text")

    def naive_test_tokenize(self):
        text = "Hello world and me"
        op = ElasticOperations(CLIENT)
        res = op.tokenize_text(text)
        self.assertEquals(len(res), 2, "Tokenize is incorrect for this text")

