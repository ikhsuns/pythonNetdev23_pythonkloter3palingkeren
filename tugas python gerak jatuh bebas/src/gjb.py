## gerak jatuh bebas

# import pygame
import pygame

## inisiliasi pygame nya dulu
# install pygame, pergi ke cmd 
# pip install pygame
pygame.init()

# konfigurasi tampilan layar game
# membuat display surface object
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gerak Jatuh Bebas")

## konfigurasi objek gerak jatuh bebas
# koordinat, posisi, ketinggian awal
x, y = 300, 88 

# kecepatan awal, waktu awal, delta waktu, gravitasi
v = 0
g = 9.8 
t = 0 
dt = 0.01 

while True:

    # handle event
    # mengambil semua yang terjadi dalam pygame
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # exit game, close pygame
            pygame.quit()
            quit()

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # objek jatuh dan berhenti jika menekan spasi
    if keys[pygame.K_SPACE] == False and y < height-10:
        y += v*dt
        v += g*dt
        t += dt
    
    # update asset
    # membuat layar menjadi putih
    window.fill((255, 255, 255))

    # gambar objek jatuh
    pygame.draw.circle(window, (0, 0, 0), (int(x), int(y)), 10)

    # tampilkan waktu simulasi 
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Waktu: {:.2f} detik'.format(t), True, (0, 0, 0))
    window.blit(text, (10, 10))

    # render ke display, update layar
    pygame.display.update()

# exit pygame
# pygame.quit()


# +-------------------+
# |      START        |
# +-------------------+
# |                   |
# |Inisialisasi Pygame|
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# | Konfigurasi layar |
# +-------------------+
# |                   |
# |   Set Caption     |
# |   Buat Display    |
# |  Set Ukuran Layar |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# | Inisialisasi Objek|
# +-------------------+
# |                   |
# |  Set Posisi Awal  |
# | Set Kecepatan Awal|
# |  Set Waktu Awal   |
# |  Set Delta Waktu  |
# |  Set Gravitasi    |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |      WHILE        |
# +-------------------+
# |                   |
# |   Handle Event    |
# |   Ambil Keyboard  |
# |    Gerak Objek    |
# |   Update Layar    |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |    Handle Event   |
# +-------------------+
# |                   |
# |  Cek event type   |
# |    Jika QUIT      |
# |   Exit pygame     |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |   Ambil Keyboard  |
# +-------------------+
# |                   |
# |  Ambil Key Press  |
# |    Jika SPACE     |
# |    Jatuh Objek    |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |    Gerak Objek     |
# +-------------------+
# |                   |
# |    Gerak Objek    |
# |  Update Kecepatan |
# |    Update Waktu   |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |   Update Layar    |
# +-------------------+
# |                   |
# |     Fill Layar    |
# | Gambar Objek Jatuh|
# |  Tampilkan Waktu  |
# |                   |
# +-------------------+
#           |
#           v
# +-------------------+
# |      END          |
# +-------------------+
# |                   |
# |    Exit Pygame    |
# |                   |
# +-------------------+
