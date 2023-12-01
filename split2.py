import yearextractor as ys
 
 
str2=ys.yearsemextractor()
result = str2.split('-')
d2=result[1]
d3=result[2]

#print(d2)
print(d3)


result2 = d2.split(' ')

year=result2[1]
term=result2[3]
print("----Year----")
print(year)
print("----Term----")
print(term)