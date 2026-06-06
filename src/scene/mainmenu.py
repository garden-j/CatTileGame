import pygame

from src.board import GameBoard
from src.config import GAME_WIDTH, GAME_HEIGHT, Y_OFFSET
from src.scene.base import BaseScene
from src.scene.gameplay import GameplayScene


class MainScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.board = GameBoard()
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.desc_font = pygame.font.SysFont("Arial", 18)
        self.button_font = pygame.font.SysFont("Arial", 24, bold=True)
        self.start_btn_rect = pygame.Rect(GAME_WIDTH // 2 - 100, 380, 200, 65)

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
                absolute_btn_rect = self.start_btn_rect.copy()
                absolute_btn_rect.x += center_x
                absolute_btn_rect.y += center_y

                # 3. 마우스의 날것 그대로의 좌표(event.pos)가
                # 실제 눈에 보이는 저 빨간 박스(absolute_btn_rect) 안에 들어왔는지 검사합니다!
                if absolute_btn_rect.collidepoint(event.pos):
                    print("🎮 [검증 완료] 시작 버튼 영역 클릭 성공! 게임 화면으로 이동합니다.")
                    self.change_to(GameplayScene)


    def draw(self, screen):
        screen.fill((255, 0, 0))
        pygame.display.flip()
        print("DRAW CALLED")
        # 1. 가상 도화지에 격자 배경 그리기
        self.game_surface.fill("white")
        self.board.draw(self.game_surface)

        # 2. [디자인] 배경 격자 위에 글씨가 잘 보이도록 약간 어두운 반투명 레이어 얹기
        # 파이게임에서 반투명 효과를 주기 위해 임시 서피스를 만듭니다.
        overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))  # 검은색에 알파값(투명도) 100
        self.game_surface.blit(overlay, (0, 0))

        # 3. 게임 이름 (타이틀) 그리기
        title_text = self.title_font.render("CAT TILES", True, (255, 255, 255))
        self.game_surface.blit(title_text, (GAME_WIDTH // 2 - title_text.get_width() // 2, 120))

        # 4. 게임 설명 그리기
        # desc1 = self.desc_font.render("빈 격자를 누르면 상하좌우에서 가장 가까운", True, (220, 220, 220))
        # desc2 = self.desc_font.render("같은 색상의 블록들이 마법처럼 제거됩니다!", True, (220, 220, 220))
        # desc3 = self.desc_font.render("목표: 화면의 모든 색상 블록을 없애세요.", True, (245, 210, 121))

        # self.game_surface.blit(desc1, (GAME_WIDTH // 2 - desc1.get_width() // 2, 220))
        # self.game_surface.blit(desc2, (GAME_WIDTH // 2 - desc2.get_width() // 2, 250))
        # self.game_surface.blit(desc3, (GAME_WIDTH // 2 - desc3.get_width() // 2, 290))

        # 5. 시작 버튼 UI 그리기
        # 마우스 오버 효과를 넣으면 더 좋지만 우선 기본 사각형으로 그립니다.
        pygame.draw.rect(self.game_surface, (102, 183, 113), self.start_btn_rect, border_radius=10)  # 녹색 버튼
        btn_text = self.button_font.render("GAME START", True, (255, 255, 255))
        self.game_surface.blit(btn_text, (GAME_WIDTH // 2 - btn_text.get_width() // 2, 400))

        # 6. 실제 창(screen) 중앙에 얹기
        center_x = (screen.get_width() - GAME_WIDTH) // 2
        center_y = (screen.get_height() - GAME_HEIGHT) // 2
        screen.blit(self.game_surface, (center_x, center_y))


