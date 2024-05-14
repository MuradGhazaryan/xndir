def filter(arr: list[int], divisor: int) -> list[int]:
    """veradarcnel bolor zuyq elementnere voronq bajanvumen bajanordi vrya - Anahit

    Args:
        arr (list[int]): tvain list vore petqe filtrvi
        divisor (int): bajanord vore ogtagorcveluya filterlu hamar

    Returns:
        list[int]: filtrac list
    """
    res = []
    
    for num in arr:
        num_int = int(num)  
        if num_int % 2 == 0 and num_int % divisor == 0:  
            res.append(num_int)

    return res

def testFilter():
    print('test filter')

def sort(arr): #veradarcnel sortavorac list - Murad
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def testSort():
    print('Testing sort with arr = [2, 3, 10, 7, 6, 15, 20] ...')
    arr1 = [2, 3, 10, 7, 6, 15, 20]
    expected1 = [2, 3, 6, 7, 10, 15, 20]
    sorted_arr1 = sort(arr1)
    if sorted_arr1 == expected1:
        print('Test 1 passed!')
    else:
        print('Test 1 failed!')

    print('Testing sort with arr = [] ...')
    arr2 = []
    expected2 = []
    sorted_arr2 = sort(arr2)
    if sorted_arr2 == expected2:
        print('Test 2 passed!')
    else:
        print('Test 2 failed!')

    print('Testing sort with arr = [8] ...')
    arr3 = [8]
    expected3 = [8]
    sorted_arr3 = sort(arr3)
    if sorted_arr3 == expected3:
        print('Test 3 passed!')
    else:
        print('Test 3 failed!')


def isValid(arr, expectedStr): #stugel ardzyok trvac tveri liste hamapatasxanume aknkalvox patasxanin - Artur
    expectedArr = expectedStr.split(',')
    for i in range(len(arr)):
        if int(arr[i]) != int(expectedArr[i]):
            return False
    
    return True

def testIsValid():
    print('Testing IsValid with arr = [1,2,3], expectedStr = 1,2,3...')
    if isValid([1,2,3], '1,2,3'):
        print('Test passed!')
    else:
        print('Test failed!')
    print('Testing IsValid with arr = [2,4,6], expectedStr = 1,2,3...')
    if isValid([2,4,6], '1,2,3'):
        print('Test failed!')
    else:
        print('Test passed!')
    print('Testing IsValid with arr = [2,3,4], expectedStr = 2,3,4...')
    if isValid([2,3,4], '2,3,4'):
        print('Test passed!')
    else:
        print('Test failed!')


a = [2, 3, 10, 7, 6, 15, 20]
arr = a
rezult = sort(arr)
print(rezult)  

filterRes = filter(a, 5)
if isValid(filterRes, '10,20') == False:
    print('Filtravorume sxale')

sortRes = sort(filterRes)
if isValid(sortRes, '10,20') == False:
    print('Sortavorume sxale')


