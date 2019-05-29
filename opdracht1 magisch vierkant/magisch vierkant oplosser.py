import numpy

def same(echelon):
    deleteColums = []
    counter = 0
    for item in range(10):
        listOfLetter = [echelon[0][counter], echelon[1][counter], echelon[2][counter], echelon[3][counter], echelon[4][counter], echelon[5][counter], echelon[6][counter], echelon[7][counter], echelon[8][counter]]
        if all(element == 0 for element in listOfLetter):
            deleteColums.append(counter)
        counter += 1
    return deleteColums

def check(variable1, variable2, variable3, J):
    uitkomst = 0
    formule = []
    index1 = 0
    index2 = 0
    index3 = 0

    if variable2 == "geen waarde":
        if type(variable1) == type(int):
            uitkomst -= 3 * variable1
            index1 = variable1
        else:
            formule.append(variable1)

    else:
        if type(variable1) == int:
            uitkomst -= variable1
            index1 += variable1
            formule.append("-")
        else:
            formule.append(variable1)

        if type(variable2) == int:
            uitkomst -= variable2
            index2 += variable2
            formule.append("-")
        else:
            formule.append(variable2)

        if type(variable3) == int:
            uitkomst -= variable3
            index3 += variable3
            formule.append("-")
        else:
            formule.append(variable3)

    return [formule, J, uitkomst, index1, index2, index3]


def echelonFillIn(formulex):
    totaal = 0
    counter = 0
    set1 = 0
    set2 = 0
    set3 = 0

    if len(formulex[0]) == 1:
        if formulex[0] == '-':
            set1 = 0
            totaal -= 3 * formulex[-1]
        else:
            set1 = 3

    else:
        if formulex[0][0] == '-':
            set1 = 0
            totaal -= formulex[-3]
        else:
            set1 = 1

        if formulex[0][1] == '-':
            set2 = 0
            totaal -= formulex[-2]
        else:
            set2 = 1

        if formulex[0][2] == '-':
            set3 = 0
            totaal -= formulex[-1]
        else:
            set3 = 1

    return [set1, set2, set3, totaal]


matrix = [[5, "B", "C"],
          ["D", "E", 4],
          ["G", "H", 6]]

A = matrix[0][0]
B = matrix[0][1]
C = matrix[0][2]
D = matrix[1][0]
E = matrix[1][1]
F = matrix[1][2]
G = matrix[2][0]
H = matrix[2][1]
I = matrix[2][2]
J = "J"



formule1 = check(A, B, C, J)
formule2 = check(D, E, F, J)
formule3 = check(G, H, I, J)
formule4 = check(A, E, I, J)
formule5 = check(G, E, C, J)
formule6 = check(A, D, G, J)
formule7 = check(B, E, H, J)
formule8 = check(C, F, I, J)
formule9 = check(E, "geen waarde", "geen waarde", J)

#           A  B  C  D  E  F  G  H  I   J  T
echelon = [[1, 1, 1, 0, 0, 0, 0, 0, 0, -1],
           [0, 0, 0, 1, 1, 1, 0, 0, 0, -1],
           [0, 0, 0, 0, 0, 0, 1, 1, 1, -1],
           [1, 0, 0, 0, 1, 0, 0, 0, 1, -1],
           [0, 0, 1, 0, 1, 0, 1, 0, 0, -1],
           [1, 0, 0, 1, 0, 0, 1, 0, 0, -1],
           [0, 1, 0, 0, 1, 0, 0, 1, 0, -1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, -1],
           [0, 0, 0, 0, 3, 0, 0, 0, 0, -1]]

totaal = [0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0]

echelon[0][0] = echelonFillIn(formule1)[0]
echelon[0][1] = echelonFillIn(formule1)[1]
echelon[0][2] = echelonFillIn(formule1)[2]
totaal[0] = echelonFillIn(formule1)[3]

echelon[1][3] = echelonFillIn(formule2)[0]
echelon[1][4] = echelonFillIn(formule2)[1]
echelon[1][5] = echelonFillIn(formule2)[2]
totaal[1] = echelonFillIn(formule2)[3]

echelon[2][6] = echelonFillIn(formule3)[0]
echelon[2][7] = echelonFillIn(formule3)[1]
echelon[2][8] = echelonFillIn(formule3)[2]
totaal[2] = echelonFillIn(formule3)[3]

echelon[3][0] = echelonFillIn(formule4)[0]
echelon[3][4] = echelonFillIn(formule4)[1]
echelon[3][8] = echelonFillIn(formule4)[2]
totaal[3] = echelonFillIn(formule4)[3]

echelon[4][2] = echelonFillIn(formule5)[0]
echelon[4][4] = echelonFillIn(formule5)[1]
echelon[4][6] = echelonFillIn(formule5)[2]
totaal[4] = echelonFillIn(formule5)[3]

echelon[5][0] = echelonFillIn(formule6)[0]
echelon[5][3] = echelonFillIn(formule6)[1]
echelon[5][6] = echelonFillIn(formule6)[2]
totaal[5] = echelonFillIn(formule6)[3]

echelon[6][1] = echelonFillIn(formule7)[0]
echelon[6][4] = echelonFillIn(formule7)[1]
echelon[6][7] = echelonFillIn(formule7)[2]
totaal[6] = echelonFillIn(formule7)[3]

echelon[7][2] = echelonFillIn(formule8)[0]
echelon[7][5] = echelonFillIn(formule8)[1]
echelon[7][8] = echelonFillIn(formule8)[2]
totaal[7] = echelonFillIn(formule8)[3]

echelon[8][4] = echelonFillIn(formule9)[0]
totaal[8] = echelonFillIn(formule9)[3]


deleteFormuleIndex = same(echelon)

if deleteFormuleIndex != []:
    del echelon[0][deleteFormuleIndex[0]], echelon[1][deleteFormuleIndex[0]], echelon[2][deleteFormuleIndex[0]], echelon[3][deleteFormuleIndex[0]], echelon[4][deleteFormuleIndex[0]], echelon[5][
        deleteFormuleIndex[0]], echelon[6][deleteFormuleIndex[0]], echelon[7][deleteFormuleIndex[0]], echelon[8][deleteFormuleIndex[0]]


nump_echelon = numpy.array(echelon)
pseudo_inverse = numpy.linalg.pinv(nump_echelon)

uitkomst = numpy.dot(pseudo_inverse, totaal)


showMagicSquare = [[0,0,0],[0,0,0],[0,0,0]]
row = 0
colum = 0
uitkomstCounter = 0
for rows in showMagicSquare:
    for colums in showMagicSquare[0]:
        checker = row*3 + colum
        if checker != deleteFormuleIndex[0]:
            if uitkomstCounter != 8:
                showMagicSquare[row][colum] = uitkomst[uitkomstCounter]
                colum+=1
                uitkomstCounter += 1
            else:
                showMagicSquare[row][colum] = uitkomst[8]
                colum+=1
                uitkomstCounter += 1
        else:
            if row != 3:
                showMagicSquare[row][colum] = matrix[row][colum]
                colum += 1
    colum = 0
    row += 1

showMagicSquare[0].append(0)
showMagicSquare[1].append(0)
showMagicSquare[2].append(0)
showMagicSquare.append([])

if deleteFormuleIndex != 8:
    showMagicSquare[0][3] = uitkomst[8]
    showMagicSquare[1][3] = uitkomst[8]
    showMagicSquare[2][3] = uitkomst[8]
    showMagicSquare[3] = [uitkomst[8], uitkomst[8], uitkomst[8], uitkomst[8]]
else:
    showMagicSquare[0][3] = J
    showMagicSquare[1][3] = J
    showMagicSquare[2][3] = J
    showMagicSquare[3] = [J, J, J, J]
print(numpy.array(showMagicSquare))