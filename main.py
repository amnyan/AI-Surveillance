class Image:
    def __init__(self, x , y):
        self.width = x
        self.height = y
        self.pixels = [[[0,0,0] for i in range(x)] for i in range(y)]
     
    def display(self):
         for row in self.pixels:
            for pixel in row:
                print(f"({pixel[0]}, {pixel[1]}, {pixel[2]})", end=" ")
            print()
            
    def set_pixel(self,x,y,r,g,b):
        self.pixels[y][x] = [r,g,b]
        
    def get_pixel(self,x,y):
        return self.pixels[y][x]
    
   
            
img = Image(4, 5)

img.set_pixel(3, 2, 255, 0,45)
img.set_pixel(1, 4, 10, 33,92)
img.set_pixel(0, 1, 23, 68,100)
img.set_pixel(2, 3, 215, 70,75)
img.display()

pixelValue = img.get_pixel(3, 2)
print("pixel (3, 2):", pixelValue)