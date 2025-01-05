# Zach Bernas and Mariel King
# gjv6js and uhy6sa

# How to Play:
# Press space to start, arrow keys to move around, and 'f' key to pass. Avoid the defenders and pass to the receiver in
# a white uniform. Good luck!

# Imports
import uvage
import random

# Global Variables
camera = uvage.Camera(800, 600)
health = 3
game_on = False
startscreen = True
level = 0
score = 0
ball_passed = False
coin_collected = False

# Main Gameboxes
hearts = [uvage.from_image(20, 550, 'fullheart.png'), uvage.from_image(50, 550, 'fullheart.png'),
          uvage.from_image(80, 550, 'fullheart.png')]
player = uvage.from_image(400, 550, 'player.png')
logo1 = uvage.from_image(500, 450, 'gamelogo1.png')
logo2 = uvage.from_image(400, 400, 'gamelogo2.png')
text1 = uvage.from_text(400, 100, 'ULTIMATE Football Game', 50, 'black', bold=True)
text2 = uvage.from_text(400, 150, 'Press \'Space\' to start', 40, 'light blue', bold=False)
sidelines = [uvage.from_color(20, 300, 'white', 20, 800),
             uvage.from_color(780, 300, 'white', 20, 800),
             uvage.from_color(400, 450, 'dark blue', 740, 5),
             uvage.from_color(400, 600, 'dark green', 800, 5)]
defender1 = uvage.from_image(400, 150, 'defender1.png')
defender2 = uvage.from_image(-100, 200, 'defender1.png')
defender3 = uvage.from_image(-100,250, "defender1.png")
receiver = uvage.from_image(400, 80, 'receiver.png')
footballfield = uvage.from_image(400, 700, 'footballfield.png')
try_again = uvage.from_text(400, 200, '-1 Heart - Press \'Space\' to try again.', 50, 'red', bold=True)
interception = uvage.from_text(400, 100, "INTERCEPTION!", 60, "red",bold=True)
gmovr = uvage.from_text(400, 300, 'Game Over. Press \'Space\' to try again.', 50, 'red', bold=True)
ball = uvage.from_image(1000, -1000, 'ball.png')
coinx = random.randint(50, 550)
# Scale Functions
logo1.scale_by(1)
logo2.scale_by(.75)
footballfield.scale_by(3.2)
footballfield.rotate(90)
player.scale_by(1.5)
defender1.scale_by(1.5)
defender2.scale_by(1.5)
defender3.scale_by(1.5)
receiver.scale_by(1.25)

defender1.speedx = 3
receiver.speedx = -3
defender2.speedx = 5
defender3.speedx = 3



# Main Function ---------------------
def tick():
    global health
    global game_on
    global startscreen
    global level
    global ball_passed
    global coin_collected
    camera.clear('dark green')

    # Start Screen
    if not game_on and startscreen and health == 3:
        camera.draw(logo1)
        camera.draw(logo2)
        camera.draw(text1)
        camera.draw(text2)
    if uvage.is_pressing('space') and startscreen:
        game_on = True
        startscreen = False
        level += 1


    # Hearts Code
    _hearts = [uvage.from_image(50, 550, 'fullheart.png'), uvage.from_image(80, 550, 'fullheart.png'),
               uvage.from_image(110, 550, 'fullheart.png')]


    # Coin Spawning
    coin = uvage.from_image(coinx, 15, 'coin.png')
    coin.scale_by(1.25)


    # Passing Function
    if game_on:
        if uvage.is_pressing('f') and not startscreen and game_on:
            ball_passed = True
        if ball_passed is True:
            if ball.y < -100:
                ball.x = player.x
                ball.y = player.y
            ball.speedy = -15
            ball.move_speed()
        if ball.y <= -100:
            ball_passed = False
        if ball.touches(coin):
            coin_collected = True
        if ball.touches(receiver):
            level += 1
            ball_passed = False
            ball.y = -200
        elif ball.touches(defender1) or ball.touches(defender2) or ball.touches(defender3):
            ball.y = -100
            ball.x = -100
            ball.move_to_stop_overlapping(defender1)
            ball.move_to_stop_overlapping(defender2)
            ball.move_to_stop_overlapping(defender3)
            health -= 1
            game_on = False

    # Game Over Function
    if game_on is False and startscreen is False and health > 0:
        camera.draw(try_again)
        camera.draw(interception)
        if uvage.is_pressing('space'):
            game_on = True
    elif game_on is False and startscreen is False and health <= 0:
        camera.draw(gmovr)
        if uvage.is_pressing('space'):
            game_on = True
            level = 1
            health = 3
            coin_collected = False
            defender2.x = -100
            defender3.x = -100
            defender1.speedx = 3
            defender2.speedx = 5
            defender3.speedx = 3
            receiver.speedx = -3




    # Level Up Function
    if game_on:
        camera.draw(footballfield)
        if level == 2:

            if coin_collected is False:
                camera.draw(coin)
            if defender1.speedx < 0:
                defender1.speedx = -5
            else:
                defender1.speedx = 5
            if receiver.speedx < 0:
                receiver.speedx = -5
            else:
                receiver.speedx = 5
        elif level == 3:
            if defender1.speedx < 0:
                defender1.speedx = -6
            else:
                defender1.speedx = 6
            if receiver.speedx < 0:
                receiver.speedx = -5
            else:
                receiver.speedx = 5
        elif level == 4:
            if defender1.speedx < 0:
                defender1.speedx = -7
            else:
                defender1.speedx = 7
            if receiver.speedx < 0:
                receiver.speedx = -6
            else:
                receiver.speedx = 6
            camera.draw(defender2)
            defender2.move_speed()
            if defender2.x == -100:
                defender2.x = 100
        elif level == 5:
            if defender1.speedx < 0:
                defender1.speedx = -8
            else:
                defender1.speedx = 8

            if receiver.speedx < 0:
                receiver.speedx = -6
            else:
                receiver.speedx = 6
            camera.draw(defender2)
            if defender2.speedx < 0:
                defender2.speedx = -7
            else:
                defender2.speedx = 7
            defender2.move_speed()
            camera.draw(defender3)
            if defender3.speedx < 0:
                defender3.speedx = -3
            else:
                defender3.speedx = 3
            defender3.move_speed()
            if defender3.x < -100:
                defender3.x = 500
        elif level > 5:
            if defender1.speedx < 0:
                defender1.speedx = -level - 5
            else:
                defender1.speedx = level + 5

            if receiver.speedx < 0:
                receiver.speedx = -7
            else:
                receiver.speedx = 7
            camera.draw(defender2)
            if defender2.speedx < 0:
                defender2.speedx = -(level + 7)
            else:
                defender2.speedx = level + 7
            defender2.move_speed()
            camera.draw(defender3)
            if defender3.speedx < 0:
                defender3.speedx = -3
            else:
                defender3.speedx = 3
            defender3.move_speed()

    # Player Movement
    if game_on and coin_collected is False:
        if uvage.is_pressing('up arrow'):
            player.move(0, -5)
        if uvage.is_pressing('left arrow'):
            player.move(-5, 0)
        if uvage.is_pressing('right arrow'):
            player.move(5, 0)
        if uvage.is_pressing('down arrow'):
            player.move(0, 5)
    elif game_on and coin_collected:
        if uvage.is_pressing('up arrow'):
            player.move(0, -7)
        if uvage.is_pressing('left arrow'):
            player.move(-7, 0)
        if uvage.is_pressing('right arrow'):
            player.move(8, 0)
        if uvage.is_pressing('down arrow'):
            player.move(0, 8)


    # Collision
    if game_on:
        for side in sidelines:
            if player.touches(side):
                player.move_to_stop_overlapping(side)
            if defender1.touches(side):
                defender1.speedx *= -1
                defender1.move_to_stop_overlapping(side)
            if receiver.touches(side):
                receiver.speedx *= -1
            if defender2.touches(side):
                defender2.speedx *= -1
                defender2.move_to_stop_overlapping(side)
            if defender3.touches(side):
                defender3.speedx *= -1
                defender3.move_to_stop_overlapping(side)


    # Main Drawings
    if game_on:
        for x in sidelines:
            camera.draw(x)
        camera.draw(defender1)
        defender1.move_speed()
        camera.draw(receiver)
        receiver.move_speed()
        camera.draw(ball)

        # Draw Player LAST
        camera.draw(player)
        level_count = uvage.from_text(700, 550, 'Level: ' + str(level), 30, 'black', bold=False)
        camera.draw(level_count)
        for heart in _hearts:
            if health == 3:
                camera.draw(heart)
            if health == 2:
                _hearts[2] = uvage.from_image(110, 550, 'emptyheart.png')
                camera.draw(heart)
            if health == 1:
                _hearts[2] = uvage.from_image(110, 550, 'emptyheart.png')
                _hearts[1] = uvage.from_image(80, 550, 'emptyheart.png')
                camera.draw(heart)
            if health <= 0:
                game_on = False



    camera.display()


uvage.timer_loop(60, tick)
