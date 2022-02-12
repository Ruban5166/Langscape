def displayn (n):
    print(n)
    n = n + 1
    if n <= 5:
        displayn(n)
    

displayn(1)    