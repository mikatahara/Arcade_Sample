# (6)スプライトを表示する
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # スプライトの初期化
        image_source = ":resources:/images/space_shooter/playerShip1_blue.png"
        self.player_sprite = arcade.Sprite(image_source, 0.8)   # サイズ0.8
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_sprite.angle = 0

        # 「リスト」はスプライトを管理するためのものです。スプライトは、いずれかのリストに入れる必要があります。
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        self.player_list.draw() # スプライトの再描画
    # --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run() 
