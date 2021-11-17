
s_d = {0: [[0, 0], [16, 16]],  # normal
            1: [[0, 16], [16, 16]],  # jump with board
            2: [[32, 0], [16, 16]],  # jump_onlyman
            3: [[16, 8], [16, 8]],  # board
            4: [[48, 0], [16, 16]],  # mae age
            5: [[0, 112], [16, 16]],  # usiro age
            6: [[16, 24], [16, 8]],  # sleep
            7: [[16, 48], [16, 16]],  # suc_hippie
            8: [[32, 48], [16, 16]],  # suc_ollie
            9: [[48, 48], [16, 16]],  # suc_back
            10: [[80, 0], [16, 16]],  # ready push
            11: [[80, 16], [16, 16]]  # do push
            }

k = 10
print(s_d[k])

for i in range(-1,3):
    print(i)