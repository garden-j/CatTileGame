import pygame
import random
from src.config import *

class GameBoard(object):
    def __init__(self):
        self.rows = GRID_ROWS
        self.cols = GRID_COLS
        self.block_size = BLOCK_SIZE

        self.grid = self.generate_blocks()
        self.score = 0
        self.isWrong = True

        self.cat_images = {}
        self.load_cat_assets()

        # self.falling_cats = []

        # sounds
        try:
            self.pop_sound = pygame.mixer.Sound('assets/sounds/cat_pop.ogg')
            self.pop_sound.set_volume(0.5)
        except Exception as e:
            print("pop sound error:", e)
            self.pop_sound = None

        try:
            self.wrong_sound = pygame.mixer.Sound('assets/sounds/cat_wrong.ogg')
            self.wrong_sound.set_volume(0.5)
        except Exception as e:
            print("wrong sound error:", e)
            self.wrong_sound = None

    def load_cat_assets(self):
        for block_id, img_path in CAT_IMG_PATHS.items():
            original_img = pygame.image.load(img_path).convert_alpha()
            scaled_img = pygame.transform.scale(original_img, (self.block_size, self.block_size))
            self.cat_images[block_id] = scaled_img

    def generate_blocks(self):
        block_pool = []
        for _ in range(COLOR_BLOCK_COUNT):
            random_color = random.randint(1, 9)
            block_pool.append(random_color)
            block_pool.append(random_color)
        empty_cnt = TOTAL_TILES - len(block_pool)
        for _ in range(empty_cnt):
            block_pool.append(0)
        random.shuffle(block_pool)

        new_grid = []
        for row in range(self.rows):
            start_idx = row * self.cols
            end_idx = start_idx + self.cols

            row_data = block_pool[start_idx:end_idx]
            new_grid.append(row_data)
        return new_grid

    def handle_click(self, mouse_x, mouse_y, scene=None):
        col = mouse_x // self.block_size
        row = (mouse_y - Y_OFFSET) // self.block_size

        if not (0 <= col < self.cols and 0 <= row < self.rows):
            self.isWrong = False
            return
        if self.grid[row][col] != 0:
            self.isWrong = False
            return
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        found_blocks = []

        for x, y in zip(dx, dy):
            nx = x + row
            ny = y + col
            while 0 <= nx < self.rows and 0 <= ny < self.cols:
                block_id = self.grid[nx][ny]
                if block_id != 0:
                    found_blocks.append([nx, ny, block_id])
                    break
                nx += x
                ny += y
        color_ids = [block[2] for block in found_blocks]
        unique_ids = set(color_ids)

        self.isWrong = True
        for color_id in unique_ids:
            if color_ids.count(color_id) > 1:
                for x, y, c in found_blocks:
                    if c == color_id:
                        screen_x = y * self.block_size + (self.block_size // 2)
                        screen_y = x * self.block_size + Y_OFFSET + (self.block_size // 2)

                        if scene is not None:
                            scene.trigger_cat_escape(screen_x, screen_y, color_id)

                        # vx = random.uniform(-3, 3)
                        # vy = -5
                        #
                        # self.falling_cats.append({
                        #     "x": screen_x, "y": screen_y,
                        #     "vx": vx, "vy": vy,
                        #     "id": color_id
                        # })

                        self.grid[x][y] = 0
                        self.score += 1
                        self.isWrong = False
        if not self.isWrong:
            if self.pop_sound:
                self.pop_sound.play()
        else:
            if self.wrong_sound:
                self.wrong_sound.play()

    def update_effects(self):
        #  # 리스트를 역순으로 순회하거나 새로 짜서 제거 시 인덱스 꼬임 방지
        # alive_falling_cats = []
        #
        # for cat in self.falling_cats:
        #     # 1. 속도만큼 위치 이동
        #     cat["x"] += cat["vx"]
        #     cat["y"] += cat["vy"]
        #
        #     # 2. 중력 가속도 적용 (세로 속도가 매 프레임 점점 빨라집니다)
        #     cat["vy"] += 0.5
        #
        #     # 3. 아직 화면 안(y 좌표가 화면 맨 밑바닥을 뚫고 나가기 전)에 있을 때만 살려둡니다.
        #     # 대략 창 높이가 700~800이니 900 이하일 때만 유지하는 안전장치
        #     if cat["y"] < 900:
        #         alive_falling_cats.append(cat)
        #
        # self.falling_cats = alive_falling_cats
        pass

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.block_size
                y = row * self.block_size + Y_OFFSET
                block_id = self.grid[row][col]
                if (row + col) % 2 == 0:
                    tile_color = "white"
                else:
                    tile_color = (243, 243, 243)
                pygame.draw.rect(screen, tile_color, (x, y, self.block_size, self.block_size),)

                if self.cat_images.get(block_id) is not None:
                    screen.blit(self.cat_images[block_id], (x, y))
                else:
                    if block_id != 0:
                        block_color = BLOCK_TYPES[block_id]
                        pygame.draw.rect(screen, block_color, (x, y, self.block_size - 1, self.block_size - 1),
                                         border_radius=3)

        # for cat in self.falling_cats:
        #     cat_id = cat["id"]
        #     if self.cat_images.get(cat_id) is not None:
        #         cat_img = self.cat_images[cat_id]
        #         # 실시간으로 추락 중인 물리 좌표에 고양이를 blit 합니다.
        #         screen.blit(cat_img, (cat["x"], cat["y"]))
