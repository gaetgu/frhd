

from frhd import Encode as En #import Encode.py (for encoding base32)

class Track():
    """Create a freerider track instance."""

    def __init__(self):
        self.trackdata = '' #This will hold the track's mathematical parts
        self.tracklist = [[],[],[]] #3 lists: one for physics lines, one for scenery, and one for powerups

    def insLine(self, typeofline, *points):
	    points = list(points)
	    formattedPoints = []
	    unpack = (lambda x, n:[formattedPoints.append(item) if type(item) == int else unpack(item, n+1) for item in x if n <= 100])
	    unpack(points, 0)
	    if len(formattedPoints) % 2 == 1:
		    points.pop()
	    if len(formattedPoints) < 4:
		    return
	    if typeofline == 'p': #physics
		    self.tracklist[0] += [formattedPoints]
	    if typeofline == 's': #scenery
		    self.tracklist[1] += [formattedPoints]

    def insStar(self,x,y):
        self.tracklist[2] += [['C',x,y]]

    def insCheck(self,x,y):
        self.tracklist[2] += [['T',x,y]]

    def insSlowMo(self,x,y):
        self.tracklist[2] += [['S',x,y]]

    def insBomb(self,x,y):
        self.tracklist[2] += [['O',x,y]]

    def insGravity(self,x,y,rot):
        assert rot in range(360) #gravity has rotation too
        self.tracklist[2] += [['G',x,y,rot]]

    def insBoost(self,x,y,rot):
        assert rot in range(360)
        self.tracklist[2] += [['B',x,y,rot]]
    
    def insStartLine(self):
        insLine(-40, 50, 40, 50, 'p')
    

    def moveTrack(track):
	
	#from google.colab import files
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

def bten(number, printt=False):
    if len(number) > 0:
        if number[0] == '-':
            negative = 1
            number = number[1:]
        else:
            negative = 0
        answer = 0
        digit = len(number) - 1
        pv = 0
        while digit >= 0:
            answer += (numbers.index(number[digit]) * (32 ** pv))
            digit -= 1
            pv += 1
        if negative == 1:
            answer *= -1
        return answer

def b32(number):
    number = int(number)
    if number < 0:
        negative = 1
        number = abs(number)
    else:
        negative = 0
    if number != 0:
        answer = []
        while number != 0:
            remain = int(number % 32)
            answer.insert(0, str(numbers[remain]))
            number = int((number - remain) / 32)
        if negative == 1:
            answer.insert(0, '-')
        answer = ''.join(answer)
    else:
        answer = '0'
    return answer


code = input('Please input your track text below:\n')
codes = list(code.split('#'))
codes = [[item] for item in codes]
codes = [item[0].split(',') for item in codes]
tempcodes = []
temp = []
for item in codes:
    for point in item:
        temp.append(point.split(' '))
    tempcodes.append(temp)
    temp = []
codes = tempcodes



print('\n')
x = None
while not(type(x) is int):
    x = input('How far would you like to move the track on the x axis?\nNote: 10 units = one 10 size grid square\n')
    try: x = int(x)
    except: print('\nPlease enter an integer for x, or this will not work.\n')

print('\n')
y = None
while not(type(y) is int):
    y = input('How far would you like to move the track on the y axis?\nNote: a positive y value moves the track down, while a negative y value moves the track up.\n')
    try: y = int(y)
    except: print('\nPlease enter an integer for y, or this will not work.\n')

for linetype in range(len(codes)):
    for line in range(len(codes[linetype])):
        coordpair = []
        for point in range(len(codes[linetype][line])):
            if point >= 0:
                coordpair.append([codes[linetype][line][point], point])
                if (point % 2 == 1 and linetype < 2) or (point % 2 == 0 and linetype == 2):
                    if (linetype < 2 or (codes[linetype][line][point].isupper() == False)) and len(coordpair) > 1:
                        codes[linetype][line][coordpair[0][1]] = b32(bten(coordpair[0][0]) + x)
                        codes[linetype][line][coordpair[1][1]] = b32(bten(coordpair[1][0]) + y)
                    coordpair = []

end = ''
for linetype in codes:
    for line in linetype:
        end += ' '.join(line) + ','
    end += '#'

doit = 'n'
while not(doit == 'y'):
    file = input('\nWhat would you like to save your track as?\n')
    try: f = open(file + '.txt')
    except: doit = 'y'
    else: doit = input('\nThere is already a file with this name. Are you sure you would like to overwrite it?\n"y" = yes\nliterally anything else = no\n')

with open(file + '.txt', 'w') as f:
    f.write(end)
print('\nThe moved track,', file + '.txt' + ', is now available wherever your python script is kept.')


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

if __name__ == '__main__':
    my_track = Track()
    my_track.insLine(6,6,6,6,'p')
    my_track.insLine(6,6,6,6,'s')
    my_track.insStar(6,6)
    my_track.insCheck(6,6)
    my_track.insSlowMo(6,6)
    my_track.insBomb(6,6)
    my_track.insGravity(6,6,6)
    my_track.insBoost(6,6,6)
    my_track.genCode()
    print(my_track.genCode())

			
