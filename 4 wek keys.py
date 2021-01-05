
  
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

SHIFT_TABLE = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

key = input(str("Anahtar giriniz: "))
keytoBin = ''.join(format(ord(i), 'b').zfill(8) for i in key)


def permute(bin_ptext ,i_p, n):
    permutation = ""
    for index in range(0, n):
        permutation = permutation + bin_ptext[i_p[index] - 1]
    return permutation
    

# for shift left
def shift_left(k, nthShift):
    s = ""
    for i in range(nthShift):
        for j in range(1,len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k

keyPermuted = permute(keytoBin, PC_1, 56)
#splitting keys
left  = keyPermuted[0:28]
right = keyPermuted[28:56]


roundkey = []

for i in range(0,16):
    left = shift_left(left, SHIFT_TABLE[i])
    right = shift_left(right, SHIFT_TABLE[i])
    #

    combineKey = left + right

    round_key = permute(combineKey, PC_2, 48)

    roundkey.append(round_key)

    print("Round ", i + 1, "-->","C",i+1,": ", left, "D",i+1,": ",right, "K",i+1,": " ,round_key)
    