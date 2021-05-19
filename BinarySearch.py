def binarySearch(list,elm):
    li=0
    ui=len(list)-1
    while li<=ui:
        mi=(li+ui)//2
        if list[mi]==elm:
            return mi
        else:
            if list[mi]<elm:
                li=mi+1
            else:
                ui=mi-1
    return -1
l=[1,5,8,9,12,15,17,20]
si=binarySearch(l,0)
if si==-1:
    print("not found")
else:
    print("found at ",si)