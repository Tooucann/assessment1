import game
import barbarian
import wizard

pickteam = int(input("Select if you want to be a swordsmen or a wizard. Type 1 into the terminal if you would like to be a swordsman, type 2 into the terminal if you would like to be a wizard"))

if pickteam == 1:
    print("You are a swordsman. goodluck on your journey")
    print("Welcome to the barbarians adventure. There will be 3 quests you must complete. You must roll a dice to gain attribute points. You must win each quest to complete the game.")
    print("GREAT! Lets start with the first attribute. Strength. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    print("This first quest will be for strength")
    strngthstat = print(game.display_message())
    strngthstatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    strengthnumber=0
    if strngthstatval==1:
        print("CRITICAL LOSS -1 STRENGTH",strengthnumber - 1)
    elif strngthstatval==2:
        print("LOSS NO POINTS REMOVED")
    elif strngthstatval==3:
        print("WIN NO POINTS ADDED")
    elif strngthstatval==4:
        print("CRITICAL WIN +1 Strength",strengthnumber + 1)
    else:
        print("INVALID INPUT")
        

        
        print(strengthnumber)
    int(input("Press any key to keep going"))
    print("Now time for the second quest. Health. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    healthstat = print(game.display_message())
    healthstatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    healthnumber=0
    if healthstatval==1:
        print("CRITICAL LOSS -1 HEALTH",healthnumber - 1)
    elif healthstatval==2:
        print("LOSS NO POINTS REMOVED")
    elif healthstatval==3:
        print("WIN NO POINTS ADDED")
    elif healthstatval==4:
        print("CRITICAL WIN +1 HEALTH",healthnumber + 1)
    else:
        print("INVALID INPUT")
    
        print(healthnumber)
    int(input("Press any key to keep going"))
    print("Now the final quest. The stat in this quest is IQ. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    iqstat = print(game.display_message())
    iqstatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    iqnumber=0
    if iqstatval==1:
        print("CRITICAL LOSS -1 HEALTH",iqnumber - 1)
    elif iqstatval==2:
        print("LOSS NO POINTS REMOVED")
    elif iqstatval==3:
        print("WIN NO POINTS ADDED")
    elif iqstatval==4:
        print("CRITICAL WIN +1 HEALTH",iqnumber + 1)
    else:
        print("INVALID INPUT")
        print(iqnumber)
    print("If any of the numbers are negative, you are an unworthy barbarian")
    print("If you had no negative values, you are a good barbaian")
elif pickteam ==2:
    print("You are a wizard. goodluck on your journey")
    print("Welcome to the wizards adventure. There will be 3 quests you must complete. You must roll a dice to gain attribute points. You must win each quest to complete the game.")
    print("GREAT! Lets start with the first attribute. mana. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    print("This first quest will be for strength")
    manastat = print(game.display_message())
    manastatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    mananumber=0
    if manastatval==1:
        print("CRITICAL LOSS -1 STRENGTH",mananumber - 1)
    elif manastatval==2:
        print("LOSS NO POINTS REMOVED")
    elif manastatval==3:
        print("WIN NO POINTS ADDED")
    elif manastatval==4:
        print("CRITICAL WIN +1 Strength",mananumber + 1)
    else:
        print("INVALID INPUT")
        

        
        print(mananumber)
    int(input("Press any key to keep going"))
    print("Now time for the second quest. wisdom. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    wisdomstat = print(game.display_message())
    wisdomstatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    wisdomnumber=0
    if wisdomstatval==1:
        print("CRITICAL LOSS -1 HEALTH",wisdomnumber - 1)
    elif wisdomstatval==2:
        print("LOSS NO POINTS REMOVED")
    elif wisdomstatval==3:
        print("WIN NO POINTS ADDED")
    elif wisdomstatval==4:
        print("CRITICAL WIN +1 HEALTH",wisdomnumber + 1)
    else:
        print("INVALID INPUT")
    
        print(wisdomnumber)
    int(input("Press any key to keep going"))
    print("Now the final quest. The stat in this quest is magicpower. You will roll the dice to see if you can increase or decrese the value. You will roll 1 dices. Critical Loss if you roll 1 challenge is lost and the attribute that is based on is decreased, if you rolled 2 challenge is lost, no change in the character’s attributes, if rolled 3 challenge is won, no change in the character’s attributes, Critical Win is when 4 is rolled and the challenge is won and the attribute that is based on increases. So lets begin.")
    magicpowerstat = print(game.display_message())
    magicpowerstatval=int(input("What number did you roll (IF YOU INPUT A NUMBER THAT ISNT 1-4 YOUR POINTS WILL STAY AT 0 AND THE GAME CONTINUES)"))
    magicpowernumber=0
    if magicpowerstatval==1:
        print("CRITICAL LOSS -1 HEALTH",magicpowernumber - 1)
    elif magicpowerstatval==2:
        print("LOSS NO POINTS REMOVED")
    elif magicpowerstatval==3:
        print("WIN NO POINTS ADDED")
    elif magicpowerstatval==4:
        print("CRITICAL WIN +1 HEALTH",magicpowernumber + 1)
    else:
        print("INVALID INPUT")
        print(magicpowernumber)
    print("If any of the numbers are negative, you are an unworthy barbarian")
    print("If you had no negative values, you are a good barbaian")