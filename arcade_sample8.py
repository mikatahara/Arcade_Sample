# (8) ボタンを押すとゲームスタート
import arcade
import numpy as np

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # 緑ボタンの初期化
        image_source = ":resources:/gui_basic_assets/window/panel_green.png"
        self.player_sprite_green = arcade.Sprite(image_source, 1.0)
        self.player_sprite_green.center_x = 640-64
        self.player_sprite_green.center_y = 480-32
        self.player_sprite_green.visible = True
        self.player_sprite_green.color = (180, 180, 180)    # 少し暗く表示

        # 赤ボタンの初期化
        image_source = ":resources:/gui_basic_assets/window/panel_red.png"
        self.player_sprite_red = arcade.Sprite(image_source, 1.0)
        self.player_sprite_red.center_x = 640-30
        self.player_sprite_red.center_y = 480-32
        self.player_sprite_red.visible = True
        self.player_sprite_red.color = (255, 255, 255)      # 明るく表示

        # ロケットの初期化
        image_source = ":resources:/images/space_shooter/playerShip1_blue.png"
        self.player_sprite = arcade.Sprite(image_source, 0.8)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_sprite.angle = 60
        self.player_sprite.change_x=2
        self.player_sprite.change_y=1
        self.dest = np.array([640,480])     # 目的地


        # 「リスト」はスプライトを管理するためのものです。スプライトは、いずれかのリストに入れる必要があります。
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite_green)
        self.player_list.append(self.player_sprite_red)
        self.player_list.append(self.player_sprite)

        # ゲームスタートフラグ
        self.game_started = False   # 停止中

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        self.player_list.draw() # スプライトの再描画

    def on_mouse_press(self, x, y, button, modifiers):
        # 緑ボタンでクリック
        if self.player_sprite_green.collides_with_point((x, y)):
            self.start_game()   #ゲームスタート
            self.player_sprite_red.color = (180, 180, 180)
            self.player_sprite_green.color = (255, 255, 255)
            self.player_sprite.center_x = 64
            self.player_sprite.center_y = 128

        # 赤ボタンでクリック
        if self.player_sprite_red.collides_with_point((x, y)):
            self.stop_game()   #ゲームストップ
            self.player_sprite_red.color = (255, 255, 255)
            self.player_sprite_green.color = (180, 180, 180)

    def on_update(self, delta_time):
        if(self.game_started):
            pos = np.array([self.player_sprite.center_x,self.player_sprite.center_y])
            dist = np.linalg.norm(pos-self.dest)    # 目的地までの距離
            if(dist < 100):                         # 目的地までの距離が大きかったら
                self.player_sprite.center_x = 64
                self.player_sprite.center_y = 128
            self.player_sprite.update()         # 位置をアップデートする

    # ゲームスタート
    def start_game(self):
        self.game_started = True
        print("ゲーム開始")

    # ゲームスタート
    def stop_game(self):
        self.game_started = False
        print("ゲーム停止")

    # --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
