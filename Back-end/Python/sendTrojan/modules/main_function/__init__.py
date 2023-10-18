import pyautogui
import keyboard


def flood(mensage: str, number_of_times: int):
    """Types the message passed as an argument a certain number of times
    For when the message has already been typed all the times or when the user presses esc

    Args:
        mensage (str): message to be sent
        number_of_times (int): number of times the message will be sent
    """

    keyboard.wait('f2')

    if keyboard.is_pressed('f2'):
        for iterator in range(number_of_times):
            pyautogui.write(f'{mensage} {iterator}', interval=0)
            pyautogui.press('enter')

            if keyboard.is_pressed('esc'):
                print('\n', 'The flood has stopped!')
                break
