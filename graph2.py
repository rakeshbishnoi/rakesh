import matplotlib.pyplot as p

xaxis=[1,2,3,4,5]
yaxis=[10,24,36,40,5]
p.bar(xaxis,yaxis,tick_label=['one','two','three','four','five'],width = 0.8,color = ['blue','green'])
p.xlabel('x axis')
p.ylabel('y axis')
p.title('my 2nd graph !')
p.show()
