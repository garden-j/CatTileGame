import pygame
from src.board import GameBoard
from src.config import GAME_WIDTH, GAME_HEIGHT, Y_OFFSET
from src.scene.base import BaseScene


class GameOverScene(BaseScene):
    def __init__(self, final_score):
        super().__init__()
        self.score = final_score
        self.board = GameBoard()
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.over_font = pygame.font.SysFont("Arial", 50, 5)
        self.score_font = pygame.font.SysFont("Arial", 40, 3)
        self.btn_font = pygame.font.SysFont("Arial", 30)
        self.restart_btn_rect = pygame.Rect(GAME_WIDTH // 2 - 100, 380, 200, 65)
        self.main_btn_rect = pygame.Rect(GAME_WIDTH // 2 - 100, 380, 200, 80)


    def handle_events(self, event):
        from src.scene.gameplay import GameplayScene
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 1. 현재 창 크기와 중앙 정렬을 위한 여백(오프셋)을 구합니다.
                current_sw, current_sh = pygame.display.get_surface().get_size()
                center_x = (current_sw - GAME_WIDTH) // 2
                center_y = (current_sh - GAME_HEIGHT) // 2

                # 2. [핵심 수정] 도화지 내부 기준이었던 start_btn_rect를
                # 실제 전체 창 기준으로 이동시킨 '진짜 버튼 영역'을 임시로 만듭니다.
                restart_btn_rect = self.restart_btn_rect.copy()
                restart_btn_rect.x += center_x
                restart_btn_rect.y += center_y

                main_btn_rect = self.main_btn_rect.copy()
                main_btn_rect.x += center_x
                main_btn_rect.y += center_y



                if restart_btn_rect.collidepoint(event.pos):
                    print("재시작 버튼 영역 클릭 성공!")
                    self.change_to(GameplayScene)

    def draw(self, screen):
        self.game_surface.fill("white")
        self.board.draw(self.game_surface)

        overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))
        self.game_surface.blit(overlay, (0, 0))

        over_text = self.over_font.render("Game Over!", True, "white")
        self.game_surface.blit(over_text, (GAME_WIDTH // 2 - over_text.get_width() // 2, 110))
        score_text = self.score_font.render(f"Score: {self.score}", True, "white")
        self.game_surface.blit(score_text, (GAME_WIDTH // 2 - score_text.get_width() // 2, 170))

        pygame.draw.rect(self.game_surface, (200, 200, 200), self.restart_btn_rect, border_radius=10)
        btn_text = self.btn_font.render("Restart", True, "white")
        text_x = self.restart_btn_rect.x + (self.restart_btn_rect.width // 2) - (btn_text.get_width() // 2)
        text_y = self.restart_btn_rect.y + (self.restart_btn_rect.height // 2) - (btn_text.get_height() // 2)
        self.game_surface.blit(btn_text, (text_x, text_y))
        # 6. 실제 창(screen) 중앙에 얹기
        center_x = (screen.get_width() - GAME_WIDTH) // 2
        center_y = (screen.get_height() - GAME_HEIGHT) // 2
        screen.blit(self.game_surface, (center_x, center_y))
