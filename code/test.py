import public_value

a = int(public_value.CONSTANT.PALYER_NUM ** 0.5) * 4
port_xy = [None] * 9
port_xy_all= [None] * public_value.CONSTANT.PALYER_NUM

for key in range(public_value.CONSTANT.PALYER_NUM):
    for num in range(9):
        port_xy[num] = [(1 / a * (num % 3+1)+key%(a/4)/(a/4),(1 / a * (num // 3+1))+key//(a/4)/(a/4))]
    print(port_xy)
    port_xy_all[key]=port_xy