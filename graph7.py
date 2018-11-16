import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))
        


plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')

plt.show()


