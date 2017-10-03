#python for approximating size of a population of organisms.
#code created by Jessica Lam and Kevin Kye. For HW3 problem 3 due on October 6, 2017

num_organisms=int(input("Input approximate size of organisms: "))
avg_daily_increase= int(input("Input average daily increase: "))
num_days= int(input("Input number of days the organisms will be left to multiply: "))

avg_daily_increase_percent= avg_daily_increase/100
print("Day","\t","Approximate Population")
print("-"*50)
for nums in range(num_days):
    if (nums==0):
        approx_pop=num_organisms
        day=1
    else:
        approx_pop+=avg_daily_increase_percent*num_organisms
        num_organisms=approx_pop
        day=nums+1

    print(day,"\t", approx_pop)

