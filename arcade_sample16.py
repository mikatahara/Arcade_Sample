# 横スクロール
import arcade

WIDTH = 640

# MyGame クラスの定義 ---
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        # 親クラスの初期化関数をコールする
        super().__init__(width, height, title)
        # 背景色
        arcade.set_background_color(arcade.color.SKY_BLUE)
        # 背景
        self.background1 = arcade.Sprite("bg1.png")
        self.background2 = arcade.Sprite("bg2.png")
        self.wood = arcade.Sprite("wood1.png")

        self.bk_list = arcade.SpriteList()
        self.bk_list.append(self.background1)
        self.background1.center_x=WIDTH/2
        self.background1.center_y=60
        self.background1.change_x=-1

        self.bk_list.append(self.background2)
        self.background2.center_x=WIDTH*3/2
        self.background2.center_y=60
        self.background2.change_x=-1

        self.bk_list.append(self.wood)
        self.wood.center_x=WIDTH
        self.wood.center_y=100
        self.wood.change_x=-2

    # １秒間に60回、この関数が呼び出され再描画します。
    def on_draw(self):
        self.clear()
        self.bk_list.draw()

    def on_update(self, delta_time):
        self.bk_list.update(delta_time)
        if(self.background1.center_x<=-WIDTH/2):
            self.background1.center_x = WIDTH*3/2
        if(self.background2.center_x<=-WIDTH/2):
            self.background2.center_x = WIDTH*3/2
        if(self.wood.center_x<-0):
            self.wood.center_x += WIDTH

# --- クラスの定義終わり

# MyGame を作成
mywindow = MyGame(640, 480, "MyGame Example")
arcade.run() 
