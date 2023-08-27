input_val = input()
num_couples = input_val.split()
probab_res = 0
for index, val in enumerate(num_couples):
    if index < 3: 
        probab_res += (int(val) * 1)
    elif index == 3:
        probab_res += (int(val) * .75)
    elif index == 4:
        probab_res += (int(val) * .5)
print(probab_res*2)
