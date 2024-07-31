#Shortest Job First(SJF)
size = int(input("Enter the number of processes -- "))
bt,wt,tat,p = [],[],[],[]
for i in range(size) :
    bt.append(int(input("Enter Brust Time for Process {} -- ".format(i))))
    p.append(i)
for i in range(size-1) :
    for j in range(i+1,size):
        if(bt[i]>bt[j]):
            bt[i],bt[j]=bt[j],bt[i]
            p[i],p[j]=p[j],p[i]
print("PROCESS\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
sum1 = 0
for i in range(size):
    wt.append(sum1)
    sum1=sum1+bt[i]
    tat.append(sum1)
    print("P",p[i],"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i],sep="")
avg1=sum(wt)/size
avg2=sum(tat)/size
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
