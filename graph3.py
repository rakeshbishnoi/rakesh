#my third graph
import matplotlib.pyplot as p

  
#line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
#line 1 points  
p.plot(x1, y1, label = "line 1") 
 
x2 = [1,2,3] 
y2 = [4,1,3] 
  
p.plot(x2, y2, label = "line 2") 
  
p.xlabel('x-axis')

p.ylabel('y-axis') 
 
p.title('Two lines on same graph!') 
   
p.show() 
