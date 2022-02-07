import cv2 as cv
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
import typing
from PIL.Image import Image


# Read template symbol images for matching
_PLUS = cv.imread('templates/plus.png', cv.IMREAD_UNCHANGED)
PLUS = cv.cvtColor(_PLUS, cv.COLOR_BGR2GRAY)
_MINUS = cv.imread('templates/minus.png', cv.IMREAD_UNCHANGED)
MINUS = cv.cvtColor(_MINUS, cv.COLOR_BGR2GRAY)
_ONE = cv.imread('templates/one.png', cv.IMREAD_UNCHANGED)
ONE = cv.cvtColor(_ONE, cv.COLOR_BGR2GRAY)
_TWO = cv.imread('templates/two.png', cv.IMREAD_UNCHANGED)
TWO = cv.cvtColor(_TWO, cv.COLOR_BGR2GRAY)
_THREE = cv.imread('templates/three.png', cv.IMREAD_UNCHANGED)
THREE = cv.cvtColor(_THREE, cv.COLOR_BGR2GRAY)


def _filter_string(string: str) -> str:
    """Function to filter string by recurring characters (for '111--22' it returns '1-2').

    Args:
        string (str): string to filter

    Returns:
        str: filtered string
    """
    _string = ''
    _last = ''

    for i, symbol in enumerate(string):
        if i != len(string)-1 and  string[i+1] != symbol:
            _string += symbol
        else:
            _last = symbol

    return _string + _last


def click_to_start(start_button_coords: typing.Tuple[int, int]) -> None:
    """Clicks start button

    Args:
        start_button_coords (typing.Tuple[int, int]): coordinates of start button (center)
    """
    pyautogui.click(start_button_coords)


def grab_image(crop_coords: typing.Tuple[int, int]) -> Image:
    """Grabs screenshot of main screen and crop it

    Args:
        crop_coords (typing.Tuple[int, int]): coordinates to crop screenshot (top left and bottom right)

    Returns:
        Image: Pillow cropped image
    """
    screen = pyautogui.screenshot()
    image = screen.crop(crop_coords)

    return image


def match_numbers_on_image(image: Image, templates: typing.Tuple[Image, str]) -> str:
    """Searchs numbers on given cropped screenshot by template images

    Args:
        image (Image): cropped screenshot for searching numbers
        templates (typing.Tuple[Image, str]): template images of numbers and symbols

    Returns:
        str: equation string
    """

    threshold = 0.97
    results = []
    string = ''
    image = np.array(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    for template in templates:
        template_img, symbol = template
        result = cv.matchTemplate(image,template_img,cv.TM_CCOEFF_NORMED)
        located = np.where(result >= threshold)
        for part in zip(*located[::-1]):
            results.append((symbol, part[0]))
    
    sorted_by_coords = sorted(results, key=lambda tup: tup[1])

    for symbol, coord in sorted_by_coords:
        string += symbol
    
    print(f"Matched equation string: {string}")
    print(f"Filtered equation string: {_filter_string(string)}")
    
    return _filter_string(string)


def click_on_answer(answer: int, coords: typing.Dict[int, tuple]) -> None:
    """Clicks on answer by given button coords

    Args:
        answer (int): calculated answer of equation
        coords (typing.Dict[int, tuple]): dict of answer-coord pairs
    """
    if answer in coords.keys():
        pyautogui.click(coords[answer])
    else:
        print(f'! Wrong answer / No coords given for this answer')

    

