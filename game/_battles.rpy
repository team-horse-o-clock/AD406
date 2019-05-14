label jeromeVSbandits:

    screen stats_screen_jerome:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 220 xmaximum 220
            vbox:
                text "Aziz Jerome" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value jerome_hp
                        range jerome_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[jerome_hp] / [jerome_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 220 xmaximum 220
            vbox:
                text "Haydutlar" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value bandits_hp
                        range bandits_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[bandits_hp] / [bandits_max_hp]" size 16
                    
        text "Aziz Jerome vs. Haydutlar" xalign 0.5 yalign 0.05 size 30
                    
    label battle_jerome:
        $ bandits_max_hp = 50
        $ jerome_max_hp = 90
        $ bandits_hp = bandits_max_hp
        $ jerome_hp = jerome_max_hp
        $ health_potion = 2
        
        scene bg jerome with_bandits

        show ch bandit2 at right
        with dissolve
        
        jump battle_loop_jerome

    label battle_loop_jerome:

        show screen stats_screen_jerome

        while (bandits_hp > 0) and (jerome_hp > 0):
            
            menu:
                "Saldırı yap.":
                    $ jerome_damage = renpy.random.randint(1, 5)

                    $ bandits_hp -= jerome_damage
                    anlatici "Jerome'nin saldırısı [jerome_damage] can götürdü."
                    
                "Kendini iyileştir. ([health_potion] defa kullanabilirsin)" if health_potion > 0:
                    $ jerome_hp = min(jerome_hp+50, jerome_max_hp)
                    $ health_potion-= 1
                    anlatici "Jerome, iksir kullanarak 50 can kazandı."
            
            $ bandits_damage = renpy.random.randint(15, 20)
            
            $ jerome_hp -= bandits_damage
            scene bg jerome with_bandits
            with flash
            show ch bandit1 at right
            with dissolve
            anlatici "Haydutlar saldırarak [bandits_damage] hasar verdi."
            
        hide screen stats_screen_jerome
        
        if bandits_hp <= 0:
            
            jerome "Kazandım."
                
        else:

            python:
                _preferences.set_volume('music', 0.2)

            hide ch bandit1

            play sound "sounds/haydutlar/haydut_1_3.mp3"

            $ renpy.notify("BAŞARIM KAZANILDI: Jerome! Jerome!! Jeromeeeeee!!!")

            haydut_1 "Bizi yenebileceğini mi sandın, seni yaşlı bunak! Şimdi gördün mü gününü, he? GÖRDÜN MÜ??"

            stop sound

            play sound "sounds/haydutlar/haydut_2_2.mp3"

            haydut_2 "Bağırmayı kes, seni salak. Hemen üzerindekilerini toplayalım ve buradan kaybolalım."

            stop sound

            $ jerome_IsDeath = True

            scene bg black
        
        return

    return



#/******************************************************************************************************************************************************************************/#



label trainingVS:

    screen training_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[player]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value playerTraining_hp
                        range playerTraining_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[playerTraining_hp] / [playerTraining_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[general]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value general_hp
                        range general_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[general_hp] / [general_max_hp]" size 16
                    
        text "[player] vs. [general]" xalign 0.5 yalign 0.05 size 30

    label battle_training:
        $ general_max_hp = 100
        $ playerTraining_max_hp = 100
        $ general_hp = general_max_hp
        $ playerTraining_hp = playerTraining_max_hp
        $ health_potion_training = 10
        
        scene bg pre meet_general
        
        jump battle_training_loop

    label battle_training_loop:

        show screen training_screen
        
        general "Dövüş sırasında seçebileceğin iki farklı özellik var."

        general "Karşı tarafa saldırı yapabilirsin ya da iksir içerek canını yükseltebilirsin."

        general "Oyunun ilerleyen kısımlarındaki savaşlarda, verdiğin kararların yeteneklerine farklı etkisi olacak."

        general "Şimdi senden, bana tüm gücünle saldırmanı istiyorum."

        while (general_hp > 0) and (playerTraining_hp > 0):
                        
            $ general_damage = renpy.random.randint(5, 10)
            
            menu:
                "Saldırı yap.":
                    $ playerTraining_damage = renpy.random.randint(10, 15)

                    $ general_hp -= playerTraining_damage
                    anlatici "[player]'ın saldırısı [playerTraining_damage] can götürdü."
                    
                "Kendini iyileştir. ([health_potion_training] defa kullanabilirsin)" if health_potion_training > 0:
                    $ playerTraining_hp = min(playerTraining_hp+100, playerTraining_max_hp)
                    $ health_potion_training -= 1
                    anlatici "[player], iksir kullanarak 100 can kazandı."
            
            $ playerTraining_hp -= general_damage

            scene bg pre meet_general
            with flash
            show ch general at left
            with dissolve

            anlatici "General saldırarak [general_damage] hasar verdi."
            
        hide screen training_screen
        
        if general_hp <= 0:
            
            anlatici "[player] kazandı."
                
        else:

            anlatici "[general] kazandı."

            scene bg black
        
        return

    return



#/******************************************************************************************************************************************************************************/#



label phase_one:

    screen firstmen_war_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Öncü Birlikleriniz" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value firstmen_hp
                        range firstmen_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[firstmen_hp] / [firstmen_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 400 xmaximum 400
            vbox:
                text "Roma Ordusu" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value roman_army_hp
                        range roman_army_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[roman_army_hp] / [roman_army_max_hp]" size 16
                    
        text "Öncü Birlikleriniz vs. Roma Ordusu" xalign 0.5 yalign 0.05 size 30

    label firstmen_war_battle:

        if diff_md == 0:
            $ roman_army_max_hp = 1750
        elif diff_md == 1:
            $ roman_army_max_hp = 2250
        else:
            $ roman_army_max_hp = 3000

        if spears_OnFront == True:
            $ firstmen_max_hp = 450
        elif swords_OnFront == True:
            $ firstmen_max_hp = 350
        else:
            $ firstmen_max_hp = 600
        
        $ roman_army_hp = roman_army_max_hp
        $ firstmen_hp = firstmen_max_hp

        if med_q1_IsActive == True and med_q2_IsActive == True:
            $ sup_unit = 5
        elif med_q1_IsStupid == True and med_q2_IsStupid == True:
            $ sup_unit = 1
        else:
            $ sup_unit = 3

        $ skill_point = 1
        
        scene bg firstmen_war
        with dissolve
        
        jump firstmen_war_battle_loop

    label firstmen_war_battle_loop:

        show screen firstmen_war_stat_screen

        while (roman_army_hp > 0) and (firstmen_hp > 0):
            
            $ roman_army_damage = renpy.random.randint(20, 35)

            menu:
                "Saldırı yap.":
                    $ firstmen_damage = renpy.random.randint(10, 60)
                    $ roman_army_hp -= firstmen_damage
                    anlatici "[player]'ın saldırısı [firstmen_damage] kişiyi öldürdü."
                    
                "Destek ünitesi çağır. ([sup_unit] defa kullanabilirsin)" if sup_unit > 0:
                    $ firstmen_hp = min(firstmen_hp+100, firstmen_max_hp)
                    $ sup_unit -= 1
                    anlatici "[player], destek ünitesi çağırdı."

                "{b}ÖZEL YETENEK{/b} - Mızrak fırlatma!" if spears_OnFront == True and skill_point > 0:
                    $ firstmen_damage = 150
                    $ roman_army_hp -= firstmen_damage
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı, daha güçlü bir vuruş yaptı ve [firstmen_damage] kişiyi öldürdü."

                "{b}ÖZEL YETENEK{/b} - Kalkanlar yukarıya!" if shields_OnFront == True and skill_point > 0:
                    $ roman_army_damage = 0
                    $ firstmen_damage = renpy.random.randint(20, 80)
                    $ roman_army_hp -= firstmen_damage
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve bir sonraki el, saldırıyı savuşturacak. Aynı zamanda [firstmen_damage] kişiyi öldürdü."

                "{b}ÖZEL YETENEK{/b} - Hızlı saldırı!" if swords_OnFront == True and skill_point > 0:
                    $ firstmen_damage = renpy.random.randint(0, 300)
                    $ roman_army_hp -= firstmen_damage
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve hızlı saldırı yaparak [firstmen_damage] kişiyi öldürdü."
                
            $ firstmen_hp -= roman_army_damage

            scene bg firstmen_war
            with flash

            anlatici "Roma Ordusu saldırarak [roman_army_damage] hasar verdi."
        
        hide screen firstmen_war_stat_screen
    
        if roman_army_hp <= 0:
            
            anlatici "[player] savaşı kazandı!"
            
            $ renpy.notify("BAŞARIM KAZANILDI: Muzaffer ordu.")

            $ renpy.notify("BAŞARIM KAZANILDI: Roma ordusunun büyük utancı.")

            $ war_IsWon = True
                
        else:

            general "Atlı birliklerimiz yolda, efendim. Savaşa onlarla devam edeceğiz."
            
            scene bg black
            with fade

            call phase_two from _call_phase_two
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label phase_two:

    screen cavalry_war_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Atlı Birlikleriniz" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value cav_hp
                        range cav_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[cav_hp] / [cav_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 400 xmaximum 400
            vbox:
                text "Roma Ordusu" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value roman_army_hp
                        range roman_army_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[roman_army_hp] / [roman_army_max_hp]" size 16
                    
        text "Atlı Birlikleriniz vs. Roma Ordusu" xalign 0.5 yalign 0.05 size 30

    label cavalry_war_battle:
        $ cav_max_hp = 600
        $ cav_hp = cav_max_hp

        $ skill_point += 1
        
        scene bg cavalry_war
        with dissolve
        
        jump cavalry_war_battle_loop

    label cavalry_war_battle_loop:

        show screen cavalry_war_stat_screen

        while (roman_army_hp > 0) and (cav_hp > 0):
        
            $ roman_army_damage = renpy.random.randint(30, 55)

            menu:
                "Saldırı yap.":
                    $ cav_damage = renpy.random.randint(25, 35)
                    $ roman_army_hp -= cav_damage
                    anlatici "[player]'ın saldırısı [cav_damage] kişiyi öldürdü."
                    
                "Destek ünitesi çağır. ([sup_unit] defa kullanabilirsin)" if sup_unit > 0:
                    $ cav_hp = min(cav_hp+100, cav_max_hp)
                    $ sup_unit -= 1
                    anlatici "[player], destek ünitesi çağırdı."

                "{b}ÖZEL YETENEK{/b} - Güç koşusu!" if cav_IsCorrect == True and skill_point > 0:
                    $ cav_damage = renpy.random.randint(0, 600)
                    $ roman_army_hp -= cav_damage
                    $ cav_hp -= cav_damage/2
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve [cav_damage] kişiyi öldürdü. Ancak kendi takımının yarısını da kaybetti."
            
            $ cav_hp -= roman_army_damage

            scene bg cavalry_war
            with flash

            anlatici "Roma Ordusu saldırarak [roman_army_damage] hasar verdi."
    
        hide screen cavalry_war_stat_screen

        if roman_army_hp <= 0:
            
            anlatici "[player] savaşı kazandı!"
            
            $ renpy.notify("BAŞARIM KAZANILDI: Muzaffer ordu.")

            $ war_IsWon = True
                
        else:

            general "Okçu birliklerimiz yolda, efendim. Savaşa onlarla devam edeceğiz."
            
            scene bg black
            with fade

            call phase_three from _call_phase_three
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label phase_three:

    screen archery_war_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Okçu Birlikleriniz" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value arc_hp
                        range arc_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[arc_hp] / [arc_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 400 xmaximum 400
            vbox:
                text "Roma Ordusu" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value roman_army_hp
                        range roman_army_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[roman_army_hp] / [roman_army_max_hp]" size 16
                    
        text "Okçu Birlikleriniz vs. Roma Ordusu" xalign 0.5 yalign 0.05 size 30

    label archery_war_battle:
        $ arc_max_hp = 200
        $ arc_hp = arc_max_hp

        $ skill_point += 1
        
        scene bg archery_war
        with dissolve
        
        jump archery_war_battle_loop

    label archery_war_battle_loop:

        show screen archery_war_stat_screen

        while (roman_army_hp > 0) and (arc_hp > 0):
        
            $ roman_army_damage = renpy.random.randint(30, 65)

            menu:
                "Saldırı yap.":
                    $ arc_damage = renpy.random.randint(15, 25)
                    $ roman_army_hp -= arc_damage
                    anlatici "[player]'ın saldırısı [arc_damage] kişiyi öldürdü."
                    
                "Destek ünitesi çağır. ([sup_unit] defa kullanabilirsin)" if sup_unit > 0:
                    $ arc_hp = min(arc_hp+100, arc_max_hp)
                    $ sup_unit -= 1
                    anlatici "[player], destek ünitesi çağırdı."

                "{b}ÖZEL YETENEK{/b} - Yayılım ateşi!" if bowm_IsCorrect == True and skill_point > 0:
                    $ arc_damage = arc_hp*2
                    $ roman_army_hp -= arc_damage
                    $ roman_army_damage = 0
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve [arc_damage] kişiyi öldürdü. Bir sonraki el, hasar da almayacak."

                "{b}ÖZEL YETENEK{/b} - Gizli saldırı!" if bowm_EscapeRoute == True and skill_point > 0:
                    $ arc_damage = 0
                    $ roman_army_hp -= arc_damage
                    anlatici "[player], özel yetenek kullandı ve ... Hiçbir şey olmadı."
                    $ arc_max_hp = 500
                    $ arc_hp = arc_max_hp
                    $ roman_army_damage = 0
                    $ skill_point -= 1
                    anlatici "Hayır, oldu! [player], düşmanın destek yolunu kesti ve bu sürede, birliklerini güçlendirdi."
            
            $ arc_hp -= roman_army_damage

            scene bg archery_war
            with flash

            anlatici "Roma Ordusu saldırarak [roman_army_damage] hasar verdi."
    
        hide screen archery_war_stat_screen

        if roman_army_hp <= 0:
            
            anlatici "[player] savaşı kazandı!"

            $ war_IsWon = True

            $ renpy.notify("BAŞARIM KAZANILDI: Muzaffer ordu.")
                
        else:
            
            scene bg black
            with fade

            general "Hayır.... Askerlerimiz... Ölüyorlar.... HAYIIIIIIIIR"

            $ renpy.notify("BAŞARIM KAZANILDI: Bir kabilenin çöküşü.")
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label lvl1_boss_fight:

    screen lvl1_boss_fight_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[player]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value player_hp
                        range player_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[player_hp] / [player_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Ogre Magi" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value lvl1_boss_hp
                        range lvl1_boss_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[lvl1_boss_hp] / [lvl1_boss_max_hp]" size 16
                    
        text "[player] vs. Ogre Magi" xalign 0.5 yalign 0.05 size 30

    label lvl1_boss_battle:

        $ player_max_hp = 100
        $ lvl1_boss_max_hp = 150
        
        $ player_hp = player_max_hp
        $ lvl1_boss_hp = lvl1_boss_max_hp

        $ skill_point = 3

        if med_q1_IsActive == True and med_q2_IsActive == True:
            $ h_pot = 5
        elif med_q1_IsStupid == True and med_q2_IsStupid == True:
            $ h_pot = 1
        else:
            $ h_pot = 3

        scene bg lvl1_boss
        with dissolve
        
        jump lvl1_boss_battle_loop

    label lvl1_boss_battle_loop:

        show screen lvl1_boss_fight_stat_screen

        while (lvl1_boss_hp > 0) and (player_hp > 0):
            
            $ lvl1_boss_damage = renpy.random.randint(0, 25)

            menu:
                "Saldırı yap.":
                    $ player_damage = renpy.random.randint(35, 50)
                    $ lvl1_boss_hp -= player_damage
                    anlatici "[player]'ın saldırısı [player_damage] hasar verdi."
                    
                "Canını tazele. ([h_pot] defa kullanabilirsin)" if h_pot > 0:
                    $ player_hp = min(player_hp+100, player_max_hp)
                    $ h_pot-= 1
                    anlatici "[player], can iksiri kullandı."

                "{b}ÖZEL YETENEK{/b} - Zafer çığlığı!" if war_IsWon == True and skill_point > 1:
                    $ player_damage = renpy.random.randint(0, 150)
                    $ lvl1_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], özel yetenek kullandı, daha güçlü bir vuruş yaptı ve [player_damage] hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Atıl kurt!" if puppy_IsTrue == True and skill_point > 1:
                    anlatici "Hiçbir yardım, karşılıksız kalmaz."
                    puppy "HAV HAV"
                    $ player_damage = 80
                    $ lvl1_boss_damage = 0
                    $ lvl1_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], cesur dostunun yardımıyla, hem kendini savundu, hem de garanti bir vuruş yaptı ve [player_damage] hasar verdi."
                
                "{b}ÖZEL YETENEK{/b} - Çelik kalkan savunması!" if skill_point > 0:
                    $ lvl1_boss_damage = 0
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve bir sonraki saldırıyı savuşturdu."

                "{b}ÖZEL YETENEK{/b} - Medyum'un tılsımı!" if skill_point > 0:
                    $ player_damage = lvl1_boss_hp/2
                    $ lvl1_boss_hp -= player_damage
                    $ skill_point -= 1
                    anlatici "[player], Medyum'un ona verdiği tılsımı kullanarak, rakibinin canının yarısı kadar hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Adrenalin patlaması!" if skill_point > 0:
                    $ player_damage = renpy.random.randint(0, 30)
                    $ lvl1_boss_hp -= player_damage/2
                    $ player_hp += player_damage*2
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve rakibine verdiği hasarın dört katını canına ekledi."
            
            $ player_hp -= lvl1_boss_damage

            scene bg lvl1_boss
            with flash

            anlatici "Ogre Magi saldırarak [lvl1_boss_damage] hasar verdi."
        
        hide screen lvl1_boss_fight_stat_screen
    
        if lvl1_boss_hp <= 0:
            
            anlatici "[player] düelloyu kazandı!"
            
            $ renpy.notify("BAŞARIM KAZANILDI: Savaşçı ruhlu bir lider.")

            $ player_IsAlive = True

            if emperor_IsAngry == True:
                jump emperor_boss_fight

            else:
                jump results
                
        else:

            scene bg black
            with fade
            
            $ renpy.notify("BAŞARIM KAZANILDI: Kalbimizde yaşıyor.")

            anlatici "Maalesef, [player] başaramadı. Arkasında gözü yaşlı bir kabile bırakarak dünyaya veda etti."

            $ player_IsAlive = False

            jump results
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label lvl2_boss_fight:

    screen lvl2_boss_fight_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[player]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value player_hp
                        range player_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[player_hp] / [player_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Zırhlı Ogre Magi" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value lvl2_boss_hp
                        range lvl2_boss_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[lvl2_boss_hp] / [lvl2_boss_max_hp]" size 16
                    
        text "[player] vs. Zırhlı Ogre Magi" xalign 0.5 yalign 0.05 size 30

    label lvl2_boss_battle:

        $ player_max_hp = 100
        $ lvl2_boss_max_hp = 260
        
        $ player_hp = player_max_hp
        $ lvl2_boss_hp = lvl2_boss_max_hp

        $ skill_point = 3

        if med_q1_IsActive == True and med_q2_IsActive == True:
            $ h_pot = 5
        elif med_q1_IsStupid == True and med_q2_IsStupid == True:
            $ h_pot = 1
        else:
            $ h_pot = 3

        scene bg duello
        with dissolve

        show ch lvl2_boss at right
        with dissolve
        
        jump lvl2_boss_battle_loop

    label lvl2_boss_battle_loop:

        show screen lvl2_boss_fight_stat_screen

        while (lvl2_boss_hp > 0) and (player_hp > 0):
            
            $ lvl2_boss_damage = renpy.random.randint(0, 60)

            menu:
                "Saldırı yap.":
                    $ player_damage = renpy.random.randint(25, 35)
                    $ lvl2_boss_hp -= player_damage
                    anlatici "[player]'ın saldırısı [player_damage] hasar verdi."
                    
                "Canını tazele. ([h_pot] defa kullanabilirsin)" if h_pot > 0:
                    $ player_hp = min(player_hp+100, player_max_hp)
                    $ h_pot-= 1
                    anlatici "[player], can iksiri kullandı."

                "{b}ÖZEL YETENEK{/b} - Zafer çığlığı!" if war_IsWon == True and skill_point > 1:
                    $ player_damage = renpy.random.randint(0, 150)
                    $ lvl2_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], özel yetenek kullandı, daha güçlü bir vuruş yaptı ve [player_damage] hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Atıl kurt!" if puppy_IsTrue == True and skill_point > 1:
                    anlatici "Hiçbir yardım, karşılıksız kalmaz."
                    puppy "HAV HAV"
                    $ player_damage = 80
                    $ lvl2_boss_damage = 0
                    $ lvl2_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], cesur dostunun yardımıyla hem kendini savundu, hem de garanti bir vuruş yaptı ve [player_damage] hasar verdi."
                
                "{b}ÖZEL YETENEK{/b} - Çelik kalkan savunması!" if skill_point > 0:
                    $ lvl2_boss_damage = 0
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve bir sonraki saldırıyı savuşturdu."

                "{b}ÖZEL YETENEK{/b} - Medyum'un tılsımı!" if skill_point > 0:
                    $ player_damage = lvl2_boss_hp/2
                    $ lvl2_boss_hp -= player_damage
                    $ skill_point -= 1
                    anlatici "[player], Medyum'un ona verdiği tılsımı kullanarak, rakibinin canının yarısı kadar hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Adrenalin patlaması!" if skill_point > 0:
                    $ player_damage = renpy.random.randint(0, 30)
                    $ lvl2_boss_hp -= player_damage/2
                    $ player_hp += player_damage*2
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve rakibine verdiği hasarın dört katını canına ekledi."
            
            $ player_hp -= lvl2_boss_damage

            scene bg duello
            with flash

            show ch lvl2_boss at right
            with dissolve

            anlatici "Zırhlı Ogre Magi saldırarak [lvl2_boss_damage] hasar verdi."
        
        hide screen lvl2_boss_fight_stat_screen
    
        if lvl2_boss_hp <= 0:
            
            anlatici "[player] düelloyu kazandı!"

            $ renpy.notify("BAŞARIM KAZANILDI: Savaşçı ruhlu bir lider.")

            $ player_IsAlive = True

            if emperor_IsAngry == True:
                jump emperor_boss_fight

            else:
                jump results
                
        else:

            scene bg black
            with fade

            anlatici "Maalesef, [player] başaramadı. Arkasında gözü yaşlı bir kabile bırakarak dünyaya veda etti."

            $ renpy.notify("BAŞARIM KAZANILDI: Kalbimizde yaşıyor.")

            $ player_IsAlive = False

            jump results
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label lvl3_boss_fight:

    screen lvl3_boss_fight_stat_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[player]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value player_hp
                        range player_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[player_hp] / [player_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Star Knight" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value lvl3_boss_hp
                        range lvl3_boss_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[lvl3_boss_hp] / [lvl3_boss_max_hp]" size 16
                    
        text "[player] vs. Star Knight" xalign 0.5 yalign 0.05 size 30

    label lvl3_boss_battle:

        $ player_max_hp = 100
        $ lvl3_boss_max_hp = 350
        
        $ player_hp = player_max_hp
        $ lvl3_boss_hp = lvl3_boss_max_hp

        $ skill_point = 3

        if med_q1_IsActive == True and med_q2_IsActive == True:
            $ h_pot = 5
        elif med_q1_IsStupid == True and med_q2_IsStupid == True:
            $ h_pot = 1
        else:
            $ h_pot = 3

        scene bg lvl3_boss
        with dissolve
        
        jump lvl3_boss_battle_loop

    label lvl3_boss_battle_loop:

        show screen lvl3_boss_fight_stat_screen

        while (lvl3_boss_hp > 0) and (player_hp > 0):
            
            $ lvl3_boss_damage = renpy.random.randint(0, 90)

            menu:
                "Saldırı yap.":
                    $ player_damage = renpy.random.randint(25, 35)
                    $ lvl3_boss_hp -= player_damage
                    anlatici "[player]'ın saldırısı [player_damage] hasar verdi."
                    
                "Canını tazele. ([h_pot] defa kullanabilirsin)" if h_pot > 0:
                    $ player_hp = min(player_hp+100, player_max_hp)
                    $ h_pot-= 1
                    anlatici "[player], can iksiri kullandı."

                "{b}ÖZEL YETENEK{/b} - Zafer çığlığı!" if war_IsWon == True and skill_point > 1:
                    $ player_damage = renpy.random.randint(0, 150)
                    $ lvl3_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], özel yetenek kullandı, daha güçlü bir vuruş yaptı ve [player_damage] hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Atıl kurt!" if puppy_IsTrue == True and skill_point > 1:
                    anlatici "Hiçbir yardım, karşılıksız kalmaz."
                    puppy "HAV HAV"
                    $ player_damage = 80
                    $ lvl3_boss_damage = 0
                    $ lvl3_boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], cesur dostunun yardımıyla hem kendini savundu, hem de garanti bir vuruş yaptı ve [player_damage] hasar verdi."
                
                "{b}ÖZEL YETENEK{/b} - Çelik kalkan savunması!" if skill_point > 0:
                    $ lvl3_boss_damage = 0
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve bir sonraki saldırıyı savuşturdu."

                "{b}ÖZEL YETENEK{/b} - Medyum'un tılsımı!" if skill_point > 0:
                    $ player_damage = lvl3_boss_hp/2
                    $ lvl3_boss_hp -= player_damage
                    $ skill_point -= 1
                    anlatici "[player], Medyum'un ona verdiği tılsımı kullanarak, rakibinin canının yarısı kadar hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Adrenalin patlaması!" if skill_point > 0:
                    $ player_damage = renpy.random.randint(0, 30)
                    $ lvl3_boss_hp -= player_damage/2
                    $ player_hp += player_damage*2
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve rakibine verdiği hasarın dört katını canına ekledi."
            
            $ player_hp -= lvl3_boss_damage

            scene bg lvl3_boss
            with flash

            anlatici "Star Knight saldırarak [lvl3_boss_damage] hasar verdi."
        
        hide screen lvl3_boss_fight_stat_screen
    
        if lvl3_boss_hp <= 0:
            
            anlatici "[player] düelloyu kazandı!"

            $ renpy.notify("BAŞARIM KAZANILDI: Savaşçı ruhlu bir lider.")

            $ player_IsAlive = True

            if emperor_IsAngry == True:
                jump emperor_boss_fight

            else:
                jump results
                
        else:

            scene bg black
            with fade

            anlatici "Maalesef, [player] başaramadı. Arkasında gözü yaşlı bir kabile bırakarak dünyaya veda etti."

            $ renpy.notify("BAŞARIM KAZANILDI: Kalbimizde yaşıyor.")

            $ player_IsAlive = False

            jump results
    
        return

    return



#/******************************************************************************************************************************************************************************/#



label emperor_boss_fight:

    play music "music/chapter four/ost-3.mp3"

    scene bg two_army
    with dissolve

    anlatici "Zorlu bir mücadeleden çıkan [player], karşısında hiç beklemediği birini görür."

    show ch emperor_boss at left
    with dissolve

    $ renpy.notify("BAŞARIM KAZANILDI: İmparator'un dönüşü.")

    python:
        _preferences.set_volume('music', 0.2)

    play sound "sounds/imparator_boss/imparator_boss_1.mp3"
    imparator_boss "Ah, seni zavallı, kendini bir şey zanneden, küçük sefil!"
    stop sound

    play sound "sounds/imparator_boss/imparator_boss_2.mp3"
    imparator_boss "KOSKOCA ROMA İMPARATORLUĞU İLE BAŞ EDEBİLECEĞİNİ Mİ SANIYORSUN??"
    stop sound

    play sound "sounds/imparator_boss/imparator_boss_3.mp3"
    imparator_boss "Silahını kuşan ve karşıma çık, böylelikle senin o kendini bir şey zanneden bedenini dünyadan silebileyim."
    stop sound

    python:
        _preferences.set_volume('music', 0.8)

    screen emperor_boss_screen:
        frame:
            xalign 0.01 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "[player]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value player_hp
                        range player_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[player_hp] / [player_max_hp]" size 16
                    
                    
        frame:
            xalign 0.99 yalign 0.05
            xminimum 350 xmaximum 350
            vbox:
                text "Kanlı Honorius" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 250
                        value boss_hp
                        range boss_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        
                    null width 5
                    
                    text "[boss_hp] / [boss_max_hp]" size 16
                    
        text "[player] vs. Kanlı Honorius" xalign 0.5 yalign 0.05 size 30

    label emperor_boss_battle:

        $ player_max_hp = 120
        $ player_hp = player_max_hp

        $ boss_max_hp = 550
        $ boss_hp = boss_max_hp

        $ skill_point += 3
        $ h_pot += 3

        scene bg two_army
        with dissolve

        show ch emperor_boss at left
        with dissolve
        
        jump emperor_boss_battle_loop

    label emperor_boss_battle_loop:

        show screen emperor_boss_screen

        while (boss_hp > 0) and (player_hp > 0):
            
            $ boss_damage = renpy.random.randint(35, 60)

            menu:
                "Saldırı yap.":
                    $ player_damage = renpy.random.randint(60, 110)
                    $ boss_hp -= player_damage
                    anlatici "[player]'ın saldırısı [player_damage] hasar verdi."
                    
                "Canını tazele. ([h_pot] defa kullanabilirsin)" if h_pot > 0:
                    $ player_hp = min(player_hp+120, player_max_hp)
                    $ h_pot-= 1
                    anlatici "[player], can iksiri kullandı."

                "{b}ÖZEL YETENEK{/b} - Zafer çığlığı!" if war_IsWon == True and skill_point > 1:
                    $ player_damage = renpy.random.randint(0, 150)
                    $ boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], özel yetenek kullandı, daha güçlü bir vuruş yaptı ve [player_damage] hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Atıl kurt!" if puppy_IsTrue == True and skill_point > 1:
                    anlatici "Hiçbir yardım, karşılıksız kalmaz."
                    puppy "HAV HAV"
                    $ player_damage = 80
                    $ boss_damage = 0
                    $ boss_hp -= player_damage
                    $ skill_point -= 2
                    anlatici "[player], cesur dostunun yardımıyla hem kendini savundu, hem de garanti bir vuruş yaptı ve [player_damage] hasar verdi."
                
                "{b}ÖZEL YETENEK{/b} - Çelik kalkan savunması!" if skill_point > 0:
                    $ boss_damage = 0
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve bir sonraki saldırıyı savuşturdu."

                "{b}ÖZEL YETENEK{/b} - Medyum'un tılsımı!" if skill_point > 0:
                    $ player_damage = boss_hp/2
                    $ boss_hp -= player_damage
                    $ skill_point -= 1
                    anlatici "[player], Medyum'un ona verdiği tılsımı kullanarak, rakibinin canının yarısı kadar hasar verdi."

                "{b}ÖZEL YETENEK{/b} - Adrenalin patlaması!" if skill_point > 0:
                    $ player_damage = renpy.random.randint(0, 30)
                    $ boss_hp -= player_damage/2
                    $ player_hp += player_damage*2
                    $ skill_point -= 1
                    anlatici "[player], özel yetenek kullandı ve rakibine verdiği hasarın dört katını canına ekledi."
            
            $ player_hp -= boss_damage

            scene bg two_army
            with flash

            show ch emperor_boss at left
            with dissolve

            anlatici "Kanlı Honorius saldırarak [boss_damage] hasar verdi."
        
        hide screen emperor_boss_screen
    
        if boss_hp <= 0:

            $ renpy.notify("BAŞARIM KAZANILDI: Sonsuza kadar ayakta.")
            
            anlatici "[player] düelloyu kazandı!"

            $ player_IsAlive = True
                
            jump results
                
        else:

            scene bg black
            with fade

            $ renpy.notify("BAŞARIM KAZANILDI: Asla bir imparatoru kızdırmayın.")

            anlatici "Maalesef, [player] başaramadı. Arkasında gözü yaşlı bir kabile bırakarak dünyaya veda etti."

            $ player_IsAlive = False

            jump results
    
        return
        
    return