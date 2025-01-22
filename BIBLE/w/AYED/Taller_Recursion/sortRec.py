# sortRec

def sortRec(A):
    if len(A) <= 1:
        return A
    minValue = min(A)
    A.remove(minValue)
    return [minValue] + sortRec(A)


def main(A):
    return sortRec(A)

main()

print(main([18, 2,12,15,1,6,7]))
print(main([2,6,7,4,5,1,9,8]))
print(main([1,6,7,8,9,2]))
print(main([123,45,67,90,512]))