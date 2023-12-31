a, b, c = map(int,input().split(" "))

mAB = (a+b+abs(a-b))/2
mMC = int((mAB+c+abs(mAB-c))/2)
print(f"{mMC} eh o maior")
