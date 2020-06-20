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

#  ============================================================= #
#  Track.py
#  ============================================================= #

from frhd import Encode as En  # Import the encode.py file to encode to base32

# =============================== DEPRECATED =============================== #
# import random                                                              #
# from time import sleep                                                     #
# =============================== DEPRECATED =============================== #

Class Track:

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
    
    
    """Create a bezier curve (beta)"""
    
    def insCurve(self, linetype, num, minlen, *points):
    '''linetype: type of line ('s' = scenery, 'p' = physics')
    num: number of line segments making up the curve
    minlen: minimum length of a line segment in the curve
    i'm not going to bother to reimplement unpack or anything right now so points needs to be either a single list of points or a bunch of individual points'''
    #should get things out of a single list
    if len(points) == 1 and (type(points[0]) == list or type(points[0]) == tuple):
        points = points[0]
    
    if len(points) < 3:
        return
    
    N = len(points)
    t = range(num + 1)
    curve = [[0, 0] for i in range(num)]
    
    factorial = lambda x: 1 if x < 2 else x * factorial(x - 1)
    
    for i in range(N):
        #binomial coefficient
        binomial = factorial(N - 1) / float(factorial(i) * factorial((N - 1) - i))
        #bernstein polynomial
        bernstein = [binomial * ((m / num) ** i) * ((1 - (m / num)) ** ((N - 1) - i)) for m in t]
        #thing to add to curve(product of the bernstein and the current point)
        cCurve = [[b * points[i][0], b * points[i][1]] for b in bernstein]
        #adding cCurve to the total curve
        curve = list(map(lambda a, b: [a[0] + b[0], a[1] + b[1]], curve, cCurve))
    
    prevx = points[0][0]
    prevy = points[0][1]
    for i in range(num):
        x = int(curve[i][0])
        y = int(curve[i][0])
        if (prevx - x > minlen or prevx - x < -1 * minlen) or (prevy - y > minlen or prevy - y < -minlen):
            self.insLine(kind, prevx, prevy, x, y)
            prevx = x
            prevy = y
    self.insLine(kind, prevx, prevy, x, y)
    

    """Insert the default "Start Line"."""

    def insStart(self):  # Needs no x/y since the line is defined in the code.

        insLine('p', -40, 50, 40, 50)  # Probably bad practice, but whatever.


    """Generate a random track."""

    # ============================= DEPRECATED ============================= #
    # == Code @ raw.githubusercontent.com/asdase26/FreeGen/master/main.py == #
    # ============================= DEPRECATED ============================= #


    """Generate final code"""

    def genCode(self):
        self.trackdatalist = [[],[],[]] #holds raw data to be joined into frhd text

        for pline in self.tracklist[0]: #physics
            self.trackdatalist[0] += En.encline(pline)

        for sline in self.tracklist[1]: #scenery
            self.trackdatalist[1] += En.encline(sline)

        for pup in self.tracklist[2]: #powerups
            if len(pup) == 3: #if powerup does not have the rotation attribute
                self.trackdatalist[2] += En.encpup(pup[1],pup[2],pup[0])
            if len(pup) == 4: #if powerup does have rotation attribute
                self.trackdatalist[2] += En.encpupr(pup[1],pup[2],pup[3],pup[0])

        self.finalData = '' #this will be put into frhd

        for typ in self.trackdatalist: #type of object
            for indiv in typ: #individual object
                self.finalData += indiv[0]
            self.finalData += '#'#add object end marker

        return self.finalData


    # ====================================================================== #
    # ============================ END OF CLASS ============================ #
    # ====================================================================== #


if __name__ == 'main':
    my_track = Track()
    my_track.insLine(6, 6, 6, 6, 'p')
    my_track.insLine(6, 6, 6, 6, 's')
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
