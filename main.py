import matplotlib
matplotlib.use('TkAgg')
from scipy.linalg import lstsq
import numpy as np
import matplotlib.pyplot as plt

# ============================================
#           DONNEES REELLES
# ============================================

# Paramètres réels
a_reel = 2.0
b_reel = 1.0

# point
N = 300
x = np.linspace(0, 10, N)

# Bruit
bruit = np.random.normal(0, 0.6, N)

# Données mesurées
y = a_reel * x + b_reel + bruit

# ============================================
#        MOINDRES CARRES
# ============================================

# Matrice A
A = np.column_stack((np.ones(N), x))

# Estimation equivalant de theta = np.linalg.inv(A.T @ A) @ A.T @ y
theta, residuals, rank, s = lstsq(A, y)
b_est = theta[0]
a_est = theta[1]

print("===== PARAMETRES =====")
print("a estimé =", a_est)
print("b estimé =", b_est)

# ============================================
#           MODELES
# ============================================

# Modèle réel (sans bruit)
y_reel = a_reel * x + b_reel

# Modèle estimé
y_est = a_est * x + b_est
#Erreur
Erreur = y-y_est
#Erreur quadratique
A = np.sum((Erreur)**2)
print("Somme erreur quadratique =",A)
# ============================================
#            GRAPHIQUE
# ============================================

plt.figure(figsize=(9,6))

# Valeurs mesurées(green)
plt.scatter(x, y, s=5, alpha=0.5, label="Valeurs mesurées", color='green')
# Modèle estimé (bleu)
plt.plot(x, y_est, color='blue', linewidth=3, label="Modèle estimé")
#  Erreur visuelle (zone entre les deux)
plt.fill_between(x,y,y_est, alpha=0.2, label="Erreur")
plt.title("Identification par moindres carrés (avec bruit)")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("resultat.png")
plt.show()
