def validate_number(ask):
    while True:
        try:
            number = float(input(ask))
            return number
        except ValueError:
            print('Digite um número válido!')
