# [main.py]

import asyncio
import sys
from src.config import *
from src.board import GameBoard
from src.scene.gameplay import GameplayScene
from src.scene.mainmenu import MainScene
import pygame



async def main():
    # 1. 초기화 (웹 브라우저 크래시 방지를 위해 순서 정돈 및 중복 제거)
    pygame.mixer.pre_init()
    pygame.init()

    current_sw = SCREEN_WIDTH
    current_sh = SCREEN_HEIGHT
    screen = pygame.display.set_mode((current_sw, current_sh), pygame.RESIZABLE)
    pygame.display.set_caption("Color Block Game")
    clock = pygame.time.Clock()

    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    board = GameBoard()

    # ⚠️ config.py에 정의한 이미지 로더 함수 (오타 주의: load_cat_run_images 혹은 load_cat_run_img)
    load_cat_run_img()

    running = True
    current_scene = MainScene()

    print("LOOP START")
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

            # 현재 씬의 이벤트 핸들러 작동
            current_scene.handle_events(event)

        print("UPDATE")
        # B. 게임 상태 업데이트
        current_scene.update()

        # C. 화면 그리기 (렌더링 구조 안정화)
        screen.fill("white")
        game_surface.fill("white")

        print("DRAW")
        # 현재 씬을 화면에 그리기
        current_scene.draw(screen)

        # 🎯 [웹 최적화 핵심] 씬 전환 로직 구조적 보완
        # 클래스 인스턴스 주소값 비교가 웹 환경에서 꼬이지 않도록 안전하게 대입 후 다음 씬의 체인 끊기
        if current_scene.next_scene is not None and current_scene.next_scene != current_scene:
            next_target = current_scene.next_scene
            current_scene.next_scene = current_scene  # 무한 루프 방지용 락 해제
            current_scene = next_target

        pygame.display.flip()  # 버퍼를 화면에 반영

        # ⚠️ 웹 브라우저에게 한 프레임 끝났음을 명시적으로 알려주는 생명선 코드
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # pygbag 웹 환경에서는 최상단에서 asyncio.run을 통해 호출해야 완벽하게 인지합니다.
    asyncio.run(main())