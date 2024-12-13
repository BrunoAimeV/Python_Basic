for num in range(2,101):
    primer = True
    for i in range(2, num):
        if num%i==0:
            primer = False
            break
    if primer:
        print(num)