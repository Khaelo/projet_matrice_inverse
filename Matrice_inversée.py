a = ([[3,-2,4],[2,-4,5],[1,8,2]])
b = ([1,7],[3,4])
def determinant2(matrice):
    m = (matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0]) 
    return m

def determinant3(matrice):
    j = (matrice[0][0] * ((matrice[1][1]*matrice[2][2])-(matrice[2][1]*matrice[1][2]))) - (matrice[0][1]* ((matrice[1][0]*matrice[2][2])-(matrice[2][0]*matrice[1][2]))) + (matrice[0][2]* ((matrice[1][0]*matrice[2][1])-(matrice[2][0]*matrice[1][1])))
    return j

def transposer3(matrice):
    y = ([matrice[0][0],matrice[1][0],matrice[2][0]],[matrice[0][1],matrice[1][1],matrice[2][1]],[matrice[0][2],matrice[1][2],matrice[2][2]])
    return y 


def transposer2(matrice):
    v = ([matrice[0][0],matrice[1][0]],[matrice[0][1],matrice[1][1]])
    return v

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
    comatricee = [[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]
    return comatricee

def inverse(transpo, deter):
    x = []
    for i in range(3):
        for j in range(3):
            a1 = transpo[i][j] / deter
            x.append(a1)
    return x
comatrice = comatrice(a)
transposer3(comatrice)
print(inverse(comatrice,determinant3(a)))




