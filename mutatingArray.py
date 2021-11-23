def mutatingArray(n, a):
    b = [None] * n
    for i in range(n):
        if ( i-1 >= 0 and a[i-1]):
            b[i] = a[i-1]
        else:
            b[i] = 0
        if(a[i]):
            b[i] = b[i] + a[i]
        if( i+1 < n and a[i+1]):
            b[i] = b[i] + a[i+1]
    return b
