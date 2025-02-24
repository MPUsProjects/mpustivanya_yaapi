import pygame as pg


MAINSCR = 1


def shutdown():
    global running
    running = False
    pg.quit()


def main_screen():
    global scr, scrnow, running, clock

    while running and scrnow == MAINSCR:
        scr.fill((0, 0, 0))

        # КОД

        # тех.часть
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutdown()
                break


pg.init()
scr = pg.display.set_mode((600, 600))
pg.display.set_caption("БОЛЬШАЯ ЗАДАЧА НА MAPS API ЧАСТЬ N")
running = True
clock = pg.time.Clock()
scrnow = MAINSCR

while running:
    if scrnow == MAINSCR:
        main_screen()