## gerak jatuh bebas

# import pygame dan math
import pygame
# import math

# inisiliasi pygame nya dulu, jika belum install pygame, pergi ke cmd python -m pip install pygame
pygame.init()

# konfigurasi tampilan layar game
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gerak Jatuh Bebas")

# masukkan format warna
white = (255, 255, 255)
black = (0, 0, 0)

# konfigurasi objek gerak jatuh bebas
x, y = 300, 88 # ketinggian awal
v = 0 # kecepatan awal
g = 9.8 # gravitasi
t = 0 # waktu awal
dt = 0.01 # delta waktu

# loop 1
while True:
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # update objek jatuh
    y += v*dt
    v += g*dt
    t += dt

    # bersihkan layar tampilan
    screen.fill(white)

    # gambar objek jatuh
    pygame.draw.circle(screen, black, (int(x), int(y)), 10)

    # tampilkan waktu simulasi 
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Waktu: {:.2f} detik'.format(t), True, black)
    screen.blit(text, (10, 10))

    # update layar
    pygame.display.update()

    # masukkan ketinggian
    if y > height:
        break

# exit pygame
pygame.quit()
