import re


class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        self.formatted_cpf = re.sub(r"\D+", "", cpf)

    def validate(self):
        cpf_without_verification_digits = self.formatted_cpf[:-2]

        validated_cpf = self.discover_verification_digit(
            cpf_without_verification_digits, 1)
        validated_cpf = self.discover_verification_digit(validated_cpf, 0)
        
        return True if validated_cpf == self.formatted_cpf else False

    def discover_verification_digit(self, cpf, first_or_second_digit):
        total = 0
        iterator = first_or_second_digit
        for c in cpf:
            total += int(c) * iterator
            iterator += 1
        total %= 11
        if total > 9:
            total = 0

        return cpf + str(total)