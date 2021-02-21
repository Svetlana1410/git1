from openpyxl import load_workbook
class Dot:

    def __init__(self,a,b,c):
        self.__x = a
        self.__y = b
        self.__z = c

    def info(self):
        return f"x = {self.__x} y = {self.__y} z = {self.__z}"



wb = load_workbook('dots.xlsx')
sheet = wb['Second']
x = []
y = []
z = []
counter = 1
counter1 = 1
counter2 = 1
while sheet['A' + str(counter)].value != None:
    x.append(sheet['A' + str(counter)].value)
    counter += 1
while sheet['B' + str(counter1)].value != None:
    y.append(sheet['B' + str(counter1)].value)
    counter1 += 1
while sheet['C' + str(counter2)].value != None:
    z.append(sheet['C' + str(counter2)].value)
    counter2 += 1

f = open('Output.txt', 'w')
s=""
for i in range(len(x)):
    a = Dot(x[i],y[i],z[i])  
    s+=a.info()+"\n"
    
f.write(s)
f.close()
print(s)

