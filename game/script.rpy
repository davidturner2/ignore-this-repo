# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("professor")
image moon = "professor.png"
image class = Transform("class.jpg",zoom=0.50)
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





define MC = Character("[name]", who_color="#1b2fe2",what_prefix="{cps=25}",what_suffix="{/cps}")

define yes = Character("Shadow The Hedgehog", what_prefix="{cps=25}",who_color="#000000")

define e2 = Character("profesor", what_prefix="{cps=25}",what_textshader="wave:10")
define mathteacher = Character("wattew",what_prefix="{cps=25}",who_color="#fff200",who_outlines=[( 1, "#000000", 0, 0 )] )
define Sonic = Character("Sonic Girl",what_prefix="{cps=25}",who_color="#ff0011" )
default soniclove = 0
define Rizz = Character("Daddy Rizz",what_prefix="{cps=25}",who_color="#000000" )
#define Rizz = Character("Daddy Rizz",who_color="#000000" )
define at = Character("Andrew Tate", who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )], window_background=None)

 
# The game starts here.
default week = 1
default name = "Andrew"
screen button_example(a):
    frame:
        xalign 0.5 yalign 0.50
        button action Jump("explore"):
            text "[a]" style "button_text"
screen calender:
    text "Week [week]":
        xalign 0.5
        yalign 0
    

label start:
    #play sound "fmc.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #moon2 "are you ready to have {shader=jitter}babies with me?{/shader}" 

    window hide dissolve

    pause 1.0

    

    pause 1.0
    show screen calender

    scene antat:
        zoom 0.6
        yalign 0.6
        xalign 0.5
        linear 2 yalign 0.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    at "{cps=25}Men in this society have it hard... {w}like my reproductive organ."    



    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Sabah"
    MC "What is my life? I have no girlfriends, no ps5, no maidens... and I'm gonna die alone. "
    Rizz "Not if I can help it!"
    show daddy:
        offscreenleft
        easein_elastic 3 xalign 0.0
    MC "What the—who the heck are you"
    Rizz "They call me Daddy Rizz... and I’m your grandpapa."
    MC "A ghost? For real? "
    Rizz "Damn right I am. My mission: to get you laid, Sonny Boy."
    MC "Wait... seriously?! I mean, thanks, bra. "
    Rizz "Yeah, but step one: take a shower. You smell like straight booty cheeks." 
    MC "Okay, Daddy Rizz." 
    # This ends the game.
label shower:   
    menu:
        MC "What should I do?"
        "Take a shower":
            jump label_name
        "try to sneak out again":
            Rizz "YOU NEED TO TAKE A SHOWER. You smell like straight booty cheeks."
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
    Rizz "Ah, spring. The scent of new beginnings. A perfect time for love."
    MC "I thought that last semester... "
    Rizz "Yeah, but this time you’ve got me, baby boy. Now get to class—I need to see what I’m working with."
    MC "Wait, can other people see you?"
    Rizz "Nah, I’m your personal wingman. Think of me as your rizzing subconscious—now class first. Chop-chop."
    scene class
    with Dissolve(.5)
    show math:        
        yoffset 90
        ease_quad 0.5 yoffset 100.4
        ease_quad 0.5 yoffset 90.0
        repeat
    mathteacher "Okay, welcome back, nerds. I know most professors make you introduce yourselves, but I don't care. Y’all can awkwardly mingle on your own time. Today, I'm talking about processing."
    Rizz "We’re skipping this, cause its boring. I mean it's a game design class. back in my day the we game we was at the club getting girls getting maidens."
    mathteacher "Thats it for today. Bye "
    show math:        
        yalign 0.0
        linear 1 offscreenleft
    MC "choose interaction or work \"WIP\""
    show nerdy
    with Dissolve(.5)
    Sonic "hey [name]! Is your shirt the same blue as Sonic in Sonic Adventure? "
    Rizz "Say yes. We’ve hooked a nerd."
menu:
    "No":
        Sonic "I would know if it wasn’t. His color only changes when the tech improves, which only happened in—"
        jump ahh 

        
        

    "Yes, I think it is":
        Sonic "I knew it! Did you know that in Sonic Superstars, they finally gave Sonic the ability to swim? In earlier games, he’d just drown because..."
        jump ahh       

label ahh:
    menu:
        "Stay and listen":
            python:
                renpy.notify("{color=#0f0}Love +1.")
            $soniclove +=1
            Rizz "Wow, two hours of hardcore Sonic lore. Truly, you’re built different."
            Sonic "Uh, thanks for listening. Most people just... leave."
            MC "I get it."
            Sonic "What do you mean"
            MC "You come on a little strong, dude."
            Sonic "Oh. Okay. I'll, uh, try to tone it down."
            

        

        "Walk away":
            python:
                renpy.notify("{color=#f00}Love -1.")
            $soniclove -=1
            Sonic "Wow. Okay. Hella rude—go touch grass or something."
            Rizz "Yikes. Anyway, I guess you’ve got someone else in mind?"





label after_menu:
    if week == 1:
        show nerdy:        
            yalign 0.0
            linear 1 offscreenleft
        MC "ahh"
        call screen button_example("sonic girl love you")

   

label explore:
    if week == 1:        
        MC "ahhahahahah"        


    return


        




