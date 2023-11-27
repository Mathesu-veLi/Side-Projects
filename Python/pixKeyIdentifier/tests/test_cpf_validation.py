import sys
sys.path.append('../pixKeyIdentifier/pixKeyIdentifier/classes')
from cpfValidate import Cpf


def test_cpf_validation():
    valid_cpf = Cpf('092.675.600-18').validate()
    invalid_cpf = Cpf('092.675.600-13').validate()
    assert valid_cpf, "Cpf validator error! (Should be True)"
    assert not invalid_cpf, "Cpf validator error! (Should be False)"
