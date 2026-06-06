# 화면 크기, FPS, 색상 등 상수 정의
import pygame


GRID_COLS = 25
GRID_ROWS = 17
BLOCK_SIZE = 25
FPS = 60
Y_OFFSET = 50

GAME_WIDTH = GRID_COLS * BLOCK_SIZE          # 625
GAME_HEIGHT = (GRID_ROWS * BLOCK_SIZE) + Y_OFFSET # 505

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


TOTAL_TILES = GRID_COLS * GRID_ROWS
COLOR_BLOCK_COUNT = 110

TIMER = 120

BLOCK_TYPES = {
    0: None,
    1: (186,218,85),
    2: (217,83,83),
    3: (245,210,121),
    4: (122,199,245),
    5: (171,122,245),
    6: (245,122,242),
    7: (48,61,186),
    8: (122,245,226),
    9: (102,183,113),
}

CAT_IMG_PATHS = {
    1: "assets/images/cat_yellow.png",
    2: "assets/images/cat_blue.png",
    3: "assets/images/cat_orange.png",
    4: "assets/images/cat_red.png",
    5: "assets/images/cat_green.png",
    6: "assets/images/cat_brown.png",
    7: "assets/images/cat_purple.png",
    8: "assets/images/cat_grey.png",
    9: "assets/images/cat_pink.png",
}

CAT_RUN01_PATHS = {
    1: "assets/images/run/cat_run04_yellow.png",
    2: "assets/images/run/cat_run04_blue.png",
    3: "assets/images/run/cat_run04_orange.png",
    4: "assets/images/run/cat_run04_red.png",
    5: "assets/images/run/cat_run04_green.png",
    6: "assets/images/run/cat_run04_brown.png",
    7: "assets/images/run/cat_run04_purple.png",
    8: "assets/images/run/cat_run04_grey.png",
    9: "assets/images/run/cat_run04_pink.png",
}
CAT_RUN02_PATHS = {
    1: "assets/images/run/cat_run03_yellow.png",
    2: "assets/images/run/cat_run03_blue.png",
    3: "assets/images/run/cat_run03_orange.png",
    4: "assets/images/run/cat_run03_red.png",
    5: "assets/images/run/cat_run03_green.png",
    6: "assets/images/run/cat_run03_brown.png",
    7: "assets/images/run/cat_run03_purple.png",
    8: "assets/images/run/cat_run03_grey.png",
    9: "assets/images/run/cat_run03_pink.png",
}
CAT_RUN03_PATHS = {
    1: "assets/images/run/cat_run02_yellow.png",
    2: "assets/images/run/cat_run02_blue.png",
    3: "assets/images/run/cat_run02_orange.png",
    4: "assets/images/run/cat_run02_red.png",
    5: "assets/images/run/cat_run02_green.png",
    6: "assets/images/run/cat_run02_brown.png",
    7: "assets/images/run/cat_run02_purple.png",
    8: "assets/images/run/cat_run02_grey.png",
    9: "assets/images/run/cat_run02_pink.png",
}

CAT_RUN04_PATHS = {
    1: "assets/images/run/cat_run01_yellow.png",
    2: "assets/images/run/cat_run01_blue.png",
    3: "assets/images/run/cat_run01_orange.png",
    4: "assets/images/run/cat_run01_red.png",
    5: "assets/images/run/cat_run01_green.png",
    6: "assets/images/run/cat_run01_brown.png",
    7: "assets/images/run/cat_run01_purple.png",
    8: "assets/images/run/cat_run01_grey.png",
    9: "assets/images/run/cat_run01_pink.png",
}


ALL_RUN_PATHS = [CAT_RUN01_PATHS, CAT_RUN02_PATHS, CAT_RUN03_PATHS, CAT_RUN04_PATHS]

CAT_RUN_IMGS = {}


def load_cat_run_img():
    scale_factor = 1.5
    for idx in range(1, 10):
        CAT_RUN_IMGS[idx] = []
        for path_dict in ALL_RUN_PATHS:
            file_path = path_dict[idx]
            try:
                img = pygame.image.load(file_path).convert_alpha()
                # 2. 원본 이미지의 현재 가로, 세로 크기를 가져옵니다.
                orig_w, orig_h = img.get_size()

                # 3. 배율을 곱해서 새로운 크기를 계산합니다.
                new_w = int(orig_w * scale_factor)
                new_h = int(orig_h * scale_factor)

                # 4. 크기를 키운 이미지로 변환합니다. (도트 느낌을 살리려면 scale, 부드럽게 하려면 smoothscale)
                scaled_img = pygame.transform.scale(img, (new_w, new_h))

                # 5. 크기가 커진 이미지를 리스트에 담습니다.
                CAT_RUN_IMGS[idx].append(scaled_img)
            except Exception as e:
                print(f"이미지 로드 실패 ({file_path}): {e}")



