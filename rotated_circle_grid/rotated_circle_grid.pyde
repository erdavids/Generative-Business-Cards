w, h = 1050, 600

colors = [(188, 216, 193), (214, 219, 178), (227, 217, 133), (229, 122, 68)]
colors = [(219, 177, 188), (211, 196, 227), (143, 149, 211), (137, 218, 255)]
colors = [(191, 107, 99), (217, 163, 132), (91, 158, 166), (169, 212, 217)]

grid_x = 22
grid_y = 22

grid_x_pixels = 1200
grid_y_pixels = 1200

sep_x = float(grid_x_pixels) / (grid_x - 1)
sep_y = float(grid_y_pixels) / (grid_y - 1)

def get_random_element(l):
    return l[int(random(len(l)))]

def setup():
    size(w, h)
    background(150)
    
    strokeWeight(3)
    
    pixelDensity(2)
    
    current_x = w/2.0 - grid_x_pixels/2.0 - 200
    current_y = h/2.0 - grid_y_pixels/2.0
    
    rotate(QUARTER_PI)
    for i in range(grid_x):
        for j in range(grid_y):
            
            fill(0)
            circle(current_x, current_y, 35)
            
            
            if (random(1) < .3):
                fill(200, 100, 100)
            else:
                fill(230, 230, 230)
            if (random(1) < .6):
                offset = random(10, 15)
            else:
                offset = 0
            circle(current_x - offset, current_y, 35)
            
            
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0
        current_x += sep_x
        
    save("Examples/" + str(int(random(100000))) + ".png"
    
    
