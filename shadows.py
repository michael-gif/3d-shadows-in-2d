from PIL import Image
import math
#campos = [int(input('Camera x:')),int(input('Camera y:')),int(input('Camera z:'))]
light = [-100,-100,-25]
wall = [0,0,-5]
image = Image.open('canvas.png')
pixels = image.load()
distances = []
z = 0
for y in range(image.size[1]):
    for x in range(image.size[0]):
        diffx = light[0] - x
        diffy = light[1] - y
        diffz = light[2] - z
        xsquared = diffx ** 2
        ysquared = diffy ** 2
        zsquared = diffz ** 2
        hypotenuse = xsquared + zsquared + ysquared
        distance = math.sqrt(hypotenuse)

        scalefactor = wall[2] / light[2]
        wallx = diffx * scalefactor
        wallx += x
        wally = diffy * scalefactor
        wally += y
        #wallx = light[0] * scalefactor
        #wally = light[1] * scalefactor
        wallpixel = [wallx,wally,wall[2]]
        diffx = wallpixel[0] - x
        diffy = wallpixel[1] - y
        diffz = wallpixel[2] - z
        xsquared = diffx ** 2
        ysquared = diffy ** 2
        zsquared = diffz ** 2
        hypotenuse = xsquared + zsquared + ysquared
        distance2 = math.sqrt(hypotenuse)
        
        if distance > distance2:
            if wallpixel[0] >= 0 and wallpixel[0] <= 200 and wallpixel[1] >= 0 and wallpixel[1] <= 200:
                c = 0
            else:
                fraction = distance/1000
                fraction = 1 - fraction
                c = int(fraction * 255)
                #c = 255
        else:
            fraction = distance/1000
            fraction = 1 - fraction
            c = int(fraction * 255)
        pixels[x,y] = (c,c,c)
image.save('mod.png')
