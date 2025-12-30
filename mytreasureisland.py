print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
""")

print("Welcome to Treasure Island.")
print("You're at a cross road. Where do you want to go?")
rule1 = input("---Type 'left' to walk LEFT or Type 'right' to Walk RIGHT---\n  ")

if rule1 =="left":
    print("You've come to a lake. There is an Island in the middle of the lake.")
    rule2 = input("Type 'wait' to WAIT for a boat. Type 'swim'to SWIM across.\n  ")
    if rule2 =="swim":
        print("You arrive at the island unharmed,Thanks to the Magic Guards. There is a house with 3 doors.")
        rule3 = input("One red, one yellow and one blue. Which colour do you choose?")
        if rule3 =="red":
            print("Burned by 🔥fire.")
            rule4 = input("do you want the magical lord skin recovering Treatment? y for YES and n for NO.\n  ")
            if rule4 =="y":
                print("Welcome back🤗, treasure Hunter.")
                rule6 = input("Dead End no way through, Type D to disappear or W to wait.\n  ")
                if rule6 =="D":
                    print("Luck you Hunter... You're out of the island...pass through the start Door again.")
                else:
                    print("\nGame over... The living Dead is Here.😂")
            else:
                print("\nGame Over🤪... No treatment...Start all over again.")
        elif rule3 =="yellow":
            print("Welcome to the Safe route player😀, No beast or Fire burner.")
            rule7 = input("Welcome to treasure store.. 'OPEN' or 'CLOSE' it.\n  ").upper()
            if rule7 =="OPEN":
                print("Sometimes open is just another way of saying close, and close is the first step to truly open")
                print("\nGame Over ... Hunter, thanks😁🙏 for reach this far.")
            else:
                print("\n When open feels like a wall and close feels like freedom, you realize words dont always mean what they say.")

                print("Congratulation..🎉🎉🤗 You Found the Treasure. ")
        else:
            print("\nEaten by beasts🐕.😂")
            print("Bad News.. No treatment, Game Over...Sorry Hunter.")
    else:
        print("\n📎Attacked⚔️ by trout🥷.Game Over.😂")
else:
    print("\n😁Fall into a hole..😂 GAME OVER !!")










