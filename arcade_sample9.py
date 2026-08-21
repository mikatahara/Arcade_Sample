# (9) 回転方向を左右のみにする
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # 魚の初期化
        image_source = ":resources:/images/enemies/fishGreen.png"
        self.player_sprite = arcade.Sprite(image_source, 1.0)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_sprite.angle = 0
        self.player_sprite.change_x=2       # 右へ進む
        self.player_sprite.scale_x = -1.0   # 右を向く

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # 左右の壁を作る
        wall = ":resources:/images/tiles/boxCrate.png"
        self.wallR_sprite = arcade.Sprite(wall, 1.0)
        self.wallR_sprite.center_x = 680
        self.wallR_sprite.center_y = 240
        self.wallR_sprite.scale_y = 4.0
        self.player_list.append(self.wallR_sprite)
        self.wallL_sprite = arcade.Sprite(wall, 1.0)
        self.wallL_sprite.center_x = -40
        self.wallL_sprite.center_y = 240
        self.wallL_sprite.scale_y = 4.0
        self.player_list.append(self.wallL_sprite)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        self.player_list.draw() # スプライトの再描画

    def on_update(self, delta_time):
        self.player_sprite.update()             # 位置をアップデートする
        if self.player_sprite.collides_with_sprite(self.wallR_sprite):  #右の壁にぶつかった
            self.player_sprite.change_x=-2      # 左へ進む
            self.player_sprite.scale_x = 1.0    # 左を向く
        if self.player_sprite.collides_with_sprite(self.wallL_sprite):  #左の壁にぶつかった
            self.player_sprite.change_x= 2      # 右へ進む
            self.player_sprite.scale_x = -1.0   # 右を向く

    # --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
