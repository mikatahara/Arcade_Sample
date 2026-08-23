# (13)同心円上にボールを放出
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # 「リスト」はスプライトを管理するためのものです。スプライトは、いずれかのリストに入れる必要があります。
        self.player_list = arcade.SpriteList()

        # 表示されているスプライトの数
        self.visible_count=24

        # 時間のカウンント
        self.wait_time = 0
        self.waiting = True

        # スプライトの初期化
        image_source = "./ballarrow.png"
        self.player_sprite=[]
        for i in range(24):
            self.player_sprite.append(arcade.Sprite(image_source, 0.5))   # サイズ0.8

        # 真ん中へ15度ごとに配置する
        for i in range(24):
            self.player_sprite[i].center_x = 320
            self.player_sprite[i].center_y = 240
            self.player_sprite[i].angle = i*15
            self.player_sprite[i].visible = False
            self.player_list.append(self.player_sprite[i])

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 120, arcade.csscolor.GREEN)
        self.player_list.draw() # スプライトの再描画

    def on_update(self, delta_time):

        # 発射待ち
        if self.waiting:
            self.wait_time += delta_time

            if self.wait_time >= 0.8:
                self.waiting = False
                self.wait_time = 0

                for ball in self.player_sprite:
                    ball.visible = True
            return

        # ボールを移動
        for ball in self.player_sprite:

            if not ball.visible:
                continue

            ball.forward(2)

            # 端に到達
            if (ball.left <= 0 or ball.right >= self.width or
            ball.bottom <= 0 or ball.top >= self.height):

                # 真ん中へ戻す
                ball.center_x = 320
                ball.center_y = 240
                ball.visible = False

        # 全部のボールが端に到達した
        if all(not ball.visible for ball in self.player_sprite):
            self.waiting = True
            self.wait_time = 0
# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run() 
