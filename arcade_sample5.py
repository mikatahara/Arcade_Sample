# (5)ボールの数を増やす
import arcade
import numpy as np

# ボールのクラスの定義 ---
class Ball(arcade.Window):
    def __init__(self, xposs, yposs, bsize, bangle, bspeed, bcolor):
        self.ball_x = xposs
        self.ball_y = yposs
        self.ball_size = bsize
        self.xinc = bspeed*np.cos(bangle*np.pi/180)
        self.yinc = bspeed*np.sin(bangle*np.pi/180)
        self.color = bcolor

    def updata(self,delta_time):
        self.ball_x += self.xinc
        self.ball_y += self.yinc
        if(self.ball_x>=640):   # 右の壁にぶつかった
            self.xinc=-self.xinc
        if(self.ball_x<=0):     # 左の壁にぶつかった
            self.xinc=-self.xinc
        if(self.ball_y>=480):   # 上の壁にぶつかった
            self.yinc=-self.yinc
        if(self.ball_y<=0):     # 下の壁にぶつかった
            self.yinc=-self.yinc      

    def draw(self):
        arcade.draw_circle_filled(self.ball_x, self.ball_y , self.ball_size, self.color)
# --- クラスの定義終わり

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        # ボールを創る
        self.ballr = Ball(50,  150, 10,  43, 12, arcade.color.RED)
        self.ballg = Ball(350, 360, 15, -42,  9, arcade.color.YELLOW)
        self.ballb = Ball(250, 250, 20,  64,  6, arcade.color.BLUE)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        self.ballr.draw()
        self.ballg.draw()
        self.ballb.draw()

    # １秒間に60回、この関数が呼び出されます。
    def on_update(self, delta_time):
        self.ballr.updata(delta_time)
        self.ballg.updata(delta_time)
        self.ballb.updata(delta_time)
# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
