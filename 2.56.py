#!/usr/bin/env python
# Napisz program, który przyjmie od użytkownika pewną ilość liczb (uzytkownik decyduje ile), a następnie dokona ich sortowania. Zadanie wykonać nie korzystając z metody sort (należy samodzielnie zaprojektować algorytm sortowania).

user_arr = list(map(int, input('Podaj swoje liczby: ').split()))

def brute_force(arr):
    for i in range(1, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

print(f'Twoje liczby ale posortowane: {brute_force(user_arr)}')

assert brute_force([1,2,3,4,5]) == [1,2,3,4,5], f"{brute_force([1,2,3,4,5])}"
assert brute_force([2,2,3,41,5]) == [2,2,3,5,41], f"{brute_force([2,2,3,41,5])}"
assert brute_force([1,32,3,1,5]) == [1,1,3,5,32], f"{brute_force([1,32,3,1,5])}"
assert brute_force([1,2,12,4,5]) == [1,2,4,5,12], f"{brute_force([1,2,12,4,5])}"
