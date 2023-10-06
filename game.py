import pygame
import random

# Inicjalizacja gry
pygame.init()

# Ustawienia okna gry
szerokosc_okna = 800
wysokosc_okna = 600
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("River Raid")

# Kolory
czarny = (0, 0, 0)
bialy = (255, 255, 255)

# Wczytanie obrazków
gracz_img = pygame.image.load("gracz.png")
gracz_img = pygame.transform.scale(gracz_img, (40, 40))
przeszkoda_img = pygame.image.load("gracz.png")
przeszkoda_img = pygame.transform.scale(przeszkoda_img, (40, 40))
pocisk_img = pygame.image.load("pocisk.png")
pocisk_img = pygame.transform.scale(pocisk_img, (10, 30))
tlo_img = pygame.image.load("tlo.png")
tlo_img = pygame.transform.scale(tlo_img, (szerokosc_okna, wysokosc_okna))

# Pozycja gracza
gracz_x = 380
gracz_y = 500

# Prędkość gracza
gracz_predkosc = 5

# Lista przeszkód
przeszkody = []

# Prędkość przeszkód
przeszkoda_predkosc = 3

# Lista pocisków
pociski = []

# Prędkość pocisków
pocisk_predkosc = 7

# Punkty
punkty = 0

# Funkcja do generowania nowych przeszkód
def dodaj_przeszkode():
    x = random.randint(0, szerokosc_okna - 40)
    y = -40
    przeszkody.append([x, y])

# Funkcja do generowania pocisku
def strzel():
    x = gracz_x + 15
    y = gracz_y - 30
    pociski.append([x, y])

# Główna pętla gry
gra_aktywna = True
clock = pygame.time.Clock()

while gra_aktywna:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_aktywna = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                strzel()

    # Ruch gracza
    nacisniete_klawisze = pygame.key.get_pressed()
    if nacisniete_klawisze[pygame.K_LEFT]:
        gracz_x -= gracz_predkosc
    if nacisniete_klawisze[pygame.K_RIGHT]:
        gracz_x += gracz_predkosc

    # Aktualizacja pozycji przeszkód
    for przeszkoda in przeszkody:
        przeszkoda[1] += przeszkoda_predkosc
        if przeszkoda[1] > wysokosc_okna:
            przeszkody.remove(przeszkoda)
            punkty += 1

    # Dodawanie nowych przeszkód
    if len(przeszkody) < 5:
        dodaj_przeszkode()

    # Aktualizacja pozycji pocisków
    for pocisk in pociski:
        pocisk[1] -= pocisk_predkosc
        if pocisk[1] < -30:
            pociski.remove(pocisk)

    # Kolizja pocisków z przeszkodami
    for pocisk in pociski:
        for przeszkoda in przeszkody:
            if pocisk[0] < przeszkoda[0] + 40 and pocisk[0] + 10 > przeszkoda[0] and pocisk[1] < przeszkoda[1] + 40 and pocisk[1] + 30 > przeszkoda[1]:
                pociski.remove(pocisk)
                przeszkody.remove(przeszkoda)
                punkty += 10

    # Kolizja gracza z przeszkodami
    for przeszkoda in przeszkody:
        if gracz_x < przeszkoda[0] + 40 and gracz_x + 40 > przeszkoda[0] and gracz_y < przeszkoda[1] + 40 and gracz_y + 40 > przeszkoda[1]:
            gra_aktywna = False

    # Wyświetlanie obiektów
    okno.blit(tlo_img, (0, 0))
    okno.blit(gracz_img, (gracz_x, gracz_y))
    for przeszkoda in przeszkody:
        okno.blit(przeszkoda_img, (przeszkoda[0], przeszkoda[1]))
    for pocisk in pociski:
        okno.blit(pocisk_img, (pocisk[0], pocisk[1]))

    # Wyświetlanie punktów
    font = pygame.font.Font(None, 36)
    tekst_punkty = font.render("Punkty: " + str(punkty), True, bialy)
    okno.blit(tekst_punkty, (10, 10))

    # Aktualizacja okna
    pygame.display.update()
    clock.tick(60)

# Zakończenie gry
pygame.quit()
