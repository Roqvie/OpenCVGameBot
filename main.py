import bot
from bot import ONE, TWO, THREE, PLUS, MINUS
from time import sleep
from datetime import datetime


# Config constants #
START_BUTTON_COORDS = (965, 1025)               # Coords of start game button (center)
CROP = (685, 525, 1225, 605)                    # Rect coordinates to crop screenshot for matching equation (top left, bottom right)
DELAY_AFTER_START = 0.5                         # Delay to start game after clicking start button (seconds)
TIME_BETWEEN_ROUNDS = 2                         # Time for solving equation (seconds)

ANSWER_COORDS = {                               # Coords of answer buttons (center)
    1: (960, 650),
    2: (960, 730),
    3: (960, 810)
}
TEMPLATES = [                                   # Image instances for template symbols
    (ONE, '1'),
    (TWO, '2'),
    (THREE, '3'),
    (PLUS, '+'),
    (MINUS, '-')
]


def startBot():
    bot.click_to_start(START_BUTTON_COORDS)
    sleep(DELAY_AFTER_START)

    while True:
        start_time = datetime.now()
        image = bot.grab_image(CROP)
        equation = bot.match_numbers_on_image(image, TEMPLATES)
        answer = int(eval(equation))
        bot.click_on_answer(answer, ANSWER_COORDS)
        end_time = datetime.now()
        timedelta = (end_time - start_time).total_seconds()
        print(f"Solving time: {timedelta}s\n")
        sleep(TIME_BETWEEN_ROUNDS-timedelta)
        

if __name__ == '__main__':
    startBot()

