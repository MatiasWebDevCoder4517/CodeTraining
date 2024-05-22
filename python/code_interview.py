def draw_steps(steps: int):

    if steps > 0:
        for step in range(steps + 1):
            spaces = "  " * (steps - step)
            step_draw = "_" if step == 0 else "_|"
            print(f"{spaces}{step_draw}")
    elif steps < 0:
        for step in range(abs(steps) + 1):
            spaces = " " * ((step * 2) - 1)
            step_draw = "_" if step == 0 else "|_"
            print(f"{spaces}{step_draw}")
    else:
        print("__")


# draw_steps(0)
# draw_steps(10)
# print("----------------")
# draw_steps(-10)

def getNthFib(n):
   if n <= 2:
       print(n)
       return n - 1
   else:
      return getNthFib(n - 1) + getNthFib(n - 2)

##print("Fibonnacci:",getNthFib(2))



##-------------
# def staircaseTraversal(height, maxSteps):
#     if height == 0:
#         return 1

#     result = 0
#     for i in range(1, maxSteps + 1):
#         if i <= height:
#             result += staircaseTraversal(height - i, maxSteps)
#     return result

# print(staircaseTraversal(10, 2))