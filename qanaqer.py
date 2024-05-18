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

def sort(arr): #veradarcnel sortavorac list - Murad
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def isValid(arr: list[int], expectedStr: str) -> bool: #stugel ardzyok trvac tveri liste hamapatasxanume aknkalvox patasxanin - Artur
    expectedArr = expectedStr.split(',')

    if len(arr) == 0 and expectedStr == '':
        return True
    
    if len(arr) != len(expectedArr):
        return False
    
    for i in range(len(arr)):
        if int(arr[i]) != int(expectedArr[i]):
            return False    
    return True