import math

# a function that displays an area of circle with radius and pi 

def Area_Of_Circle(r):

    a = math.pi*r**2
    return a

# a function that displays Fahrenheit changes to Celsius degrees 

def Fahrenheit_To_Celsius(f):
    c = (f-32)*5.00/9.00
    return c

# a function that displays Miles Per Gallon – a measure of how far a car can travel if you put just one gallon

def MPG(m, g):

    mpg = float(m/g)
    return mpg

# a function that displays a vertical line at a given x coordinate on the gfx hat

def vertical_line(x):
    from gfxhat import lcd
    from time import sleep
    lcd.clear()
    lcd.show()
    for y in range(0,64):
        lcd.set_pixel(x,y,1)
        lcd.show()
    sleep(6)
    lcd.clear()
    lcd.show()

# a function that displays a horizontal line at a given y coordinate.
def horizontal_line(y):
    from gfxhat import lcd
    from time import sleep
    lcd.clear()
    lcd.show()
    for x in range(0,127):
        lcd.set_pixel(x,y,1)
        lcd.show()
    sleep(6)
    lcd.clear()
    lcd.show()
# Create a function that creates a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
from gfxhat import lcd
def staircase(x,y,w,h):
    while x <= 127 and y >= 0:
        for width in range(w):
            x = x + 1
            if(x > 127 or y < 0):
                break
            lcd.set_pixel(x,y,1)
            lcd.show()
        for height in range(h):
            y = y - 1
            if(x > 127 or y < 0):
                break
            lcd.set_pixel(x,y,1)
            lcd.show()


#Create a function that displays random pixel on the screen for a given period of time specifies in seconds.
import random,datetime
def Random_Pixel(s):
  secondsNow = datetime.datetime.now()
  secondsPlusNow = secondsNow + datetime.timedelta(seconds=s) #this five is the number of seconds that the program should run
  while(datetime.datetime.now() <= secondsPlusNow):
    x = random.randint(0,127)
    y = random.randint(0,63)
    lcd.set_pixel(x,y,1)
    lcd.show()

# Create a function clearBacklight() that resets the backlight color.

def backlight_clear_reset():
    from gfxhat import touch, lcd, backlight
    from time import sleep
    lcd.clear()
    lcd.show()
    i='0'
    if i=='0':
     backlight.set_all(220,130,110)
     backlight.show()
     sleep(1)
     backlight.set_all(120,230,110)
     backlight.show()
     sleep(1)
     backlight.set_all(0,0,110)
     backlight.show()
     sleep(3)
     for x in range(6):
         backlight.set_pixel(x, 0, 0, 0)
         touch.set_led(x, 0)
         backlight.show()
         lcd.clear()

# a function moveObject
def moveObject(obj,x,y,vx,vy):
    eraseObject(obj, x, y)
    x=x+vx
    y=y+vy
    displayObject(obj, x, y)
    sleep(0.15)
    return (x,y)

# a function moveObject
def checkCollision(obj,x,y,vx,vy,Sx=128,Sy=64):
    if x<=0:
        vx = (-vx)
    if x>Sx-1-len(obj[0]):   # size of X in gfx hat , length of width of my object , -1 (because of start from 0 no 1 and end 127 no 128 ) 
        vx = (-vx)              # change my direction on X
    if y<=0:
        vy= (-vy)                # change my direction on Y
    if y>Sy-1-len(obj):   # size ofY in gfx hat , length of height of my object , -1 (because of start from 0 no 1 and end 63 no 64 )
        vy= (-vy) 
        
    return vx,vy

# The function erases an object
def eraseObject(obj,x,y):
    for row in range(y,len(obj)+y):
        for column in range(x,len(obj[row-y])+x):
            lcd.set_pixel(column, row, 0)
    lcd.show()

