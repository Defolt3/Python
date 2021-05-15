
cl = 0
dc = False
def setup():
    size(400,400)
def draw(): 
    background(0,255,99)
    global cl,dc 
    if cl == 1:  
        text("hi master",30,200)
    if cl == 30:
        text(")))))", 30, 200) 
    if cl == 99:
        text("WIN", 100,100) ,textSize(20) ,text(cl,30,30)  
    if cl == 98:
        fill(random(0,255),random(0,255),random(0,255)) 
def mouseClicked():
    circle(56, 46, 55)
    global cl,dc 
    if mouseButton == LEFT: 
        cl += 1 
    if mouseButton == LEFT: 
        fill("#000000") 
    if cl >= 100: 
        cl = 0 
    if cl >= 99: 
        dc = True 
    if dc == True: 
        cl += 1
