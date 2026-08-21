# (7) マウスを追いかける
import arcade
import numpy as np

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.dest= [0,0]    # 目的地

        # スプライトの初期化
        image_source = ":resources:/images/space_shooter/playerShip1_blue.png"
        self.player_sprite = arcade.Sprite(image_source, 0.8)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_sprite.angle = 90

        # 「リスト」はスプライトを管理するためのものです。スプライトは、いずれかのリストに入れる必要があります。
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        self.player_list.draw() # スプライトの再描画

    # マウスが動いたら　x, y がマウスの位置
    def on_mouse_motion(self, x, y, dx, dy):
        self.dest = np.array([x,y]) # 目的地を設定
        ax = x - self.player_sprite.center_x
        ay = y - self.player_sprite.center_y
        self.player_sprite.change_x=ax/60   # 目的地までの移動速度
        self.player_sprite.change_y=ay/60   # 目的地までの移動速度
        self.player_sprite.angle = np.degrees(np.arctan2(ax,ay))    # 目的地の方向

    # １秒間に60回、この関数が呼び出されます。
    def on_update(self, delta_time):
        pos = np.array([self.player_sprite.center_x,self.player_sprite.center_y])
        dist = np.linalg.norm(pos-self.dest)    # 目的地までの距離
        if(dist > 10):                          # 目的地までの距離が大きかったら
            self.player_sprite.update()         # 位置をアップデートする
    # --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
