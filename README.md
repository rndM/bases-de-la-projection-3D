# 🎲 3D Rotating Cube - Learn 3D Simply

---

## 📚 Navigation

**[🇬🇧 English Version](README.md)** | **[🇫🇷 Version Française](README_FR.md)**

---

A pedagogical project to understand the **basics of 3D**: rotation, projection and animation.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)

## 📖 About

This program displays a 3D cube that rotates continuously. It is designed to be **simple and educational**, showing fundamental concepts of 3D programming without complex libraries.

### What you will learn

- 🔄 **3D Rotation**: How to rotate points in space
- 📐 **Perspective projection**: Transforming 3D coordinates into 2D for display
- 🎬 **Animation**: Creating smooth animation by refreshing the screen

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- Tkinter (included by default with Python)

### Running

```bash
python test3D.py
```

A window opens with a green cube rotating on a black background.

## 🧠 Concepts Explained

### 1. Cube Representation

The cube is defined by:
- **8 corners** (vertices) in 3D coordinates `(x, y, z)`
- **12 edges** (lines) connecting these corners

```python
# Example: front-bottom-left corner
(-1, -1, -1)
#  x   y   z
```

### 2. 3D Rotation

Rotation around the Y axis uses a **rotation matrix**:

```
x' = x × cos(θ) - z × sin(θ)
z' = x × sin(θ) + z × cos(θ)
y' = y  (no change)
```

This makes the cube spin like a top.

### 3. Perspective Projection

To display 3D on a 2D screen, we use **division by depth**:

```
x_screen = x / z
y_screen = y / z
```

The farther an object is (large z), the smaller it appears. It's like looking through a window!

### 4. Animation

The cube is redrawn every **16 milliseconds** (~60 frames/second):
1. Clear the screen
2. Calculate new positions (rotation)
3. Draw edges
4. Increment angle
5. Repeat

## 📁 Code Structure

```
test3D.py
├── Configuration (colors, size)
├── Cube3D Class
│   ├── __init__()      → Initialize window and data
│   ├── tourner()       → Apply 3D rotation
│   ├── projeter()      → Convert 3D → 2D
│   ├── animer()        → Animation loop
│   └── demarrer()      → Launch application
└── Main program
```

## 🎨 Customization

You can easily modify:

```python
# Window size
LARGEUR = 800
HAUTEUR = 800

# Colors
COULEUR_FOND = "#101010"    # Black background
COULEUR_LIGNE = "#50FF50"   # Green lines

# Rotation speed (in animer())
self.angle += 0.05  # Larger = faster
```

## 🔧 Further Exercises

1. **Add X-axis rotation**: Make the cube rotate on two axes
2. **Change colors**: Color each face differently
3. **Add controls**: Use the keyboard to control rotation
4. **Draw other shapes**: Pyramid, tetrahedron, etc.
5. **Add depth**: Darken distant edges

## 📚 Resources to Go Further

- [3D Mathematics](https://en.wikipedia.org/wiki/Rotation_matrix) - Rotation matrices
- [Perspective projection](https://en.wikipedia.org/wiki/Perspective_(graphical)) - Theory
- [Tkinter Canvas](https://docs.python.org/3/library/tkinter.html#tkinter.Canvas) - Documentation

## 💡 Why This Project?

3D may seem intimidating, but it relies on simple mathematical principles:
- **Geometry**: Points and lines
- **Trigonometry**: Sine and cosine for rotations
- **Perspective**: Division to simulate depth

This code shows that with a hundred lines, you can create something visually impressive!

## 📝 License

Code free to use for learning and teaching.

## 🤖 Contributions

This README and the detailed code comments were written with the help of an AI LLM (Large Language Model) to make the project more accessible and educational.

---

**Happy learning 3D! 🎓**
