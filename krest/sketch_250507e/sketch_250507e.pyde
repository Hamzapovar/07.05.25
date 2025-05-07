def setup():
    size(500,500)
def draw():
    for x in range(0,500,100):
        rect(x,250,50,50)
        rect(200,x+50,50,50)
        
