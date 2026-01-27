#!/usr/bin/env python3
"""
Cube 3D tournant - Version pédagogique
=======================================

Ce programme illustre les concepts fondamentaux de la 3D :
1. Représentation d'objets 3D (sommets et arêtes)
2. Transformations géométriques (rotation)
3. Projection perspective (3D → 2D)
4. Animation en temps réel

Parfait pour comprendre comment fonctionnent les moteurs 3D !
"""

import tkinter as tk
import math

# ============================================================================
# CONFIGURATION
# ============================================================================

LARGEUR = 800           # Largeur de la fenêtre en pixels
HAUTEUR = 800           # Hauteur de la fenêtre en pixels
COULEUR_FOND = "#101010"    # Fond noir (presque)
COULEUR_LIGNE = "#50FF50"   # Lignes vertes néon


class Cube3D:
    """
    Classe principale qui gère l'affichage et l'animation d'un cube 3D.
    
    Le cube est représenté par :
    - 8 sommets (coins) en coordonnées 3D
    - 12 arêtes (lignes) qui relient ces sommets
    """

    def __init__(self):
        """Initialise la fenêtre graphique et les données du cube."""
        
        # ====================================================================
        # CRÉATION DE LA FENÊTRE
        # ====================================================================
        self.fenetre = tk.Tk()
        self.fenetre.title("Cube 3D - Démo pédagogique")
        
        # Canvas = zone de dessin
        self.ecran = tk.Canvas(
            self.fenetre,
            width=LARGEUR,
            height=HAUTEUR,
            bg=COULEUR_FOND
        )
        self.ecran.pack()

        # ====================================================================
        # DÉFINITION DU CUBE : 8 SOMMETS
        # ====================================================================
        # Chaque sommet est un point (x, y, z) dans l'espace 3D
        # Le cube a une taille de 2×2×2, centré sur l'origine (0, 0, 0)
        
        self.coins = [
            # Face AVANT (z = -1)
            (-1, -1, -1),  # 0: Coin bas-gauche-avant
            ( 1, -1, -1),  # 1: Coin bas-droite-avant
            ( 1,  1, -1),  # 2: Coin haut-droite-avant
            (-1,  1, -1),  # 3: Coin haut-gauche-avant
            
            # Face ARRIÈRE (z = 1)
            (-1, -1,  1),  # 4: Coin bas-gauche-arrière
            ( 1, -1,  1),  # 5: Coin bas-droite-arrière
            ( 1,  1,  1),  # 6: Coin haut-droite-arrière
            (-1,  1,  1),  # 7: Coin haut-gauche-arrière
        ]

        # ====================================================================
        # DÉFINITION DU CUBE : 12 ARÊTES
        # ====================================================================
        # Chaque arête relie deux sommets (indices dans la liste self.coins)
        
        self.aretes = [
            # Les 4 arêtes de la face AVANT
            (0, 1), (1, 2), (2, 3), (3, 0),
            
            # Les 4 arêtes de la face ARRIÈRE
            (4, 5), (5, 6), (6, 7), (7, 4),
            
            # Les 4 arêtes qui relient l'avant à l'arrière
            (0, 4), (1, 5), (2, 6), (3, 7),
        ]

        # ====================================================================
        # ANIMATION
        # ====================================================================
        self.angle = 0  # Angle de rotation actuel (en radians)
        self.animer()   # Lance la boucle d'animation

    def tourner(self, point, angle):
        """
        Applique une rotation 3D autour de l'axe Y.
        
        La rotation autour de Y utilise la matrice :
        | cos(θ)   0   -sin(θ) |
        |   0      1      0    |
        | sin(θ)   0    cos(θ) |
        
        Args:
            point: Tuple (x, y, z) représentant un point 3D
            angle: Angle de rotation en radians
            
        Returns:
            Tuple (nouveau_x, y, nouveau_z) après rotation
        """
        x, y, z = point
        
        # Précalcul des fonctions trigonométriques (optimisation)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        # Application de la matrice de rotation
        # x' = x×cos(θ) - z×sin(θ)
        nouveau_x = x * cos_a - z * sin_a
        
        # y reste inchangé (rotation autour de Y)
        # y' = y
        
        # z' = x×sin(θ) + z×cos(θ)
        nouveau_z = x * sin_a + z * cos_a
        
        return (nouveau_x, y, nouveau_z)

    def projeter(self, point):
        """
        Convertit un point 3D en coordonnées 2D pour l'affichage.
        
        Utilise la projection perspective : les objets lointains
        apparaissent plus petits (division par z).
        
        Args:
            point: Tuple (x, y, z) représentant un point 3D
            
        Returns:
            Tuple (x_pixel, y_pixel) en coordonnées écran
        """
        x, y, z = point
        
        # ----------------------------------------------------------------
        # ÉTAPE 1 : Éloigner le cube de la caméra
        # ----------------------------------------------------------------
        # La caméra est à z=0, on éloigne le cube pour ne pas être "dedans"
        z = z + 3
        
        # ----------------------------------------------------------------
        # ÉTAPE 2 : Projection perspective
        # ----------------------------------------------------------------
        # Plus z est grand (objet loin), plus x/z et y/z sont petits
        # → L'objet apparaît plus petit (comme dans la réalité !)
        x_2d = x / z
        y_2d = y / z
        
        # ----------------------------------------------------------------
        # ÉTAPE 3 : Conversion en coordonnées écran (pixels)
        # ----------------------------------------------------------------
        # Le centre de l'écran est (LARGEUR/2, HAUTEUR/2)
        # On multiplie par 200 pour agrandir le cube
        x_pixel = LARGEUR / 2 + x_2d * 200
        
        # On inverse y car en Tkinter, y=0 est en HAUT de l'écran
        y_pixel = HAUTEUR / 2 - y_2d * 200
        
        return (x_pixel, y_pixel)

    def animer(self):
        """
        Boucle d'animation principale - appelée toutes les 16ms (~60 FPS).
        
        Processus :
        1. Effacer l'écran
        2. Pour chaque arête du cube :
           a. Récupérer les deux sommets
           b. Appliquer la rotation
           c. Projeter en 2D
           d. Dessiner la ligne
        3. Augmenter l'angle de rotation
        4. Se rappeler dans 16ms
        """
        
        # ----------------------------------------------------------------
        # ÉTAPE 1 : Effacer tout l'écran
        # ----------------------------------------------------------------
        self.ecran.delete("all")

        # ----------------------------------------------------------------
        # ÉTAPE 2 : Dessiner toutes les arêtes du cube
        # ----------------------------------------------------------------
        for debut, fin in self.aretes:
            # Récupère les coordonnées 3D des deux sommets de l'arête
            coin1 = self.coins[debut]
            coin2 = self.coins[fin]

            # a) Applique la rotation à chaque sommet
            coin1_tourne = self.tourner(coin1, self.angle)
            coin2_tourne = self.tourner(coin2, self.angle)

            # b) Projette les points 3D en 2D (coordonnées écran)
            p1 = self.projeter(coin1_tourne)
            p2 = self.projeter(coin2_tourne)

            # c) Dessine la ligne sur le canvas
            self.ecran.create_line(
                p1[0], p1[1],  # Point de départ (x1, y1)
                p2[0], p2[1],  # Point d'arrivée (x2, y2)
                fill=COULEUR_LIGNE,
                width=2
            )

        # ----------------------------------------------------------------
        # ÉTAPE 3 : Incrémenter l'angle pour la prochaine frame
        # ----------------------------------------------------------------
        # 0.05 radians ≈ 2.86° par frame
        # Sur 60 FPS : environ 171°/seconde (un demi-tour en ~1 seconde)
        self.angle += 0.05

        # ----------------------------------------------------------------
        # ÉTAPE 4 : Programmer le prochain rafraîchissement
        # ----------------------------------------------------------------
        # 16ms ≈ 1000ms/60 = 60 FPS
        self.fenetre.after(16, self.animer)

    def demarrer(self):
        """Lance la boucle principale de Tkinter (affichage de la fenêtre)."""
        self.fenetre.mainloop()


# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Crée une instance du cube
    cube = Cube3D()
    
    # Lance l'application (bloquant jusqu'à fermeture de la fenêtre)
    cube.demarrer()
