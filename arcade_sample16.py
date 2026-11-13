# 横スクロール    # [quick]
import arcade

WIDTH = 640

# MyGame クラスの定義 ---     # [quick]
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする    # [quick]
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        # 背景
        self.background1 = arcade.Sprite("