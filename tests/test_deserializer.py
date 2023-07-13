from .base_test import *

from tot.deserializer import TextDeserializer


class TestDeserializeText(TotTest):
    def test_simple(self):
        output = TextDeserializer("hello 1").output
        print(output)
