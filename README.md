
# OpenCV Bot

Simple bot that solves quations in Telegram game named '1+2' in @gamee Telegram bot.
https://t.me/gamee

## Demo

![Example](https://raw.githubusercontent.com/Roqvie/OpenCVGameBot/master/demo/demo.gif)



## Installation

Bot tested on Python 3.9.10

Inastalling requirements:

```bash
  cd OpenCVGameBot/
  pip install -r requirements.txt
```


    
## Usage

Open game in browser in fullscreen mode (configs for FullHD monitors) and run:
```bash
python main.py
```
in console.

If your monitor is not Full HD or not with an aspect ratio of 16:9,
expand the browser to full screen and write down in `main.py` the coordinates of
the **answer buttons**, the **start button** and the **coordinates of the rectangle**
in which the equations appear:

```python
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
```

If the bot gives errors/incorrectly finds the equation line, change `threshold` parameter in 77 line of `bot.py`