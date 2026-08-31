# (15) シューティングゲームの例
import arcade
import numpy as np
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

PLAYER_X=100
PLAYER_Y=100
PLAYER_JUMP_Y=300
ENEMY_X = 640
ENEMY_Y = 420

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
        self.texture_enemy_idle = arcade.load_texture(":resources:/images/enemies/fishGreen.png")
        self.texture_enemy_hit = arcade.load_texture(":resources:/images/enemies/fishPink.png")
        self.enemy_sprite = arcade.Sprite(
            self.texture_enemy_idle,
            scale=0.8
        )
        # ヒットの音
        self.hit_sound = arcade.load_sound(
            ":resources:sounds/error4.wav"
        )

        # プレイヤーの「リスト」
        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(self.enemy_sprite)
        self.enemy_sprite.center_x = ENEMY_X
        self.enemy_sprite.center_y = ENEMY_Y
        self.enemy_sprite.change_x = -2     # 左へ進む
        self.enemy_sprite.scale_x = 1.0     # 左を向く
        self.timmer = 0

        # ボール
        self.texture_ball = arcade.load_texture("throw_ball.png")
        self.ball_sprite = arcade.Sprite(
            self.texture_ball,
            scale=0.2
        )

        # ボールの「リスト」
        self.ball_list = arcade.SpriteList()

        # ボールを投げた時の音
        self.throw_sound = arcade.load_sound(
            ":resources:sounds/jump4.wav"
        )

        # ループで鳴らす音
        self.bgm = arcade.load_sound(
            "ELEC_01_All.wav"
        )
        self.bgm_player = arcade.play_sound(
            self.bgm,
            loop=True
        )
        self.bgm_started=True

    # ボールをクローンする
    def create_ball(self, x, y, incy):
        ball_sprite = arcade.Sprite(
            self.texture_ball,
            scale=0.15
        )
        ball_sprite.center_x = x
        ball_sprite.center_y = y
        ball_sprite.change_y = incy
        self.ball_list.append(ball_sprite)

    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 640, 0, 60, arcade.csscolor.GRAY)
        self.player_list.draw()
        self.ball_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()
        self.ball_list.update()
        self.enemy_list.update()

        for ball in self.ball_list:
            # 端に到達
            if (ball.left <= 0 or ball.right >= self.width or
            ball.bottom <= 0 or ball.top >= self.height):
                ball.remove_from_sprite_lists()

            # プレイヤーと敵が衝突したか調べる
            collision= arcade.check_for_collision_with_list(
                ball,
                self.enemy_list
            )
            #　敵にヒットした
            if collision:
                ball.remove_from_sprite_lists()
                self.enemy_sprite.texture = self.texture_enemy_hit
                self.timmer = 60
                arcade.play_sound(self.hit_sound)

        if self.timmer==0:
            self.enemy_sprite.texture = self.texture_enemy_idle
        else:
            self.timmer -=1

        # 敵の反転
        if(self.enemy_sprite.center_x<=0):
            self.enemy_sprite.change_x =  2     # 右へ進む
            self.enemy_sprite.scale_x = -1.0    # 右を向く

        if(self.enemy_sprite.center_x>=SCREEN_WIDTH):
            self.enemy_sprite.change_x = -2     # 左へ進む
            self.enemy_sprite.scale_x = 1.0     # 左を向く

    #  キーが押されたら
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -4
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 4
        if key == arcade.key.SPACE:
            self.create_ball(self.player_sprite.center_x,self.player_sprite.center_y,4)
            self.player_sprite.texture=self.texture_jump
            arcade.play_sound(self.throw_sound)

    #  キーが離されたら
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x=0
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_x=0
        if symbol == arcade.key.SPACE:
            self.player_sprite.texture=self.texture_idel

mywindow = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "MyGame Example")
arcade.run()