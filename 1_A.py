nums = input()
nums = nums.split()
t_room = int(nums[0])
t_cond = int(nums[1])
mode = input()
if mode == "freeze":
    if t_room <= t_cond:
        print(t_room)
    else:
        print(t_cond)
elif mode == "heat":
    if t_room >= t_cond:
        print(t_room)
    else:
        print(t_cond)
elif mode == "auto":
    print(t_cond)
elif mode == "fan":
    print(t_room)
else:
    print("wrong condition")
