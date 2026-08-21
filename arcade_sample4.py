# (4)壁で跳ね返るボール
import arcade
import numpy as np

Angle = 45.*np.pi/180

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.xinc = 4*np.cos(Angle)
        self.yinc = 4*np.sin(Angle)
        self.ball_x = 50
        self.ball_y = 160

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(self.ball_x, self.ball_y , 15, arcade.color.AUBURN)

    # １秒間に60回、この関数が呼び出されます。
    def on_update(self, delta_time):
        self.ball_x += self.xinc
        self.ball_y += self.yinc
        if(self.ball_x>=640):       # 右の壁にぶつかった
            self.xinc=-self.xinc    # 向きを左へ
        if(self.ball_x<=0):         # 左の壁にぶつかった
            self.xinc=-self.xinc    # 向きを右へ
        if(self.ball_y>=480):       # 上の壁にぶつかった
            self.yinc=-self.yinc    # 向きを下へ
        if(self.ball_y<=0):         # 下の壁にぶつかった
            self.yinc=-self.yinc    # 向きを上へ

# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
