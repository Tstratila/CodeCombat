# Поймай Пендер Проклинательницу чтобы узнать её секреты.

while True:  # Пендер единственный друг на уровне, поэтому она всегда ближайшая.
    pender = hero.findNearest(hero.findFriends())

    if pender:
        # moveXY()  переместит тебя в место где была Пендер,
        # но она постоянно будет убегать при твоем приближении.
        # hero.moveXY(pender.pos.x, pender.pos.y)

        # move()  передвигает тебя лишь на шаг в единицу времени,
        # поэтому ты сможешь преследовать свою цель.
        hero.move(pender.pos)