"""Dragon Mountain - a text-based adventure game to hunt a dragon for
treasure"""
# import the time and random functions
import time
import random


# define print pause to schedule delays in messages
def print_pause(message, wait_time):
    """Allows for pauses in messages to build up the story"""
    print(message)
    time.sleep(wait_time)


# define the intro sequence for the game
def intro():
    """Intro text - shows choice selection is in brackets and provides a
    story beginning"""
    print_pause("PLEASE NOTE: GAME CHOICE RESPONSES WILL BE GIVEN IN "
                "(BRACKETS)\n", 4)
    print_pause("You have been walking for several days and finally you "
                "arrive!\n", 2)
    print_pause("Toledo! The town you have been looking for since you heard a"
                " rumor about a Dragon guarding a large treasure trove.\n", 2)
    print_pause("You look for the library to do some research and speak to "
                "the local residence about what you have heard about the "
                "Dragon.\n", 1)
    print_pause("People whisper quietly about a mountain cave they have heard"
                " exists nearby where the Dragon may be.", 2)
    print_pause("They also speak about the adventurers whom have come before "
                "you and were never seen again!\n", 2)
    print_pause("You stay for a few days preparing, after which you head out "
                "of town.\n", 1)
    print_pause("You come to a fork in the road.\n", 1)


# define the first round of choices - fork in the road
def first_round():
    """This is the first choice in the game - fork in the road"""
    while True:
        choice = input("Would you like to go (left) or (right)?").lower()
        if choice in ['left', 'right']:
            break
        print("Invalid choice. Please enter 'left' or 'right'.")
    if choice == 'right':
        print_pause("You turn to the right and wander along a field.", 2)
        print_pause("Eventually you arrive at the base of a large "
                    "mountain.", 1)
        print_pause("It looks like it could be the one that people were "
                    "telling you about.\n", 2)
    # run mountain function - choose to climb the mountain or keep walking
        mountain()
    elif choice == 'left':
        print_pause("You turn to the left and wander up the trail and "
                    "come to another fork in the road.", 1)
        print_pause("The path on the left or a bridge to the right.\n", 2)
    # run bridge function - choose to continue on the path or cross the bridge
        bridge_func()


# define option 1 second round choices - keep walking/mountain climb
def mountain():
    """This function allows you to continue on the path or cross the bridge"""
    while True:
        climb = input("Do you climb the (mountain) or do you keep (walking)?"
                      ).lower()
        if climb in ['mountain', 'walking']:
            break
        print("Invalid choice. Please enter 'mountain' or 'walking'.")
    if climb == 'mountain':
        print_pause("You begin ascending the mountain, picking your way "
                    "carefully.", 2)
        print_pause("You see a small crack in the side of the mountain "
                    "that you think you can slip into.", 2)
        print_pause("You start to feel warm air coming from within and "
                    "you start getting very excited and nervous!", 1)
        print_pause("You follow the crack deep into the mountain and "
                    "start to notice a golden glow and that the air is "
                    "getting even warmer...\n", 3)
        print_pause("You come to a small ledge and see a large cavern "
                    "below you and a large pile of gold!", 1)
        print_pause("At the same time you see an ENORMOUS Red Dragon "
                    "sleeping on the gold!!!\n", 2)
    # run dragon function to sneak or rush the dragon
        dragon_func()
    elif climb == 'walking':
        print_pause("After a few days you run into another traveller who "
                    "tells you that the mountain range comes to an end "
                    "further down the road...\n", 2)
    # run tricky choice function - give up or go back to the mountain
        tricky_choice()


# define mountain2 function - no choice to keep walking just climb
def mountain2():
    """This function only allows you to climb the mountain"""
    print_pause("You begin ascending the mountain, picking your way "
                "carefully.", 2)
    print_pause("You see a small crack in the side of the mountain that "
                "you think you can slip into", 2)
    print_pause("You start to feel warm air coming from within and you "
                "start getting very excited and nervous!", 1)
    print_pause("You follow the crack deep into the mountain and start "
                "to notice a golden glow and that the air is getting even"
                " warmer...\n", 3)
    print_pause("You come to a small ledge and see a large cavern below "
                "you and a large pile of gold!", 1)
    print_pause("At the same time you see an ENORMOUS Red Dragon sleeping"
                " on the gold!!!\n", 2)
    # run dragon function to decide whether to sneak or rush the dragon
    dragon_func()


# define option 2 second round choices - path/bridge option
def bridge_func():
    """This function provides two choices - to continue on the path or
    cross the bridge"""
    while True:
        bridge = input("Do you continue on the (path) or cross the (bridge)?"
                       ).lower()
        if bridge in ['path', 'bridge']:
            break
        print("Invalid choice. Please enter 'path' or 'bridge'.")
    if bridge == 'path':
        print_pause("Eventually you come across another traveller, whom "
                    "you ask about the Dragon.\n", 2)
        print_pause("The traveller is shocked!", 1)
        print_pause("He then yells 'I can't believe it! I am looking for "
                    "the Dragon and the gold as well!!", 2)
        print_pause("He then asks 'Would you like to look together?'.", 1)
        print_pause("He then adds 'I think you may be going the wrong way"
                    " too. I believe you were meant to cross the bridge "
                    "back down the way you came...\n", 2)
# run tricky choice2 function - provides the option to trust the traveller
# or keep walking
        tricky_choice2()
    elif bridge == 'bridge':
        # This option has a random component to decide whether you are
        # attacked or cross the bridge with no issue
        option1 = "A robber jumps out and surprises you!"
        option2 = "Nothing happens and you cross without any issue."
        outcome = random.choice([option1, option2])
        print_pause("You are a little nervous and have a funny feeling..."
                    "\n", 2)
        print_pause(outcome, 1)
        if outcome == option1:
            robber = input("Do you stay and (fight) or (run)").lower()
            if robber == 'fight':
                opt1 = "You are defeated.\n"
                opt2 = "You are victorious!\n"
                robber_outcome = random.choice([opt1, opt2])
                print_pause("You are preparing yourself for a battle.", 1)
                print_pause("You come together in a meeting of swords and"
                            " everything happens so quickly.\n", 1)
                print_pause(robber_outcome, 2)
                if robber_outcome == opt1:
                    print_pause("Unfortunately the game is over...", 2)
                    return
                elif robber_outcome == opt2:
                    print_pause("You are sweaty and sore but are ready to "
                                "continue!", 2)
                    print_pause("You keep walking and eventually come to "
                                "the base of a big mountain which looks "
                                "like it could be the one you were looking"
                                " for", 1)
                    print_pause("You start to climb.\n", 2)
# run mountain2 function - provides no option but to climb the mountain
                    mountain2()
            elif robber == 'run':
                print_pause("You have successfully escaped!\n", 2)
                print_pause("You continue walking and eventually come to "
                            "the base of a big mountain which looks like "
                            "it could be the one you were looking for", 1)
                print_pause("You start to climb.\n", 2)
# run mountain2 function - provides no option but to climb the mountain
                mountain2()
        else:
            print_pause("You continue walking and eventually come to the "
                        "base of a big mountain which looks like it could"
                        " be the one you were looking for", 1)
            print_pause("You start to climb.\n", 2)
# run mountain2 function - provides no option but to climb the mountain
            mountain2()


# define bridge2 function - no choice to keep walking just cross the bridge
def bridge2():
    """This function only allows you to cross the bridge"""
    option1 = "A robber jumps out and surprises you!"
    option2 = "Nothing happens and you cross without any issue.\n"
    outcome = random.choice([option1, option2])
    print_pause("You are a little nervous and have a funny feeling..."
                "\n", 2)
    print_pause(outcome, 1)
    if outcome == option1:
        robber = input("Do you stay and (fight) or (run)").lower()
        if robber == 'fight':
            opt1 = "You are defeated."
            opt2 = "You are victorious!"
            robber_outcome = random.choice([opt1, opt2])
            print_pause("You are preparing yourself for a battle.", 1)
            print_pause("You come together and a meeting of swords and "
                        "everything happens so quickly.", 1)
            print_pause(robber_outcome, 2)
            if robber_outcome == opt1:
                print_pause("Unfortunately the game is over...", 2)
                return
            elif robber_outcome == opt2:
                print_pause("You are sweaty and sore but are ready to "
                            "continue!", 2)
                print_pause("You keep walking and eventually come to the "
                            "base of the mountain which looks like it could "
                            "be the one.\n", 1)
                print_pause("You start to climb.\n", 2)
    # run mountain2 function - provides no option but to climb the mountain
                mountain2()
        elif robber == 'run':
            print_pause("You have successfully escaped!\n", 2)
            print_pause("You keep walking and eventually come to the "
                        "base of the mountain which looks like it could "
                        "be the one.\n", 1)
            print_pause("You start to climb.\n", 2)
    # run mountain2 function - provides no option but to climb the mountain
            mountain2()
    else:
        print_pause("You keep walking and eventually come to the "
                    "base of the mountain which looks like it could "
                    "be the one.\n", 1)
        print_pause("You start to climb.\n", 2)
    # run mountain2 function - provides no option but to climb the mountain
        mountain2()


# define option 1 third round choices - dragon
def dragon_func():
    """This function allows the user to decide whether to sneak or rush the
    dragon"""
    while True:
        dragon = input("Do you want to (sneak) around and try to attack it "
                       "from behind or (rush) it head on and try to surprise "
                       "it?").lower()
        if dragon in ['sneak', 'rush']:
            break
        print("Invalid choice. Please enter 'sneak' or 'rush'.")
    if dragon == 'sneak':
        print_pause("You manage to get around behind the Dragon and sneak"
                    " close enough to be able to attack!\n", 4)
        print_pause("You successfully slay the Dragon!!!\n", 1)
        print_pause("Now you get your pick of the gold!! HURRAY!!\n", 2)
        return
    elif dragon == 'rush':
        situ1 = "The Dragon wakes and burns you to a crisp with a blast of " \
                "fire!!\n"
        situ2 = "The Dragon is startled and you attack!!\n"
        dragon_outcome = random.choice([situ1, situ2])
        print_pause("You run full speed at the Dragon...\n", 2)
        print_pause(dragon_outcome, 2)
        if dragon_outcome == situ1:
            print_pause("Unfortunately the game is over...\n", 2)
            return
        if dragon_outcome == situ2:
            print_pause("A battle ensues and you fight hard but you just "
                        "can not beat the Dragon and are defeated...", 2)
            return


# define option 2 third round choices - give up/go back
def tricky_choice():
    """This function allows the user to decide whether to give up or go back"""
    while True:
        journey = input("Do you decide to turn around and go (back) to what "
                        "you think is the mountain or do you give up and "
                        "(travel) on to the next city?").lower()
        if journey in ['back', 'travel']:
            break
        print("Invalid choice. Please enter 'back' or 'travel'.")
    if journey == 'back':
        print_pause("You turn around and begin travelling back to the "
                    "base of the large mountain you previously thought "
                    "may be the right one...", 1)
# run mountain2 function - provides no option but to climb the mountain
        mountain2()
    elif journey == 'travel':
        print_pause("You throw in the towel and decide to look for another"
                    " adventure else where...\n", 2)
        return


# define option 3 third round choices - turn around/continue walking
def tricky_choice2():
    """This function allows the user to decide whether to turn around or
    continue walking"""
    while True:
        hard_choice = input("Do you trust the traveller and (turn) around to "
                            "keep the journey going or would you like to "
                            "(continue) on the path you are travelling?"
                            ).lower()
        if hard_choice in ['turn', 'continue']:
            break
        print("Invalid choice. Please enter 'turn' or 'continue'.")
    if hard_choice == 'turn':
        print_pause("I am SO glad that I ran into you! Let us go and find "
                    "this Dragon and all the treasure!!!", 1)
        print_pause("You turn around and travel off together talking about"
                    " the exciting adventure you are going to have "
                    "together!\n", 2)
        print_pause("Eventually you arrive back at the bridge you went past "
                    "earlier which leads to the base of a large mountain."
                    "\n", 1)
        print_pause("It looks like it could be the one that people were "
                    "telling you about and your companion agrees.\n", 2)
        print_pause("But first you have to cross the bridge.\n", 1)
# run the bridge2 function which is the option that has no choice
        bridge2()
    elif hard_choice == 'continue':
        print_pause("You decide that you don't totally trust the traveller"
                    " and decide to continue in the direction you have "
                    "been going.\n", 3)
        print_pause("After a couple of days you begin to notice that you "
                    "are actually slowly arcing back towards Toledo.", 1)
        print_pause("Aarrrrr, Damn! Now what?\n", 2)
# run the to quit function allowing the play the quit or continue
        to_quit()


# define fourth round choice - to quit or not to quit
def to_quit():
    """This function allows the user to decide whether to quit or continue"""
    while True:
        quit_continue = input("Do you still want to continue the (adventure) "
                              "or give the (dream) away?").lower()
        if quit_continue in ['adventure', 'dream']:
            break
        print("Invalid choice. Please enter 'adventure' or 'dream'.")
    if quit_continue == 'adventure':
        print_pause("There is no way I am quitting that easy!\n", 1)
        print_pause("You turn around and start the trip back to where you "
                    "came from... Slightly frustrated but still excited!", 3)
        print_pause("You finally get back to the bridge after a few days "
                    "and are ready to cross.\n", 2)
# run the bridge2 function which is the option that has no choice
        bridge2()
    elif quit_continue == 'dream':
        print_pause("It has been a fun adventure, even if you didn't find"
                    " the Dragon.\n", 1)
        print_pause("You continue on towards Toledo to rest up and plan "
                    "your next move...\n", 2)
        return


def play_again():
    """Prompts the player to play again and returns whether to continue."""
    while True:
        replay = input("Do you want to play again? (Y / N): ").lower()
        if replay == 'y':
            print_pause("Excellent! Restarting the game ...\n", 1)
            return True
        elif replay == 'n':
            print_pause("Thanks for playing!", 1)
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def dragon_mountain():
    """Defines the function to run the game"""
    intro()
    first_round()


while True:
    dragon_mountain()
    if not play_again():
        break
# End-of-file (EOF)
