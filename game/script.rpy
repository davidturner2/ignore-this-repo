# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("professor")
image moon = "professor.png"
image class = "bg.png"
image sss = "mc.png"



image antat = "watchingandrew.jpg"
image tt = "title.jpg"
image idkk = "idk.png"

image campus = "campus.png"
image sab = "easteregg.png"
image oof = "foo.png"
image math = "mathteacher.png"
image nerdy = "nerd.png"
image nerdate = "nerd date.png"
image date1 = "date1.png"
image daddy = "rizz.png"





define mc = Character("[name]", who_color="#1b2fe2",what_prefix="{cps=25}",what_suffix="{/cps}")

define yes = Character("Shadow The Hedgehog", what_prefix="{cps=25}",who_color="#000000")

define e2 = Character("profesor", what_prefix="{cps=25}",what_textshader="wave:10")
define mathteacher = Character("wattew",what_prefix="{cps=25}",who_color="#fff200",who_outlines=[( 1, "#000000", 0, 0 )] )
define nerd = Character("nerd girl",what_prefix="{cps=25}",who_color="#ff0011" )
define rizz = Character("Daddy Rizz",what_prefix="{cps=25}",who_color="#000000" )
#define rizz = Character("Daddy Rizz",who_color="#000000" )
define at = Character("Andrew Tate", who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )], window_background=None)

 
# The game starts here.
default name = "Andrew"

label start:
    #play sound "fmc.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #moon2 "are you ready to have {shader=jitter}babies with me?{/shader}" 
    screen button_example():
        frame:
            xalign 0.5 ypos 50
            button:
                action Notify("You clicked the button.")
                text "Click me." style "button_text"
    call screen button_example
    window hide dissolve

    pause 1.0

    scene antat:
        zoom 0.6
        yalign 0.6
        xalign 0.5
        linear 2 yalign 0.0

    pause 1.0



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    at "{cps=25}Men in this society have it hard... {w}like my reproductive organ."    
 


    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Sabah"
    mc "What is my life? I have no girlfriends, no ps5, no maidens... and I'm gonna die alone. "
    rizz "Not if I can help it!"
    show daddy:
        offscreenleft
        easein_elastic 3 xalign 0.0
    mc "What the—who the heck are you"
    rizz "They call me Daddy Rizz... and I’m your grandpapa."
    mc "A ghost? For real? "
    rizz "Damn right I am. My mission: to get you laid, Sonny Boy."
    mc "Wait... seriously?! I mean, thanks, bra. "
    rizz "Yeah, but step one: take a shower. You smell like straight booty cheeks." 
    mc "Okay, Daddy Rizz." 
    # This ends the game.
label shower:   
    menu:
        mc "What should I do?"
        "Take a shower":
            jump label_name
        "try to sneak out again":
            rizz "YOU NEED TO TAKE A SHOWER. You smell like straight booty cheeks."
            jump shower


label label_name:
    scene title
    with Dissolve(3.5)
    "THIS IS A PG GAME. MAKE SURE YOU'RE PARENT IS WITH YOU." 
    "WATCHING YOU PLAY THIS IN CASE YOU SEE ANYTHING REMOTELY SEXUAL. {w}YOUR PARENT SHOULD BE THERE TO COVER YOUR EYES!"
    scene campus
    with Dissolve(.5)
    show daddy:
        offscreenleft
        easein_elastic 3 xalign 0.0
    rizz "Ah, spring. The scent of new beginnings. A perfect time for love."
    mc "I thought that last semester... "
    rizz "Yeah, but this time you’ve got me, baby boy. Now get to class—I need to see what I’m working with."
    mc "Wait, can other people see you?"
    rizz "Nah, I’m your personal wingman. Think of me as your rizzing subconscious—now class first. Chop-chop."
    scene class
    with Dissolve(.5)
    show math:        
        yalign 0.0
        linear 0.5 yalign 0.4
        linear 0.5 yalign 0.0
        repeat
    mathteacher "Okay, welcome back, nerds. I know most professors make you introduce yourselves, but I don't care. Y’all can awkwardly mingle on your own time. Today, I'm talking about processing."
    rizz "We’re skipping this, cause its boring. I mean it's a game design class. back in my day the we game we was at the club getting girls getting maidens."
    mathteacher "Thats it for today. Bye "
    show math:        
        yalign 0.0
        linear 1 offscreenleft
    mc "choose interaction or work \"WIP\""
    show nerdy
    with Dissolve(.5)
    nerd "hey [name]! Is your shirt the same blue as Sonic in Sonic Adventure? "
    rizz "Say yes. We’ve hooked a nerd."
menu:
    mc "What should I do?"
    "minigame 13+ (pg13 minigame requires parental guidance)":
        play sound "mc.mp3"
        show nerdy:        
            xalign 0.5
            linear 1 xalign 1.0
        show sss:        
            offscreenleft
            easein_elastic 3 xalign 0.0
        yes "SORRY YOU HAVE TO PAY $9,000,000,000,000,000,000,000 SUBSCRIPTION TO THE PATREON TO PLAY THE FULL RELEASE"
        

    "um yes":
        nerd "ara ara is your face red and blushing for me. come here let me give you a hug. "
        play sound "mc.mp3"
        show nerdy:        
            xalign 0.5
            linear 1 xalign 1.0
        show sss:        
            offscreenleft
            linear 1 xalign 0.0
        yes "TO PLAY THE REST OF THE GAME WITH PG13 SCENES SUBSCRIBE TO THE PATREON FOR $9,000,000,000,000,000,000,000"

label after_menu:
    nerd "FRICK YOU [name] IM GONNA DATE SHADOW INSTEAD OF YOU"
    yes "MARIA!!!!"
    scene date1:
        zoom 2.1
        yalign 0.6
        xalign 0.5
        linear 2 yalign 0.5
    with dissolve
    show sss at left
    show nerdate at right
    yes "hey maria. do you like my chaos emeralds"
    nerd "yes shadow the hedghog i like your chaos emeralds."
 

    return


        




