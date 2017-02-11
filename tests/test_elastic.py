# -*- coding: utf-8 -*-
from unittest import main, TestCase
from elasticsearch import Elasticsearch
from elastic import ElasticOperations


CLIENT = Elasticsearch()

GLOBAL_TEXT = """
--- דרוש מפתח WEB עם 3 שנות ניסיון לעבודה בתל אביב ---

דרוש לנו מפתח WEB עם ניסיון מוכח בPHP
java script
css
html
מיקום: תל אביב מרכז, תל אביב יפו, ישראל

דרישות התפקיד:
העבודה במרכז תל אביב
"""


class TestElastic(TestCase):

    def test_analyze_text(self):
        op = ElasticOperations(CLIENT)
        res = op.analyze_with_idf(GLOBAL_TEXT)
        self.assertTrue(len(res) > 0, "Tokenize is incorrect for global text")

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

    def test_word_count(self):
        word = 'שלום'
        op = ElasticOperations(CLIENT)
        res = op.get_word_frequency(word)
        self.assertFalse((res == 0), msg='Word not found check it')

    def test_hebrew_text_analyze_and_idf(self):
        text = "שלום אדון עולם של אני"
        op = ElasticOperations(CLIENT)
        res = op.analyze_with_idf(text)
        self.assertEquals(len(res), 2, "Tokenize is incorrect for this text")