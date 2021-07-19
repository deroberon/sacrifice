define start=0
define end=0
define intro__start=0
define tramo_a__start=0
define tramo_a__question1=0
define tramo_a__question2=0
define tramo_a__question3=0
define tramo_a__question4=0
define tramo_a__question5=0
define tramo_a__question6=0
define tramo_a__question7=0
define tramo_b__start=0
define tramo_b__question1=0
define tramo_b__question2=0
define tramo_b__question3=0
define tramo_b__question4=0
define tramo_b__question5=0
define tramo_c__start=0
define tramo_c__question1=0
define endings__start=0
define endings__end_1=0
define endings__end_2=0
define endings__end_3=0
define endings__end_4=0
define endings__end_5=0
define endings__end_6=0
define endings__special_end1=0


label start:
    $ start=start+1
    jump intro__start



label end:
    $ end=end+1
    return



define darkness=0
define suicide=0
define madness=0
define creature=Character('Creature', color="#c8ffc8")

label intro__start:
    $ intro__start=intro__start+1
    "..."
    "..."
    "You just wake up feeling a little bit dizzy..."
    "What the hell... Where am I?"
    "..."
    "The last thing you remember is to go out with your new friends."
    "Now that your eyes are beginning to get used to the darkness, you can see you are in some kind of cave."
    scene bg cave
    "Some occult symbols were drawed in the floor and you notice you cannot move. You are tied."
    "But worse than that... You can hear something on the other side of the room..."
    "What they did to me?"
    play music "audio/malignchords.ogg"
    creature "--They drugged you. And now you are my sacrifice. And I probabbly will kill you. Perhaps not. There are worse destines than death. But the way I will inflict pain to you will depends of your answers."
    "You hear an a inhuman voice coming from the other side of the cave."
    jump tramo_a__start



label tramo_a__start:
    $ tramo_a__start=tramo_a__start+1
    scene bg creature1
    jump tramo_a__question1



label tramo_a__question1:
    $ tramo_a__question1=tramo_a__question1+1
    creature "-- Tell me, disgusting human... Do you want to live?"
    menu opca1:
        "Yes":
            $ darkness=darkness-1
            $ suicide=suicide-1
            $ madness=madness-1
            jump tramo_a__question2
        "No":
            $ darkness=darkness+1
            $ suicide=suicide+1
            $ madness=madness+1
            jump tramo_a__question3




label tramo_a__question2:
    $ tramo_a__question2=tramo_a__question2+1
    creature "-- Pathetic... You want so bad to live, but you even can tell me what life is. I'll give you a chance. What is life for you?"
    menu opca2:
        "Something meaningless":
            $ suicide=suicide+1
            jump tramo_a__question4
        "Something between two existences":
            jump tramo_a__question5
        "Something unique":
            creature "You still believe you can save your life by given me optimistic answers? You are so dumb. Make me want to kill you right now."
            $ suicide=suicide-1
            jump tramo_b__start




label tramo_a__question3:
    $ tramo_a__question3=tramo_a__question3+1
    creature "--So, you want to die. Are you freely give yourself to me, human?"
    menu opca3:
        "Yes, take me":
            $ darkness=darkness+1
            $ madness=madness+1
            jump tramo_a__question6
        "No, I'm not":
            $ darkness=darkness-1
            jump tramo_a__question7




label tramo_a__question4:
    $ tramo_a__question4=tramo_a__question4+1
    creature "-- You can even make sense. If life is meaningliess, why do you want to live? Are you just afraid of me?"
    creature "-- Answer! Why do you want to live?"
    menu opca4:
        "To have fun":
            creature "-- Do you think that fun is everything in life? You ignorant fool. You are a disgrace to the human race."
            $ madness=madness-1
            jump tramo_b__start
        "To have pleasure":
            creature "-- Now we are beginning to undestand each other. You see why I'll have to kill you? This is what gives me pleasure."
            $ darkness=darkness+1
            jump tramo_b__start
        "To make something great":
            creature "-- You are useless. You always have been. You didn't anything great until now, what makes you believe that it will be different now? It won't! Nobody will remember your name after tonight."
            $ darkness=darkness-1
            jump tramo_b__start




label tramo_a__question5:
    $ tramo_a__question5=tramo_a__question5+1
    creature "So you in your inferior mind thinks that it's just something between planes... Do you at least think your life is real?"
    menu opca5:
        "Yes it is":
            creature "Do you really believe it? You are so blind as an ape. You are not different from them. Just more annoying."
            $ madness=madness-1
            jump tramo_b__start
        "No, it isn't":
            creature "Good for you. So it will be just an illusion all the pain I will make you suffer"
            $ madness=madness+1
            jump tramo_b__start




label tramo_a__question6:
    $ tramo_a__question6=tramo_a__question6+1
    creature "-- It sounds interesting. I can think a million ways to have fun with you while watch you suffer."
    creature "-- Will you do everything I order? Anything?"
    menu opca6:
        "Yes, as you command":
            creature "So pathetic... You are just a miserable slave. You really deserve to suffer."
            $ madness=madness+1
            $ darkness=darkness+1
            jump tramo_b__start
        "No, I have my limits":
            creature "So pathetic... You still think you have some control about yourself... So funny."
            $ madness=madness-1
            $ darkness=darkness-1
            jump tramo_b__start




label tramo_a__question7:
    $ tramo_a__question7=tramo_a__question7+1
    creature "-- If you are not going to die willingly, you just converted yourself in a perfect sacrifice."
    menu opta7:
        "Yes, you are correct":
            creature ": What a shame. You will even put a fight. Coward."
            $ madness=madness+1
            $ darkness=darkness+1
            jump tramo_b__start
        "No":
            creature ": So you just want to suicide. What a coincidence to hace such good friends... At least your death will make them rich. If I decide to kill you."
            $ suicide=suicide+1
            jump tramo_b__start




label tramo_b__start:
    $ tramo_b__start=tramo_b__start+1
    scene bg creature2
    jump tramo_b__question1



label tramo_b__question1:
    $ tramo_b__question1=tramo_b__question1+1
    creature "Now that I know you a little bit more, let me come closer. My name is..."
    creature "In fact... Who do you think I am?"
    menu opcb1:
        "The God":
            $ madness=madness+1
            $ darkness=darkness-1
            jump tramo_b__question2
        "A god":
            $ madness=madness-1
            jump tramo_b__question3
        "A demon":
            $ darkness=darkness-1
            jump tramo_b__question4
        "Something older":
            $ darkness=darkness+1
            $ madness=madness+1
            jump tramo_b__question5




label tramo_b__question2:
    $ tramo_b__question2=tramo_b__question2+1
    "Me? The god? I'm feeling flattered... And a little bit sad for you."
    creature "Do you think that exist such thing? God?"
    menu opcb2:
        "Yes":
            creature "Do you really think that with so many planes and this gigantic universe there exists just one of what you call god? You are so limited."
            $ suicide=suicide-1
            jump tramo_c__start
        "No":
            creature "Your mind is already rotten. You don't make sense. How can I be the God if you believe that there's no god? Probabbly I expect too much of your ape brain."
            $ madness=madness-1
            jump tramo_c__start




label tramo_b__question3:
    $ tramo_b__question3=tramo_b__question3+1
    creature "Well, if you think I'm such thing as a god, what kind of god am I?"
    menu opcb3:
        "A god of death":
            creature "Usually people projects on their gods exactly what they are searching for. In that case, perhaps I'll be the answer for your prayers."
            $ suicide=suicide+1
            jump tramo_c__start
        "A god of pleasure":
            creature "I see you have a very distorced view of what pleasure is. But perhaps you can feel the pleasure and extasis of pain, flesh and blood."
            $ darkness=darkness+1
            jump tramo_c__start




label tramo_b__question4:
    $ tramo_b__question4=tramo_b__question4+1
    creature "So, am I correct if I say you are attracted to the darkside?"
    menu opcb4:
        "Yes, I'm attracted to the dark side":
            creature "It's good to know. Darkness is all that exists when you die, and you will have a lot of time to enjoy the darkness of the void."
            $ darkness=darkness+1
            jump tramo_c__start
        "No, I just think you are evil":
            creature "Humans... always simplifying things. I'm beyond your primitive concepts of good and evil. Forget it, you will never understand."
            creature "Even if you have a lot of time to think about it. But you don't."
            $ darkness=darkness-1
            jump tramo_c__start




label tramo_b__question5:
    $ tramo_b__question5=tramo_b__question5+1
    creature "It's the first plausible answer you give me in our little conversation. So I will concede you the honor of see my true form. Do you want it?"
    menu opcb5:
        "Yes, it will be an honor":
            creature "You are fool... You really believe you deserve some honor? Learn a last thing before your destiny: be carefull with what you wish."
            jump endings__special_end1
        "No, keep it for yourself":
            creature "Wise choice. You should have used your judgment when you chose your friends. But now it's to late for this."
            $ madness=madness-1
            jump tramo_c__start




label tramo_c__start:
    $ tramo_c__start=tramo_c__start+1
    scene bg creature3
    jump tramo_c__question1



label tramo_c__question1:
    $ tramo_c__question1=tramo_c__question1+1
    creature "Now I'm already bored. So, just one final question before I decide what to do with you."
    creature "If I let you live, what will you do?"
    menu opcc1:
        "Suicide":
            creature "So it's indiferent if I kill you. You don't deserve to live."
            $ suicide=suicide+1
            jump endings__start
        "Do only good things":
            creature "Everyone said the same thing... You are a liar. And I hate liars"
            $ darkness=darkness-1
            jump endings__start
        "Serve the the dark powers":
            creature "Perhaps you can be usefull in the end... I have something in my mind..."
            $ darkness=darkness+1
            jump endings__start
        "Kill my 'friends'":
            creature "That's an excelent choice. Revenge! Nothing make us feel more alive than this!"
            $ madness=madness+1
            jump endings__start
        "Visit a doctor. I'm mad":
            creature "Do you still think that you are alucinating? I will show you what an alucination can do you."
            $ madness=madness-1
            jump endings__start
        "Enjoy life the better I can":
            creature "Pathetic. You keep believing you will have a life after I finish you."
            $ suicide=suicide-1
            jump endings__start




label endings__start:
    $ endings__start=endings__start+1
    scene bg closedeyes
    creature "Now, it's time for you to know your fate. Close your eyes."
    "You closed your eyes, and when you opened..."
    if suicide>darkness and darkness>madness :
        "->end_1"
    if suicide>madness and madness>darkness :
        "->end_2"
    if darkness>suicide and suicide>madness :
        "->end_3"
    if darkness>madness and madness>suicide :
        "->end_4"
    if madness>darkness and darkness>suicide :
        "->end_5"
    if madness>suicide and suicide>darkness :
        "->end_6"




label endings__end_1:
    $ endings__end_1=endings__end_1+1
    scene bg end1
    "You commit suicide, offering your soul to the dark forces of the universe."
    jump end



label endings__end_2:
    $ endings__end_2=endings__end_2+1
    scene bg end2
    "Your mind begins to fade. All of this... This cannot be real.. But if it is real? This thing will haunt me forever."
    "You commit suicide to escape this torment."
    jump end



label endings__end_3:
    $ endings__end_3=endings__end_3+1
    scene bg end3
    "You cut yourself and offer your blood to the dark forces of evil."
    jump end



label endings__end_4:
    $ endings__end_4=endings__end_4+1
    scene bg end4
    "You went out to kill the responsibles for this. You offer their souls to the dark forces of the universe"
    jump end



label endings__end_5:
    $ endings__end_5=endings__end_5+1
    scene bg end5
    "You went out to kill the responsibles for this. You kill one by one in a frenesi of blood and flesh. You rape them and cum over theri open guts"
    jump end



label endings__end_6:
    $ endings__end_6=endings__end_6+1
    scene bg end6
    "You was found insane, with a knife on your hand, repeating: I could not do it! I could not do it! I didn't have the courage. Kill me! Kill me please!!!"
    "You was taken and forced to live the rest of your life in an Asylum"
    jump end



label endings__special_end1:
    $ endings__special_end1=endings__special_end1+1
    scene bg especialend
    "A transformation take place in the cave..."
    "It's it's something that cannot be described.."
    "The creature.. The cave... Everything is the same thing"
    "The creature, me, the cave...."
    "Oh god, make it stop..."
    "I can't breath.."
    "I'm suffocating"
    "I'm done..."
    "It's .."
    "It's ..."
    "It's so beautiful"
    "Hahahaha..."
    "HAHAHAHAHAHAHAHAHAHAH......"
    jump end
