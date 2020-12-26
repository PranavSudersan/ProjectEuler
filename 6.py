n = 100 #n natural numbers
s1 = 0 #sum of squares
for i in range(1,n+1):
    s1 += i**2

s2 = (n*(n+1)/2)**2 #square of sum

print(f'Difference is {s2-s1}')
