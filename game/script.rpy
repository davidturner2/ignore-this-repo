# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("profesor")
image moon = "Professor.jpg"
image bg = "bg.png"
image sss = "mc.png"

define mc = Character("mc", who_color="#1b2fe2")

define yes = Character("Shadow The Hedgehog", who_color="#000000")

define moon2 = Character("profesor", what_textshader="wave:10")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show moon

    # These display lines of dialogue.
    play sound "fmc.mp3"
    e "See me after class sweetie"
    play sound "fmc.mp3"
    moon2 "are you ready to have {shader=jitter}babies with me?{/shader}" 

    # This ends the game.
menu:
    mc "What should I do?"
    "Impregnante (you must be 18+ to see the following scene)":
        play sound "mc.mp3"
        show moon:        
            xalign 0.5
            linear 1 xalign 1.0
        show sss:        
            offscreenleft
            easein_elastic 3 xalign 0.0
        yes "SORRY YOU HAVE TO PAY $9,000,000,000,000,000,000,000 SUBSCRIPTION TO THE PATREON TO SEE THIS SCENE"
        

    "GET THE HECK OUT!!!":
        play sound "fmc.mp3"
        e "ara ara is your face red and blushing for me"
        play sound "mc.mp3"
        show moon:        
            xalign 0.5
            linear 1 xalign 1.0
        show sss:        
            offscreenleft
            linear 1 xalign 0.0
        yes "TO PLAY THE REST OF THE GAME WITH UNCENSORED SCENES SUBSCRIBE TO THE PATREON FOR $9,000,000,000,000,000,000,000"
label after_menu:
    play sound "fmc.mp3"
    e "FRICK YOU"
    return
