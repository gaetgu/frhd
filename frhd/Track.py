#  /$$$$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$
# | $$_____/| $$__  $$| $$  | $$| $$__  $$
# | $$      | $$  \ $$| $$  | $$| $$  \ $$
# | $$$$$   | $$$$$$$/| $$$$$$$$| $$  | $$
# | $$__/   | $$__  $$| $$__  $$| $$  | $$
# | $$      | $$  \ $$| $$  | $$| $$  | $$
# | $$      | $$  | $$| $$  | $$| $$$$$$$/
# |__/      |__/  |__/|__/  |__/|_______/


#  =============================================================
#   A python package to generate tracks completely with python.
#   Created and maintained by Gabriel Gutierrez.
#   Special thanks to Pie42 for helping out.
#
#   The directory structure:
#   .
#   ├── LICENSE
#   ├── README.rst
#   ├── _config.yml
#   ├── frhd
#   │   ├── Decode.py
#   │   ├── Decode.pyc
#   │   ├── Encode.py
#   │   ├── Loader.py
#   │   ├── Track.py
#   │   ├── __init__.py
#   │   └── __pycache__
#   │       ├── Decode.cpython-34.pyc
#   │       ├── Encode.cpython-34.pyc
#   │       ├── Loader.cpython-34.pyc
#   │       ├── Track.cpython-34.pyc
#   │       └── __init__.cpython-34.pyc
#   ├── frhd.egg-info
#   │   ├── PKG-INFO
#   │   ├── SOURCES.txt
#   │   ├── dependency_links.txt
#   │   └── top_level.txt
#   ├── index.html
#   ├── logo_v_one.png
#   ├── script.js
#   ├── setup.cfg
#   ├── setup.py
#   └── style.css
#  =============================================================

#  =============================================================
#  Track.py
#  =============================================================

from frhd import Encode as En  # Import the encode.py file to encode to base32
import random                  # Import the random library for track generator

# == Soon to be deprecated == #

from time import sleep         # Import the sleep libary for the track generator

# == /Soon to be deprecated = #

Class Track():

    # =========================== START OF CLASS =========================== #

    """Initialize the *self* item, a required argument for all funtions."""

    def __init__(self):

        # This will hold the track's mathematics.
        self.trackdata = ''

        # 3 empty lists, one each for physics, scenery, and powerups.
        self.tracklist = [[], [], []]

    """Insert Line"""

    def insLine(self, typeofline, *points):

        # Converts the *points argument to a list
        points = list(points)
        formatted_points = []

        # Unpacks points
        def unpack(x, n):
            if n <= 100:
                for item in x:
                    if type(item) == int:
                        formatted_points.append(item)
                    else:
                        unpack(item, n + 1)
                        unpack(points, 0)

        # Arrange the lists
        if len(formatted_points) % 2 == 1:
            points.pop()
        if len(formatted_points) < 4:
            return

        # Physics Line
        if typeofline == 'p':
            self.tracklist[0] += [formatted_points]

        # Scenery Line
        if typeofline == 's':
            self.tracklist[1] += [formatted_points]

    """Insert Star"""

    def insStar(self, x, y):

        self.tracklist[2] += [['T', x, y]]

    """Insert Checkpoint"""

    def insCheck(self, x, y):

        self.tracklist[2] += [['C', x, y]]

    """Insert Slow-Motion"""

    def insSlo(self, x, y):

        self.tracklist[2] += [['S', x, y]]

    """Insert Bomb"""

    def insBomb(self, x, y):

        self.tracklist[2] += [['O', x, y]]

    """Insert Gravity"""

    def insGrav(self, x, y, rot):

        # As you see below, certain powerups have a *rotation*. This is equal to
        # degrees clockwise starting at the top.

        assert rot in range(360)

        self.tracklist[2] += [['G', x, y, rot]]

    """Insert Boost"""

    def insBoost(self, x, y, rot):

        assert rot in range(360)

        self.tracklist[2] += [['B', x, y, rot]]

    """Insert the default "Start Line"."""

    def insStart(self):  # Needs no x/y since the line is defined in the code.

        insLine('p', -40, 50, 40, 50)  # Probably bad practice, but whatever.

    """Generate a random track."""

    # ============================= DEPRECATED ============================= #
    # == Code @ raw.githubusercontent.com/asdase26/FreeGen/master/main.py == #
    # ============================= DEPRECATED ============================= #

    # ====================================================================== #
    # ============================ END OF CLASS ============================ #
    # ====================================================================== #

"""Return the final track code"""

if __name__ == 'main':
    my_track = Track()
    my_track.insLine('p', 6, 6, 6, 6)
    my_track.insLine('s', 6, 6, 6, 6)
    my_track.insStar(6, 6)
    my_track.insCheck(6, 6)
    my_track.insSlowMo(6, 6)
    my_track.insBomb(6, 6)
    my_track.insGravity(6, 6, 6)
    my_track.insBoost(6, 6, 6)
    my_track.genCode()
    print(my_track.genCode())

# =========================================================================== #
# ============================== END OF FILE ================================ #
# =========================================================================== #
