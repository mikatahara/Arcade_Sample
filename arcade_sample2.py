# (2)描画の更新
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()    #全部消す
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 240, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(50, 300, 15, arcade.color.AUBURN)

# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()