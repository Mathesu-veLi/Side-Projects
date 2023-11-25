import re


class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        self.formatted_cpf = re.sub(r"\D+", "", cpf)

    def validate(self):
        cpf_without_verification_digits = self.formatted_cpf[:-2]

        total = 0
        iterator = 1
        for c in cpf_without_verification_digits:
            total += int(c) * iterator
            iterator += 1
        total %= 11
        if total > 9:
            total = 0
        cpf_without_verification_digits += str(total)

        total = 0
        iterator = 0
        for c in cpf_without_verification_digits:
            total += int(c) * iterator
            iterator += 1
        total %= 11
        if total > 9:
            total = 0
        cpf_without_verification_digits += str(total)
        return cpf_without_verification_digits


cpf = Cpf('864.200.505-02')
print(cpf.validate())
