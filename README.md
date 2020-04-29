# FRHD 
Free Rider HD is an HTML5 game that utilizes the canvas element to display an interactive biking game. This script allows you to make your own tracks using Python! Let's go over the basic syntax:

First of all, import the library:
```python
import frhd
```
Now create a track class:
```python
my_track = frhd.Track.Track()
```
Now that you have the frontmatter out of the way, create a line by calling
```python
my_track.insLine('p',-40,50,100,50)
```
The `'p'` in that statement tells the code to create a physics line.
Now you need to print out this code:
```python
print(my_track.genCode())
```
To create a scenery line you use the same code as last time, with the exception of replacing the `'p'` with an `'s'`. What you have should look like this:
```python
import frhd
my_track = frhd.Track.Track()
my_track.insLine('s',-40,50,100,50)
print(my_track.genCode())
```
To add a boost just use this syntax:
```python
my_track.insBoost(90,-10,90)
```

A quick note on how the coordinates work: The origin of the cartesian coordinate plane (0,0) is located near the center of the rider. To see where this is, turn on the grid in the editor. Zoom out. You should see thicker, darker lines at certain intervals. Where they intersect inside the rider is (0,0). When drawing a line, the first argument is the line type and then you can add as many coordinates as you want (e.g. `my_track.insLine('p', x1, y1, x2, y2, x3, y3, x4, y4)`). When using any kind of power-up, the third coordinate is acually degrees of rotation. Every coordinate is one-tenth of a ten grid square (the default size when you show the grid).

The other power-ups are as follows:

```python
my_track.insBoost(90,-10,90) # Boost
my_track.insBomb(90,10) # Bomb (no rotation as it is omni-directional)
my_track.insGravity(90,10,90) # Gravity
my_track.insCheck(90,10) # Checkpoint
my_track.insStar(90,10) # Star
my_track.insSlowMo(90,10) # Slow Motion
```

---


Some new syntax (still in beta):

```python
my_track.moveTrack(track_code)
```
This is pretty self-explanatory. just make a variable containing a *string* of your track code, then move it a certain amount in x-y axes.

--- 
PLANS:
  - Have the ability to open a file *or* use a variable
  - Tell it how much to move in the function, instead of inputting into the cmd

NOTE:
  - All beta developments are in the *beta* branch. If you would like to help, file an issue and I will get back to you ASAP.
  
---


This was all inspired by frhd.js, a library made by ObeyLordGoomy that does the same thing, but for JavaScript

