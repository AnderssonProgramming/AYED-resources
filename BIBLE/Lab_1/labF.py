def invertir(s, index=0):
    if index == len(s)//2:
        return s
    else:
        elemento, s[-index-1] = s[-index-1], s[index]
        s[index], index = elemento, index+1
        return invertir(s, index)

def main():
    s = [i for i in range(10)]
    print("Lista original:",s)
    print("Lista invertida:", invertir(s))


main()
