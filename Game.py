import os
import sys
from time import sleep
from random import shuffle, randint

class enemy:
    def __init__(self, name, moves, hp, att, defense, stun, starthp):
        self.name = name
        self.moves = moves
        self.hp = hp
        self.att = att
        self.defense = defense
        self.stun = stun
        self.starthp = starthp

class player:
    def __init__(self, name, hp, items, att, defense, bucks, moves, enemies, currency, damageTaken, score):
        self.name = name
        self.hp = hp
        self.items = items
        self.att = att
        self.defense = defense
        self.bucks = bucks
        self.moves = moves
        self.enemies = enemies
        self.currency = currency
        self.damageTaken = damageTaken
        self.score = score

class item:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

TERM_WIDTH = 115
LINES_FROM_TOP = 5
DIFFICULTY = 1
HEAL_COST = 100
STAT_INCREASE_COST = 200
STUN_COST = 40
ENEMY_HP = 30
ENEMY_ATTACK = 20
ENEMY_DEFENSE = 20
PLAYER_START_STAT = 20
PLAYER_START_HP = 100
COINS = 65
BOSS_HP = 100
BOSS_STAT = 20
BOSS_HP2 = 200
BOSS_STAT2 = 25
MINION_HP = 75
MINION_STAT = 20
MULTIPLIER = 1.3
HIGH_SCORE = 0
HIGH_SCORE_OWNER = ""
MEDIUM = 1.2
HARD = 1.4
IMPOSSIBLE = 1.6
SCOREMULT = 1
MED_SCORE = 1.5
HARD_SCORE = 2
IMPOS_SCORE = 3

theGame1 =  " _______ _               _____                      "
theGame2 =  "|__   __| |             / ____|                     "
theGame3 =  "   | |  | |__   ___    | |  __  __ _ _ __ ___   ___ "
theGame4 =  "   | |  | '_ \ / _ \   | | |_ |/ _` | '_ ` _ \ / _ \\"
theGame5 =  "   | |  | | | |  __/   | |__| | (_| | | | | | |  __/"
theGame6 =  "   |_|  |_| |_|\___|    \_____|\__,_|_| |_| |_|\___|"

def printHeader(*args):
    os.system("clear")
    if (len(args)):
        health = args[0].hp
        score = args[0].score
        bucks = args[0].bucks
        currency = args[0].currency
    else:
        health = 100
        score = 0
        bucks = 0
        currency = "Bucks"
    spaces = TERM_WIDTH - len("High Score: ") - len(str(HIGH_SCORE)) - len(" - ") - len(HIGH_SCORE_OWNER) - len(str(health)) - len("Health: ") - len ("/100")
    print("High Score: " + str(HIGH_SCORE) + " - " + HIGH_SCORE_OWNER + " " * spaces + "Health: " + str(health) + "/100")
    header = [theGame1, theGame2, theGame3, theGame4, theGame5, theGame6]
    spaces = TERM_WIDTH - len("Score: ") - len(str(score)) - len(currency)- len(": ") - len(str(bucks))
    print("Score: " + str(score) + " " * spaces + currency + ": " + str(bucks))
    for line in header:
        print (line.center(TERM_WIDTH, " "))
    print("\n" * 2)

def pressEnter():
    print("\n")
    myPrint ("press ENTER to continue")
    input()

def getInput(*args):
    if (type(args[0]) == list):
        args = args[0]
    print ("\n" * 2)
    while (1):
        myPrint("Enter your choice: ", 1)
        c = input()
        if (c in args):
            return int(c)

def myPrint(*args):
    toPrint = args[0]
    if(len(args) == 1):
        newStr = toPrint.center(TERM_WIDTH, " ")
    else:
        howManyFiller = TERM_WIDTH//2 - len(toPrint)//2
        newStr = (" " * howManyFiller + toPrint)
    for char in newStr:
        print(char, end="")
        sys.stdout.flush()
        sleep(.01)

def giveItem(player):
    printHeader(player)
    myPrint("One more thing before you are off. What item would you like?")
    print('\n')
    myPrint("(1): Defense Potion (permanently increase defense)")
    myPrint("(2): Strength Potion (permanently increase strength)")
    res = getInput('1', '2')
    printHeader(player)
    if (res == 1):
        myPrint("Your Defense has increased.")
        player.defense += 5
    else:
        player.att += 5
        myPrint("Your Strength has increased.")
    print("\n")
    goodie = item("Heal Potion", "hp")
    player.items.append(goodie)
    myPrint("I'm feeling generous today. I'm gonna throw in a heal potion. Full heal in battle")
    print ("\n")
    myPrint("(1): Thanks!")
    myPrint("(2): Boo! I wanted more.")
    getInput('1', '2')
    printHeader(player)
    myPrint("Alright I think you are ready to get into the game! Good Luck!")
    pressEnter()

def titlescreen():
    os.system("clear")
    header = [theGame1, theGame2, theGame3, theGame4, theGame5, theGame6]
    print ("\n" * LINES_FROM_TOP)
    for line in header:
        toPrint = line.center(TERM_WIDTH, " ")
        print (toPrint)
        sleep(1)

    print ("\n" * 2)
    myPrint("Hello and welcome to the game. I'll be your narrator Jimmy.")
    pressEnter()
    printHeader()
    myPrint("All input in the game will be given my entering a number")
    print ("\n")
    myPrint("(1): Okay got it")
    myPrint("(2): I don't understand.")
    getInput('1', '2')

def shop(player):
    while(1):
        printHeader(player)
        myPrint("Wecome to the shop! Here you can buy cool items to use in battle!")
        print("\n")
        myPrint("You have " + str(player.bucks) + player.currency + ". What would you like to buy?")
        print ("\n")
        myPrint("(1): Heal Potion 100" + player.currency)
        myPrint("(2): Defense Potion (permanently increase defense) 200" + player.currency)
        myPrint("(3): Strength Potion (permanently increase strength) 200" + player.currency)
        myPrint("(4): Freeze Potion (freeze enemy and do damage for 1 move) 40" + player.currency)
        myPrint("(5): Damage Potion (permanently decrease enemy defense) 100" + player.currency)
        myPrint("(6): Go on to Next Battle")
        res = getInput('1','2','3', '4', '5', '6')
        if (res == 1):
            if (player.bucks < HEAL_COST):
                myPrint("You don't have enough for that")
                pressEnter()
                continue
            goodie = item("Heal Potion", "hp")
            player.bucks -= HEAL_COST
        elif (res == 2):
            if (player.bucks < STAT_INCREASE_COST):
                myPrint("You don't have enough for that")
                pressEnter()
                continue
            myPrint("Your defense has increased!")
            player.defense += 5
            goodie = 0
            player.bucks -= STAT_INCREASE_COST
        elif (res == 3):
            if (player.bucks < STAT_INCREASE_COST):
                myPrint("You don't have enough for that")
                pressEnter()
                continue
            myPrint("Your strength has increased!")
            player.att += 5
            goodie = 0
            player.bucks -= STAT_INCREASE_COST
        elif (res == 4):
            if (player.bucks < STUN_COST):
                myPrint("You don't have enough for that")
                pressEnter()
                continue
            goodie = item("Freeze Potion", "stun")
            player.bucks -= STUN_COST
        elif (res == 5):
            if (player.bucks < HEAL_COST):
                myPrint("You don't have enough for that")
                pressEnter()
                continue
            goodie = item("Damage Potion", "def")
            player.bucks -= HEAL_COST
        else:
            break
        try:
            myPrint(goodie.name + " has been added to your bag!")
            player.items.append(goodie)
        except:
            pass
        pressEnter()
        printHeader(player)
        myPrint("Would you like to keep shopping? You have " + str(player.bucks) + player.currency)
        print("\n")
        myPrint("(1): Yes!")
        myPrint("(2): No")
        res = getInput('1', '2')
        if (res == 1):
            continue
        break

def useItem(player):
    printHeader(player)
    myPrint("What item would you like to use?")
    print('\n')
    options = []
    for i in range(len(player.items)):
        myPrint("(" + str(i + 1) + "): " + player.items[i].name)
        options.append(str(i + 1))
    myPrint("(" + str(i + 2) + "): Nevermind I don't want to use an item!" )
    options.append(str(i + 2))
    res = getInput(options)
    if (res == i + 2):
        return 3
    stat = player.items[res - 1].stat
    del(player.items[res - 1])
    if (stat == "hp"):
        myPrint("You drinks the water, and fully heals!")
        player.hp = PLAYER_START_HP
        pressEnter()
    elif (stat == "stun"):
        return 1
    elif (stat == "def"):
        myPrint ("Enemy's defense has decreased!")
        return 2
    return 0

def enemyMove(player, e):
    printHeader(player)
    if (not e.stun):
        move = e.moves[randint(0,1)]
        lower = e.att - player.defense
        upper = e.att
        damage = randint(lower, upper)
        if (damage <= 0):
            damage = 1
        player.hp -= damage
        player.damageTaken += damage
        myPrint(e.name + " uses " + move + " which does " + str(damage) + " damage")
        myPrint("You now have " + str(player.hp) + " health")
        pressEnter()
    else:
        myPrint(e.name + " is frozen.")
        pressEnter()
        e.stun = 0
    if (player.hp <= 0):
        return 0
    return 1

def playerMove(player, e):
    while(1):
        printHeader(player)
        myPrint("What would you like to do?")
        print("\n")
        options = ['1', '2']
        move1 = player.moves[0]
        move2 = player.moves[1]
        myPrint("(1): " + move1)
        myPrint("(2): " + move2)
        if (len(player.items) > 0):
            myPrint("(3): Use item from bag")
            options.append('3')
        res = getInput(options)
        move = ""
        skipTurn = 0
        if (res == 1):
            move = move1
        elif (res == 2):
            move = move2
        else:
            res = useItem(player)
            if (res):
                if (res == 3):
                    continue
                if (res == 1):
                    e.stun = 1
                else:
                    e.defense -= 5
                    skipTurn = 1
            else:
                skipTurn = 1
        break
    if (skipTurn):
        return
    elif (not e.stun):
        lower = player.att - e.defense
        upper = player.att
        damage = randint(lower, upper)
        if (damage <= 0):
            damage = 1
        e.hp -= damage
        myPrint(move + " does " + str(damage) + " damage to " + e.name)
    else:
        damage = randint(8,15)
        myPrint("You use Freeze Potion which freezes " + e.name + " and does " + str(damage) + " damage")
        pressEnter()
        e.hp -= damage
    if (e.hp > 0):
        print("\n")
        myPrint(e.name + " now has " + str(e.hp) + " health")
        pressEnter()
        return 1
    else:
        if (e.name != "Dragon"):
            print ("\n")
            myPrint("Congrats! The wild " + e.name + " has been defeated")
            print ('\n')
            lower = COINS - 20
            upper = COINS + 20
            reward = randint(lower, upper)
            myPrint("You received " + str(reward) + player.currency)
            player.bucks += reward
            points = reward + e.starthp - player.damageTaken
            points *= SCOREMULT
            if (points <= 0):
                points = SCOREMULT
            player.score += int(points)
            player.damageTaken = 0
            print("\n")
            myPrint("You scored " + str(int(points)) + " points.")
            pressEnter()
            return 0
        return 0

def exitScreen(player):
    printHeader(player)
    myPrint("You lost. Way to suck at life.")
    print("\n" * 10)
    os.system("tput cnorm");
    sys.exit()

def battleTransition(player, e):
    order = randint(0,1)
    if (order == 0):
        res = playerMove(player, e)
        if (res == 1):
            res = enemyMove(player, e)
            if (res == 0):
                exitScreen(player)
    else:
        res = enemyMove(player, e)
        if (res == 1):
            playerMove(player, e)
        else:
            exitScreen(player)

def battle(player, i):
    printHeader(player)
    e = player.enemies[i]
    myPrint("You are approached by a wild " + e.name)
    pressEnter()
    while(e.hp > 0):
        battleTransition(player, e)

def doBattles(player):
    for i in range(6):
        printHeader(player)
        myPrint("What would you like to do?")
        print ("\n")
        myPrint("(1): Head into battle " + str(i + 1) + "/6")
        myPrint("(2): Go to the shop")
        res = getInput('1', '2')
        if (res == 1):
            battle(player, i)
        else:
            shop(player)
            battle(player, i)


def bossBattle1(player):
    printHeader(player)
    Dragon = enemy("Dragon", ["Fire Breath", "Tail Whip"], BOSS_HP, BOSS_STAT, BOSS_STAT, 0, BOSS_HP)
    myPrint("You are approached by a Dragon")
    print("\n")
    myPrint("Dragon: Whatever. Prepare to die.")
    pressEnter()
    flee = Dragon.hp/5
    Ally = 1
    stickyHP = PLAYER_START_HP/5
    while(Dragon.hp >= flee):
        if (player.hp <= stickyHP and Ally):
            printHeader(player)
            myPrint("Ally: Player you are looking a little low on health. Let me help you out")
            print("\n")
            myPrint("Ally tosses Damage Potion at Dragon.")
            print("\n")
            myPrint("The burn decreases Dragon's defense")
            pressEnter()
            Dragon.defense -= 5
            Ally = 0
        battleTransition(player, Dragon)
    printHeader(player)
    myPrint("Dragon: You are stronger than I had anticipated. I shall return")
    print("\n")
    prize = randint(130, 170)
    myPrint("Dragon has fled the battle. You receive " + str(prize) + player.currency)
    print("\n")
    points = prize + Dragon.starthp - player.damageTaken
    points *= SCOREMULT
    if (points <= 0):
        points = SCOREMULT
    myPrint("You scored " + str(int(points)) + " points.")
    player.score += points
    player.bucks += prize
    player.damageTaken = 0
    pressEnter()

def doBoss1(player):
    printHeader(player)
    myPrint("What would you like to do?")
    print("\n")
    myPrint("(1): Head into first boss battle")
    myPrint("(2): Go to the shop")
    res = getInput('1', '2')
    if (res == 1):
        bossBattle1(player)
    else:
        shop(player)
        bossBattle1(player)

def firstBossTransition(player):
    printHeader(player)
    myPrint("Good job! You defeated Dragon... Well sort of!")
    print("\n")
    myPrint("Are you ready to continue on?")
    print("\n")
    myPrint("(1): Heck yeah!")
    myPrint("(2): Nope.")
    res = getInput('1', '2')
    printHeader(player)
    if (res == 1):
        myPrint("Good! Here take this Strength Potion")
    else:
        myPrint("Well too bad! Here's a Strength potion")
    print("\n")
    myPrint("Your Strength has increased")
    pressEnter()

def bossBattle2(player):
    printHeader(player)
    Dragon = enemy("Dragon", ["Fire Breath", "Tail Whip"], BOSS_HP2, BOSS_STAT2, BOSS_STAT2, 0, BOSS_HP2)
    dragon1 = enemy("Dragon Baby 1", ["Fire Burn", "bite"], MINION_HP, MINION_STAT, MINION_STAT, 0, MINION_HP)
    dragon2 = enemy("Dragon Baby 2", ["Fire Burn", "bite"], MINION_HP, MINION_STAT, MINION_STAT, 0, MINION_HP)
    dragon3 = enemy("Dragon Baby 3", ["Fire Burn", "bite"], MINION_HP, MINION_STAT, MINION_STAT, 0, MINION_HP)
    dragon4 = enemy("Dragon Baby 4", ["Fire Burn", "bite"], MINION_HP, MINION_STAT, MINION_STAT, 0, MINION_HP)

    myPrint("Dragon: I'm back! With some friends this time.")
    print("\n")
    myPrint("(1): Absolutely no problem.")
    myPrint("(2): Can't handle it")
    res = getInput('1', '2')
    printHeader(player)
    myPrint("Dragon: Prepare to die")
    pressEnter()
    twoDays = [dragon1, dragon2, dragon3, dragon4]
    for e in twoDays:
        printHeader(player)
        myPrint("You are approached by a wild " + e.name)
        pressEnter()
        while(e.hp > 0):
            battleTransition(player, e)
    printHeader(player)
    myPrint("What would you like to do?")
    print("\n")
    myPrint("(1): Go to shop (last chance)")
    myPrint("(2): Take on Dragon like a boss")
    res = getInput('1','2')
    if (res == 1):
        shop(player)
    printHeader(player)
    myPrint("Dragon: Ugh. Do I have to do everything myself?")
    print("\n")
    myPrint("(1): Come and Get it")
    myPrint("(2): Let's do this")
    res = getInput('1', '2')
    printHeader(player)
    if (res == 1):
        myPrint("Dragon: Prepare to Die")
    else:
        myPrint("Dragon: Prepare for death.")
    pressEnter()
    printHeader(player)
    AllyHP = Dragon.hp/5
    while (Dragon.hp > AllyHP):
        battleTransition(player, Dragon)
    printHeader(player)
    myPrint("Dragon uses rip out heart, which completely drains your health.")
    myPrint("Dragon uses your heart to completely heal.")
    Dragon.hp = BOSS_HP2
    player.hp = 0
    print("\n")
    myPrint("Dragon: I told you that you couldn't win")
    pressEnter()
    printHeader(player)
    myPrint("Ally: Player I have a heal potion for you!")
    print("\n")
    myPrint("You drink the water and fully heal.")
    player.hp = PLAYER_START_HP
    pressEnter()
    printHeader(player)
    myPrint("Dragon: Ugh. Stupid Ally...")
    print("\n")
    myPrint("(1): Are you ready to end this?")
    myPrint("(2): Prepare to die.")
    res = getInput('1', '2')
    printHeader(player)
    if (res == 1):
        myPrint("Dragon: Time to die.")
    else:
        myPrint("Dragon: Prepare for death.")
    pressEnter()
    while (Dragon.hp > 0):
        battleTransition(player, Dragon)
    printHeader(player)
    myPrint("Congratulations! You have defeated the Dragon")
    print("\n")
    prize = randint(200, 250)
    myPrint("You recieve " + str(prize) + player.currency)
    print("\n")
    points = prize + Dragon.starthp - player.damageTaken
    points *= SCOREMULT
    if (points <= 0):
        points = SCOREMULT
    myPrint("You scored " + str(int(points)) + " points.")
    player.bucks += prize
    player.score += points
    player.damageTaken = 0
    pressEnter()


def doBoss2(player):
    printHeader(player)
    myPrint("What would you like to do?")
    print("\n")
    myPrint("(1): Head into second boss battle")
    myPrint("(2): Go to the shop")
    res = getInput('1', '2')
    if (res == 1):
        bossBattle2(player)
    else:
        shop(player)
        bossBattle2(player)

def farewell(player):
    printHeader(player)
    myPrint("Player you get to choose your final prize!!")
    print('\n')
    myPrint("(1): Apache Helicopter " + str(player.bucks) + player.currency)
    myPrint("(2): Harambe " + str(player.bucks) + player.currency)
    myPrint("(3): Memes " + str(player.bucks) + player.currency)
    res = getInput('1', '2', '3')
    printHeader(player)
    myPrint("Good choice!")
    print("\n")
    myPrint("You have completed the game. Your final score is " + str(player.score))
    pressEnter()

def makeNathan(mode):
    Goblin = enemy("Goblin", ["Stab", "Jab"], ENEMY_HP, ENEMY_ATTACK, ENEMY_DEFENSE, 0, ENEMY_HP)
    PettyThief = enemy("Petty Thief", ["Quick Blow", "Pickpocket"], ENEMY_HP, ENEMY_ATTACK, ENEMY_ATTACK, 0, ENEMY_HP)
    DarkKnight = enemy("Dark Knight", ["Low Kick", "Sword Slice"], ENEMY_HP, ENEMY_ATTACK, ENEMY_ATTACK, 0, ENEMY_HP)
    Goblin2 = enemy("Goblin", ["Stab", "Jab"], ENEMY_HP, ENEMY_ATTACK, ENEMY_DEFENSE, 0, ENEMY_HP)
    PettyThief2 = enemy("Petty Thief", ["Quick Blow", "Pickpocket"], ENEMY_HP, ENEMY_ATTACK, ENEMY_DEFENSE, 0, ENEMY_HP)
    DarkKnight2 = enemy("Dark Knight", ["Low Kick", "Sword Slice"], ENEMY_HP, ENEMY_ATTACK, ENEMY_DEFENSE, 0, ENEMY_HP)

    enemies = [Goblin, PettyThief, DarkKnight, Goblin2, PettyThief2, DarkKnight2]

    shuffle(enemies)

    if (mode == 1):
        moves = ["Sword Swing", "Ninja Chop"]
        currency = " Gold"
    elif (mode == 2):
        moves = ["Sword Swing", "Ninja Chop"]
        currency = " Silver"
    elif (mode == 3):
        moves = ["Sword Swing", "Ninja Chop"]
        currency = " Bronze"
    else:
        moves = ["Sword Swing", "Ninja Chop"]
        currency = " Nothingness"

    return player("Player", PLAYER_START_HP, [], PLAYER_START_STAT, PLAYER_START_STAT, 0, moves, enemies, currency, 0, 0)

def mode():
    global DIFFICULTY
    global SCOREMULT
    global ENEMY_HP
    global BOSS_HP
    global BOSS_HP2
    global MINION_HP
    printHeader()
    myPrint("Good! You get it!")
    print("\n")
    myPrint("What mode would you like to play on?")
    print("\n")
    myPrint("(1): Easy")
    myPrint("(2): Medium")
    myPrint("(3): Hard")
    myPrint("(4): Impossible")
    res = getInput('1', '2', '3', '4')
    printHeader()
    if (res == 1):
        pass
    elif (res == 2):
        DIFFICULTY = MEDIUM
        SCOREMULT = MED_SCORE
    elif (res == 3):
        DIFFICULTY = HARD
        SCOREMULT = HARD_SCORE
    else:
        DIFFICULTY = IMPOSSIBLE
        SCOREMULT = IMPOS_SCORE
    pressEnter()
    ENEMY_HP = int(ENEMY_HP * DIFFICULTY)
    BOSS_HP = int(BOSS_HP * DIFFICULTY)
    BOSS_HP2 = int(BOSS_HP2 * DIFFICULTY)
    MINION_HP = int(MINION_HP * DIFFICULTY)
    return res

def doScore(player):
    printHeader()
    myPrint("Congrats on the new high score of " + str(player.score) + "!")
    print("\n")
    myPrint("Enter your name: ", 1)
    name = input()
    os.system("rm score.txt")
    os.system("touch score.txt")
    f = open("score.txt", "r+")
    toWrite = str(player.score) + "\n" + name
    f.write(toWrite)
    f.close()
    pressEnter()

def main():
    global HIGH_SCORE
    global HIGH_SCORE_OWNER
    f = open("score.txt", "r+")
    HIGH_SCORE = int(f.readline().strip())
    HIGH_SCORE_OWNER = f.readline().strip()
    os.system('tput civis')
    titlescreen()
    m = mode()
    player = makeNathan(m)
    giveItem(player)
    doBattles(player)
    doBoss1(player)
    firstBossTransition(player)
    player.att += 5
    for e in player.enemies:
        e.hp = int(ENEMY_HP * MULTIPLIER)
    shuffle(player.enemies)
    doBattles(player)
    doBoss2(player)
    res = farewell(player)
    if (player.score > HIGH_SCORE):
        doScore(player)
    os.system("tput cnorm");

main()
