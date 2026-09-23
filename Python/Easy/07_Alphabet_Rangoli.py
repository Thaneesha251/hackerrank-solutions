def print_rangoli(size):
     for i in range(2*size-1):
        row=i if i<size else 2*size-2-i
        letters=[]
        
        for j in range(row+1):
            letters.append(chr(97+size-1-j))
        
        letters=letters+letters[-2::-1]
        pattern="-".join(letters)
        print(pattern.center(4*size-3,"-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)