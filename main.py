import pygame
import asyncio
import sys
from src.config import *
from src.board import GameBoard
from src.scene.gameplay import GameplayScene
from src.scene.mainmenu import MainScene


async def main():
    # 1. 초기화
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    current_sw = SCREEN_WIDTH
    current_sh = SCREEN_HEIGHT
    screen = pygame.display.set_mode((current_sw, current_sh), pygame.RESIZABLE)
    pygame.display.set_caption("Color Block Game")
    clock = pygame.time.Clock()


    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    board = GameBoard()

    load_cat_run_img()
    # gameplay = GameplayScene()

    running = True
    current_scene = MainScene()

    # 2. 게임 루프
    while running:
        # FPS 제한
        clock.tick(FPS)

        # A. 이벤트 처리 (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                current_sw = event.w
                current_sh = event.h
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            current_scene.handle_events(event)

        current_scene.update()
        # gameplay.update()

        screen.fill("white")
        game_surface.fill("white")
        current_scene.draw(screen)

        if current_scene.next_scene != current_scene:
            current_scene = current_scene.next_scene

        pygame.display.flip()  # 버퍼를 화면에 반영

        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()


# if __name__ == "__main__":
#     main()
asyncio.run(main())