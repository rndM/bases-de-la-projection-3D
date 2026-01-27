# 🎲 Cube 3D Rotatif - Apprendre la 3D simplement

Un projet pédagogique pour comprendre les **bases de la 3D** : rotation, projection et animation.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)

## 📖 À propos

Ce programme affiche un cube en 3D qui tourne en continu. Il est conçu pour être **simple et éducatif**, montrant les concepts fondamentaux de la programmation 3D sans bibliothèque complexe.

### Ce que vous allez apprendre

- 🔄 **Rotation 3D** : Comment faire tourner des points dans l'espace
- 📐 **Projection perspective** : Transformer des coordonnées 3D en 2D pour l'affichage
- 🎬 **Animation** : Créer une animation fluide en rafraîchissant l'écran

## 🚀 Lancement rapide

### Prérequis

- Python 3.x
- Tkinter (inclus par défaut avec Python)

### Exécution

```bash
python test3D.py
```

Une fenêtre s'ouvre avec un cube vert qui tourne sur fond noir.

## 🧠 Concepts expliqués

### 1. Représentation du cube

Le cube est défini par :
- **8 coins** (sommets) en coordonnées 3D `(x, y, z)`
- **12 arêtes** (lignes) reliant ces coins

```python
# Exemple : coin avant-gauche-bas
(-1, -1, -1)
#  x   y   z
```

### 2. Rotation 3D

La rotation autour de l'axe Y utilise une **matrice de rotation** :

```
x' = x × cos(θ) - z × sin(θ)
z' = x × sin(θ) + z × cos(θ)
y' = y  (pas de changement)
```

Cela fait "tourner" le cube comme une toupie.

### 3. Projection perspective

Pour afficher la 3D sur un écran 2D, on utilise la **division par la profondeur** :

```
x_écran = x / z
y_écran = y / z
```

Plus un objet est loin (z grand), plus il apparaît petit. C'est comme regarder par une fenêtre !

### 4. Animation

Le cube est redessiné toutes les **16 millisecondes** (~60 images/seconde) :
1. Effacer l'écran
2. Calculer les nouvelles positions (rotation)
3. Dessiner les arêtes
4. Incrémenter l'angle
5. Répéter

## 📁 Structure du code

```
test3D.py
├── Configuration (couleurs, taille)
├── Classe Cube3D
│   ├── __init__()      → Initialise la fenêtre et les données
│   ├── tourner()       → Applique la rotation 3D
│   ├── projeter()      → Convertit 3D → 2D
│   ├── animer()        → Boucle d'animation
│   └── demarrer()      → Lance l'application
└── Programme principal
```

## 🎨 Personnalisation

Vous pouvez modifier facilement :

```python
# Taille de la fenêtre
LARGEUR = 800
HAUTEUR = 800

# Couleurs
COULEUR_FOND = "#101010"    # Fond noir
COULEUR_LIGNE = "#50FF50"   # Lignes vertes

# Vitesse de rotation (dans animer())
self.angle += 0.05  # Plus grand = plus rapide
```

## 🔧 Exercices pour aller plus loin

1. **Ajouter une rotation sur l'axe X** : Faire tourner le cube sur deux axes
2. **Changer les couleurs** : Colorer différemment chaque face
3. **Ajouter des contrôles** : Utiliser le clavier pour contrôler la rotation
4. **Dessiner d'autres formes** : Pyramide, tétraèdre, etc.
5. **Ajouter de la profondeur** : Assombrir les arêtes lointaines

## 📚 Ressources pour approfondir

- [Mathématiques de la 3D](https://fr.wikipedia.org/wiki/Rotation_dans_l%27espace) - Matrices de rotation
- [Projection perspective](https://fr.wikipedia.org/wiki/Perspective_(repr%C3%A9sentation)) - Théorie
- [Tkinter Canvas](https://docs.python.org/fr/3/library/tkinter.html#tkinter.Canvas) - Documentation

## 💡 Pourquoi ce projet ?

La 3D peut sembler intimidante, mais elle repose sur des principes mathématiques simples :
- **Géométrie** : Des points et des lignes
- **Trigonométrie** : Sinus et cosinus pour les rotations
- **Perspective** : Division pour simuler la profondeur

Ce code montre qu'avec moins de 100 lignes, on peut créer quelque chose de visuellement impressionnant !

## 📝 Licence

Code libre d'utilisation pour l'apprentissage et l'enseignement.

## 🤖 Contributions

Ce README et les commentaires détaillés du code ont été rédigés avec l'aide d'une IA LLM (Large Language Model) pour rendre le projet plus accessible et pédagogique.

---

**Bon apprentissage de la 3D ! 🎓**
