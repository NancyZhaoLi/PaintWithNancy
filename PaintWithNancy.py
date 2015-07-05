#Nancy Li's Paint Porgram
#This paint porgram will allow users to select their tool of choice and to draw on the canvas.
#Some of the tools are pencil, eraser, stamps and more!!!
#The size of the stokes can change and the chosen colour is showed at the upper left corner of the canvas.
#Position of the mouse is showed at lower right corner.
#Please enjoy!!!!!!!


from pygame import *
from random import*


def running():
    for evnt in event.get():          
        if evnt.type == QUIT:
            return False
    if key.get_pressed()[27]:return False
    return True
    
init()
screen = display.set_mode((990, 742))
pic = image.load("background-with stamps.jpg")   #load background
screen.blit(pic,(0,0))



#Sizes--------------------------------------------------
showcolourRect = Rect(275,100,50,20)
colourRect = Rect(0,540,255,202)
canvasRect = Rect(268,82,558,553)
eraserRect = Rect(835,80,70,60)
paintbrushRect = Rect(910,80,65,60)
lineRect = Rect(835,145,70,65)
pencilRect = Rect(910,145,65,65)
filledovalRect = Rect(825,215,70,65)
filledrectangleRect = Rect(910,215,65,65)
stamponeRect = Rect(265,655,72,65)
stamptwoRect = Rect(345,660,65,65)
stampthreeRect = Rect(420,660,65,65)
stampfourRect = Rect(495,660,75,65)
stampfiveRect = Rect(580,660,85,65)
stampsixRect = Rect(670,660,90,65)
stampsevenRect = Rect(770,660,75,65)
clearRect = Rect(835,535,78,78)
saveRect =  Rect(915,490,60,60)
rectangleRect = Rect(950,285,25,60)
ovalRect = Rect(915,285,25,60)
spraypaintRect = Rect(835,285,70,60)
loadRect = Rect(855,440,55,55)

#Preset------------------------------------------------
tool = "pencil"
colour=(0,0,0)
running = True
mx=my=0
init()
fnt = font.SysFont("Papyrus",18)
size=2

#Porgram starts--------------------------------------
while running:
    for evnt in event.get():    
        if evnt.type == QUIT:
            running = False 
        if evnt.type==MOUSEBUTTONDOWN:
            copy=screen.copy()
            amx,amy=mouse.get_pos()   #for the line tool, this is the first point 
            if evnt.button ==5:    #change size of stoke
                size+=2
            if evnt.button ==4:
                size= max(2, size-2)
    if key.get_pressed()[27]:break
    omx,omy=mx,my                 #position of the mouse
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    #SHOW POSITION------------------------------------
    text = "%4d %4d" % (mx,my)
    textPic = fnt.render(text,1,(0,0,0))  
    screen.blit(textPic, (900,700))
    
    #SELECT COLOUR------------------------------------
    if mb[0]==1 and colourRect.collidepoint(mx,my):
        colour=screen.get_at((mx, my)) 
        draw.rect(screen,colour,showcolourRect)
            
    # SELECT TOOLS --------------------------------------
    #have all pictures loaded here
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool = "pencil"
    if mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool = "eraser"
    if mb[0]==1 and paintbrushRect.collidepoint(mx,my):
        tool = "paintbrush"
    if mb[0]==1 and lineRect.collidepoint(mx,my):
        tool = "line"
    if mb[0]==1 and filledovalRect.collidepoint(mx,my):
        tool = "filledoval"
    if mb[0]==1 and ovalRect.collidepoint(mx,my):
        tool = "oval"
    if mb[0]==1 and filledrectangleRect.collidepoint(mx,my):
        tool = "filledrectangle"
    if mb[0]==1 and rectangleRect.collidepoint(mx,my):
        tool = "rectangle"
    if mb[0]==1 and spraypaintRect.collidepoint(mx,my):
        tool = "spraypaint"
    if mb[0]==1 and clearRect.collidepoint(mx,my):   #clear canvas by filling the canvas white
        draw.rect(screen,(250,250,250),canvasRect)
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        name=raw_input("Enter file name to be saved as and file type")   #save here
        image.save(screen,name)
    if mb[0]==1 and loadRect.collidepoint(mx,my):
        name=raw_input("Enter file name that you want to load(example:  folder//filename.extension ")
        image.load(name)                               #load here
    if mb[0]==1 and stamponeRect.collidepoint(mx,my):    #start choosing stamps here
        tool = "stampone"
        stampone = image.load("butterfly-size copy.png")
    if mb[0]==1 and stamptwoRect.collidepoint(mx,my):
        tool = "stamptwo"
        stamptwo = image.load("tree-sized copy.png")
    if mb[0]==1 and stampthreeRect.collidepoint(mx,my):
        tool = "stampthree"
        stampthree = image.load("nancy-sized copy.png")
    if mb[0]==1 and stampfourRect.collidepoint(mx,my):
        tool = "stampfour"
        stampfour = image.load("heart-sized copy.png")
    if mb[0]==1 and stampfiveRect.collidepoint(mx,my):
        tool = "stampfive"
        stampfive = image.load("Cherry B1-sized copy.png")
    if mb[0]==1 and stampsixRect.collidepoint(mx,my):
        tool = "stampsix"
        stampsix = image.load("rose-sized copy.png")
    if mb[0]==1 and stampsevenRect.collidepoint(mx,my):
        tool = "stampseven"
        stampseven = image.load("Leaf-sized copy.png")
    
    # DRAW ON CANVAS ------------------------------------    
    if mb[0]==1 and canvasRect.collidepoint(mx,my): #pencil and paint brush are the same since user can decide how thick the stoke is
        screen.set_clip(canvasRect)
        if tool == "pencil":
            draw.line(screen,colour,(omx,omy),(mx,my),size)
        if tool == "eraser":
            draw.line(screen,(250,250,250),(omx,omy),(mx,my),size)
        if tool == "paintbrush":
            draw.line(screen,colour,(omx,omy),(mx,my),size)
        if tool == "line":  
            screen.blit(copy,(0,0))
            draw.line(screen,colour,(amx,amy),(mx,my),size)
        if tool == "spraypaint":
            x=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]   #random points
            shuffle(x)
            a=mx+x[2]
            b=my+x[5]
            draw.circle(screen,colour,(a,b),1)
        if tool == "filledrectangle":       #didn't use absolute value 
            screen.blit(copy,(0,0))   
            if amx>mx:   #drag between left to right
                if amy>my:   #drag between up and down
                    draw.rect(screen,colour,Rect(mx,my,amx-mx,amy-my))
                if amy<=my:
                    draw.rect(screen,colour,Rect(mx,amy,amx-mx,my-amy))
            elif amx<=mx:
                if amy>my:
                    draw.rect(screen,colour,Rect(amx,my,mx-amx,amy-my))
                if amy<=my:
                    draw.rect(screen,colour,Rect(amx,amy,mx-amx,my-amy))
        if tool == "rectangle":
            screen.blit(copy,(0,0))
            if amx>mx:
                if amy>my:
                    draw.rect(screen,colour,Rect(mx,my,amx-mx,amy-my),size)
                if amy<=my:
                    draw.rect(screen,colour,Rect(mx,amy,amx-mx,my-amy),size)
            elif amx<=mx:
                if amy>my:
                    draw.rect(screen,colour,Rect(amx,my,mx-amx,amy-my),size)
                if amy<=my:
                    draw.rect(screen,colour,Rect(amx,amy,mx-amx,my-amy),size)
        if tool == "oval":   
            screen.blit(copy,(0,0))
            if amx-mx>1:   #width must be larger than radius
                if amy-my>1:
                    draw.ellipse(screen,colour,Rect(mx,my,amx-mx,amy-my),size)
                if my-amy>1:
                    draw.ellipse(screen,colour,Rect(mx,amy,amx-mx,my-amy),size)
            elif mx-amx>1:
                if amy-my>1:
                    draw.ellipse(screen,colour,Rect(amx,my,mx-amx,amy-my),size)
                if my-amy>1:
                    draw.ellipse(screen,colour,Rect(amx,amy,mx-amx,my-amy),size)
        if tool == "filledoval":
            screen.blit(copy,(0,0))
            if amx>mx:
                if amy>my:
                    draw.ellipse(screen,colour,Rect(mx,my,amx-mx,amy-my))
                if amy<=my:
                    draw.ellipse(screen,colour,Rect(mx,amy,amx-mx,my-amy))
            elif amx<=mx:
                if amy>my:
                    draw.ellipse(screen,colour,Rect(amx,my,mx-amx,amy-my))
                if amy<=my:
                    draw.ellipse(screen,colour,Rect(amx,amy,mx-amx,my-amy))
#stamps-------------------------------------------------------
        if tool == "stampone":             
            screen.blit(copy,(0,0))
            screen.blit(stampone,(mx-50,my-50))
        if tool == "stamptwo": 
            screen.blit(copy,(0,0))
            screen.blit(stamptwo,(mx-50,my-50))        
        if tool == "stampthree": 
            screen.blit(copy,(0,0))
            screen.blit(stampthree,(mx-50,my-50))
        if tool == "stampfour": 
            screen.blit(copy,(0,0))
            screen.blit(stampfour,(mx-50,my-50))
        if tool == "stampfive": 
            screen.blit(copy,(0,0))
            screen.blit(stampfive,(mx-50,my-50))
        if tool == "stampsix": 
            screen.blit(copy,(0,0))
            screen.blit(stampsix,(mx-50,my-50))
        if tool == "stampseven": 
            screen.blit(copy,(0,0))
            screen.blit(stampseven,(mx-50,my-50))
    
    display.flip()                     

del fnt 
quit()
