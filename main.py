import pygame
import sys
from player import PlayerModule

# 基礎解析度設定
WIDTH, HEIGHT = 800, 600

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("多媒體模組化專題 - 延伸性架構")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # 核心清單：所有「功能模組」都會掛載到這裡
        self.modules = []

    def add_module(self, module):
        """用於掛載新功能的介面"""
        self.modules.append(module)

    def run(self):
        while self.running:
            # 1. 事件偵測
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # 2. 邏輯更新 (Base 不動，循環呼叫所有模組)
            for module in self.modules:
                module.update()

            # 3. 畫面繪製
            self.screen.fill((30, 30, 30)) # 背景深灰色
            for module in self.modules:
                module.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameEngine()
    game.add_module(PlayerModule())
    game.run()