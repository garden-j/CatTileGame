# src/scenes/gameplay.py
import pygame
from src.scene.base import BaseScene
from src.board import GameBoard
from src.scene.gameover import GameOverScene

from src.config import GAME_WIDTH, GAME_HEIGHT, TIMER


class GameplayScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.start_ticks = pygame.time.get_ticks()
        self.timer_font = pygame.font.SysFont("Arial", 30)
        self.time_left = TIMER
        self.penalty_time = 0
        self.game_over = False
        # 메인 화면의 보드와는 별개로, 게임용 새로운 랜덤 보드판 생성!
        self.board = GameBoard()

    def handle_events(self, event):
        if self.game_over:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 중앙 정렬 오프셋 계산 후 마우스 좌표 가공
                current_sw, current_sh = pygame.display.get_surface().get_size()
                center_x = (current_sw - GAME_WIDTH) // 2
                center_y = (current_sh - GAME_HEIGHT) // 2

                game_mx = event.pos[0] - center_x
                game_my = event.pos[1] - center_y

                # 여태까지 완성한 상하좌우 매치 및 삭제 로직 실행!
                self.board.handle_click(game_mx, game_my)
                if self.board.isWrong:
                    self.penalty_time += 10

    def update(self):
        if self.game_over:
            return
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = TIMER - (seconds_passed + self.penalty_time)

        self.board.update_effects()

        if self.time_left <= 0:
            self.game_over = True
            self.time_left = 0
            self.change_to(GameOverScene(self.board.score))

    def draw(self, screen):
        self.game_surface.fill("white")

        # 순수한 게임판 격자와 블록만 그리기
        self.board.draw(self.game_surface)

        score_text = self.timer_font.render("Score: " + str(self.board.score), True, "black")
        self.game_surface.blit(score_text, (480, 0))

        time_text = self.timer_font.render("Time: " + str(int(self.time_left)), True, "black")
        self.game_surface.blit(time_text, (0, 0))  # 왼쪽 상단 적당한 위치에 배치

        bar_x = 20
        bar_y = 35
        bar_max_width = GAME_WIDTH - 40  # 양옆 여백 20px씩 제외한 전체 가로 폭
        bar_height = 10

        # 배경 회색 바 그리기
        pygame.draw.rect(self.game_surface, (220, 220, 220), (bar_x, bar_y, bar_max_width, bar_height), border_radius=5)

        # 남은 시간 비율에 맞춰서 실제 초록색 바의 가로 길이 계산 (0.0 ~ 1.0 비율)
        time_ratio = self.time_left / TIMER
        current_bar_width = int(bar_max_width * time_ratio)

        # 시간이 흐를수록 초록색에서 노란색, 빨간색으로 역동적으로 변하는 센스!
        if time_ratio > 0.5:
            bar_color = (102, 183, 113)  # 초록색
        elif time_ratio > 0.2:
            bar_color = (245, 210, 121)  # 노란색
        else:
            bar_color = (217, 83, 83)  # 빨간색 (위험)

        # 실제 남은 시간을 가리키는 게이지 채우기
        if current_bar_width > 0:
            pygame.draw.rect(self.game_surface, bar_color, (bar_x, bar_y, current_bar_width, bar_height),
                             border_radius=5)

        center_x = (screen.get_width() - GAME_WIDTH) // 2
        center_y = (screen.get_height() - GAME_HEIGHT) // 2
        screen.blit(self.game_surface, (center_x, center_y))