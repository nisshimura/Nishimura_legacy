import copy
def get_sisoku(target):
    result_list = []
    for x in sisoku_list:
        for y in sisoku_list:
            for z in sisoku_list:
                result = target[0]
                if x==0:
                    result += target[1]
                elif x==1:
                    result -= target[1]
                elif x==2:
                    result *= target[1]
                elif x==3:
                    result /= target[1]

                if y==0:
                    result += target[2]
                elif y==1:
                    result -=target[2]
                elif y==2:
                    result *=target[2]
                elif y==3:
                    result /=target[2]

                if z==0:
                    result += target[3]
                elif z==1:
                    result -= target[3]
                elif z==2:
                    result *= target[3]
                elif z==3:
                    result /= target[3]

                if result==10:
                    result_list.append([x,y,z])

    for index in result_list:
        if index[0]==0:
            sisoku1 = '+'
        elif index[0]==1:
            sisoku1 = '-'
        elif index[0]==2:
            sisoku1 = '*'
        elif index[0]==3:
            sisoku1 = '/'

        if index[1]==0:
            sisoku2 = '+'
        elif index[1]==1:
            sisoku2 = '-'
        elif index[1]==2:
            sisoku2 = '*'
        elif index[1]==3:
            sisoku2 = '/'

        if index[2]==0:
            sisoku3 = '+'
        elif index[2]==1:
            sisoku3 = '-'
        elif index[2]==2:
            sisoku3 = '*'
        elif index[2]==3:
            sisoku3 = '/'

        if sisoku2=='*' or sisoku2=='/':
            if sisoku1=='+' or sisoku1=='-':
                print(f'({target[0]}{sisoku1}{target[1]}){sisoku2}{target[2]}{sisoku3}{target[3]}=10')
            elif sisoku3=='+' or sisoku3=='-':
                print(f'{target[0]}{sisoku1}{target[1]}{sisoku2}({target[2]}{sisoku3}{target[3]})=10')
            else:
                print(f'{target[0]}{sisoku1}{target[1]}{sisoku2}{target[2]}{sisoku3}{target[3]}=10')
        elif sisoku3=='*' or sisoku3=='/':
            if (sisoku1=='+' or sisoku1=='-') and (sisoku3=='+' or sisoku3=='-'):
                print(f'({target[0]}{sisoku1}{target[1]}{sisoku2}{target[2]}){sisoku3}{target[3]}=10')
            if sisoku1=='+' or sisoku1=='-':
                print(f'({target[0]}{sisoku1}{target[1]}){sisoku2}{target[2]}{sisoku3}{target[3]}=10')
            elif sisoku3=='+' or sisoku3=='-':
                print(f'{target[0]}{sisoku1}({target[1]}{sisoku2}{target[2]}){sisoku3}{target[3]}=10')
            else:
                print(f'{target[0]}{sisoku1}{target[1]}{sisoku2}{target[2]}{sisoku3}{target[3]}=10')

        else:
            print(f'{target[0]}{sisoku1}{target[1]}{sisoku2}{target[2]}{sisoku3}{target[3]}=10')

target_list = [1,2,4,5]
sisoku_list = [0,1,2,3]

for i in target_list:
    for j in target_list:
        for k in target_list:
            for l in target_list:
                if len(set([i,j,k,l]))==len([i,j,k,l]): 
                    get_sisoku([i,j,k,l])

#get_sisoku(target_list)
















