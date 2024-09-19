import numpy as np
import math
from PIL import Image, ImageDraw, ImageFont
import random

# Definice vrcholů kostky
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Definice hran kostky
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Funkce pro rotaci bodů okolo osy X
def rotate_x(angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return np.array([[1, 0, 0],
                     [0, cos_theta, -sin_theta],
                     [0, sin_theta, cos_theta]])

# Funkce pro rotaci bodů okolo osy Y
def rotate_y(angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return np.array([[cos_theta, 0, sin_theta],
                     [0, 1, 0],
                     [-sin_theta, 0, cos_theta]])

# Funkce pro rotaci bodů okolo osy Z
def rotate_z(angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return np.array([[cos_theta, -sin_theta, 0],
                     [sin_theta, cos_theta, 0],
                     [0, 0, 1]])

# Funkce pro projekci 3D bodů do 2D
def project(points, img_size, scale, distance):
    projected_points = []
    for point in points:
        factor = distance / (distance + point[2])
        x = int(point[0] * factor * scale) + img_size[0] // 2
        y = int(point[1] * factor * scale) + img_size[1] // 2
        projected_points.append((x, y))
    return projected_points

# Funkce pro vykreslení kostky do obrázku
def draw_cube(vertices, img_size=(1920, 1080), save_as="cube.jpg", font_size=20):
    # Vytvoření obrázku s černým pozadím
    img = Image.new("RGB", img_size, "black")
    draw = ImageDraw.Draw(img)

    # Projekce bodů do 2D
    projected_points = project(vertices, img_size, scale=300, distance=5)

    # Vykreslení hran kostky (bílou barvou)
    for edge in edges:
        start, end = edge
        x1, y1 = projected_points[start]
        x2, y2 = projected_points[end]
        draw.line((x1, y1, x2, y2), fill="white", width=3)

    # Přidání tmavě zeleného textu přes obrázek
    font = ImageFont.load_default()  # Můžete načíst i vlastní TTF font
    text_color = (0, 128, 0)  # Tmavě zelená barva

    # Generování náhodných čísel
    for i in range(150):  # Zvýšený počet náhodných čísel kvůli většímu prostoru
        number = str(random.randint(1000, 9999))  # Čtyřciferné náhodné číslo
        x_pos = random.randint(0, img_size[0] - 50)
        y_pos = random.randint(0, img_size[1] - 20)

    # Uložení obrázku
    img.save(save_as)
    print(f"Obrázek byl uložen jako {save_as}")

# Hlavní funkce pro vykreslení rotující kostky a přidání textu
def save_rotated_cube_with_text(angle_x, angle_y, angle_z, save_as="cube_with_text.jpg"):
    # Rotace vrcholů
    rotation_matrix = rotate_x(angle_x) @ rotate_y(angle_y) @ rotate_z(angle_z)
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Vykreslení a uložení obrázku s textem
    draw_cube(rotated_vertices, save_as=save_as)

# Příklad uložení obrázku s rotovanou kostkou a textem
angle_x, angle_y, angle_z = 0.5, 0.8, 0.2  # Úhly rotace
save_rotated_cube_with_text(angle_x, angle_y, angle_z, save_as="cube_with_text_1.jpg")
