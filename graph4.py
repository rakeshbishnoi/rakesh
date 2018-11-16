import matplotlib.pyplot as P

a = ['eat','sleep','code','repeat']
b = [1,2,3,4]
P.pie(b, labels = a, colors=['red','blue','green','yellow'],startangle=90, shadow = True, explode = (0, 0, 0.1, 0),radius = 1.2, autopct = '%1.1f%%')
P.show()
