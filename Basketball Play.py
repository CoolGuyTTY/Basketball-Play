from gamelib import*
#variables
game = Game(800,600,"Basketball Play")#game variable
bk = Image("gym.jpg",game)

bk.resizeTo(800,600)
bk.draw()
game.update()

kyrie = Image("kyrie.png",game)
kyrie.resizeBy(-47)
kyrie.setSpeed(7,125)
kobe = Image("kobe.png",game)
kobe.resizeBy(-58)
kobe.setSpeed(7,50)
basket = Image("basket.png",game)
basket.resizeBy(-50)
basket.setSpeed(5,60)
ball = Image("ball.png",game)
ball.resizeBy(-66)

#essential game loop
while not game.over:
    game.processInput()
    bk.draw()
    kyrie.move(True)
    kobe.move(True)
    basket.move(True)
    ball.draw()
    ball.moveTo(mouse.x,mouse.y)
    game.update(30)

game.quit()
