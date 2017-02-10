import numpy as np

def optimize(A,b, x0=None,eps0=None, eps1=None, kmax=None):
    return(np.linalg.inv(A)*b)


def build_A(LX):
    #LX rassemble l'ensemble des coordonnées des points mesurés sur le sol sous la forme: LX = [[X1,Y1],[X2,Y2]...]

    # Seuls les deux premières coordonées des points sur le sol sont prises
    # en compte. L'hypothèse est que le sol est à Z=0 et que la dernière
    # coordonnée est 1 (coordonnées homogènes)
    p=len(LX)
    A=np.array(np.zeros((3*p,12)))
    for i in range(0,p):
        for t in range(0,3):
            for j in range(0,2):
                A[3*i+t,j+4*t]=LX[i][j]
                # A[p*t+i,j+4*t]=LX[i][j]
            A[3*i+t,2+4*t]=0
            A[3*i+t,3+4*t]=1
            # A[p*t+i,2+4*t]=0
            # A[p*t+i,3+4*t]=1
    return(A)

# Code original. Quelle est l'idée qu'il implémente ? La matrice produite
# contient des zéros à la fin, mais je n'arrive pas à saisir pourquoi.
# def build_b(Lx):
#     p=len(Lx)
#     L=[]
#     for j in range(0,2):
#         for i in range(0,p):
#             L.append(Lx[i][j])
#     l=[0 for i in range(0,p)]
#     L=L+l
#     return(np.matrix(L))

def build_b(Lx):
    #Lx rassemble l'ensemble des coordonnées des points sur l'écran sous la forme: Lx = [[x1,y1],[x2,y2]...]
    p=len(Lx)
    L=np.array(np.ones((3*p, 1)))
    # Seuls les deux premières coordonées des points dans le plan projecteur
    # sont prises en compte. L'hypothèse est que la dernière coordonnée
    # est 1 (coordonnées homogènes).
    for j in range(0,2):
        for i in range(0,p):
            L[3*i+j] = Lx[i][j]
    return(np.matrix(L))

def build_H(h):
    p = np.size(h)
    H=np.matrix(np.zeros((3,4)))
    for i in range(0,3):
        for j in range(0,4):
            H[i,j] = h[0, 4*i+j]
    return(H)


def homography(Lx,LX):
    #Lx rassemble l'ensemble des coordonnées des points sur l'écran sous la forme: Lx = [[x1,y1],[x2,y2]...]
    #LX rassemble l'ensemble des coordonnées des points mesurés sur le sol sous la forme: LX = [[X1,Y1],[X2,Y2]...]
    A=build_A(LX)
    b=build_b(Lx)
    print(A)
    print(b)
    h=optimize(A,b)
    H=build_H(h)
    return(H)
