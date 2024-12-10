# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("professor")
image moon = "professor.png"
image cllass = Transform("Class.jpg",zoom=0.50)
image hally = Transform("Hall.jpg",zoom=0.50)
image cllass2 = Transform("Class2.jpg",zoom=0.50)
image mappp = Transform("map.png",zoom=0.50)
image gothy = "latina.png"
image lib = "R.jpg"

image sss = "mc.png"

image whites = Solid("#fff")


image antat = "watchingandrew.jpg"
image tt = "title.jpg"
image idkk = "idk.png"

image campus = Transform("enter.png",zoom=1.50)
image sab = "easteregg.png"
image oof = "foo.png"
image math = "mathteacher.png"
image nerdy = "nerd.png"
image nerdate = "nerd date.png"
image date1 = "date1.png"
image daddy = "rizz.png"


default teacherLove = 0
default work = False


define MC = Character("[name]", who_color="#1b2fe2",what_prefix="{cps=25}",what_suffix="{/cps}")

define yes = Character("Shadow The Hedgehog", what_prefix="{cps=25}",who_color="#000000")

define Teacher = Character("profesor", what_prefix="{cps=25}",)
define mathteacher = Character("wattew",what_prefix="{cps=25}",who_color="#fff200",who_outlines=[( 1, "#000000", 0, 0 )] )
define Sonic = Character("Sonic Girl",what_prefix="{cps=25}",who_color="#ff0011" )
define GothYandere = Character("Goth Yandere",what_prefix="{cps=25}",who_color="#4f354e" )
default gothLove = 0


default sonicLove = 0
define Rizz = Character("Daddy Rizz",what_prefix="{cps=25}",who_color="#000000" )
#define Rizz = Character("Daddy Rizz",who_color="#000000" )
define at = Character("Andrew Tate", who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )], window_background=None)
define Woo = Character("Woo", what_prefix="{cps=25}",who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )])

 
# The game starts here.
default week = 1
default name = "Andrew"
default morning = True
default sonic1 = True
default sonic2 = True
default sonic3 = True
default goth1 = True
default teacher1 = True
default teacher2 = True
default teacher3 = True
default teacher4 = True

screen button_example(a):
    frame:
        xalign 0.5 yalign 0.50
        button action Jump("explore"):
            text "[a]" style "button_text"
screen calender:
    text "{color=#fff}Week [week]":
        xalign 0.5
        yalign 0
screen map:
    frame:
        background "whites" size 12
        vbox:
            spacing 10 
            text "Go to"      
            button action Jump("class"):
                if morning==False:                
                    if week == 2 or week == 4 or week == 3:
                        text "Class{color=#f00}!" style "button_text"
                else:
                    text "Class" style "button_text"
            button action Jump("main_halls"):
                if week == 2 and sonic1:
                    text "Main halls{color=#f00}!" style "button_text"
                else:
                    text "Main halls" style "button_text"

            button action Jump("class_hall"):
                if week == 1 and goth1:
                    text "class hall{color=#f00}!" style "button_text"
                else:
                    text "class hall" style "button_text"
            button action Jump("building_entrance"):
                if morning:
                    text "Building entrance" style "button_text"
                else:
                    text "Building exit {color=#f00}!" style "button_text"
            button action Jump("cafeteria"):
                text "Cafeteria" style "button_text"
            if work:
                button action Jump("work"):
                    if week == 2:
                        text "work{color=#f00}!" style "button_text"
                    else:
                        text "work" style "button_text"


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
    scene cllass
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
            $sonicLove +=1
            Rizz "Wow, two hours of hardcore Sonic lore. Truly, you’re built different."
            Sonic "Uh, thanks for listening. Most people just... leave."
            MC "I get it."
            Sonic "What do you mean"
            MC "You come on a little strong, dude."
            Sonic "Oh. Okay. I'll, uh, try to tone it down."
            

        

        "Walk away":
            python:
                renpy.notify("{color=#f00}Love -1.")
            $sonicLove -=1
            Sonic "Wow. Okay. Hella rude—go touch grass or something."
            Rizz "Yikes. Anyway, I guess you’ve got someone else in mind?"





label after_menu:
    scene cllass
    if week == 1:
        show nerdy:        
            yalign 0.0
            linear 1 offscreenleft
        menu:
            MC "What should I do?"

            "explore":
                call screen button_example("explore")


            "talk to Goth":                
                jump goth_lab

label goth_lab:
    show gothy
    with Dissolve(.5)
    Rizz "well aint she something"
    Rizz "you got this"
    menu:
        MC "what should I say?"
        "are you waiting for class?":
            MC "Are you, uh, waiting for class?"
            GothYandere "No. I’m waiting for the apocalypse."
            MC "Oh, cool. So... not class, then?"
            GothYandere "You have a strange aura. Do you know how it feels to be... watched?"
            Rizz "Buddy, she’s giving “I'm the main character” vibes. Stay frosty."
            MC "Um, not really?"
            GothYandere "Hm. Interesting. Maybe I’ll show you sometime."
            jump goth_lab2


        "I like your style":
            python:
                renpy.notify("{color=#0f0}Love +1.")
            $gothLove +=1
            MC "I, uh, like your style. Very unique."
            GothYandere "Unique? Is that what you call flirting these days?"
            MC "Uh—"
            GothYandere "Let me guess. You’re one of those people who thinks darkness is just a vibe. Cute."
            Rizz "I think she's high."
            MC "I mean, you do have a cool aesthetic."
            GothYandere "Careful with your compliments. I might start to believe you."
            jump goth_lab2


label goth_lab2:
    show gothy
    menu:
        "what are you yapping about?":
            if gothLove == -1:
                MC "What are you even yapping about?"
                GothYandere "Yapping? Like a dog? Is that what I am to you?"
                Rizz "You just activated her villain arc."
                GothYandere "People who talk to me like that... don’t last long. Maybe you should leave before I get bored."
            elif gothLove == 0:
                MC "What are you yapping about?"
                GothYandere "Exactly what I said. Do you need me to dumb it down for you?"
                Rizz "Wow. I think she likes you."
            python:
                renpy.notify("{color=#f00}Love -2.")
            $gothLove -=2
            jump weekend
        "Nice":
            if gothLove == 1:
                MC "Uh, nice."
                GothYandere "“Nice”? That’s all you’ve got? You’re either very brave or very stupid."
                Rizz "Why not both?"
                MC "I mean it in a good way."
                GothYandere "Hm. I’ll allow it. For now."
            elif gothLove==2:
                MC "Nice."
                GothYandere "Hmm. Maybe you’re not as dull as you look. Keep saying things I like, and maybe I’ll let you stay by my side."
                Rizz "Congrats, you’re on her good side. I think. Try not to ruin it."
            python:
                renpy.notify("{color=#0f0}Love +1.")
            jump weekend
            $gothLove +=1



label weekend:
    Rizz "Damn the time really went by, head home hotshot"
    $morning = False    
    $goth1 = False
    jump main_halls

label explore:
    call screen map()       


label class:
    scene cllass2
    if week==1:
        "You have no class right now."
        jump class_hall
    elif week == 2 and teacher1:
        show moon at left
        Teacher "Good morning, class. Welcome to “English Literature“ today we are talking about the book Themes of Solitude."
        Teacher "Yes, I know. Everyone loves English class. And by loves, I mean tolerates because it’s required."
        Rizz "Oof, she’s already roasting the room. I like her."
        Teacher "Let’s dive right in. Can anyone tell me what Ben Dover meant by This is the Hour of Lead?"
        Teacher "Nobody? Wow, and here I thought this generation was obsessed with cryptic posts."
        Teacher "You there, in the back. What do you think?"
        MC "Uh, maybe… it’s about heartbreak?"
        Teacher "That’s actually not bad. Heartbreak, grief, existential dread—all valid interpretations. Unlike the rest of you, he’s trying."
        Rizz "Bro, she just gave you a gold star. You’re her favorite now."
        menu:
            "Ask a question about the poem":
                python:
                    renpy.notify("{color=#0f0}Love +1.")
                $teacherLove+=1
                MC "So, does “Hour of Lead” mean something heavier than just sadness?"
                Teacher "Good question. Yes, Ben was capturing the weight of loss—the kind that doesn’t just hurt but lingers, shaping you."
                Teacher "She knew how to put loneliness into words better than most of us can admit to feeling it."
                Teacher "I’m glad at least someone is curious. Keep asking questions like that, and you might make this class bearable."
                Rizz "“Bearable”? High praise, dude. You’re locked in."
            "Stay silent and avoid attention":
                Teacher "Fine. I’ll continue talking to myself. It’s not like that’s new for an English teacher."
                Rizz "Ouch. You just left her hanging. Not cool, man."
        Teacher "All right, that’s enough Dickinson for one day. I’m sure you’re all thoroughly thrilled by the nuances of 19th-century poetry."
        Teacher "Before you go, I have an announcement. The English department is organizing a small project in the library. We need a few 'responsible' volunteers to help organize some literary materials."
        Teacher "Those who show up and actually contribute will be compensated for their time. Yes, I said paid."
        Teacher "Don’t get too excited. It’s not much. But it’ll look good on your resume if you can spin it well enough."
        Rizz "Paid to hang out with books? Its a trap but money is money."
        Teacher "If you’re interested, meet me in the library after hours. I’ll be there making sure nobody burns the place down."
        Teacher "That’s all for today. Dismissed."
        $work = True
        $teacher1 = False
        jump class_hall
    elif week==3 and sonicLove>-3 and sonic2:
        show nerdy
        if sonicLove == -2:
            Sonic "Oh great. Stuck with you. This is worse than Sonic being stuck in a loading screen."
            MC "Wow, you really know how to make a guy feel special."
            Sonic "Look, let’s just get this over with. I’ll handle the important stuff—you can… staple the pages or something."
            MC "I can do more than that, you know."
            Sonic "Sure you can. Just like Sonic could totally swim before Superstars."
            jump ohyea

        if sonicLove==-1:
            Sonic "Okay, so… you’re my partner. Cool, I guess."
            MC "Not exactly a glowing endorsement."
            Sonic "Hey, I’m just saying. Group work usually means one person carries, and it’s not gonna be you."
            MC "You could at least give me a chance."
            Sonic "Fine. Just… don’t make me regret it."
            jump ohyea

        if sonicLove == 0:
            Sonic "Alright, let’s divide this up. I’ll take the first part, you handle the second."
            MC "Sounds fair."
            Sonic "Good. Oh, and if you mess up, I’m totally blaming you."
            MC "Wow, so much trust."
            Sonic "Hey, trust is earned. Don’t make me regret this."
            jump ohyea

        if sonicLove == 1:
            Sonic "Hey, partner. Let’s knock this out quick, yeah?"
            MC " You sound like you’ve got other plans."
            Sonic "Nah, just don’t want this assignment to take forever. Group work usually drags. But hey, I think we can make a good team."
            MC "You actually have faith in me?"
            Sonic "Don’t push it. But yeah, you seem… alright."
            jump ohyea

        if sonicLove >= 2:
            Sonic "Hey, partner-in-crime. Ready to ace this thing?"
            MC " Wow, someone’s confident."
            Sonic "Of course. You’ve got me, and I’ve got you. That’s the dream team right there."
            MC " Now that’s the kind of enthusiasm I can get behind."
            Sonic "Don’t get cocky. But seriously, this might actually be… fun?"
            jump ohyea
        
    else:
        if week == 3:
            if week==4:
                if teacherLove <= -1:
                    Teacher "Good morning. Let's get started. Today we’ll dive into Wordsworth, not to be confused with whatever you might be doing instead of listening."
                    Rizz "Yikes, you’re not getting any special treatment today."
                    Teacher "Now, for those of you who decided to show up to the library on time and do the work, thank you. And for the rest of you, remember, I’ll be reviewing your efforts for participation."
                    Teacher "The rest of you can stay awake long enough to get through this, right?"
                    Rizz "Bro, you’re just another face in the crowd right now. You’ll have to work harder to break that ice."
                if teacherLove >= 1:
                    Teacher "Good morning. Let’s get into Wordsworth, shall we? Or should I say, let’s get into the noble struggle of man versus nature?"
                    Rizz "Dude, she’s looking at you with “I kinda like you” energy. Keep it cool."
                    Teacher "Now, I’m sure most of you would rather be somewhere else right now, but bear with me. Poetry can actually be fun."
                    Teacher "Some of you in the class know that already, don’t you? I’m looking at you, library star."
                    Teacher "Anyway, if you actually read Wordsworth, you might understand why nature is so deeply connected to the human experience. It’s not just trees and lakes, it’s the essence of life itself."
                    Teacher "As for the rest of you… well, if you’re not in this for the love of language, I suggest you at least pretend for the grade."
                    Teacher "But you, library star, I expect you to have some deep thoughts on the nature of words by now. You’ve been doing more than just shelving books, right?"
                    Rizz "Bro, you’re basically the TA at this point. She’s like, low-key impressed with you."
                menu:
                    "Try to catch her attention after class":
                        python:
                            renpy.notify("{color=#0f0}Love +1.")
                        $teacherLove +=1
                        if teacherLove == -1:
                            MC "So, outside of teaching, what do you do? You must have some hobbies, right?"
                            Teacher "I guess I don’t get asked that very often. I mostly spend my time grading papers or pretending to have a life."
                            Teacher "Honestly, it’s mostly reading, anything from classic literature to whatever’s trending on the best-seller lists. I guess you could say I work all the time."
                            Teacher "Not exactly the exciting answer you were hoping for, huh? But teaching is more than just a job; it’s a whole lifestyle. Not everyone can handle it."
                            Rizz "She’s not opening up today, huh? Guess you’ll have to try harder."

                        if teacherLove >= 1:
                            MC "So, outside of teaching… What do you do? I’m sure there’s more to you than just books and lectures."
                            Teacher "I guess most people don’t ask me about that. Well, when I’m not stuck in the classroom, I’m usually reading, writing, or going to those boring faculty meetings that feel like they’ll never end."
                            Teacher "I’m also trying to get back into writing fiction, actually. Teaching’s a full-time job, so I don’t get to spend as much time on it as I’d like. It’s a little hard to balance the two."
                            Rizz "Okay, she's not shutting you down, but don’t go getting too personal. You’re doing fine, though."
                            MC "I should get going."
                            Teacher "Okay goodbye [name]"
                        $morning = False
                        jump class_hall
                    "Leave quietly":
                        $morning = False
                        jump class_hall
            if morning:
                $morning = False
                "Class finished"
            else:
                "You have no class right now."
            jump class_hall
        else:
            "You have no class right now."
            jump class_hall



label ohyea:
    menu:
        "Take the Lead":
            python:
                renpy.notify("{color=#0f0}Love +1.")
            $sonicLove+=1
            if sonicLove == -2:
                Sonic " Oh, you want to lead? Sure, let’s see how fast this crashes and burns."
                Rizz "Bro, she’s roasting you like you’re Eggman in a bad boss fight. Time to prove her wrong."

            if sonicLove == -1:
                Sonic " Alright, fine. But if this goes sideways, I’m taking over."
                Rizz "It’s a test of speed and strategy. Don’t choke."

            if sonicLove == 0:
                Sonic " Cool, let’s see what you’ve got. Just… keep me in the loop, alright?"
                Rizz "Respectable. You’re stepping up to the plate, and she’s not shutting you down. Progress."

            if sonicLove == 1:
                Sonic " Alright, leader. I’ll follow your lead—for now."
                Rizz "A little trust? Nice. Don’t fumble this bag, bro."

            if sonicLove >= 2:
                Sonic "Oh, look at you, Mr. Confident. Fine, let’s do it your way. Just don’t get carried away."
                Rizz "She’s vibing with you. You’ve got the green light—make it count."
          

        "Divide The Work":
            if sonicLove == -2:
                Sonic "You do your half, I’ll do mine. But don’t expect me to fix your mess."
                Rizz "Man, she’s got trust issues. Can’t blame her if you keep slacking."

            if sonicLove == -1:
                Sonic "That’s probably for the best. Just… keep it simple, okay?"
                Rizz "A reluctant truce. Let’s see if you can impress her."
            if sonicLove == 0:
                Sonic "Sounds good. Let’s meet in the middle if we need to."
                Rizz "A fair split. It’s like Sonic and Tails—teamwork makes the dream work."
            if sonicLove == 1:
                Sonic "Works for me. And hey, if you need help, just let me know."
                Rizz "Look at that. She’s offering to help? That’s practically a love confession."
            if sonicLove >= 2:
                Sonic "Sure thing. Teamwork makes the dream work, right? We’ve got this."
                Rizz "She’s hyped for this partnership. You’re in sync, my guy"
    Sonic "Well, that wasn’t too bad. We got through it without any major screw-ups. Not bad for a bunch of newbies."
    Rizz "Hey, not bad at all. You managed to keep it together. Looks like you're getting closer to pulling off a solid team-up."
    Sonic "Yeah, I guess I’ll let you live. But next time, don’t hold back. Let's see what you really got."
    Rizz "Bro, you're cruising. Keep the momentum going—looks like you've earned her trust... for now."
    $morning = False
    $sonic2 = False
    jump class_hall

label work:
    scene lib with Dissolve(0.5)
    show oof
    Woo "Oh, you’re one of the 'volunteers'."
    Woo "Great. Let me guess, you’re here for the money, not the love of 19th-century literature?"
    MC "Uh, does anyone actually love 19th-century literature?"
    Woo "Fair point. I think even Ben Dover would’ve left if she had Netflix."
    Rizz "This one’s got jokes or thinks he has."
    Woo "Anyway, I’m Woo. I manage the chaos around here while the professors pretend we’re in some highbrow academy. You can call me “Sam the Overqualified Shelf Jockey.”"
    Woo "First task, these go in the poetry section. Shelve them alphabetically by author. Think you can handle that, or you got no balls?"
    menu:
        MC "minigame"
        "press to win":
            $work = False
            $morning = False

            call screen map()

label cafeteria:
    scene whites
    MC "WHERES THE TOMBODY I CANT SEE"
    call screen map()




label class_hall:
    scene cllass
    if week==1 and goth1:
        jump after_menu
    else:
        call screen map()

label main_halls:
    scene hally
    if week == 2 and sonic3:
        show nerdy
        if sonicLove <= -1 and sonicLove>-3:
            Sonic "Ugh, stupid machine! Just like Sonic '06, nothing works when you need it to."
            MC "Pretty sure you’re just weak."
            Rizz "Bro what are you doing?!"
            Sonic "You better spin dash outta here before I lose my rings, buddy."
            Rizz "Lock in, don't be rude."
        elif sonicLove >= 1:
            Sonic "This vending machine is slower than Sonic underwater."
            MC "So like, OG Sonic?"
            Sonic "Exactly! You get it. Wanna kick it to see if it works?"
        menu:
            "Help her":
                python:
                    renpy.notify("{color=#0f0}Love +1.")
                $sonicLove+=1
                if sonicLove <= -1 and sonicLove >-3:
                    MC "Fine, let me help."
                    Sonic "Don’t break it. I don’t want to get banned from campus like last time."
                    MC "Last time?! What did you do?"
                    Sonic "Tried to suplex the vending machine. It won."
                    Rizz "This girl is on a different level, man"
                    Sonic "Thanks umm, whats your name again?"
                    MC "Its [name]and whats yours."
                    Sonic "Princess Elise"
                else:
                    MC "All right, let’s kick it."
                    Sonic "Yes! Just like Sonic in Sonic Generations!"
                    MC "Wait, are we seriously comparing vandalism to Sonic lore?"
                    Sonic "If you’re gonna do something, at least do it canonically."
                    Sonic "Nice! You’re pretty fast after all."
                    Rizz "And just like that, she’s impressed. You’re welcome."
                    Sonic"Thanks umm, whats your name again?"
                    MC "Its [name]and whats yours."
                    Sonic "Princess Elise"

            

            "Dip":
                $sonicLove-=1
                python:
                    if sonicLove<=-3:
                        renpy.notify("{color=#f00}Love -1. She will avoid you for now on")
                    else:
                        renpy.notify("{color=#f00}Love -1.")
                
                if sonicLove <= -1:
                    MC "You’re on your own."
                    Sonic "Yeah, I figured. Bet you’d leave Sonic stranded too."
                    Rizz "Bro, you just gave her a villain origin story."
                else:
                    MC "Nah, I gotta go."
                    Sonic "That’s fine. I’ll just... wait for my power-up, I guess."
                    MC "Power-up?"
                    Sonic "You wouldn’t get it."
                    Rizz "Smooth move, leaving her to bond with a vending machine instead."
        $sonic3 = False
        hide nerdy



    call screen button_example("explore")

label building_entrance:
    scene campus
    if morning:
        Rizz "Theres More stuff to do"
        call screen map()
    else:
        if week == 4:
            show nerdy
            if sonicLove == -2:
                Rizz "Oh great, it’s her. Miss “Sass Over Speed.” She’s gonna love tearing you apart again."
                MC "Hey, what’s up?"
                Sonic "Gravity. Taxes. The crushing disappointment of seeing you here."
                MC "Wow, someone’s in a mood today."
                Sonic "Oh no, this is me in a great mood. You’d know if I were in a bad one. So, what do you want?"
                MC" I was just passing by and thought I’d say hi."
                Sonic "Mission accomplished. You can go now."
                Rizz "Bro, she’s rejecting you harder than Sonic rejected physics in ‘06."
            
            if sonicLove == -1:
                Rizz" Alright, she’s less hostile today,, cook."
                MC" Hey, Sonic Girl. Busy?"
                Sonic "Not really. Just waiting for the bus and mentally preparing to pretend to care about homework. What about you?"
                MC" Oh, y’know, the usual. Roaming campus, looking for someone who’ll actually talk to me."
                Sonic "Well, I guess you got lucky today."
                MC" I’ll take that as a win. So I take it you don't live on campus?"
                Sonic "My house isn't that far so why live here?"
            
            if sonicLove == 0:
                Rizz" Okay, neutral ground. No hostility, but don’t expect a parade, my dude."
                MC" Hey, waiting for the bus?"
                Sonic "Yeah, what gave it away? My stressed-out expression or the fact I’m standing next to the giant bus stop sign?"
                MC" It was the aura of quiet frustration. A dead giveaway."
                Sonic "Ha, yeah, that checks out. This bus is always late. What about you? Just wandering, or did you follow the scent of sarcasm?"
                MC" I figured the sarcasm trail would lead to you eventually."
                Sonic "Touché. You’re getting better at keeping up."
                Rizz" Look at you! Trading jabs like a pro. Keep it up, maybe she won’t roast you alive."
            
            if sonicLove == 1:
                Rizz" She’s smiling already? Nice. Don’t screw it up."
                MC" Hey! Fancy meeting you here."
                Sonic "Hey, yourself. What are you doing out here? Don’t tell me you’re stalking me."
                MC" What? No! I was just... walking. And I saw you."
                Sonic "Hmm. Convenient. Anyway, I’m just killing time before the bus. It’s one of those rare moments where I’m not running around like a maniac."
                MC" So you’re embracing the slow life?"
                Sonic "Don’t get used to it. I’m only stopping for a breather. What about you? Got plans, or just embracing your inner Sonic wandering Green Hill?"
                MC" I guess I’m taking a breather, too. Mind if I join you?"
                Sonic "Sure. But if you start talking about physics, I’m out."
            
            if sonicLove >= 2:
                Rizz" Alright, she’s looking comfortable. You’re in the sweet spot. Don’t blow it."
                MC" Hey, Sonic Girl! Waiting for the bus?"
                Sonic "Yeah, it’s running late as usual. But hey, gives me time to think—or more likely to overthink."
                MC" What’s on your mind?"
                Sonic "Oh, you know, the usual. Life, classes, why vending machines can’t ever just work. The mysteries of the universe."
                MC" Vending machines and existential crises? Sounds like a fun combo."
                Sonic "Exactly. What about you? Out for a stroll, or did fate send you here to keep me company?"
                MC" I guess I’m here to brighten your wait."
                Sonic "Brighten, huh? You’re setting a pretty high bar."
                Rizz" Bro, she’s smiling. Keep riding this wave—don’t sink it with awkwardness."
            menu:
                "Stay and chat":
                    python:
                        renpy.notify("{color=#0f0}Love +1.")
                    $sonicLove +=1
                    jump date                

        else:
            menu:
                "Leave":
                    $week+=1
                    show screen calender
                    jump start2
                    $morning = True
                "Back":
                    jump main_halls
        
        

label start2:

    scene antat:
        zoom 0.6
        yalign 0.6
        xalign 0.5
        linear 2 yalign 0.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    at "{cps=25}Men in this society have it hard... {w}like my reproductive organ."   
    MC "Why Am I still watching this?????? time for a new day of school."
label start3:
    menu:
        MC "What should I do?"
        "Take a shower":
            $morning = True
            jump building_entrance
        "try to sneak out again":
            show daddy:
                offscreenleft
                easein_elastic 3 xalign 0.0
            Rizz "YOU NEED TO TAKE A SHOWER. You smell like straight booty cheeks."
            jump start3


label date:
    scene date1:
        zoom 2.1
        yalign 0.6
        xalign 0.5
        linear 2 yalign 0.5
    with dissolve
    show sss at left
    show nerdate at right
    "mc" "wanna make babies"
    Sonic "WHAT THE HECK!!!!!!!????????? RIGHT NOW!!!!!!"

