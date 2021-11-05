from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    text1 = 'Good Morning :)'
    text2 = 'Good Night :('
    shift1 = 2
    shift2 = 11
    shift3 = 23
    actual1 = encrypt(text1, shift1)
    actual2 = encrypt(text1, shift2)
    actual3 = encrypt(text1, shift3)
    actual4 = encrypt(text2, shift1)
    excpected1 = 'Iqqf Oqtpkpi :)'
    excpected2 = 'Rzzo Xzcytyr :)'
    excpected3 = 'Dlla Jlokfkd :)'
    excpected4 = 'Iqqf Pkijv :('

    assert actual1 == excpected1
    assert actual2 == excpected2
    assert actual3 == excpected3
    assert actual4 == excpected4


def test_decrypt():
    text = 'Good Morning :)'
    shift = 3
    actual = decrypt(text, shift)
    excpected = 'Dlla Jlokfkd :)'
    assert actual == excpected


def test_crack():
    text = 'Pa dhz aol ilza vm aptlz, pa dhz aol dvyza vm aptlz.'
    actual = crack(text)
    excpected = 'It was the best of times, it was the worst of times.'
    assert actual == excpected
