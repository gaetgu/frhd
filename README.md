# FRHD 
Free Rider HD is an HTML5 game that utilizes the canvas element to display an interactive biking game. This script allows you to make your own tracks using Python! Let's go over the basic syntax:

First of all, import the library:
```python
import frhd
```
Now create a track class:
```python
my_track = frhdtools.Track.Track()
```
Now that you have the frontmatter out of the way, create a line by calling
```python
my_track.insLine(-40,50,100,50,'p')
```
The `'p'` in that statement tells the code to create a physics line.
Now you need to print out this code:
```python
print(my_track.genCode())
```
To create a scenery line you use the same code as last time, with the exception of replacing the `'p'` with an `'s'`. What you have should look like this:
```python
import frhdtools
my_track = frhdtools.Track.Track()
my_track.insLine(-40,50,100,50,'s')
print(my_track.genCode())
```
To add a boost just use this syntax:
```python
my_track.insBoost(90,-10,90)
```
<br>
---
<br>
A quick note on how the coordinates work: The origin of the cartesian coordinate plane (0,0) is located near the center of the rider. To see where this is, turn on the grid in the editor. Zoom out. You should see thicker, darker lines at certain intervals. Where they intersect inside the rider is (0,0). When drawing a line, the first two coordinates are the starting point and the second two are the endpoint. When using any kind of power-up, the third coordinate is acually degrees of rotation. Every coordinate is one-tenth of a ten grid square (the default size when you show the grid).
<br>
--- 
<br>
<br>
The other power-ups are as follows:
<br>
```python

my_track.insBoost(90,-10,90) # Boost
my_track.insBomb(90,10) # Bomb (no rotation as it is omni-directional)
my_track.insGravity(90,10,90) # Gravity
my_track.insCheck(90,10) # Checkpoint
my_track.insStar(90,10) # Star
my_track.insSlowMo(90,10) # Slow Motion
```

This was all inspired by frhd.js, a library made by ObeyLordGoomy that does the same thing, but for JavaScript

