def filter(arr, bajanord): #veradarcnel bolor zuyq elementnere voronq bajanvumen bajanordi vrya - Anahit
    return [10, 20]

def sort(arr): #veradarcnel sortavorac list - Murad
    arr = a
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr



def isValid(arr, expectedStr): #stugel ardzyok trvac tveri liste hamapatasxanume aknkalvox patasxanin - Artur
    return False

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


