def f1_sort(s):
    if len(s)<=1:
        return s
    elem=s[0]
    left=list(filter(lambda x:x<elem,s))
    center=[i for i in s if i==elem]
    right=list(filter(lambda x:x>elem,s))

    return f1_sort(left)+center+f1_sort(right)
print (f1_sort([7,6,10,5,9,8,3,4]))