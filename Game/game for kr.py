import arcade
import random



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="ball")
        self.ball = None
        self.platform = None
        self.score = 0
        self.spriteList = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.spriteList.draw()
        arcade.draw_text(f"score: {self.score}", 20, self.height - 30, arcade.color.ROSE)

    def on_update(self, delta_time: float):
        self.platform.update()
        self.ball.update()
        if self.platform.center_x < 0:
            self.platform.center_x = 0
        if self.platform.center_x > self.width:
            self.platform.center_x = self.width
        if self.ball.center_x < 0:
            self.ball.change_x =- self.ball.change_x
        if self.ball.center_x > self.width:
            self.ball.change_x = -self.ball.change_x
        if self.ball.center_y > self.height:
            self.ball.change_y = -self.ball.change_y
        if self.ball.center_y < 0:
            self.ball.change_y = -self.ball.change_y
            self.restart()

        platform1_collision = arcade.check_for_collision(self.platform, self.ball)

        if platform1_collision:
            self.ball.change_y =- self.ball.change_y
            self.ball.change_y = self.ball.change_y + self.platform.change_y / 2 + random.randint(-1, 1)
            self.score += 1


    def setup(self):
        self.ball = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png",
                                  center_x=self.height/2,
                                  center_y= 450,
                                  scale=0.3)

        self.platform = arcade.Sprite(":resources:images/tiles/bridgeA.png",
                                       center_x=self.width/2,
                                       center_y=120,
                                       angle=180)
        self.spriteList.append(self.ball)
        self.spriteList.append(self.platform)
        self.ball.change_y = -5
        self.ball.change_x = 3

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.platform.change_x = 4

        if symbol == arcade.key.A:
            self.platform.change_x = -4

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D or symbol == arcade.key.A:
            self.platform.change_x = 0

    def restart(self):
        self.platform.center_x = self.width/2
        self.ball.center_y = 450
        self.ball.center_x = self.height / 2
        self.score = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
   main()
