import numpy as np


#Test norme_vecteur

X=np.matrix([[1],[2],[6]])
print("Test norme_vecteur: ",norme_vecteur(X)==41)


#Test produit_scalaire_vecteurs(X,Y)

X=np.matrix([[1],[2],[6]])
Y=np.matrix([[2],[3],[7]])
print("Test produit_scalaire_vecteurs: ",produit_scalaire_vecteurs(X,Y)==50)

X=np.matrix([[1],[2],[6]])
Y=np.matrix([[2],[3],[7]])
A=np.matrix([[1,0,0],[0,2,0],[0,0,5]])
print("Test produit_scalaire_vecteurs: ",produit_scalaire_vecteurs(X,Y,A))
print("Test produit_scalaire_vecteurs: ",produit_scalaire_vecteurs(X,Y,A)==224)


#Test gradient

X=np.matrix([[1],[2],[6]])
A=np.matrix([[1,0,0],[0,2,0],[0,0,5]])
Y=A*X
R=np.matrix([[0.1],[0.3],[1.5]])
x0 = X-R
#print(x0)
eps0 = 0.0000000001
eps1 = 0.001
kmax = 10000
(x, k,diff_normes_x) = gradient(A,Y, x0,eps0, eps1, kmax)
print("La solution est: ", x)
print(k, "itérations ont été effectuées")
print("Le vecteur résidu est ", x-X)
print("La norme du vecteur résidu est de ", norme_vecteur(x-X))
print("La différence entre les deux dernières solutions est: ", diff_normes_x)

#print("Test gradient: ",(norme_vecteur(gradient(A,Y, x0,eps0, eps1, kmax)[0]-X))<=eps1) or (gradient(A,Y, x0,eps0, eps1, kmax)[1]>=kmax or gradient(A,Y, x0,eps0, eps1, kmax)[2]<=eps0 )