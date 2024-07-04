word = "bottles"
for beerNum in range(99, 0, -1):
    print(beerNum, word, "of beer on the wall.")
    print(beerNum, word, "of beer.")
    print("take one down.")
    print("pass it around.")
    if beerNum == 1:
        print("no more bottles of beer on the wall.")
    else:
        newNum = beerNum -1
        if newNum == 1:
            word = "bottle"
            print(newNum, word, "of beer on the wall.")
        print()