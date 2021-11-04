original_list=[10,20,30,40,50]
new_list=[]
if len(original_list)>1:
    new_list[0]=original_list[0]+original_list[1]
    for i in xrange(1,len(original_list)-1):
        new_list[i]=original_list[i-1]+original_list[i]+original_list[i+1]
        new_list[len(original_list)-1]=original_list[len(original_list)-2]+original_list[len(original_list)-1]
else:
    new_list[0]=original_list[0]
print(original_list)
print (new_list)
