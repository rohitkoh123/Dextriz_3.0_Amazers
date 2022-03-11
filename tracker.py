import math

def update(self,objects_rect):
#To find centre point of new object


    for rect in objects_rect:
        x,y,w,h,index =rect
        cx=(x+x+h)//2
        cy=(y+y+h)//2
#Check is it new object

        same_object=False
        for id,pt in self.center_points.items():
            dist = math.hypot(cx-pt[0],cy-pt[1])
            if dist<25:
                self.center_points[id]=(cx,cy)
                