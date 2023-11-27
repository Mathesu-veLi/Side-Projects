import re


regExs = {
    "cpf": r"^(\d{3})\.?(\d{3})\.?(\d{3})\-?(\d{2})$",
    "phone number": r"^(\+?\d{1,3}(\-\d{3})?)?\s?(\()?(\d{2,3})(\))?\s?(9?\d{4})\-?(\d{4})$",
    "email": r"^[\w+\.]+@([\w-]+\.)+[\w-]{2,4}$"
}


def test_cpf_regex():
    correct_cpf_sintax = ['123.456.789-10', '12345678910']
    incorrect_cpf_sintax = ['123.456.789.10', '123-456-789.10', '123']

    for c in correct_cpf_sintax:
        assert re.search(regExs["cpf"],
                         c), "CPF regex not valid! (Should be True)"
    for c in incorrect_cpf_sintax:
        assert not re.search(regExs["cpf"],
                             c), "CPF regex not valid! (Should be False)"

