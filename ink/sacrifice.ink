VAR darkness=0
VAR suicide=0
VAR madness=0

##CH: define creature=Character('Creature', color="#ff0000")

-> intro.start

=== intro ===
= start
...
...
You just wake up feeling a little bit dizzy... 
What the hell... Where am I? 
...
The last thing you remember is to go out with your new friends. 
Now that your eyes are beginning to get used to the darkness, you can see you are in some kind of cave.
##CO: scene bg cave
Some occult symbols were drawed in the floor and you notice you cannot move. You are tied.
But worse than that... You can hear something on the other side of the room... 
What they did to me?
##CO: scene bg creature1
##CO: play music "audio/malignchords.ogg"
 They drugged you. And now you are my sacrifice. And I probably will kill you. Perhaps not. There are worse destines than death. But the way I will inflict pain to you will depends of your answers.  #CH:creature

You hear an a inhuman voice coming from the other side of the cave. 
->tramo_a.start

=== tramo_a ===
= start

-> tramo_a.question1
= question1
Tell me, disgusting human... Do you want to live? #CH:creature
-(opca1)
    *[Yes] 
        ~darkness=darkness-1
        ~suicide=suicide-1
        ~madness=madness-1
        ->tramo_a.question2
    *[No]
        ~darkness=darkness+1
        ~suicide=suicide+1
        ~madness=madness+1
        ->tramo_a.question3

= question2
Pathetic... You want so bad to live, but you even can tell me what life is. I'll give you a chance. What is life for you? #CH:creature
    -(opca2)
    *[Something meaningless]
        ~suicide=suicide+1
        ->question4
    *[Something between two existences]
        ->question5
    *[Something unique] You still believe you can save your life by given me optimistic answers? You are so dumb. Make me want to kill you right now. #CH:creature
        ~suicide=suicide-1 
        ->tramo_b.start
    
=question3
So, you want to die. Are you freely give yourself to me, human? #CH:creature
    -(opca3)
    *[Yes, take me] 
        ~darkness=darkness+1
        ~madness=madness+1
        -> question6
    *[No, I'm not]
        ~darkness=darkness-1
        -> question7

=question4
You can even make sense. If life is meaningless, why do you want to live? Are you just afraid of me? #CH:creature
Answer! Why do you want to live? #CH:creature
    -(opca4)
    *[To have fun] Do you think that fun is everything in life? You ignorant fool. You are a disgrace to the human race. #CH:creature
        ~madness=madness-1
        -> tramo_b.start
    *[To have pleasure] Now we are beginning to undestand each other. You see why I'll have to kill you? This is what gives me pleasure. #CH:creature
        ~darkness=darkness+1
        -> tramo_b.start
    *[To make something great] You are useless. You always have been. You didn't anything great until now, what makes you believe that it will be different now? It won't! Nobody will remember your name after tonight. #CH:creature
        ~darkness=darkness-1
        ->tramo_b.start
    
=question5
So you in your inferior mind thinks that it's just something between planes... Do you at least think your life is real? #CH:creature
    -(opca5)
    *[Yes it is] Do you really believe it? You are so blind as an ape. You are not different from them. Just more annoying. #CH:creature
        ~madness=madness-1
        ->tramo_b.start
    *[No, it isn't] Good for you. So it will be just an illusion all the pain I will make you suffer #CH:creature
        ~madness=madness+1
        ->tramo_b.start


=question6
It sounds interesting. I can think a million ways to have fun with you while I watch you suffer. #CH:creature
Will you do everything I order? Anything? #CH:creature
    -(opca6)
    *[Yes, as you command] So pathetic... You are just a miserable slave. You really deserve to suffer. I can bet you want it. #CH:creature
        ~madness=madness+1
        ~darkness=darkness+1
        ->tramo_b.start
    *[No, I have my limits] So pathetic... You still think you have some control about yourself... So funny. #CH:creature
        ~madness=madness-1
        ~darkness=darkness-1
        ->tramo_b.start


=question7
If you are not going to die willingly, you just converted yourself in a perfect sacrifice. #CH:creature
    -(opta7)
    *[Yes, you are correct]: What a shame. You will even put a fight. Coward. #CH:creature
        ~madness=madness+1
        ~darkness=darkness+1
        ->tramo_b.start
    *[No]: So you just want to suicide. What a coincidence to have such good friends... At least your death will make them rich. If I decide to kill you. #CH:creature
        ~suicide=suicide+1
        ->tramo_b.start


=== tramo_b ===
= start
-> question1

= question1
Now that I know you a little bit more, let me come closer. 
##CO: scene bg creature2
My name is... #CH:creature
In fact... Who do you think I am? #CH:creature
    -(opcb1)
    *[The God]
        ~madness=madness+1
        ~darkness=darkness-1
        ->question2
    *[A god]
        ~madness=madness-1
        ->question3
    *[A demon]
        ~darkness=darkness-1
        ->question4
    *[Something older]
        ~darkness=darkness+1
        ~madness=madness+1
        ->question5

=question2
Me? The god? I'm feeling flattered... And a little bit sad for you. 
Do you think that exist such thing? God? #CH:creature
    -(opcb2)
    *[Yes] Do you really think that with so many planes and this gigantic universe there, there are just one of what you call god? You are so limited. #CH:creature
        ~suicide=suicide-1
        ->tramo_c.start
    *[No] Your mind is already rotten. You don't make sense. How can I be the God if you believe that there's no god? Probably I expect too much of your ape's brain. #CH:creature
        ~madness=madness-1
        ->tramo_c.start 


=question3
Well, if you think I'm such thing as a god, what kind of god am I? #CH:creature
    -(opcb3)
    *[A god of death] Usually people projects on their gods exactly what they are searching for. In that case, perhaps I'll be the answer for your prayers. #CH:creature
        ~suicide=suicide+1
        ->tramo_c.start
    *[A god of pleasure] I see you have a very distorced view of what pleasure is. But perhaps you can feel the pleasure and extasis of pain, flesh and blood. #CH:creature
        ~darkness=darkness+1
        ->tramo_c.start

=question4
So, am I correct if I say you are attracted to the darkside? #CH:creature
    -(opcb4)
    *[Yes, I'm attracted to the dark side] It's good to know. Darkness is all that exists when you die, and you will have a lot of time to enjoy the darkness of the void. #CH:creature
        ~darkness=darkness+1
        ->tramo_c.start
    *[No, I just think you are evil] Humans... always simplifying things. I'm beyond your primitive concepts of good and evil. Forget it, you will never understand. #CH:creature
        Even if you had a lot of time to think about it. But you don't. #CH:creature
        ~darkness=darkness-1
        ->tramo_c.start

=question5
It's the first plausible answer you give me in our little conversation. So I will concede you the honor of see my true form. Do you want it? #CH:creature
    -(opcb5)
    *[Yes, it will be an honor] You are fool... You really believe you deserve some honor? Learn a last thing before your destiny: be carefull with what you wish. #CH:creature
    ->endings.special_end1
    *[No, keep it for yourself] Wise choice. You should have used your judgment when you chose your friends. But now it's to late for this. #CH:creature
    ~madness=madness-1
    ->tramo_c.start


=== tramo_c===
=start
##CO: scene bg creature3
->question1

= question1
Now I'm already bored. So, just one final question before I decide what to do with you. #CH:creature
If I let you live, what will you do? #CH:creature
    -(opcc1)
    *[Suicide] So it's indiferent if I kill you. You don't deserve to live. #CH:creature
    ~suicide=suicide+1
    ->endings.start
    *[Do only good things] Everyone said the same thing... You are a liar. And I hate liars #CH:creature
    ~darkness=darkness-1
    ->endings.start
    *[Serve the the dark powers] Perhaps you can be usefull in the end... I have something in my mind...  #CH:creature
    ~darkness=darkness+1
    ->endings.start
    *[Kill my 'friends'] That's an excelent choice. Revenge! Nothing make us feel more alive than this! #CH:creature
    ~madness=madness+1
    ->endings.start
    *[Visit a doctor. I'm mad] Do you still think that you are alucinating? I will show you what an alucination can do you. #CH:creature
    ~madness=madness-1
    ->endings.start
    *[Enjoy life the better I can] Pathetic. You keep believing you will have a life after I finish you.  #CH:creature
    ~suicide=suicide-1
    ->endings.start
    

=== endings ===
=start
##CO: scene bg closedeyes
Now, it's time for you to know your fate. Close your eyes. #CH:creature
You close your eyes...
...
And when you open them...
...

{suicide>darkness and darkness>madness: ->end_1 }
{suicide>madness and madness>darkness: ->end_2 }

{darkness>suicide and suicide>madness: ->end_3}
{darkness>madness and madness>suicide: ->end_4}

{madness>darkness and darkness>suicide: ->end_5}
{madness>suicide and suicide>darkness: ->end_6}


= end_1
##CO: scene bg end1
You notice you are untied.
A knife is in your hands.
You know what you have to do. #CH: creature
You stab yourself direct in the heart while thinking about serving this creature.
You offered your soul to the dark forces of the universe.
You die.
THE END
->END

= end_2
##CO: scene bg end2
You notice you are untied.
A knife is in your hands.
The creature isn't there.
Your mind begins to fade. All of this... This cannot be real.. But if it is real? This thing will haunt me forever. 
And even if it's not real, it will haunt me forever... I know it!
You pickup the knife and cut your throat seeing your blood spills while everything is becoming darker...
You die.
THE END
->END

= end_3
##CO: scene bg end3
You notice you are untied.
A knife is in your hands.
The creature isn't there.
Perhaps it was a dream, but it seems so real...
Perhaps it was just a warning. You have to do your offerings to the dark powers...
Offerings of blood.
You pickup the knife...
And cut yourself offering your blood to the dark forces of evil, while tracing strange symbols on the floor. 
You will serve them. Forever. Your soul belong to them.
THE END
->END

= end_4
##CO: scene bg end4
You notice you are untied.
A knife is in your hands.
The creature isn't there.
It allowed you to live, but you know what you should do.
The forces of evil never forgive, they never forget.
They demand blood. And if it's not your blood, it have to be someone else's blood.
You go out of the cave to hunt and kill the responsibles for this. 
You will offer their souls to the dark forces of the universe.
THE END
->END

= end_5
##CO: scene bg end5
You notice you are untied.
A knife is in your hands.
You know what you have to do. Do it, and have fun doing it. #CH:creature
You thank the creature and go out of the cave.
To hunt the responsibles for this. 
You tracked and kill one by one in an extasy of blood and flesh. 
You rape their dead bodies and cum over their open guts.
When the police catch you, you was naked, covered in blood and laughing insanely.
You was taken and forced to live the rest of your life in an Asylum
THE END
->END

= end_6
##CO: scene bg end6
You notice you are untied.
A knife is in your hands.
The creature isn't there.
You stay there, unable to move.
But you know what you should do.
...
You was found in the cave days later...
with a knife on your hand, repeating: I could not do it! I could not do it! I didn't have the courage. Kill me! Kill me please!!! 
You was taken and forced to live the rest of your life in an Asylum
THE END
->END

= special_end1
##CO: scene bg especialend
A transformation take place in the cave... 
It's... 
It's something that cannot be described.. 
The creature.. The cave... Everything is the same thing 
The creature, me, the cave.... 
Oh god, make it stop... 
I can't breath..
I'm suffocating
I'm done... 
It's ..
It's ...
It's so beautiful
Hahahaha...
HAHAHAHAHAHAHAHAHAHAH......
You were embraced by madness and consumed by the creature.
THE END
->END