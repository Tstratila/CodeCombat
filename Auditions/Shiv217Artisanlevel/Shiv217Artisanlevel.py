# http://codecombat.com/play/level/shiv217-artisanlevel
summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (hero.health < hero.maxHealth * 0.6):
            target = self
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        hero.command(paladin, "shield")
    else:
        target = hero.findNearestEnemy()
        hero.command(paladin, "attack", target)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        elif (hero.isReady("attack")):
            hero.attack(target)
        else:
            pass

while True:
    flag = hero.findFlag()
    summonTroops()
    commandTroops()
    if flag:
        hero.pickUpFlag(flag)
    else:
        enemy = hero.findNearestEnemy()
        if enemy:
            attack(enemy)
            # find some enemy to attack
            # use cleave when ready
