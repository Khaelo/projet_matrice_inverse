w = ([[1,2,3],[4,5,6],[7,8,9]])
y = ([1,7],[3,4])
def determinant2(matrice):
    m = (matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0]) 
    return m
determinant2(w)
def determinant3(matrice):
    j = (matrice[0][0] * ((matrice[1][1]*matrice[2][2])-(matrice[2][1]*matrice[1][2]))) - (matrice[0][1]* ((matrice[1][0]*matrice[2][2])-(matrice[2][0]*matrice[1][2]))) + (matrice[0][2]* ((matrice[1][0]*matrice[2][1])-(matrice[2][0]*matrice[1][1])))
    return j
determinant3(w)
def transposer2(matrice):
    y = ([matrice[0][0],matrice[1][0],matrice[2][0]],[matrice[0][1],matrice[1][1],matrice[2][1]],[matrice[0][2],matrice[1][2],matrice[2][2]])
    return y 
transposer2(w)
def transposer3(matrice):
    v = ([matrice[0][0],matrice[1][0]],[matrice[0][1],matrice[1][1]])
    return v
transposer3(y)




