# (14) ジャンプで敵を避ける
# 右手から進んでくる敵のヘビをジャンプで避けるゲームです。
# スペースバーを押すとプレーヤはジャンプします。
# 着地すると、次のヘビが現れます。
# ヘビの速度はだんだん早くなります。
# プレーヤと敵がぶつかると終了です。
import arcade
import numpy as np
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

PLAYER_X=100
PLAYER_Y=100
PLAYER_JUMP_Y=300
ENEMY_X = 512
ENEMY_Y = 80

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)

        # 背景
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # プレイヤー
        self.texture_idel = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_idle.png")
        self.texture_jump = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_jump.png")
        self.texture_fall = arcade.load_texture(":resources:/images/animated_characters/female_person/femalePerson_fall.png")
        self.player_sprite = arcade.Sprite(
            self.texture_idel,
            scale=1.0
        )

        self.player_sprite.center_x = PLAYER_X
        self.player_sprite.center_y = PLAYER_Y

        # プレイヤーの「リスト」
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # 敵
        self.enemy_sprite = arcade.Sprite(
            ":resources:images/enemies/wormPink.png",
            scale=0.5
        )
        self.enemy_sprite.center_x = ENEMY_X
        self.enemy_sprite.center_y = ENEMY_Y
        self.enemy_sprite.change_x = -2

        # 的の「リスト」
        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(self.enemy_sprite)

        # 音声ファイルを読み込む
        # 失敗の音
        self.hit_sound = arcade.load_sound(
            ":resources:sounds/lose1.wav"
        )
        # ジャンプの音
        self.jump_sound = arcade.load_sound(
            ":resources:sounds/jump1.wav"
        )
        # ループで鳴らす音
        self.bgm = arcade.load_sound(
            ":resources:music/1918.mp3"
        )
        self.bgm_player = arcade.play_sound(
            self.bgm,
            loop=True
        )
        self.bgm_started=True

        # ジャンプフラグ
        self.jump = False

        # 衝突フラグ
        self.was_collision = False

        # 点数
        self.point = 0

        # 乱数
        self.rng = np.random.default_rng()

        # ゲーム失敗
        self.gamefailure=False

        # ゲームスタート
        self.start_wait=0
        self.game_started =False

    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 60, arcade.csscolor.GRAY)
        arcade.draw_text("点数:"+str(self.point),30, 420,arcade.color.BLACK, 24)

        if(not self.game_started):
            arcade.draw_text(str(np.floor((3.0-self.start_wait)*10)/10),170, 200,arcade.color.RED, 128)

        if(self.gamefailure):
            arcade.draw_text("失敗",140, 200,arcade.color.RED, 128)

        else:
            self.player_list.draw()
            self.enemy_list.draw()

    def on_update(self, delta_time):
        # 失敗したらアップデートしない
        if(self.gamefailure):
            return

        # BGMが鳴り始めるのを待つ
        if not self.game_started:
            self.start_wait += delta_time
            if self.start_wait >= 3.0:
                self.game_started = True
            return
        
        # プレイヤーを動かす
        self.player_list.update()

        # Playerのジャンプ
        if(self.jump):
            # 頂点に達したら
            if(self.player_sprite.change_y<0):
                self.player_sprite.texture = self.texture_fall
            self.player_sprite.change_y -= 0.06

            # 着地
            if(self.player_sprite.center_y<PLAYER_Y):
                self.player_sprite.center_y = PLAYER_Y
                self.player_sprite.texture = self.texture_idel
                self.player_sprite.change_y= 0
                self.jump = False

        # 敵を動かす
        self.enemy_list.update()

        # プレイヤーと敵が衝突したか調べる
        collision= arcade.check_for_collision_with_list(
            self.player_sprite,
            self.enemy_list
        )

        #　最初に衝突した時
        if(collision and not self.was_collision):
            # 衝突したスプライトに変更
            self.player_sprite.texture = self.texture_fall
            # 衝突したら音を鳴らす
            arcade.play_sound(self.hit_sound)
            # 衝突状態を保存する
            self.was_collision = collision
            # 失敗
            self.bgm_player.delete()
            self.gamefailure = True

        # 衝突が解除された時
        if(not collision and self.was_collision):
            # 普通のスプライトに変更
            self.player_sprite.texture = self.texture_idel
            # 衝突状態を保存する
            self.was_collision = collision

        # 敵が左端に到達したら、右へ戻す
        if(self.enemy_sprite.center_x<=20 and not self.jump):
            self.enemy_sprite.center_x=ENEMY_X
            # 敵の速度
            self.enemy_sprite.change_x=-4*self.rng.random() - self.point*0.5 - 1
            # 点数を１点追加
            self.point += 1

    #  スペースバーが押されたらジャンプする
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.texture = self.texture_jump
            self.player_sprite.change_y= 4
            self.jump = True
           # ジャンプサウンド
            arcade.play_sound(self.jump_sound)

mywindow = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "MyGame Example")
arcade.run()