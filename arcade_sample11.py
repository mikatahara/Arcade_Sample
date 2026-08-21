# (11) 敵のスプライトに当たったら音が出る
import arcade

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.DARK_GRAY)

        # プレイヤー
        self.texture_idel = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_idle.png")
        self.texture_fall = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_fall.png")
        self.player_sprite = arcade.Sprite(
            self.texture_idel,
            scale=1.0
        )

        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 240

        # プレイヤーの「リスト」
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # 敵
        self.enemy_sprite = arcade.Sprite(
            ":resources:images/enemies/slimeBlue.png",
            scale=1.0
        )
        self.enemy_sprite.center_x = 512
        self.enemy_sprite.center_y = 240
        self.enemy_sprite.change_x = -2

        # 的の「リスト」
        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(self.enemy_sprite)

        # 音声ファイルを読み込む
        self.hit_sound = arcade.load_sound(
            ":resources:sounds/coin1.wav"
        )

        self.was_collision = False

    def on_draw(self):
        self.clear()

        self.player_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        # 敵を動かす
        self.enemy_list.update()

        # プレイヤーと敵が衝突したか調べる
        collision= arcade.check_for_collision_with_list(
            self.player_sprite,
            self.enemy_list
        )

        # 衝突していない状態から、衝突する時を判定する
        if(collision and not self.was_collision):
            # 衝突したスプライトに変更
            self.player_sprite.texture = self.texture_fall
            # 衝突したら音を鳴らす
            arcade.play_sound(self.hit_sound)
            # 今回の衝突判定を保存する
            self.was_collision = collision

        # 敵が左端に到達したら、右へ戻す
        if(self.enemy_sprite.center_x<=20):
            # 普通のスプライトに変更
            self.player_sprite.texture = self.texture_idel
            self.enemy_sprite.center_x=512
            self.was_collision = False

mywindow = MyGame(640, 480, "MyGame Example")
arcade.run()
