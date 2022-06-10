def canMakeArithmeticProgression(arr):
    seen = {}
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff not in seen:
                seen[diff] = 1
            else:
                seen[diff] += 1
    for s in seen:
        if seen[s] == len(arr) - 1:
            return True
    return False

if canMakeArithmeticProgression([0,0,0,0]) == True:
    print("Da")
else:
    print("Nu")
