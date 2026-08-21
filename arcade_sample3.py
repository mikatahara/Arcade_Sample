# (3)アニメーション
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.ball_x = 0

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(self.ball_x, 160, 15, arcade.color.AUBURN)

    # １秒間に60回、この関数が呼び出されます。
    def on_update(self, delta_time):
        self.ball_x += 2
        if(self.ball_x>=640):
            self.ball_x=0

# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
