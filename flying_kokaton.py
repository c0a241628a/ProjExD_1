import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #1
    bg_img2 = pg.transform.flip(bg_img,True,False) #8
    KK_img = pg.image.load("fig/3.png") #2
    KK_img = pg.transform.flip(KK_img,True,False) #2
    KK_rct = KK_img.get_rect() #10:Rectの抽出
    KK_rct.center = 300,200 #10
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x=tmr%3200 #7,9
        screen.blit(bg_img, [-x, 0]) #3,6
        screen.blit(bg_img2, [-x+1600,0]) #7,8
        screen.blit(bg_img, [-x+3200, 0]) #9
        
        screen.blit(KK_img, KK_rct) #4,10
        
        #KK_rct.move_ip((-1, 0))
        
        key_lst = pg.key.get_pressed() #10
        xziku=0
        yziku=0
        if key_lst[pg.K_UP]:
            yziku+=-1
        if key_lst[pg.K_DOWN]:
            yziku+=1
        if key_lst[pg.K_RIGHT]:
            xziku+=2
        if key_lst[pg.K_LEFT]:
            xziku+=-1
        xziku+=-1
        KK_rct.move_ip((xziku, yziku))
        
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()