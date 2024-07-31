#FIRST COME FIRST SERVE(FCFS)
size = int(input("Enter the number of processes -- "))
bt,wt,tat = [],[],[]
for i in range(size) :
    bt.append(int(input("Enter Brust Time for Process {} -- ".format(i))))
print("PROCESS\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
time = 0
for i in range(size):
    wt.append(time)
    time=time+bt[i]
    tat.append(time)
    print("P",i,"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i],sep="")
avg1=sum(wt)/size
avg2=sum(tat)/size
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
