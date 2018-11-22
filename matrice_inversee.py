a = [[3,-2,4],[2,-4,5],[1,8,2]]

def determinant2(matrice):
    determinant_matrice = (matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0]) 
    return determinant_matrice

def determinant3(matrice):
    determinant_matrice = (matrice[0][0] * ((matrice[1][1]*matrice[2][2])-(matrice[2][1]*matrice[1][2]))) - (matrice[0][1]* ((matrice[1][0]*matrice[2][2])-(matrice[2][0]*matrice[1][2]))) + (matrice[0][2]* ((matrice[1][0]*matrice[2][1])-(matrice[2][0]*matrice[1][1])))
    return determinant_matrice

def transposer3(matrice):
    resultat = [[0,0,0],[0,0,0],[0,0,0]]
    for ligne in range(3):
            for colonne in range(3):
                    resultat[ligne][colonne] = matrice[colonne][ligne]
    return resultat


def transposer2(matrice):
    transposer_matrice = ([matrice[0][0],matrice[1][0]],[matrice[0][1],matrice[1][1]])
    return transposer_matrice

def comatrice(matrice):
    a1 = (matrice[1][1] * matrice[2][2]) - (matrice[1][2] * matrice[2][1])
    a2 = ((matrice[1][0] * matrice[2][2]) - (matrice[1][2] * matrice[2][0])) * (-1)
    a3 = ((matrice[1][0] * matrice[2][1]) - (matrice[1][1] * matrice[2][0]))
    b1 = ((matrice[0][1] * matrice[2][2]) - (matrice[0][2] * matrice[2][1])) * (-1)
    b2 = ((matrice[0][0] * matrice[2][2]) - (matrice[0][2] * matrice[2][0]))
    b3 = ((matrice[0][0] * matrice[2][1]) - (matrice[0][1] * matrice[2][0])) * (-1)
    c1 = ((matrice[0][1] * matrice[1][2]) - (matrice[0][2] * matrice[1][1]))
    c2 = ((matrice[0][0] * matrice[1][2]) - (matrice[0][2] * matrice[1][0])) * (-1)
    c3 = ((matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0]))
    comatrice_matrice = [[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]
    return comatrice_matrice

def inverse(transpo, deter):
    inverse_matrice = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            a1 = transpo[i][j] / deter
            inverse_matrice[i][j] = a1
    return inverse_matrice
    
comatrice = comatrice(a)
print(inverse(transposer3(comatrice),determinant3(a)))




