"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
state_order=["red", "red_amber", "green", "amber"]
state_index=0

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
duration_left=states[state]-1
systime +=1

# At the end of each step you should output the time and state using the statement on line 14
while True:
    if systime>maxtime:
        break
    if duration_left==0:
        state_index = (state_index+1)%len(state_order)
        state=state_order[state_index]
        duration_left=states[state]
    print(f"Time {systime:03} State {state}")
    duration_left-=1
    systime+=1