a=[]
for x in range(0,10):
  a.append(int(input("Введіть елемент масиву")))
print(a)
srt=a[:]
srt.sort(reverse=True)
if srt[0]==srt[1]:
    num1=a.index(srt[0])
    num2=a.index(srt[1],num1+1)
    num3=a.index(srt[2],num2+1)
    num4=a.index(srt[3],num3+1)
    num5=a.index(srt[4],num4+1)
else:
    num1=a.index(srt[0])
    num2=a.index(srt[1])
    num3=a.index(srt[2])
    num4=a.index(srt[3])
    num5=a.index(srt[4])
print("Перший максимум = ", srt[0],"його номер ", num1)
print("Другий максимум = ", srt[1],"його номер ", num2)
print("Третій максимум = ", srt[2],"його номер ", num3)
print("Четвертий максимум = ", srt[3],"його номер ", num4)
print("Пятий максимум = ", srt[4],"його номер ", num5)