w=1
def setup():
    size(500,500)
def draw():
    global w 
    for x in range(0,500,50):
        frameRate(5)
        fill(random(1,255),random(1,255),random(1,255))
        rect(x,x,w,w)
        w=w+1
        if w >=200:
            noLoop()
