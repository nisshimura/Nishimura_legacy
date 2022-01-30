import time

def syracuse(target, tesu):
    while target != 1:
        if target % 2 == 1:
            target = target * 3 + +1
            tesu += 1
        else:
            target /= 2
    return tesu


def quick_sort(arr):
    left_arr = []
    right_arr = []
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    pivot_count = 0

    for ele in arr:
        if ele[2] < pivot[2]:
            left_arr.append(ele)
        elif ele[2] > pivot[2]:
            right_arr.append(ele)

        else:
            pivot_count += 1


    left_arr = quick_sort(left_arr)
    right_arr = quick_sort(right_arr)


    return left_arr + [pivot] * pivot_count + right_arr
def main():
    n = 56000
    ar = []
    for i in range (n):
        num = 2 * (i + 1) - 1
        tesu = syracuse(num, 1)
        tesu_per_num = tesu / num
        ar.append([num,tesu,tesu_per_num])
    
    start = time.perf_counter()
    ar = quick_sort(ar)
    print("time is "+ str(time.perf_counter()-start))
    print(ar[0])


if __name__ == '__main__':
    main()

