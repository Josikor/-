def f1_search(d,search_k):
    low=0
    high=len(d)-1
    search_res=False
    while low<=high and not search_res:
        middle=(low+high)//2
        guess=d[middle]
        if guess==search_k:
            search_res=True
            return search_res
        if guess>search_k:
            high=middle-1
        else:
            low=middle+1
    return search_res
d=[3,7,2,9,11,23,75,46,83,24,76,55]
value=55
result=f1_search(d,value)
if result:
    print("Елемент не знайдено")
else:
    print("Елемент знайдено")
