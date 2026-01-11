import pygame

class PlayerModule:
    def __init__(self):
        # 設定玩家初始位置與顏色
        self.pos = [400, 300]
        self.color = (0, 255, 0) # 綠色
        self.speed = 5

    def update(self):
        # 讀取按鍵輸入來移動方塊
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed

    def draw(self, screen):
        # 在螢幕上畫出玩家
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], 50, 50))