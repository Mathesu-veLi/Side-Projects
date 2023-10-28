def check_if_it_is_number(ask: str):
    """checks if the value entered is a number

    Args:
        ask (str): Question to ask at the input

    Returns:
        int: Number entered
    """
    
    
    while True:
        try:
            number = int(input(ask))
            return number
        except ValueError:
            print('Type only numbers')
