import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
a = []
b = []
c = []
d = []
e = []
with open('data2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
        a.append(float(row[3]))
        b.append(float(row[4]))
        c.append(float(row[5]))
        d.append(float(row[6]))
        e.append(float(row[7]))




plt.bar(x,y)
plt.plot(x,z)
plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)
plt.plot(x,d)
plt.plot(x,e)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')

plt.show()
