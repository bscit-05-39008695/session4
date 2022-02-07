maths=int(input("Enter the maths score:"))
english=int(input("Enter the english score:"))
kiswahili=int(input("Enter the kiswahili score:"))
geo=int(input("Enter the geo score:"))
business=int(input("Enter the business score:"))
score=(maths+english+kiswahili+geo+business)/5
print('score:',score)
if score>=70 and score<=100 :
 print('A')
elif score>=60 and score<=69:
 print('B')
elif score>=50 and score <=59:
 print('C')
elif score>=40 and score<=49:
 print('D')
elif score>=0 and score<39:
 print('fail')
else:
 print("Invalid marks")