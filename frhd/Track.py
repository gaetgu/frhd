from frhd import Encode as En #import Encode.py (for encoding base32)

class Track():
	"""Create a freerider track instance."""

	def __init__(self):
		self.trackdata = '' #This will hold the track's mathematical parts
		self.tracklist = [[],[],[]] #3 lists: one for physics lines, one for scenery, and one for powerups
	
	def genPicture(self, inputted_image):
		if inputted_image[-2] == 'n':
			def convertIntB32(i):
	    		negative = False
	    		b = ''
	    		conv = "0123456789abcdefghijklmnopqrstuv"
	    		if i < 0:
	        		negative = True
	        		i = -i
	    		if i == 0: return '0'
	    		while(i>0):
	        		b = conv[i%32] + b
	        		i=(int)(i//32)
	    
	    		if negative:
	        		b = "-"+b
	        
	    		return(b)
	
			def convertB32Int(s):
	    		return(int(s,32))
	
			#You Need To Have PIL (pillow) and CV2 For This Part To Work
			#You Need To Name The File To A File From Your Computer
			import PIL.Image
			import cv2
	
			def get_image(filename):
	    		PIL.Image.open(filename)
	    		PIL.Image.open(inputted_image).convert('RGB').save('c.jpg')
	    		image = cv2.imread("c.jpg")
	    		return image
	
			filename = inputted_image
			image = get_image(filename)
	
	
			# Converting to grayscale
			try:
	    		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			except:
	    		gray = image
	
			from IPython.display import Image, display 
				gimage = Image('temp.png')
			
			cv2.imshow('sample image',gray)
	 
			cv2.waitKey(0) # waits until a key is pressed
			
			cv2.destroyAllWindows() # destroys the window showing image
	
			#This Part Was Made By Alex!
			def convert3(image):
	    		BLACK = 0
	    		WHITE = 255
	    		black_img = image.copy()
	    		gray_img = image.copy()
	    		for i in range(len(image)):
	        		for j in range(len(image[i])):
	            		if image[i][j] < 64:
	                		black_img[i][j] = BLACK
	                		gray_img[i][j] = WHITE
	            		if image[i][j] >= 64:
	                		black_img[i][j] = WHITE
	                		gray_img[i][j] = BLACK
	            		if image[i][j] > 191:
	                		black_img[i][j] = WHITE
	                		gray_img[i][j] = WHITE
	    		return black_img, gray_img
			(a3_black, a3_gray) = convert3(gray)
	
			print(a3_black.shape)
			print(a3_gray.shape)
	
			cv2.imshow('sample image',a3_black)
	 
			cv2.waitKey(0) # waits until a key is pressed
	
			cv2.destroyAllWindows() # destroys the window showing image
	
			cv2.imshow('sample image',a3_gray)
	 
			cv2.waitKey(0) # waits until a key is pressed
	
			cv2.destroyAllWindows() # destroys the window showing image
	
			bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	
	
			#cv2.imshow("sample image 2", gray) 
	
			#cv2.waitKey(0) # waits until a key is pressed
	
			#cv2.destroyAllWindows() # destroys the window showing image
	
			#Change The 0.5 To A Bigger Number
			img_black = cv2.resize(a3_black,None,fx=2,fy=2)
			img_gray = cv2.resize(a3_gray,None,fx=2,fy=2)
	
	
			img_black.shape
			img_gray.shape
	
			#This Part May Take A Bit Of Time
			def output_track_codes(bw_image):
	    		DEBUG = False
	    		line_coordinates = []
	    		for i in range(len(bw_image)):
	        		start = ""
	        		end = ""
	        		for j in range(len(bw_image[i])):
	            		if DEBUG: 
	                		print ("i = " + str(i) + " j = " + str(j) + " start = '" + start + "'" + 
	                   		" end = '" + end + "'" + " pixel value = " + str(bw_image[i][j]))
	            		if start == "" and bw_image[i][j] < 1:
	                		start = (str(j) + " " + str(i))
	                		if DEBUG: print("starting line at " + str(j) + "," + str(i))
	            		elif start != "" and bw_image[i][j] < 1:
	                		pass
	            		elif start == "" and bw_image[i][j] > 0:
	                		pass
	            		else:
	                		if DEBUG: print("ending line at " + str(j) + "," + str(i))
	                		end = str(j) + " " + str(i)
	                		line_coordinates = line_coordinates + [start + " " + end]
	                		start = ""
	                		end = ""
	                    
	        		if start != "" and end == "":
	            		if DEBUG: print("also ending line")
	            		end = (str(j) + " " + str(i))
	            		line_coordinates = line_coordinates + [start + " " + end]
	            		start = ""
	            		end = ""
	    
	    		# print(",".join([[convertIntB32(y) for y in x] for x in line_coordinates]))
	    
	    		return line_coordinates
	
			black_track_codes = output_track_codes(img_black)
			gray_track_codes = output_track_codes(img_gray)
	
			black_freerider_codes = (",".join([" ".join([convertIntB32(int(y)) for y in x.split()]) for x in black_track_codes])) 
			gray_freerider_codes = (",".join([" ".join([convertIntB32(int(y)) for y in x.split()]) for x in gray_track_codes]))
	
			def offsetFrhdCodes (track, xoffset, yoffset):
	    		track2 = []
	    		lines = track.split(",")
	    	
	    		for line in lines:
	        		splitline = line.split()
	        		line_offset = []
	        		line_offset.append(convertIntB32(convertB32Int(splitline[0]) + xoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[1]) + yoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[2]) + xoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[3]) + yoffset))
	        		track2.append(" ".join(line_offset))    
	    	
	    	return (",".join(track2))
	    
			black_offset_frhd_codes = offsetFrhdCodes(black_freerider_codes, -100, 100)
			gray_offset_frhd_codes = offsetFrhdCodes(gray_freerider_codes, -100, 100)
			
			#Your Final Code:
			print(black_offset_frhd_codes + "#" + gray_offset_frhd_codes + "#")

		elif inputted_image[-2] == 'p':
			def convertIntB32(i):
	    		negative = False
	    		b = ''
	    		conv = "0123456789abcdefghijklmnopqrstuv"
	    		if i < 0:
	        		negative = True
	        		i = -i
	    		if i == 0: return '0'
	    		while(i>0):
	        		b = conv[i%32] + b
	        		i=(int)(i//32)
	    
	    		if negative:
	        		b = "-"+b
	        
	    		return(b)
	
			def convertB32Int(s):
	    		return(int(s,32))
	
			#You Need To Have PIL (pillow) and CV2 For This Part To Work
			#You Need To Name The File To A File From Your Computer
			import PIL.Image
			import cv2
	
			def get_image(filename):
	    		PIL.Image.open(filename)
	    		#PIL.Image.open('c.png').convert('RGB').save('c.jpg')
	    		image = cv2.imread(inputted_image)
	    		return image
	
			filename = inputted_image
			image = get_image(filename)
	
	
			# Converting to grayscale
			try:
	    		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			except:
	    		gray = image
	
			from IPython.display import Image, display 
				gimage = Image('temp.png')
			
			cv2.imshow('sample image',gray)
	 
			cv2.waitKey(0) # waits until a key is pressed
			
			cv2.destroyAllWindows() # destroys the window showing image
	
			#This Part Was Made By Alex!
			def convert3(image):
	    		BLACK = 0
	    		WHITE = 255
	    		black_img = image.copy()
	    		gray_img = image.copy()
	    		for i in range(len(image)):
	        		for j in range(len(image[i])):
	            		if image[i][j] < 64:
	                		black_img[i][j] = BLACK
	                		gray_img[i][j] = WHITE
	            		if image[i][j] >= 64:
	                		black_img[i][j] = WHITE
	                		gray_img[i][j] = BLACK
	            		if image[i][j] > 191:
	                		black_img[i][j] = WHITE
	                		gray_img[i][j] = WHITE
	    		return black_img, gray_img
			(a3_black, a3_gray) = convert3(gray)
	
			print(a3_black.shape)
			print(a3_gray.shape)
	
			cv2.imshow('sample image',a3_black)
	 
			cv2.waitKey(0) # waits until a key is pressed
	
			cv2.destroyAllWindows() # destroys the window showing image
	
			cv2.imshow('sample image',a3_gray)
	 
			cv2.waitKey(0) # waits until a key is pressed
	
			cv2.destroyAllWindows() # destroys the window showing image
	
			bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	
	
			#cv2.imshow("sample image 2", gray) 
	
			#cv2.waitKey(0) # waits until a key is pressed
	
			#cv2.destroyAllWindows() # destroys the window showing image
	
			#Change The 0.5 To A Bigger Number
			img_black = cv2.resize(a3_black,None,fx=2,fy=2)
			img_gray = cv2.resize(a3_gray,None,fx=2,fy=2)
	
	
			img_black.shape
			img_gray.shape
	
			#This Part May Take A Bit Of Time
			def output_track_codes(bw_image):
	    		DEBUG = False
	    		line_coordinates = []
	    		for i in range(len(bw_image)):
	        		start = ""
	        		end = ""
	        		for j in range(len(bw_image[i])):
	            		if DEBUG: 
	                		print ("i = " + str(i) + " j = " + str(j) + " start = '" + start + "'" + 
	                   		" end = '" + end + "'" + " pixel value = " + str(bw_image[i][j]))
	            		if start == "" and bw_image[i][j] < 1:
	                		start = (str(j) + " " + str(i))
	                		if DEBUG: print("starting line at " + str(j) + "," + str(i))
	            		elif start != "" and bw_image[i][j] < 1:
	                		pass
	            		elif start == "" and bw_image[i][j] > 0:
	                		pass
	            		else:
	                		if DEBUG: print("ending line at " + str(j) + "," + str(i))
	                		end = str(j) + " " + str(i)
	                		line_coordinates = line_coordinates + [start + " " + end]
	                		start = ""
	                		end = ""
	                    
	        		if start != "" and end == "":
	            		if DEBUG: print("also ending line")
	            		end = (str(j) + " " + str(i))
	            		line_coordinates = line_coordinates + [start + " " + end]
	            		start = ""
	            		end = ""
	    
	    		# print(",".join([[convertIntB32(y) for y in x] for x in line_coordinates]))
	    
	    		return line_coordinates
	
			black_track_codes = output_track_codes(img_black)
			gray_track_codes = output_track_codes(img_gray)
	
			black_freerider_codes = (",".join([" ".join([convertIntB32(int(y)) for y in x.split()]) for x in black_track_codes])) 
			gray_freerider_codes = (",".join([" ".join([convertIntB32(int(y)) for y in x.split()]) for x in gray_track_codes]))
	
			def offsetFrhdCodes (track, xoffset, yoffset):
	    		track2 = []
	    		lines = track.split(",")
	    	
	    		for line in lines:
	        		splitline = line.split()
	        		line_offset = []
	        		line_offset.append(convertIntB32(convertB32Int(splitline[0]) + xoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[1]) + yoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[2]) + xoffset))
	        		line_offset.append(convertIntB32(convertB32Int(splitline[3]) + yoffset))
	        		track2.append(" ".join(line_offset))    
	    	
	    	return (",".join(track2))
	    
			black_offset_frhd_codes = offsetFrhdCodes(black_freerider_codes, -100, 100)
			gray_offset_frhd_codes = offsetFrhdCodes(gray_freerider_codes, -100, 100)
			
			#Your Final Code:
			print(black_offset_frhd_codes + "#" + gray_offset_frhd_codes + "#")
		
		else:
			print('ERROR:\n\n\t PLEASE USE A VALID FILETYPE (E.G. FILENAME.jpg, FILENAME.png)')
	
	def moveTrack(self, fov, track, xcoord, ycoord):

			if fov == 'f':
				with open(track, 'r') as file:
					track_code = file.read().replace('\n', '')
					print((lambda c,n,x,y,l:'#'.join([','.join([(lambda o:' '.join([(lambda m:(lambda p,v:'0'if p==0else(('-'if v else'')+''.join([n[((p//(32**q))%32)]for q in range(int(l.log(p,32))+1)][::-1])))(abs(m),(m<0)))(int(m,32)+x if(t!=2and j%2==0)or(t==2and j%2==1)else int(m,32)+y)if(t!=2or j!=0)else m for j,m in enumerate(o)if m!='']))(i.split(' '))for i in d])for t,d in enumerate(c)]))([a.split(',')for a in track_code.split('#')],list('0123456789abcdefghijklmnopqrstuv'),int(xcoord),int(ycoord),__import__('math')))
			else:
				track_code = str(track)
				print((lambda c,n,x,y,l:'#'.join([','.join([(lambda o:' '.join([(lambda m:(lambda p,v:'0'if p==0else(('-'if v else'')+''.join([n[((p//(32**q))%32)]for q in range(int(l.log(p,32))+1)][::-1])))(abs(m),(m<0)))(int(m,32)+x if(t!=2and j%2==0)or(t==2and j%2==1)else int(m,32)+y)if(t!=2or j!=0)else m for j,m in enumerate(o)if m!='']))(i.split(' '))for i in d])for t,d in enumerate(c)]))([a.split(',')for a in track_code.split('#')],list('0123456789abcdefghijklmnopqrstuv'),int(xcoord),int(ycoord),__import__('math')))

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
