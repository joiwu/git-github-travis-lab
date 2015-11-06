from nose.tools import assert_equal
from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char():
    assert_equal("n", rot13_char("a"))
    assert_equal("-", rot13_char("-"))
    assert_equal("a", rot13_char("n"))

#def test_rot13():
#    assert_equal("n", rot13("a"))
