# 화면 크기, FPS, 색상 등 상수 정의



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