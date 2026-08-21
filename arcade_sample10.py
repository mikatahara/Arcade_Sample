# (10) スペースバーでジャンプする
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.dest= [0,0]    # 目的地

        # スプライトの初期化
        image_source = ":resources:/images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = arcade.Sprite(image_source, 0.8)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 80
        self.player_sprite.angle = 0

        # 通常状態/ジャンプ中/降下中の３つのスプライトを準備する
        self.texture_idel = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_idle.png")
        self.texture_jump = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_jump.png")
        self.texture_fall = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_fall.png")

        # 「リスト」はスプライトを管理するためのものです。スプライトは、いずれかのリストに入れる必要があります。
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 60, arcade.csscolor.GREEN)
        self.player_list.draw() # スプライトの再描画

    # １秒間に60回、この関数が呼び出されます。
    def on_update(self, delta_time):
        self.player_sprite.update()         # 位置をアップデートする
        # 一番上に到達したか？
        if(self.player_sprite.center_y>280):
            self.player_sprite.texture = self.texture_fall
            self.player_sprite.change_y= -3
        # 降りたきったか？
        if(self.player_sprite.center_y<80):
            self.player_sprite.center_y = 80
            self.player_sprite.texture = self.texture_idel
            self.player_sprite.change_y= 0

    # もし、スペースバーが押されたらジャンプする
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.texture = self.texture_jump
            self.player_sprite.change_y= 4

    # --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
