# Welcome to Track.py! This is the main file where the boring stuff happens.
# If you want to see something cool, check out Encode.py and Decode.py! That's
# where all the cool stuff happens. This is where I define my methods, have my
# tutorial function, etc. etc.




#  /$$$$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$
# | $$_____/| $$__  $$| $$  | $$| $$__  $$
# | $$      | $$  \ $$| $$  | $$| $$  \ $$
# | $$$$$   | $$$$$$$/| $$$$$$$$| $$  | $$
# | $$__/   | $$__  $$| $$__  $$| $$  | $$
# | $$      | $$  \ $$| $$  | $$| $$  | $$
# | $$      | $$  | $$| $$  | $$| $$$$$$$/
# |__/      |__/  |__/|__/  |__/|_______/
#
#   A python package to generate tracks completely with python.
#   Created and maintained by Gabriel Gutierrez.
#   Special thanks to Pie42 and Calculus0972 for helping out.
#
#   The directory structure:
#   .
#   ├── LICENSE
#   ├── README.rst
#   ├── _config.yml
#   ├── frhd
#   │   ├── Decode.py
#   │   ├── Encode.py
#   │   ├── Loader.py
#   │   ├── Track.py
#   │   ├── __init__.py
#   ├── frhd.egg-info
#   │   ├── PKG-INFO
#   │   ├── SOURCES.txt
#   │   ├── dependency_links.txt
#   │   └── top_level.txt
#   ├── index.html
#   ├── logo_v_one.png
#   ├── script.js
#   ├── setup.cfg
#   ├── setup.py
#   └── style.css
#


import json                     # Import json for the getTrack and getUser
import requests                 # Import requests for the getTrack and getUser
from frhd import Encode as En  # Import the encode.py file to encode to base32


class Track:

    def __init__(self):
        # Holds the track's math
        self.trackdata = ''

        # 3 empty lists, one each for physics, scenery, and powerups.
        self.tracklist = [[], [], []]


    # Inserts a line
    # Created by gaetgu, updated by Pie42
    def insLine(self, typeofline, *points):
        # Convert the *points argument into a list
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


    # Inserts a star
    # Created by gaetgu
    def insStar(self, x, y):
        self.tracklist[2] += [['T', x, y]]


    # Inserts a CheckPoint
    # Created by gaetgu
    def insCheck(self, x, y):
        self.tracklist[2] += [['T', x, y]]


    # Insert a SlowMo
    # Created by gaetgu
    def insSlo(self, x, y):
        self.tracklist[2] += [['S', x, y]]


    # Inserts a bomb
    # Created by gaetgu
    def insBomb(self, x, y):
         self.tracklist[2] += [['O', x, y]]


    # Inserts a gravity
    # Created by gaetgu
    def insGrav(self, x, y, rot):
        # Certain powerups have a rotation, expressed in degs clockwise from
        # the top.
        assert rot in range(360)
        self.tracklist[2] += [['G', x, y, rot]]

    # Inserts a boost
    # Created by gaetgu
    def insBoost(self, x, y, rot):
        assert rot in range(360)
        self.tracklist[2] += [['B', x, y, rot]]


    # Inserts a bezier curve
    # Created by Pie42, with help from gaetgu
    def insCurve(self, typeofline, num, minlen, *points):
        # typeofline: 'p', 's'
        # num: number of line segements in the curve
        # minlen: minimum length of the line segments
        # *points: use a single list of points, e.g. ↓
        # [(x, y), (x, y), (x, y)]
        if len(points) == 1 and (type(points[0]) == list or type(points[0]) == tuple):
            points = points[0]
        if len(points) < 3:
            return

        N = len(points)
        t = range(num + 1)
        curve = [[0,0] for i in range(num)]
        factorial = lambda x: 1 if x < 2 else x * factorial(x - 1)

        for i in range(N):
            # Binomial coefficient
            binomial = factorial(N - 1) / float(factorial(i) * factorial(N - 1) - i)

            # Bernstein polynomial
            bernstein = [binomial * ((m / num) ** i) * ((1 - (m / num)) ** ((N - 1) - i)) for m in t]

            cCurve = [[b * points[i][0], b * points[i][1]] for b in bernstein]
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

        self.insLine(kin, prevx, prevy, x, y)


        # Insert the default start line
        # Created by gaetgu
        def insStart(self):
            insLine('p', -40, 50, 40, 50)


        # Get info about a user
         @staticmethod
         def getUser(username):
             response = requests.get("https://www.freeriderhd.com/u/{}?ajax".format(username))
             return response.json()


        # Get info about a track
        @staticmethod
        def getTrack(track_id):
            response = requests.get("https://www.freeriderhd.com/t/{}?ajax=true".format(track_id))
            return response.json()

        
        #Generate the final code to be printed out
        def genCode(self):
            # Holds raw data to be joined into frhd text
            self.trackdatalist = [[],[],[]]

            for pline in self.tracklist[0]: # Physics
            self.trackdatalist[0] += En.encline(pline)

            for sline in self.tracklist[1]: # Scenery
            self.trackdatalist[1] += En.encline(sline)

            for pup in self.tracklist[2]: #powerups
            if len(pup) == 3: #if powerup does not have the rotation attribute
                self.trackdatalist[2] += En.encpup(pup[1],pup[2],pup[0])
            if len(pup) == 4: #if powerup does have rotation attribute
                self.trackdatalist[2] += En.encpupr(pup[1],pup[2],pup[3],pup[0])

            self.finalData = '' # This is what will be put into frhd

            for typ in self.trackdatalist: #type of object
                for indiv in typ: #individual object
                    self.finalData += indiv[0]
                self.finalData += '#'#add object end marker

            return self.finalData


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
