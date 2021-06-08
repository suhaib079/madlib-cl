from madlib_cl import __version__

from madlib_cl.madlib_cl import *
def test_version():
    assert __version__ == '0.1.0'

def test_version():
    assert __version__ == '0.1.0'


def test_read():
    actual = read('assets/madlib_source.txt')
    expected = open('assets/madlib_source.txt','r').read()
    assert expected == actual 

def test_parse():
    actual = parse('assets/madlib_source.txt')
    expected = ['0','1', '2', '3', '4']
    assert expected == actual 


def test_merge():
    
    actual = merge('Guess how we gonna spend the night  !    My name is jegsoo i will give you a lesson about {0} and {1}, then u gonna  pay for the sins you made {2}  However i am willing to give you a chance to surive {3}, good luck', ['humanty', 'justice', 'stealing', 'payback',])
    expected = 'Guess how we gonna spend the night  !  My name is jegsoo i will give you a lesson about humanty and justice, then u gonna  pay for the sins you made stealing   However i am willing to give you a chance to surive from your sin  payback, good luck'
    assert expected == actual
