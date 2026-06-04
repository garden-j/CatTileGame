class BaseScene:
    def __init__(self):
        self.next_scene = self  # 다음 화면이 무엇인지 저장 (기본은 자기 자신)

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

    def change_to(self, scene_class):
        if callable(scene_class):
            self.next_scene = scene_class()
        else:
            self.next_scene = scene_class