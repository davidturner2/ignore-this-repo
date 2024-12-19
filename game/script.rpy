# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("professor")
image moon = "professor.png"
image cllass = Transform("Classhall.png",zoom=1.00)
image hally = Transform("Hall.png",zoom=1.00)
image cllass2 = Transform("class.png",zoom=1)
image mappp = Transform("map.png",zoom=0.50)
image gothy = "latina.png"
image tomy = Transform("tomboy.png",zoom=0.50)
image jay = "idk.png"

image lib = "lib.png"

image sss = "mc.png"

image whites = "cafe"


image antat = "watchingandrew.jpg"
image antat2 = "room.png"
image tt = "title.jpg"
image idkk = "idk.png"

image campus = Transform("campus.png",zoom=1.50)
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
define Goth = Character("Goth Yandere",what_prefix="{cps=25}",who_color="#4f354e" )
define Tomboy = Character("Tomboy",what_prefix="{cps=25}",who_color="#709fb4" )
define Japanese = Character("Japanese Student",what_prefix="{cps=25}",who_color="#709fb4" )

default gothLove = 0

default tomboyLove = 0
default sonicLove = 0
default JapaneseStudentLove = 0
define Rizz = Character("Daddy Rizz",what_prefix="{cps=25}",who_color="#000000" )
define at = Character("Andrew Tate", who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )], window_background=None)
define Woo = Character("Woo", what_prefix="{cps=25}",who_color="#000000",who_outlines=[( 1, "#ffffff", 0, 0 )],what_outlines=[( 1, "#ffffff", 0, 0 )])

 
# The game starts here.
default week = 1
default name = "Andrew"
default morning = True
default halla = True
default cafa = True
default classa = True
default teachera = True
default gotha = True

screen button_example(a):
    frame:
        xalign 0.5 yalign 0.50
        button action Jump("explore"):
            text "[a]" style "button_text"
screen calender():
    text "{color=#fff}Week [week]":
        size 40
        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0
screen that_screen_name():
    frame:
        align (.05, .3)
        padding (20, 400)
        vbox:
            button action [Hide("that_screen_name"), Show("stats")]:
                text "go back" style "button_text"    
            text "Sonic Girl Love [sonicLove]"
            text "Profesor Love [teacherLove]"
            text "goth Love [gothLove]"
            text "Tomboy Love [tomboyLove]"
            text "Japanese Girl Love [JapaneseStudentLove]"

screen stats():
    frame:
        button action [Hide("stats"), Show("that_screen_name")]:
            text "{color=#fff}stats": 
                size 40
                outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
        xalign 0.0
        yalign 0
screen map():
    frame:
        align (.05, .3)
        padding (20, 400)
        vbox:
            text "Go to"      
            button action Jump("class"):
                if teachera:
                    text "Class {color=#f00}!" style "button_text"
                else:
                    text "Class" style "button_text"
            button action Jump("main_halls"):
                if halla:
                    text "Main halls {color=#f00}!" style "button_text"
                else:
                    text "Main halls" style "button_text"

            button action Jump("class_hall"):
                if classa:
                    text "class hall {color=#f00}!" style "button_text"
                else:
                    text "class hall" style "button_text"
            button action Jump("building_entrance"):
                if morning:
                    text "Building entrance" style "button_text"
                else:
                    text "Building exit {color=#f00}!" style "button_text"
            button action Jump("cafeteria"):
                if cafa:
                    text "Cafeteria {color=#f00}!" style "button_text"
                else:
                    text "Cafeteria" style "button_text"
            if work:
                button action Jump("work"):
                    text "work{color=#f00}!" style "button_text"


init python:
    def incr():                  
        renpy.notify("{color=#0f0}Love +1.")
        return 1
    def incr3():                  
        renpy.notify("{color=#0f0}Love +3.")
        return 3
    def decr():                  
        renpy.notify("{color=#f00}Love -1.")
        return -1
    def decr2():                  
        renpy.notify("{color=#f00}Love -2.")
        return -2

label start:
    #play sound "fmc.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #moon2 "are you ready to have {shader=jitter}babies with me?{/shader}" 

    window hide dissolve

    pause 1.0
    $halla = False
    $cafa = True
    $classa = True
    $teachera = False
    

    pause 1.0
    show screen calender
    show screen stats

    scene antat:
        zoom 1.6
        yalign 0.6
        xalign 0.5
        

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
            $ sonicLove += incr()
            Rizz "Wow, two hours of hardcore Sonic lore. Truly, you’re built different."
            Sonic "Uh, thanks for listening. Most people just... leave."
            MC "I get it."
            Sonic "What do you mean"
            MC "You come on a little strong, dude."
            Sonic "Oh. Okay. I'll, uh, try to tone it down."
            show nerdy:        
                yalign 0.0
                linear 1 offscreenleft
                

        

        "Walk away":            
            $ sonicLove += decr()
            Sonic "Wow. Okay. Hella rude—go touch grass or something."
            Rizz "Yikes. Anyway, I guess you’ve got someone else in mind?"
            



transform leave:
    on show:
        yalign 0.0
        linear 1 offscreenleft

label asdf:
    scene cllass
    show nerdy:        
        yalign 0.0
        linear 1 offscreenleft
    jump after_menu
label after_menu:
    if week == 1:
        
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
            Goth "No. I’m waiting for the apocalypse."
            MC "Oh, cool. So... not class, then?"
            Goth "You have a strange aura. Do you know how it feels to be... watched?"
            Rizz "Buddy, she’s giving “I'm the main character” vibes. Stay frosty."
            MC "Um, not really?"
            Goth "Hm. Interesting. Maybe I’ll show you sometime."
            jump goth_lab2


        "I like your style":
            $ gothLove += incr()
            MC "I, uh, like your style. Very unique."
            Goth "Unique? Is that what you call flirting these days?"
            MC "Uh—"
            Goth "Let me guess. You’re one of those people who thinks darkness is just a vibe. Cute."
            Rizz "I think she's high."
            MC "I mean, you do have a cool aesthetic."
            Goth "Careful with your compliments. I might start to believe you."
            jump goth_lab2


label goth_lab2:
    show gothy
    menu:
        "what are you yapping about?":
            if gothLove == -1:
                MC "What are you even yapping about?"
                Goth "Yapping? Like a dog? Is that what I am to you?"
                Rizz "You just activated her villain arc."
                Goth "People who talk to me like that... don’t last long. Maybe you should leave before I get bored."
            elif gothLove == 0:
                MC "What are you yapping about?"
                Goth "Exactly what I said. Do you need me to dumb it down for you?"
                Rizz "Wow. I think she likes you."
            $ gothLove += decr2()
            jump weekend
        "Nice":
            if gothLove == 1:
                MC "Uh, nice."
                Goth "“Nice”? That’s all you’ve got? You’re either very brave or very stupid."
                Rizz "Why not both?"
                MC "I mean it in a good way."
                Goth "Hm. I’ll allow it. For now."
            elif gothLove==2:
                MC "Nice."
                Goth "Hmm. Maybe you’re not as dull as you look. Keep saying things I like, and maybe I’ll let you stay by my side."
                Rizz "Congrats, you’re on her good side. I think. Try not to ruin it."
            $ gothLove += incr()
            jump weekend



label weekend:
    if cafa == False:
        $morning = False 
    $classa = False
    jump main_halls

label explore:
    call screen map()       


label class:
    scene cllass2
    if week == 6 and teachera:
        show moon at left
        if teacherLove>=1:
            Teacher "You’re early. That’s... rare for a student these days."
            MC "Figured I’d try something different today."
            Teacher "What, punctuality? A bold experiment."
            Teacher "suppose you could say I’m surprised. You don’t strike me as someone who rushes to hang out in a classroom."
        else:
            Teacher "If you’re here to ask about grades, they’ll be posted at the end of the week."
            MC "Uh, no… I just got here early."
            Teacher "Early, huh? Miracles do happen, I suppose. Find a seat."
            Rizz "Bro, she’s not just annoyed, she’s done with you. Bail before it gets worse."
        menu:
            "I guess I just like your class":
                $teacherLove+=incr()
                MC "I guess I just like your class. You make it… interesting."
                Teacher "Interesting? Well, that’s not a word I hear often about English. Usually, it’s something less flattering."
                Teacher "But I suppose I’ll take the compliment. Just don’t let it go to your head. You’re still a student, and I’m still the one grading your essays."
                Rizz "Buddy, she’s almost charmed. Keep this up, and you’ll graduate with a degree in rizz."
                Teacher "Oh, and for what it’s worth… I appreciate effort, even if it’s just showing up a few minutes early."
                Teacher "Good morning, everyone. I trust you’ve all had your Gfuel—or whatever it is that keeps you awake these days."
                Teacher "Even you, who showed up early last time. A miracle I’m still processing."
                Teacher "Today, we’re talking about symbolism. Think of it as the secret handshake of literature. Done right, it makes a story resonate. Done wrong, it feels like the author is shouting “Look at this thing I hid!”"
                Teacher "Take The Great Gatsby. That green light over the water? It’s not just there to look pretty, it’s the stand-in for every unattainable dream you’ve ever had."
                Rizz "she's looking at you, balls to the wall."
                Teacher "You know, the kind that’s always just out of reach. You ever feel like that? Like no matter how close you get, it’s never enough?"
                Teacher "Anyway, Mike Hawk was a master at subtlety. It’s why we’re still talking about him a century later. Think about what that kind of symbolism adds to a story—depth, mystery, connection."
                Teacher "But not every author gets it right. Some symbolism is about as subtle as a flashing neon sign. You don’t want to be that writer."
                Teacher "And if you’re sitting there wondering why any of this matters, don’t worry. That’s the question every good writer asks themselves at some point."
                $morning = False
                $teachera = False
                $work = True
                jump class_hall
            "There wasn’t much else to do":
                MC "There wasn’t much else to do. Figured sitting here beats staring at a wall."
                Teacher "That’s… probably the closest thing to a compliment I’ll get from you, isn’t it?"
                Teacher "Fair enough. At least you’re honest. That’s more than I can say for most people who claim they love poetry while skimming the SparkNotes version."
                Rizz "She’s laughing at your lame excuse? You might actually have a shot here, bro."
                Teacher "Oh, and for what it’s worth… I appreciate effort, even if it’s just showing up a few minutes early."
                Teacher "Good afternoon. Let’s try to get through today’s topic without anyone texting under the desk or pretending to take notes."
                Teacher "Symbolism isn’t just about throwing random objects into a story and hoping they stick. It’s about layers, layers that most of you will probably miss because you’re too busy searching for a SparkNotes summary."
                Rizz "Bro she ain't even looking at us."
                Teacher "Take The Great Gyattsby, for example. The green light isn’t just a lamp on a dock. It represents unattainable dreams, the perpetual distance between what we want and what we can have."
                Teacher "Some of you might say, “Why not just tell the reader outright?” Because, believe it or not, literature isn’t Twitter or X whatever its called. Authors don’t need to spoon-feed their themes in 280 characters or less."
                $morning = False
                $teachera = False
                $work = True
                jump class_hall
    if week==1:
        "You have no class right now."
        jump class_hall
    elif week == 2 and teachera:
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
                $teacherLove+=incr()
                MC "So, does “Hour of Lead” mean something heavier than just sadness?"
                Teacher "Good question. Yes, Ben was capturing the weight of loss—the kind that doesn’t just hurt but lingers, shaping you."
                Teacher "She knew how to put loneliness into words better than most of us can admit to feeling it."
                Teacher "I’m glad at least someone is curious. Keep asking questions like that, and you might make this class bearable."
                Rizz "“Bearable”? High praise, dude. You’re locked in."
            "Stay silent and avoid attention":
                $teacherLove+=decr()
                Teacher "Fine. I’ll continue talking to myself. It’s not like that’s new for an English teacher."
                Rizz "Ouch. You just left her hanging. Not cool, man."
        Teacher "All right, that’s enough Dickinson for one day. I’m sure you’re all thoroughly thrilled by the nuances of 19th-century poetry."
        Teacher "Before you go, I have an announcement. The English department is organizing a small project in the library. We need a few 'responsible' volunteers to help organize some literary materials."
        Teacher "Those who show up and actually contribute will be compensated for their time. Yes, I said paid."
        Teacher "Don’t get too excited. It’s not much. But it’ll look good on your resume if you can spin it well enough."
        Rizz "Paid to hang out with books? Its a trap but money is money."
        Teacher "If you’re interested, meet Woo in the library after hours. He'll be there making sure nobody burns the place down."
        Teacher "That’s all for today. Dismissed." 
        $morning = False
        $work = True
        $teachera = False
        jump class_hall
    elif week==3 and teachera:
        show nerdy
        if sonicLove <= -3:
            hide nerdy
            $morning = False
            "Class finished"
            jump class_hall
            $teachera = False


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
    elif week==4 and teachera:
        show moon at left
        if teacherLove <=-1:
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
                $teacherLove+=incr()
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
                $work = True
                jump class_hall
            "Leave quietly":
                $morning = False
                $work = True
                jump class_hall
                    
    else:
        $work = True
        "You have no class right now."
        jump class_hall



label ohyea:
    menu:
        "Take the Lead":
            $ sonicLove += incr()

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
    $teachera = False
    $work = True
    jump class_hall

label work:
    scene lib with Dissolve(0.5)
    if week == 2:
        show oof
        Woo "Oh, you’re one of the 'volunteers'."
        Woo "Great. Let me guess, you’re here for the money, not the love of 19th-century literature?"
        MC "Uh, does anyone actually love 19th-century literature?"
        Woo "Fair point. I think even Ben Dover would’ve left if she had Netflix."
        Rizz "This one’s got jokes or thinks he has."
        Woo "Anyway, I’m Woo. I manage the chaos around here while the professors pretend we’re in some highbrow academy. You can call me “Sam the Overqualified Shelf Jockey.”"
        Woo "First task, these go in the poetry section. Shelve them alphabetically by author. Think you can handle that, or you got no balls?"
        jump gameee
    if week == 3:
        jump gameee2
    if week == 4:
        jump gameee3
    if week == 5:
        jump gameee4
    if week == 6:
        jump gameee5


label gameee:
    menu:
        MC "Sort (by letter)books in alphabettical order!"
        "GKNBUV":
            $work = False
            $morning = True
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2
        "ASBDJLK":
            "wrong order try again"
            jump gameee
        "EFGHJIKL":
            "wrong order try again"
            jump gameee
        "ABCZXZZ":
            "wrong order try again"
            jump gameee
        "ROFLMAO":
            "wrong order try again"
            jump gameee


label gameee5:
    menu:
        MC "Sort (by letter)books in alphabettical order!"
        "ABCDEFGJKPS":
            $work = False
            $morning = True  
            jump sonicgf
        "ABCDEFGOPMXYZ":
            "wrong order try again"
            jump gameee5
        "SABAHBABY":
            "wrong order try again"
            jump gameee5
        "FOOFOOFOOFOO":
            "wrong order try again"
            jump gameee5
        "ABCDEFGHIJKLMNOPQRSTUVWXYZNOWYOUKNOWYOUREABCSNEXTTIMEWONTYOUSINGWITHME":
            "wrong order try again"
            jump gameee5
label gameee4:
    menu:
        MC "Sort (by letter)books in alphabettical order!"
        "ABCDEFGHIXXX":
            $work = False
            $morning = True           
            jump tomboyatwork
        "ABCDEFFFGGGEILMNOP":
            "wrong order try again"
            jump gameee4
        "ASDFGHJKL":
            "wrong order try again"
            jump gameee4
        "ZXCVBNM":
            "wrong order try again"
            jump gameee4
        "QWERTYUIOP":
            "wrong order try again"
            jump gameee4
label gameee2:
    menu:
        MC "Sort (by letter) books in alphabettical order!"
        "ACDLMBPOXYZ":
            "wrong order try again"
            jump gameee2
        "AFLOOOOX":
            $work = False
            $morning = True
            jump gothic
        "ABCDEZIONFOO":
            "wrong order try again"
            jump gameee2
        "LMFAOZZ":
            "wrong order try again"
            jump gameee2
        "ASDFGHJ":
            "wrong order try again"
            jump gameee2

label gameee3:
    menu:
        MC "Sort (by letter) books in alphabettical order!"
        "ABCDEFGHA":
            "wrong order try again"
            jump gameee3
        "ABCDEFIGHT":
            "wrong order try again"
            jump gameee3
        "AABHSTV":
            $work = False
            $morning = True
            jump janime            
        "QRSTUVWXVZ":
            "wrong order try again"
            jump gameee3
        "LMNOPHARTS":
            "wrong order try again"
            jump gameee3
label sonicgf:
    if sonicLove <= -3:
        $week+=1
        MC "TIME TO GO HOME IM TIRED FROM WORK"
        jump start2
    show nerdy
    Rizz "Yo, isn’t that Sonic Girl? What’s she doing here? Gotta admit, not her usual scene."
    if sonicLove <= -1:
        Sonic "Oh, it’s you. Didn’t think I’d run into someone I know here. Guess my luck is really hitting rock bottom today."
        MC "What happened?"
        Sonic "Tried to get a job. Apparently, my “qualifications” aren’t up to their elite library standards. I mean, it’s shelving books, not rocket science."
        MC "Maybe they sensed your... chaos energy?"
        Sonic "Cute. I’ll keep that in mind next time I’m rejected for being “too cool.”"
        Rizz "Smooth, buddy. You’ve got the social grace of a broken keyboard."
    elif sonicLove == 0:
        Sonic  "Oh, hey! Didn’t think I’d run into you here."
        MC "What’s up?"
        Sonic "Tried to get a job. They said no. Something about needing “relevant experience.” Like I haven’t been leveling up my skills my whole life."
        MC "Yeah, but beating Eggman probably isn’t on their résumé requirements."
        Sonic  "Right? Guess I’ll have to grind somewhere else."
        Rizz "Okay, not bad. She’s not sprinting away, so you’re doing alright."
    elif sonicLove == 1:
        Sonic "Hey! Didn’t know you worked here. You’ve been holding out on me!"
        MC "Guilty as charged. So, what brings you to my turf?"
        Sonic "I was trying to get a job. Wanted to save up for this super rare Chaos Crystal plushie. But nope, apparently, I’m not “library material.”"
        MC "What, they don’t accept hyperactive speedsters?"
        Sonic "Can you believe it? The audacity."
        Rizz "Alright, she’s smiling. Keep this pace and don’t trip, bro."
    elif sonicLove>=2:
        Sonic "Hey! Didn’t think I’d run into you here. Guess this day isn’t a total bust after all."
        MC "What’s up?"
        Sonic "Came to snag a job. Figured I could save up for this Chaos Crystal plushie that’s calling my name. But apparently, they’re not into speedrunning applicants."
        MC "You mean you didn’t break their interview record?"
        Sonic "Nah, but I sure left an impression. Anyway, seeing you here makes up for it. You’re like my lucky charm or something."
        Rizz "Yo, she’s laying it on thick, and I’m here for it. Don’t fumble this, champ."
    menu:
        "It'll be okay":
            $sonicLove+=incr()
            MC "Sounds rough. Maybe next time, they’ll see your potential."
            Sonic "Yeah, if by “potential” you mean potential to make this place less boring."
            MC "Hey, I’m all for shaking things up. You really wanted that plushie, huh?"
            Sonic "Yeah, it’s part of this special collection. Limited edition, too. But guess it’s back to the grind elsewhere."
            MC "What if I spot you for it? Consider it an investment in chaos energy."
            Sonic "I can't let you do that."
            MC " Why not? Gotta keep the fastest person I know happy, right?"
            Rizz "Now that’s what I call smooth moves."
            Sonic "You’re kinda alright."
            Rizz "Now all you need is money to buy that gift."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2

        "Try and make joke to help her feel better":
            MC "Sounds like you just didn’t hit that boost pad, huh? Maybe they figured you’d knock over all the shelves."
            Sonic "Wow, thanks for the encouragement. Did you major in being a jerk, or is it just a side gig?"
            MC "I’m just saying, maybe you should slow down once in a while."
            Sonic "Right, because the guy who shelved books all day is clearly the expert on speed and efficiency."
            Rizz "Dude, you’re about to get blue-shelled off the track."
            Sonic "Anyway, good talk. I’ll go find someone else to not help me out."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2



label tomboyatwork:
    if tomboyLove <= -3:
        $week+=1
        MC "TIME TO GO HOME IM TIRED FROM WORK"
        jump start2
    show tomy
    Tomboy "Yo, didn’t think I’d find you stuck here. What is this, a punishment for being too boring?"
    MC "Funny. Some of us actually have jobs."
    Tomboy "Jobs? Nah, I call it 'voluntary suffering for minimum wage.' So, what’s the gig? Shelving dusty books?"
    Rizz "And here comes Ms. Anti-Work herself."
    MC "Shelving books, answering dumb questions, and keeping people from eating snacks in the non-snack zones. Real thrilling stuff."
    Tomboy "Sounds like my kind of chaos. Too bad I’m not the bookworm type."

    if tomboyLove == -1:
        Tomboy "Bet you’re loving every second of this, huh? Living the dream?"
        MC "Yeah, totally living it. Just waiting for my Employee of the Month award."
        Tomboy "Sure thing, champ. Don’t work too hard."
        Rizz "She’s laying it on thick. Might wanna hit her with something clever before she steamrolls you."
        MC "What about you? Got any thrilling skater gigs lined up?"
        Tomboy "Nah, I’m too busy being awesome."

    if tomboyLove == 0 or tomboyLove == 1:
        Tomboy "So, what’s the weirdest thing you’ve seen working here? Bet there’s some wild stories."
        MC "Depends. Do you count a guy trying to check out a dictionary like it’s a novel?"
        Tomboy "No way. Did you let him?"
        MC "Hey, knowledge is power. Who am I to judge?"
        Tomboy "You’re way too nice for this job. If it were me, I’d make up some library law and send him packing."
        Rizz "She’s vibing. Keep it rolling, chief."

    if tomboyLove == 2 or tomboyLove >= 3:
        Tomboy "So, what’s a cool guy like you doing in a place like this?"
        MC "Waiting for the skater chick of my dreams to show up, obviously."
        Tomboy "Bold move, library boy. But hey, I respect the hustle."
        MC "Hustle? You think this is my game?"
        Tomboy "Oh, it totally is. Don’t worry, though. I’m into it."
        Rizz "Alright, Casanova. That went smoother than expected. Keep it up."
    menu:
        "Help me out, and I’ll make it worth your while":
            Tomboy "Hmm. What’s “worth my while”?"
            MC "A free book recommendation, maybe."
            Tomboy "Oh yeah, super tempting. What’s next, a bookmark as a bonus?"
            MC "Hey, don’t knock bookmarks. They’re underrated."
            Tomboy "Alright, I’ll bite. What do you need help with?"
            MC "Sorting these and pretending to look busy if my boss shows up."
            Tomboy "You’re really putting me to work, huh? Alright, library boy. But you owe me big time."
            Rizz "Wow, she actually agreed. Nice save, buddy."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2
        "Why don’t you go skate or something?":
            Tomboy "Wow, kicking me out already? What, am I cramping your style?"
            MC "Pretty much. You’re too cool for this place."
            Tomboy "Damn right I am. But maybe I like slumming it with the nerds."
            Rizz "Oof. That one backfired, bro. She’s not leaving, and now you’ve gotta deal with her."
            MC "Fine, stay. Just don’t get me in trouble."
            Tomboy "No promises."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2


label janime:
    show jay with dissolve
    Rizz "Heads up, buddy. She’s back—and she brought a present? Or maybe that’s a bomb. Either way, this is about to get interesting."
    menu:
        MC "what should I do?"
        "Take the box and thank her.":
            $JapaneseStudentLove+=incr()
            MC "Oh, uh, thanks? What’s this for?"
            Japanese "Speaks in foreign language."
            Rizz "I think she’s saying it’s food. Either that or she wants you to open it and eat it now. Up to you, my guy."
            MC "Wow, this looks amazing! Did you make these?"
            Japanese "Speaks in foreign language."
            Rizz "She’s blushing, dude. That’s a green flag. Compliment the heck out of it."
            MC "This is seriously impressive. Thanks so much—this must’ve taken a lot of effort."
            Japanese "Speaks in foreign language."
            Rizz "Translation: ‘Aw, it’s nothing,’ but she’s totally loving the praise. Keep it coming."
            Japanese "Speaks in foreign language."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2
        "Politely decline, unsure what it’s for.":
            $JapaneseStudentLove+=decr2()
            MC "Oh, um, thanks, but I can’t accept this. I’m not sure what it’s for."
            Japanese "Speaks in foreign language."
            Rizz "Oh man, she’s trying to explain, but you just threw her off her game. Smooth, real smooth."
            MC "No, no, it’s not that I don’t appreciate it—I do! It’s just... I don’t really know why you’re giving it to me."
            Japanese "Speaks in foreign language."
            Rizz "Ouch. Rejection stings, even if you didn’t mean it that way. Maybe you can fix this next time."
            Rizz "It's food bro she made these. You better make it up to her later."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2
label gothic:
    show gothy with dissolve
    if gothLove <= -1:
        MC "Why is she here?"
        Rizz "Bro, don’t let her catch you staring. She’ll probably hex you or something."
        MC "Can I help you find something?"
        Goth "You could help by not talking to me. Silence is a virtue, you know."
        Rizz "Yup, she hates you. Congrats."
        MC "Right. Let me know if you need anything."
    else:
        MC "You’re here! I mean—uh, looking for something?"
        Goth "Am I not allowed to simply exist?"
        Rizz "Smooth, Casanova. Real smooth."
        MC "That’s not what I meant. It’s just... surprising."
        Goth "I’ll allow it. For now. I’m looking for something... unusual. Something that fits my aesthetic."
        MC "Right... Let me know if you need my help."
    menu:
        "Ask her what she’s reading lately.":
            MC "So, what have you been reading lately? You seem like the type who’s into heavy, thought-provoking stuff."
            Goth "Oh? You think you’ve figured me out? Careful, people who assume too much about me usually regret it."
            Goth "But since you asked... I’ve been reading about the inevitability of entropy. Quite comforting, really."
            MC "Comforting?"
            Goth "Of course. There’s something poetic about how everything eventually fades. It’s honest."
            Rizz "This girl is the final boss of overthinking. Don’t lose yourself in the vibes."
            MC "I mean, I get that. There’s a kind of beauty in the temporary, right?"
            Goth "Hm. Maybe you’re not entirely insufferable."
            Goth "What about you? Do you read, or are you just here to babysit books?"
            menu:
                "Admit you’re not much of a reader.":
                    MC "Honestly? I’m not much of a reader. I mean, I’ve read stuff for school, but nothing like… entropy poetry or whatever."
                    Goth "Hmm. Honesty. How novel. Most people try to fake it."
                    Rizz "Bruh, you just said you don’t read to a girl who probably dreams in sonnets. Risky move."
                    MC "Well, I figure lying about reading won’t impress someone like you."
                    Goth "Good instinct. Though, I can’t promise you’re off the hook yet."
                    Goth "So, if books aren’t your thing, what is? What distracts you from the crushing weight of existence?"
                    MC "Uh… video games, mostly. Maybe movies."
                    Goth "Hmm. And do these distractions... mean anything? Or are they just noise to drown out the silence?"
                    MC "I guess that depends on the game or movie. Some of them can be pretty deep."
                    Rizz "Oh, bro, she’s baiting you into a philosophy debate. Proceed with caution."
                    $gothLove+=incr()
                    Goth "Hm. If you can find meaning in those, perhaps there’s hope for you yet. Barely."
                    show gothy at leave
                    Rizz "Thank god she left, she got aura that's for sure."
                    $week+=1
                    MC "TIME TO GO HOME IM TIRED FROM WORK"
                    jump start2
                "Talk about a book you’re into (even if you have to fake it).":
                    MC "Actually, I read something recently that I really liked."
                    Goth "Oh? And what literary masterpiece captured your fleeting attention?"
                    MC "Uh, Twilight."
                    Goth "Twilight? You’re joking."
                    Rizz "Bro, you’ve done it now. The last spark of respect she had for you? Gone."
                    MC "I mean, vampires, werewolves, forbidden love—it’s got it all, right?"
                    Goth "Yes, and by “all,” you mean glorified stalking, a toxic love triangle, and the literary equivalent of a sugar rush."
                    MC "Uh, well, it’s, uh… entertaining?"
                    Goth "So is watching a train derail. Doesn’t mean it’s worth writing an essay about."
                    Goth "Let me guess; You didn’t even read it. You just watched the movies, didn’t you?"
                    MC "Uh... well..."
                    Rizz "Abort mission, bro. You’re drowning."
                    $gothLove+=decr2()
                    Goth "If you ever try to discuss sparkly vampires with me again, I’ll personally ensure a curse is placed on you."
                    show gothy at leave
                    Rizz "Congratulations, you just became that guy. Might wanna lay low for a while."
                    $week+=1
                    MC "TIME TO GO HOME IM TIRED FROM WORK"
                    jump start2
        "Let her browse in peace.":
            MC "I’ll let you browse. Holler if you need help."
            Goth "I’ll holler if the abyss starts whispering to me."
            Rizz "What does that even mean?"
            Rizz "Come on get a book, we can see what you like to read."
            Goth "I’ll take this one. Don’t disappoint me with the next recommendation."
            MC "I’ll do my best to meet your dark and brooding standards."
            Rizz "A book about cooking meat, that's not disturbing."
            $week+=1
            MC "TIME TO GO HOME IM TIRED FROM WORK"
            jump start2
label cafeteria:
    scene whites
    if cafa and week==6 and gothLove>-3:
        show gothy
        if gothLove<=-1:
            MC "Mind if I join you?"
            Goth "Does it matter what I say? You’ll sit anyway."
            MC "Well, yeah. That’s how socializing works."
            Goth "And yet, here I am, perfectly fine not socializing. Amazing, isn’t it?"
            Rizz "Buddy, she’s giving “stay away” vibes, but you just had to pull a chair up."
            MC "I thought maybe we could, you know, talk."
            Goth "Oh, I’m sure. But let me save you the trouble—I’m not looking for friends, pity, or whatever this is."
            MC "It’s just lunch."
            Goth "Then eat it somewhere else."
        elif gothLove == 0:
            MC "Hey, you look lonely. Mind if I join?"
            Goth "Lonely? That’s rich. Maybe I just like sitting alone."
            Rizz "Bro, she’s not giving you much to work with, but you’ve come too far to back out now."
            MC "Well, the cafeteria’s crowded, and your table seemed... quieter."
            Goth "Quieter until you showed up. But fine, sit if you must. Just don’t expect me to entertain you."
            MC "No problem. I’ll do all the talking."
            Goth "Somehow, that’s even worse."
        elif gothLove == 1:
            MC "This seat taken?"
            Goth "It is now, I suppose."
            MC "I figured you’d want company."
            Goth "Did I give you that impression? Maybe I need to work on my unapproachable aura."
            MC "Oh, it’s plenty unapproachable. I’m just good at ignoring it."
            Goth "Hm. Brave or stupid? I haven’t decided yet."
            Rizz "Bold move, but she didn’t shut you down, so that’s a win. Keep it rolling, champ."
        elif gothLove == 2:
            MC "Hey, mind if I sit here?"
            Goth "If you must."
            MC "You say that like you don’t secretly enjoy my company."
            Goth "Secretly being the key word. Don’t get used to it."
            MC "Too late. I’m a fast learner."
            Goth "Hm. Maybe not as insufferable as I thought. For now."
            Rizz "Wow, bro. She’s practically rolling out the red carpet. Don’t mess this up."
        elif gothLove >=3:
            MC "Is this seat free, or do I need to bribe you?"
            Goth "A bribe might’ve been nice, but I suppose I’ll let it slide."
            MC "Generous of you."
            Goth "Well, you’re not the worst company."
            MC "High praise coming from you."
            Rizz "Look at you, earning a permanent seat at her table. What’s next, matching tattoos?"
        menu:
            "Time for a joke":
                MC "You sound like a villain monologuing before a final boss fight. Should I start running, or are we good?"
                Goth "Running won’t save you. Villains always catch up. Besides, I’d make it too fun for you to stop."
                Rizz "Bro, is she threatening you or flirting? Either way, don’t trip over your words—again."
                MC "Good point. Guess I’ll just have to face the inevitable."
                Goth "Hm. Maybe you’re not entirely hopeless. I’ll let you live… for now."
                MC " Well, that’s comforting. Guess I owe you my life."
                $gothLove+=incr()
                Goth "Don’t thank me yet. I haven’t decided what I’ll do with you."
                Rizz "“I’ll let you live”? Yep, she’s officially into you—or planning your demise. Probably both. Good luck, champ."

            "We are all lost":
                MC "You talk a big game, but I bet you’re just as lost as the rest of us."
                Goth "Careful. Assuming things about me might be the last mistake you make. Or the first of many."
                Rizz "Oh, dude. Did you just poke the metaphorical bear? Bold move. Let’s see how this plays out."
                MC "I’m serious. Everyone’s trying to figure things out, even you. I mean, nobody’s walking around with a “Life Guide for Goth Queens.”"
                Goth "Hm. Bold, but misguided. I don’t need a guide, and I certainly don’t need your pity."
                MC " Not pity. Just an observation. Even villains have their moments of uncertainty, right?"
                Goth "You’re lucky I don’t despise honesty. Yet. Maybe you’re not as clueless as you look. Or maybe you’re just lucky today."
                Rizz " Hey, you didn’t get vaporized! I’ll call that a win. Might wanna tread lightly next time, though."
    if cafa and week==5 and sonicLove>-3:
        show nerdy
        if sonicLove == -1:
            MC "Hey. Mind if I sit?"
            Sonic "Free country."
            MC "So... what’s for lunch?"
            Sonic "Disappointment."
            MC "Sounds delicious. Got room for dessert?"
            Sonic "Yeah. It’s called “leave me alone cake.”"
            Rizz "Bro, she’s not just throwing shade; she’s building a whole solar eclipse. Might wanna cut your losses."
        if sonicLove == 0:
            MC "What’s up? Didn’t expect to see you here."
            Sonic "What, you thought I survived off chili dogs alone?"
            MC "I mean... the thought crossed my mind."
            Sonic "Not every day. Sometimes I mix it up with cafeteria mystery meat. Keeps life interesting."
            MC "Right, because food poisoning is the spice of life."
            Sonic "Exactly. Builds character."
            Rizz "Okay, not bad. Keep it going."
        if sonicLove == 1:
            MC "Well, well, if it isn’t (sonicGirName). Gracing us mortals with your presence in the cafeteria?"
            Sonic "Don’t get used to it. The vending machine’s broken again."
            MC "What a tragedy. Guess the cafeteria chili is your only option."
            Sonic "Yeah, and I think it’s fighting back. Want a bite?"
            MC "Hard pass. I value my life."
            Sonic "Smart choice. But hey, at least this thing hasn’t tried to kill me yet."
            Rizz "Alright, she’s laughing. You’re officially not a waste of her time. Progress!"
        if sonicLove == 2:
            MC "There you are. Was wondering where the fastest thing alive goes when she’s not saving the world."
            Sonic "To refuel, obviously. Even speedsters need snacks."
            MC "Speedsters and... caffeine addicts?"
            Sonic "Hey, don’t knock it. This is what keeps me from completely losing it in class."
            MC "Ah, so it’s not your sharp wit that keeps everyone on their toes?"
            Sonic "That too. But the caffeine helps. Want a sip?"
            MC "Only if I want my heart rate to match Sonic’s top speed. I’ll pass."
            Rizz "Smooth. She’s actually offering stuff now. Keep it cool, and you might just break into the friend zone—or better."
        if sonicLove>2:
            MC "If it isn’t the speedster herself, hiding out in the cafeteria. What’s the matter? No world to save today?"
            Sonic "Even heroes need a cheat day. What’s your excuse?"
            MC "I’m here to soak up some of that main-character energy. Clearly, it’s working."
            Sonic "Careful, you might OD on my awesomeness."
            MC "I’ll take the risk. What’s life without a little danger?"
            Sonic "Alright, I’ll give you that one. You’re starting to keep up. Barely."
            Rizz "Oh, buddy, she’s practically beaming. You’ve got this."
        menu:
            "Grab dessert together":
                $sonicLove+=incr()
                MC "Want to grab something sweet? I hear the cafeteria cookies are like a boss battle; tough on the outside but worth the fight."
                Sonic"Tough cookies, huh? Guess we’ll have to see if you’ve got the skills to unlock the secret ending."
                MC "I’m all about the side quests. Let’s go."
                Sonic"Alright, if I had to pick a power-up snack, it’d be... the chocolate muffin. What about you?"
                MC "I’m going with the oatmeal raisin cookie."
                Sonic"A raisin cookie? Who hurt you?"
                MC "Hey, don’t knock it. It’s got hidden stats."
                Sonic"Fine, but I’m judging you."
                Rizz "There it is! A shared snack and playful banter. You’re in the bonus round now, champ."

            "Match her energy":
                MC "I think I can match your speed, easy. What do you say, a chili dog race after this?"
                Sonic"Oh, you think you’ve got what it takes to keep up with me?"
                MC "Absolutely. I mean, how hard can it be?"
                Sonic"Alright, let’s see you sprint through my level of energy while juggling all my fandom trivia. First question; How fast is Sonic in meters per second in Sonic Generations?"
                MC "Uh..."
                Sonic"Yeah, thought so. Don’t try to match my energy if you don’t know the game. Rookie move."
                Rizz "Oof, buddy, that was brutal. You just got outrun before you even started. Next time, stay in your lane."
                $sonicLove +=decr2()
        Sonic "Welp, looks like it’s time for me to hit the next zone. Got class in five."
        MC "What’s the subject? Speedrunning 101?"
        Sonic "More like Sleep Deprivation Studies. But yeah, something like that."
        MC "Sounds riveting. Don’t forget to save your progress."
        Sonic "Oh, I never forget. It’s you who should worry about keeping up."
        Rizz "Alright, she’s leaving on a high note. Don’t mess this up."
        MC "Catch you later, then?"
        Sonic "If you’re lucky."
        show nerdy at leave
        Rizz "She’s gone, bro. But hey, that was solid. You didn’t totally embarrass yourself. Well... maybe with the raisin cookie."

    if cafa and week==4 and morning:
        show tomy
        if tomboyLove == 0:
            MC "Yo, morning."
            Tomboy "Oh, it’s you. Didn’t know they let people in this early to ruin my vibe."
            MC "Always a pleasure."
            Tomboy "You seriously gonna sit there? Fine, whatever. Just don’t start talking about, like, boring stuff, or I’m out."
            Rizz "She’s already regretting this, bro. You better work some magic and not the gathering."

        if tomboyLove == 1:
            MC "Morning, Tomboy."
            Tomboy "Look who’s up early. Didn’t think you were a morning person."
            MC "I’m not. But breakfast is breakfast."
            Tomboy "Respect. You gotta fuel up for the grind. I get it. Take a load off if you want."
            Rizz "She’s cool with you being here. Play it chill, though—don’t oversell."

        if tomboyLove == 2:
            MC "Hey, Tomboy. What’s up?"
            Tomboy "Oh, hey! You’re out early. Trying to impress someone?"
            MC "Nah, just... couldn’t miss the world-class cafeteria waffles."
            Tomboy "Yeah, they’re not bad. If you’re grabbing some, save me a spot. I’ll let you sit in my VIP section."
            MC "Oh, honored to be invited."
            Rizz "VIP section? Bro, you’re climbing the ranks."
        menu:
            "Share a Skating Story":
                $tomboyLove+=incr()
                MC "You know, I tried skating once. Ended with me flat on my back, staring at the sky like it was mocking me."
                Tomboy "Classic rookie move. Let me guess, you thought you could ollie on day one?"
                MC "Guilty. What gave it away?"
                Tomboy "Everyone tries to ollie first. It’s like a rite of passage. Next time, hit me up—I’ll show you how to not eat pavement."
                MC "Deal. But no laughing when I fall."
                Tomboy "Can’t make any promises."
                Rizz "Smooth. She’s laughing, and you didn’t even need a helmet."
                show tomy with dissolve      
            "Playfully Mock Her Breakfast Choices":
                MC "So, what’s a skater’s breakfast look like? Protein bars and energy drinks?"
                Tomboy "Ha, right. Nah, I’m all about waffles and syrup. Don’t let the aesthetic fool you—I’m classy."
                MC "Waffles, huh? Didn’t peg you for someone so refined."
                Tomboy "I contain multitudes, dude. Besides, carbs are fuel for greatness."
                Rizz " Good banter. You’re not skating on thin ice—yet."
                show tomy with dissolve      
    if cafa and week==1:
        $cafa = False
        if classa == False:
            $morning = False   
        show tomy with dissolve      
        Rizz "Yo, check it out—classic skater-bro energy. Bet she smells like energy drinks and rebellion."
        Tomboy "Don’t just stand there, dude. Either sit or keep it moving."
        MC "Uh, right. Mind if I sit?"
        Tomboy "Sure, why not. The table’s not mine—yet."
        Tomboy "You new or just lost?"
        MC "New...ish. You?"
        Tomboy "Been around. Not a fan of the cafeteria food, though. Ever tried their burritos? Tastes like cardboard wrapped in despair."
        MC "Yeah, I’ve, uh, heard stories."
        Tomboy "Stick to vending machines if you value your stomach. Anyway, name’s (tomboyName)."
        MC "Nice to meet you, (tomboyName)."
        Tomboy "Don’t get too comfortable. I don’t hand out free rides to the cool kids’ table."
        menu:
            MC "what should I do?"
            "Ask about her skateboard.":
                MC "So, uh, is skateboarding like, your thing?"
                Tomboy "My thing? Dude, skateboarding isn’t just a thing—it’s a lifestyle. A religion. A way of life."
                MC "That’s... intense."
                Tomboy "You don’t get it until you land your first ollie. Then you’re hooked. There’s no turning back. It’s like falling in love, but better—because a skateboard doesn’t ghost you."
                Rizz "Damn. The board gets more love than we do. That’s rough."
                MC "So how long have you been skating?"
                Tomboy "Since I was a kid. My brother handed me his old board when I was, like, six. I’ve broken more bones than I can count, but hey, no pain, no gain, right?"
                MC "Sounds... dangerous."
                Tomboy "Everything worth doing is. You ever try it?"
                MC "Once  and never again"
                Tomboy "Well, you’re missing out. Next time you see me, maybe I’ll let you try. Or maybe not. Don’t want you suing me when you eat pavement."
                Rizz "Bold of her to assume you’d survive long enough to sue."
                show tomy at leave
            "Ask if she’s always this chill.":
                MC "Are you always this... relaxed?"
                Tomboy "Relaxed? Dude, this is just my default setting. Life’s too short to walk around with a stick up your dick."
                MC "That’s one way to look at it."
                Tomboy "What, you’re one of those people who schedules your free time? Color-coded planners and all that?"
                MC "Uh, no... not exactly."
                Tomboy "Good. The second you start stressing about dumb stuff is the second you lose the point of it all. You gotta go with the flow."
                Rizz "I do absolutely no homework type shit."
                MC "So, what’s the “flow” for today?"
                Tomboy "Right now? Just hanging. Waiting to see if anything cool happens. So far, nothing’s blown my mind, but the day’s still young."
                MC "Glad I could add to the excitement."
                Tomboy "You’re alright, newbie. You got potential. Keep working on that sense of humor, though."
                Rizz "Who knew earning the respect of a skater chick would feel this rewarding?"
                show tomy at leave
    elif cafa and week==3:
        show jay with dissolve
        MC "Hey, mind if I sit here?"
        Japanese "Speaks in foreign language."
        Rizz "She either said, ‘Sure, have a seat,’ or, ‘Why are you bothering me?’ Guess we’ll find out soon enough."
        MC "That looks... really good. Did you make it yourself?"
        Japanese "Speaks in foreign language."
        Rizz "I’m no expert, but she’s probably explaining the ingredients or flexing her cooking skills. Compliment it, dude."
        MC "Looks awesome. Way better than the cafeteria food."
        Japanese "Speaks in foreign language."
        Rizz "Bro, she’s offering you a bite. If this isn’t a power move, I don’t know what is."
        MC "Oh, uh, thanks!" 
        MC "Wow, that’s really good!"
        Rizz "Alright, you’re in her good books. Next move? Up to you, champ."
        menu:
            "Ask about her lunch":
                MC "So, uh, what’s in it? It looks way more interesting than anything I’ve seen here."
                Japanese "Speaks in foreign language."
                Rizz "Alright, Sherlock, I think she’s giving you the play-by-play of her masterpiece. Nod like you understand."
                MC "That’s impressive. You really put a lot of effort into it, huh?"
                Japanese "Speaks in foreign language."
                Rizz "She’s a pro in the kitchen. And you? You’re a pro at eating."
                Japanese "Speaks in foreign language."
                Rizz "Damn I think she was late to something"
                show jay at leave
            "Change the subject to something light":
                MC "You’re really talented. I can tell you’ve got some serious cooking skills."
                Japanese "Speaks in foreign language."
                Rizz "She’s humble about it, but she knows she’s good. Keep hyping her up."
                MC "Seriously, it’s better than anything I’ve had in a long time. You could probably open a restaurant or something."
                Rizz "Smooth. You’ve got her blushing. Now don’t ruin it by saying something dumb."
                Japanese "Speaks in foreign language."
                Rizz "Damn I think she was late to something"
                show jay at leave


    $cafa = False
    call screen map()




label class_hall:
    scene cllass
    if week==1 and classa:
        jump after_menu
    if week == 3 and classa:
        menu:
            MC "What should I do?"

            "explore":
                call screen button_example("explore")

            "talk to Tomboy":
                show tomy
                if tomboyLove == 0:                
                    MC "What’re you doing here? Shouldn’t you be out... skating or something?"
                    Tomboy "And miss all this? The fluorescent lighting, the endless buzzing of people who actually care about school? No way."
                    MC "Sounds like you’re really soaking it all in."
                    Tomboy "Sarcasm noted. But seriously, this place is weirdly chill sometimes. It’s like the calm before the chaos."
                    MC "Chaos being...?"
                    Tomboy "Me, obviously."
                    Rizz "What is with everyone thinking their the main character."
                else:
                    MC "What’s up? You waiting for someone?"
                    Tomboy "Nah, just killing time. Thought I’d see if something interesting would happen. And look—you showed up."
                    MC "Oh, so I’m your entertainment now?"
                    Tomboy "Nah, don’t flatter yourself. But you’re not bad company... for someone who probably doesn’t even know what a kickflip is."
                    MC "Hey, I could totally learn."
                    Tomboy "Yeah? I’ll believe it when I see it, newbie."
                    Rizz " She’s practically daring you to break your neck."
                menu:
                    MC "What should I do?"
                    "Ask About Her Board":
                        MC "So, where’s your board? I feel like it’s weird seeing you without it."
                        Tomboy "Oh, what, do I always gotta have it on me like it’s part of my soul or something?"
                        MC "Kinda, yeah. It’s like your whole vibe."
                        Tomboy "Wow, reduced to “skater girl” status already. Thanks for the deep analysis, Einstein."
                        MC "Just saying. Feels like seeing Superman without the cape."
                        Tomboy "Okay, you’re lucky that was funny. But nah, I left it in my locker. Don’t need to flex on these kids in the hall just yet."
                        Rizz " She’s still got that pro energy, even without the board. You might wanna keep up."
                        show tomy at leave

                    "Offer to Grab a Drink from the Vending Machine Together":
                        $tomboyLove +=incr()
                        MC "You wanna grab a drink or something? There’s a vending machine down the hall."
                        Tomboy "What, you trying to bribe me with soda now?"
                        MC "Hey, everyone’s gotta hydrate. Plus, I need the company."
                        Tomboy "Hmm... I guess I can spare a few minutes to make your life less boring. Let’s go."
                        Tomboy "These machines always got the most random stuff. Like, who’s out here buying grandma's cream pie?"
                        MC "I dunno. Someone who’s desperate?"
                        Tomboy "Oh no, I’m sooo desperate for sweetness. Better buy a mystery cake that might taste like battery acid."
                        MC "You sound like you’ve tried it."
                        Tomboy "Maybe I have. Maybe I haven’t. Who’s asking?"
                        MC "You’re so cryptic. Just pick something already."
                        Tomboy "So what’s your go-to? Energy drink? Soda? Please don’t say bottled water. That’s just boring."
                        MC "Energy drink. Gotta keep up with you, right?"
                        Tomboy "Bold choice. Respect. But don’t blame me if your heart explodes from drinking those all day."
                        Rizz "She’s vibing with it."
                        Tomboy "Alright, let’s bounce before this thing eats my money."
                        show tomy at leave
                $classa = False
                call screen map()
    else:
        $classa = False
        call screen map()

label main_halls:
    scene hally
    if week == 6 and halla:
        show jay
        Rizz "Bro, look at her. That’s the face of someone who just realized her wallet can’t keep up with her dreams. You gonna step up or just keep gawking?"
        Japanese "(speaks in foreign language)"
        Rizz "Translation: ‘Dang, I really want this dress from Amozon but capitalism wins again.’"
        menu:
            "Offer some sympathy":
                MC "Yeah, that dress does look nice. Too bad stuff like this always costs an arm and a leg."
                Japanese "speaks in foreign language"
                Rizz "Okay, that was kind of adorable. She’s straight-up daydreaming right now."
                MC "I mean, you’d probably look great in it."
                Japanese "speaks in foreign language"
                Rizz "Missed opportunity, dude. You could’ve done more, but hey, at least she’s not crying in the bathroom."
                hide jay

            "Make a subtle promise to help.":
                $JapaneseStudentLove+=incr3()
                MC "That’s a nice dress. You really like it, huh?"
                Japanese "(speaks in foreign language)"
                Rizz "She’s practically saying, ‘I want this but can’t afford it.’ Go ahead, big spender. Make her day later."
                MC "Yeah, it’s a shame when good stuff is out of reach... but who knows? Maybe it’ll end up in your closet someday."
                Japanese "(speaks in foreign language)"
                Rizz "Smooth, my guy. You just planted a seed. Now all you gotta do is deliver on Valentine’s Day."

    if week == 5 and halla:
    
        show jay
        Rizz "Yo, it’s her again. And she’s giving ‘lost tourist’ vibes. Go on, be the hero—maybe she’ll reward you with more of those snacks."
        menu:
            "Offer to help her figure out the bulletin board.":
                MC "Uh, do you need help with this? I can try to explain."
                Japanese "Speaks in foreign language."
                MC "Okay, so this is about the Tostos Arcade happening today They’re showcasing different games made by students this semester. It’s pretty chill—lots of free snacks and stuff."
                Japanese "Speaks in foreign language."
                Rizz "Smooth move, translator. She seems impressed. Keep this up, and you might just level up in her heart."
                MC "Glad I could help. Also you thinking about joining any clubs?"
                Japanese "Speaks in foreign language."
                MC "Ahh tabletop club  You’d probably be great in it."
                Japanese "Speaks in foreign language."
                Rizz "That was solid, my guy. You’re practically bilingual now. Sort of."
                hide jay
            "Make a joke about not understanding it either.":
                MC "Yeah, I don’t get half of these notices either. They might as well be written in another language."
                Japanese "Speaks in foreign language."
                Rizz "Okay, I don’t know what she said, but I think she just roasted you. Respect."
                MC "Fair enough. I guess I deserved that. But seriously, do you need help with this?"
                Japanese "Speaks in foreign language."
                Rizz "Not bad, dude. A little humor goes a long way. Just don’t push it, or you’ll end up the punchline."
                MC "This is about the Tostos Arcade happening today They’re showcasing different games made by students this semester. It’s pretty chill—lots of free snacks and stuff."
                Japanese "Speaks in foreign language."
                Rizz "Alright, you’re making progress. Next step learn her language."
                hide jay
    if week == 2 and halla:
        show nerdy
        if sonicLove <= -1:
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
                $sonicLove+=incr()

                if sonicLove <= -1 and sonicLove >-3:
                    MC "Fine, let me help."
                    Sonic "Don’t break it. I don’t want to get banned from campus like last time."
                    MC "Last time?! What did you do?"
                    Sonic "Tried to suplex the vending machine. It won."
                    Rizz "This girl is on a different level, man"
                    Sonic "Thanks umm, whats your name again?"
                    MC "Its [name]and whats yours."
                    Sonic "Sonic Girl"
                else:
                    MC "All right, let’s kick it."
                    Sonic "Yes! Just like Sonic in Sonic Generations!"
                    MC "Wait, are we seriously comparing vandalism to Sonic lore?"
                    Sonic "If you’re gonna do something, at least do it canonically."
                    Sonic "Nice! You’re pretty fast after all."
                    Rizz "And just like that, she’s impressed. You’re welcome."
                    Sonic"Thanks umm, whats your name again?"
                    MC "Its [name] and whats yours."
                    Sonic "Sonic Girl"

            

            "Dip":
                $sonicLove += decr()
                
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
        $halla = False
        hide nerdy


    $halla = False
    call screen button_example("explore")

label building_entrance:
    scene campus
    if morning:        
        if week == 5 and gothLove>-3 and gotha:
            $gotha = False
            show gothy
            if gothLove<=-1:
                MC "Morning."
                Goth "Is it?"
                MC "Uh, yeah. The sun’s out, so... morning."
                Goth "I suppose even the sun can’t help being obnoxious."
                Rizz "Bro, she just called the sun obnoxious. You’re not breaking through this gloom today."
                MC "Alright, so... are you waiting for something?"
                Goth " For you to stop talking, maybe?"
                Goth "Try not to bother me unless you’ve got something interesting to say. Or don’t bother at all."
                Rizz "Yeah, she’s not feeling the small talk. Abort mission, my dude."
            if gothLove == 0:
                MC "Morning."
                Goth "Is that what you call this?"
                MC "What else would you call it?"
                Goth "A slow march toward another forgettable day."
                Rizz "Geez, she’s a ray of sunshine, huh?"
                MC "Not a morning person, then?"
                Goth "I’m not a people person. But I tolerate mornings better when they don’t involve chit-chat."
                MC "So... what’s the plan for the day?"
                Goth "Survive. Maybe thrive. What about you? Got any grand ambitions or just here to fill the void?"
                Rizz "Is she flirting? Hard to tell with this one."
                MC "Uh, thriving sounds nice."
                Goth "Hm. We’ll see."
            if gothLove == 1:
                MC "Morning."
                Goth "Look who’s awake early. Didn’t think you had it in you."
                MC "What can I say? I’m full of surprises."
                Goth "Let’s not get carried away. One surprise doesn’t make you a mystery."
                Rizz "Okay, she didn’t immediately shut you down. Keep it cool."
                MC "So, are you waiting for someone, or just enjoying the weather?"
                Goth "Weather’s overrated. But I guess I’m... waiting. Not for anyone, though. Just seeing where the day takes me."
                MC "That’s surprisingly optimistic."
                Goth "Maybe I’m full of surprises too."
                Rizz "Did she just admit to optimism? Write this down, bro. It’s historic."
            if gothLove>=2:
                MC "Morning!"
                Goth "Wow. Someone’s chipper today. Did you drink an entire pot of coffee or something?"
                MC "Nah, I’m just excited to see what kind of existential dread you’ll throw at me this time."
                Goth "Oh, so now you look forward to it? I must be rubbing off on you."
                Rizz "Careful, bro. If she rubs off too much, you’ll start wearing all black and quoting Edgar Allan Poe."
                MC "Not yet. I still like colors and stuff."
                Goth "Blasphemy. We’ll have to fix that."
                MC "You can try."
                Goth "Oh, I don’t try—I succeed."
                Goth "Don’t get too used to my company, though. I’m unpredictable like that."
                Rizz "She kinda likes you but won’t admit it. Nice."
            menu:
                "You seem different today. What's on your mind?":
                    $gothLove += incr()
                    MC "You seem different today. What’s on your mind?"
                    Goth "Observant, aren’t you?"
                    MC "Just thought I’d ask."
                    Goth "Nothing specific. Just... contemplating. Life, death, the usual existential dread."
                    MC "Heavy stuff for the morning."
                    Goth "That’s the best time for it. When the world is quiet, and everyone else is too tired to be annoying."
                    MC "I can’t say I relate, but it sounds... peaceful, in a way."
                    Goth "You’re surprisingly not stupid. Hm. Maybe there’s hope for you yet."
                    Rizz "She’s intrigued. You’re in her good graces for now, but don’t push your luck, champ."
                    show gothy at leave

                "You ever think about trying something new?":
                    $gothLove += decr2()
                    MC "You ever think about trying something new? Like... smiling?"
                    Goth "Did you really just say that to me?"
                    MC "I mean, it might look good on you—"
                    Goth "Oh, I’m sure you’d love that. A nice little makeover, right? Maybe I’ll try a pastel cardigan while I’m at it?"
                    Rizz "Bro, she’s about to body you verbally. Grab a shield or something."
                    MC "I just meant, you know, it’s worth a shot. Smiling is supposed to be healthy or something. Endorphins?"
                    Goth "Oh, is that why you’re still alive? Endorphins keeping your brain cells barely functional?"
                    MC "I’ll take that as a no, then."
                    Goth "Here’s a tip; stop trying to fix people who don’t need fixing. It’s pathetic."
                    Rizz "Damn, bro, she turned you into a side character. That was cold."
                    show gothy at leave
        Rizz "Theres More stuff to do"
        call screen map()
    else:
        if week == 6 and tomboyLove>-3 and gotha:
            $gotha = False
            show tomy
            MC "Whoa, rough day?"
            Tomboy "Nah, it’s been awesome. Love it when my board decides to snap in two while I’m mid-trick. It’s just, like, the cherry on top of an already great week."
            MC "Let me guess—you went for something over-the-top?"
            Tomboy "Just a casual stair set. Maybe it’s my fault for thinking my board wouldn’t betray me. What about you, library boy? Here to rub it in, or are you actually useful?"
            Rizz "Careful, bro. She’s on edge—don’t let her snap your ego like that board."
            MC "Maybe your board couldn’t handle your “sick” tricks. Sounds like operator error to me."
            Tomboy "Okay, wow. You know, I was about to ask for help, but now I’m reconsidering."
            menu:
                "Let me see if I can help fix it.":
                    MC "Let me take a look. Who knows? Maybe I’ve got the magic touch."
                    Tomboy "You? A magic touch? Color me skeptical."
                    MC "You don’t have much to lose at this point. Unless you’re planning to duct tape it and hope for the best."
                    Tomboy "Bold of you to assume I haven’t tried that before. Alright, go ahead, hero."
                    MC "Oof. I’ve seen better days for a plank of wood."
                    Tomboy "Yeah, so? What’s the verdict, Dr. Fix-It?"
                    MC " Hate to break it to you, but this thing is toast. You’re gonna need a new one."
                    Tomboy "Great. Guess I’m living off ramen for a month."
                    MC "Or you could just, you know, stop trying to ollie over staircases. Just a thought."
                    Tomboy "Absolutely not. The stairs had it coming."
                    Rizz " Alright, she’s got jokes. You’re not totally blowing this. Keep it going."
                    MC "You’re a lost cause, you know that?"
                    Tomboy "And you’re weirdly helpful. Thanks for trying. Guess I don’t hate you... today."
                    show tomy at leave

                "Maybe it’s time to retire from skating.":
                    MC "Maybe this is the universe telling you to find a new hobby."
                    Tomboy "Oh really? And what, pray tell, do you think I should do instead?"
                    MC "Knitting. I could totally see you making scarves with angry slogans stitched into them."
                    Tomboy "“Angry Knitter” sounds like my punk band name. “Songs about rage, bad vibes, and homemade sweaters.”"
                    Rizz "Bro, that’s either genius or the worst band concept I’ve ever heard."
                    MC "Hey, I’d buy your album. But seriously, maybe something safer? Like... I don’t know, yoga?"
                    Tomboy "Wow, thanks for the sage advice, Mom. I’ll just go meditate on my failures instead of living my life on the edge."
                    MC "I’m just saying, broken boards are expensive. Gotta watch that snack fund."
                    Tomboy "My snack fund is sacred! I’ll have you know I already spent it this week. Now I’m really broke."
                    MC "Alright, fine. I’ll stop. But seriously, you okay?"
                    Tomboy "Yeah, I’m fine. Just sucks, you know? This board’s been with me for a while."
                    MC "I get it. Want me to help you carry it to wherever skater boards go to die?"
                    Tomboy "Nah, I’ve got it. But thanks for the comedy routine. You’re pretty entertaining when you’re being annoying."
                    show tomy at leave
                    Rizz " She’s smiling, dude. You didn’t completely crash and burn. Nice work."

        if week == 1:
            show jay
            Rizz "Heads up, champ—texting while walking just got you into your first meet-cute. Classic move."
            MC "Oh, sorry! I wasn’t paying attention—are you okay?"
            Japanese "Speaks in foreign language."
            Rizz "Yeah, no clue what she just said, but she doesn’t seem mad. Help her with those books, bro."
            MC "Uh, do you... need help with these?"
            Rizz "She’s probably saying, ‘Thanks, but I got it.’ Or maybe, ‘You’re holding it upside down, dumbass.’ Hard to say."
            menu:
                MC "what should I do?"
                "Offer to carry the books for her.":
                    $JapaneseStudentLove += incr()
                    MC "Here, let me carry these for you. You’ve got your hands full."
                    Japanese "Speaks in foreign language."
                    Rizz "She’s either saying, ‘Thanks for helping,’ or, ‘Please don’t drop those.’ Stay chill."
                    MC "No problem. I got it."
                    Rizz "okay so she wanted to go to the library"
                    Rizz "she gave you a note it's her name Japanese Student"
                
                "Make a joke to lighten the mood":
                    MC "You know, we could start a new trend. People bump into each other, and instead of saying sorry, they just swap books."
                    Japanese "Speaks in foreign language."
                    Rizz "I think she likes the vibe, but she still has no idea what you’re saying. Nice one, though."
                    MC "I’ll take that as a good sign."
                    Rizz "Pretty sure she’s trying to tell you about those books. Just smile and nod, dude. Universal language."
                    Rizz "she left to the library that's where she was headed"
                    Rizz "I think I saw her name on one of the books Japanese Student"
            $week+=1
            $halla = True
            $teachera = True
            $morning = True
            jump start2
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
                    $sonicLove +=incr()
                    if sonicLove == -1:
                        MC "Waiting for the bus, huh? Always takes forever when you’re in a hurry."
                        Sonic "Yeah, it’s basically my villain origin story at this point."
                        Rizz "At least it wasn't you."
                        MC "Well, you could always run home. You are Sonic Girl, right?"
                        Sonic "If only. Pretty sure my shoes aren’t speed-boost compatible."
                        MC "Hey, I hear you. Once, I waited 40 minutes just for the bus to drive by and splash me with a puddle."
                        Sonic "Classic. What’d you do?"
                        MC "Went home, cried about it, and then swore vengeance on public transportation."
                        Sonic "Guess we’re both victims of the system."
                        Rizz "Okay, she’s laughing. You’re in the clear—for now."

                    if sonicLove == 0:
                        MC "Mind if I join you while you wait?"
                        Sonic "Sure, misery loves company, right?"
                        MC "Wow, I feel so welcomed. Is this your way of saying you’re glad to see me?"
                        Sonic "Don’t push your luck. You’re not that charming."
                        MC "Ouch. Remind me never to ask you for a compliment."
                        Sonic "Hey, I’m honest, not mean."
                        MC "Right, “honesty”."
                        Sonic "What can I say? You’re fun to mess with."
                        Rizz "Okay, okay, she’s joking now. That’s a win in my book."

                    if sonicLove == 1:
                        MC "Soo, standing here all alone? That’s not very Sonic of you."
                        Sonic "Oh, I’ve got my trusty sidekick."
                        Rizz "A phone?"
                        Sonic "It’s telling me the bus is late—again."
                        MC "Wow, even your phone’s throwing shade. Rough life."
                        Sonic "Tell me about it. Honestly, I’m considering just walking home."
                        MC "You’d make it faster than the bus, that’s for sure."
                        Sonic "No kidding. I’m starting to think this stop is just here to test my patience."
                        MC "Well, maybe you’re just waiting for the wrong bus."
                        Sonic "Yeah, because clearly, the right bus has “Sonic Girl VIP” written on it."
                        Rizz "Look at you two, bonding over bus-related trauma. Maybe love can bloom on the battlefield."
                    if sonicLove >= 2:
                        MC "You know, I was gonna head out, but you look like you could use some company."
                        Sonic "Wow, so noble. What gave it away? My “Help me, I’m bored” face?"
                        MC "Exactly. I figured, why not make your day a little brighter?"
                        Sonic "Alright, hero. But if you’re sticking around, you better bring your A-game."
                        MC "Oh, I always do. Question is, can you keep up?"
                        Sonic "Please, I’m always ahead of the pack."
                        MC "Is that so? Guess I’ll have to test that theory."
                        Sonic "Anytime, anywhere. Just don’t cry when I leave you in the dust."
                        Rizz "Okay, this is it. She’s smiling, laughing—dude, you’re practically Sonic & Knuckles right now: peak performance."
                    Sonic "Well, looks like my chariot’s here. Try not to miss me too much"
                    MC "Wouldn’t dream of it. Just don’t let the bus break down halfway there."
                    Sonic "If it does, I’ll call you to come push it."
                    show nerdy at leave
                    Rizz "Bro, she’s got jokes. Keep it cool."
                    Rizz "There she goes, the fastest thing alive, on public transport. You better step up your game next time, champ."
                    $week+=1
                    jump start2
                    $morning = True             
                "Head out":
                    $sonicLove +=decr()
                    if sonicLove <= -1:
                        MC "Well, uh, good luck with the bus."
                        Sonic "Yeah, good luck finding some personality."
                        Rizz "Oof. She’s really channeling her inner Eggman on you today. Let’s dip."
                
                    if sonicLove == 1:
                        MC "Alright, I’ll leave you to your... whatever this is."
                        Sonic "Yeah, probably for the best. Wouldn’t want you to miss your next “adventure.”"
                        Rizz "Yikes, dude. It’s like she’s speedrunning reasons to dunk on you."
                
                    if sonicLove == 0:
                        MC "I’ll catch you later. Bus’ll probably be here soon, right?"
                        Sonic "Hopefully. Knowing this place, I’ll grow roots before it shows up."
                        MC "Well, good luck with that."
                        Sonic "Thanks. Don’t trip on your way out."
                        Rizz "well... you had that, I think."
                
                    if sonicLove >1:
                        MC "I’d stick around, but I’ve got stuff to do."
                        Sonic "Wow. Leaving me to fend off the slowest bus in existence? Some hero you are."
                        MC "You’ll survive. You’re Sonic Girl, remember?"
                        Sonic "True. But don’t be surprised if I outrun you next time."
                        Rizz "Hey, she’s smiling. That’s like, flirting in her language. Good job, bro."
                    $week+=1
                    jump start2
                    $morning = True     
        menu:
            "Leave":
                $week+=1
                jump start2
                $morning = True
            "Back":
                jump main_halls
        
        

label start2:

    scene antat2:
        yalign 0.6
        xalign 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    MC "Time for a new day of school."
    if week == 2:
        $halla = True
        $classa = False
        $teachera = True
        $cafa = True
    if week == 3:
        $classa = True
        $teachera = True
        $cafa = True
    if week == 4:
        $classa = False
        $teachera = True
        $cafa = True
    if week == 5:
        $halla = True
        $classa = False
        $teachera = True
        $cafa = True
    if week == 6:
        $halla = True
        $teachera = True
        $cafa = True
    if week == 7:
        jump date
        

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
    menu:
        MC "Purchase a gift for?"
        "Sonic":
            if sonicLove>=2:
                show nerdy
                Sonic "Hey, look who it is. Didn’t expect to see you here. What’s up?"
                MC "Uh... I got you something."
                Sonic "Wait, for me? What’s the occasion?"
                Sonic "No way. Is this? It’s the Chaos Crystal plushie! How did you even?"
                MC "I heard you talking about it, and I figured you deserved it."
                Sonic "You... you actually listened. Nobody ever listens."
                MC "Well, I guess I’m not nobody."
                Sonic "Okay, you’ve officially leveled up to “cool friend.” Don’t let it go to your head."
                Rizz "Bro, she just friend-zoned you, but she did it with respect. I’d call that a W."
                Sonic "Seriously, though. This means a lot. Thanks."
                MC "So, does this mean I get free rings if I’m in trouble now?"
                Sonic "Only if you can keep up, slowpoke."
                Rizz "Alright, nice. You’re keeping the energy light."
                Rizz "Friend-zoned, but with potential DLC romance unlock. Stay in the game, champ."
            else:
                "not enough love"
                jump date

        "Teacher":
            if teacherLove>=2:
                show moon
                Teacher "Oh. Biggus Diggus. A classic. Are you trying to tell me you think I’m a tortured romantic soul?"
                MC "I just thought… it seemed like something you’d enjoy."
                Teacher "You know what? I might. Thank you."
                Teacher "Valentine’s Day isn’t really my thing. It always feels so… performative. But I’ll admit, this was a nice surprise."
                MC "I just thought… you deserved something today."
                Teacher "You’re… different from most of my students. It’s refreshing, really. But you didn’t have to go out of your way for me."
                Teacher "Still, I appreciate it. More than I can probably put into words right now."
                Teacher "Anyway, I should probably get back to this mountain of essays. But… thank you again."
                Teacher "Happy Valentine’s Day [name]."
                Rizz "Man, you really nailed it there. That was like using the perfect metaphor, unexpected but totally on point. Keep this up, and you might just rewrite her whole narrative."
            else:
                "not enough love"
                jump date

        "Goth":
            if gothLove>=2:
                show gothy
                MC "Hey, uh... Happy Valentine’s Day."
                Goth "Valentine’s Day? You mean that fabricated ritual designed to drain wallets and inflate expectations?"
                Rizz "Bro, she’s already going in. Stay cool, you’ve got this."
                MC "Yeah, that’s one way to put it. But, uh... I wanted to give you something."
                Goth "To me? Why? Did I hex you accidentally, or are you just feeling brave today?"
                MC "Neither... I just thought you might like it."
                Goth "A crescent moon bookmark... You’ve been paying attention. Or was this just a lucky guess?"
                MC "I noticed you reading a lot, and... it just felt like something you’d like."
                Goth "Hm. You’re observantion skills continue to impress me."
                Rizz "Bro, she smiled. Mission accomplished!"
                MC "So... you like it?"
                Goth "I do. But don’t think this makes us best friends or anything. You’re still... peculiar."
                MC "I’ll take that as a win."
                Goth "Hm. Maybe you’re not entirely insufferable. For today, at least."
                Rizz "“Not entirely insufferable”? Dude, I think that’s goth-girl for “I like you.”"
            else:
                "not enough love"
                jump date
        "Japanese":
            if JapaneseStudentLove>=2:
                show jay
                Rizz "Oh, it’s go time. She’s standing there like a character waiting for her next cutscene. You’ve got this, Romeo—don’t blow it."
                MC "Uh, hey. So, I remember you looking at this the other day, and, well... Happy Valentine’s Day."
                Japanese "(speaks in foreign language)"
                Japanese "(speaks in foreign language with gratitude) "
                Rizz "Bro, you just turned her day into a shoujo manga. I hope you’re ready for some serious gratitude."
                MC "I, uh... You’re welcome. You seemed like you really wanted it, so I figured... why not?"
                Japanese "(speaks in foreign language)"
                Rizz "She’s giving you her lucky charm, dude. That’s like, top-tier appreciation. You’re officially in the ‘good books.’"
                MC "Oh, uh, thanks. This is really nice."
                Japanese "(speaks in foreign language with gratitude)"
                Rizz "She’s heading out, but don’t worry—she’s probably walking on air right now. And guess who put her there? You, champ. Nice work."
            else:
                "not enough love"
                jump date
        "Tomboy":
            if tomboyLove>=2:
                show tomy
                MC "Yo, Tomboy. Happy Valentine’s Day."
                Tomboy "Valentine’s Day? Dude, you’re barking up the wrong tree. I don’t do that lovey-dovey Hallmark stuff."
                Rizz "Chill, bro. She’s about to eat those words."
                MC "Relax, it’s not what you think. I just figured you could use a pick-me-up."
                Tomboy "What’s this? A DIY heartbreak kit?"
                MC "Not even close. Just open it."
                Tomboy "No freaking way."
                MC "You said you were broke, and your old board was toast. Thought you might like it."
                Tomboy "“Tomboy Express”? Did you—did you get this custom-made?"
                MC "Yeah. Figured it had to match your vibe."
                Tomboy "Dude... this is insane. I don’t even know what to say."
                Rizz " She’s speechless, bro. That’s, like, the holy grail of compliments."
                MC "“Thanks” works."
                Tomboy "Yeah, thanks. Seriously. This is... probably the coolest thing anyone’s ever done for me."
                MC "Don’t get all sappy on me now. You said you’re not into lovey-dovey stuff."
                Tomboy "Oh, shut up. I can make an exception for this."
                Tomboy "This thing is sick! You didn’t cheap out, either. These wheels are legit."
                MC "Only the best for Tomboy Express."
                Tomboy "Alright, alright, you’re officially not the worst. I guess I’ll keep you around."
                Rizz " she’s hyped, and you just locked in best-bro status."
                Tomboy "You know what this means, right?"
                MC "That you owe me?"
                Tomboy "It means you’re testing this out with me. Come on, library boy, let’s see if you can keep up."
                Tomboy "Better hurry up, or I’m leaving you in the dust!"
                Rizz "Looks like you just got drafted into skate crew. Time to channel your inner Tony Hawk, champ."
            else:
                "not enough love"
                jump date
