label endgame:

    play music "music/chapter four/ost-1.mp3"

    $ renpy.notify("BAŞARIM KAZANILDI: Üçüncü bölüm tamamlandı.")

    scene bg two_army # İki tarafın ordularının gözüktüğü bir görsel

    general "Askerlerimiz savaşa hazır ve emirlerinizi bekliyor, Efendi [player]."

    menu war_begins:
        "Son bir sözünüz var mı?"

        "{b}HÜCUUUUM{/b}":
            jump war

        "Bu oyuna daha fazla katlanamayacağım artık! Ben bırakıyorum :'(":
            call credits from _call_credits

    label war:

        python:
            _preferences.set_volume('music', 0.8)

        call phase_one from _call_phase_one

        if not bowm_ProtectTent == True:
            jump duello
        else:

            scene bg pre boss_fight
            with dissolve

            python:
                _preferences.set_volume('music', 0.2)

            play sound "sounds/anlatici/33.mp3"
            anlatici "Savaşın devam ettiği bir anda, [tribe_name] lideri [player]'ın çadırına doğru güçlü bir düşman yaklaşmaktaydı."
            stop sound

            anlatici "Ancak [player] zeki biriydi. Tehditi daha önceden görüp, okçularını, kendisini koruması için görevlendirmişti."

            anlatici "Bu sebepten dolayı, saldıran askerler başarılı olamadı."

            $ renpy.notify("BAŞARIM KAZANILDI: Üstün zeka.")

            stop music fadeout 1.0

            jump results

        return

    label duello:

        python:
            _preferences.set_volume('music', 0.2)

        play music "music/chapter four/ost-2.mp3"

        scene bg pre boss_fight
        with dissolve

        play sound "sounds/anlatici/33.mp3"
        anlatici "Savaşın devam ettiği bir anda, [tribe_name] lideri [player]'ın çadırına doğru güçlü bir düşman yaklaşmaktaydı."
        stop sound

        play sound "sounds/anlatici/34.mp3"
        anlatici "Belki de bu, [player]'ın verdiği kararların bir sonucu olacaktır."
        stop sound
        
        python:
            _preferences.set_volume('music', 0.8)

        if diff_md == 0:
            call lvl1_boss_fight from _call_lvl1_boss_fight
        
        elif diff_md == 1:
            call lvl2_boss_fight from _call_lvl2_boss_fight

        elif diff_md == 2:
            call lvl3_boss_fight from _call_lvl3_boss_fight

        else:
            jump start

    label results:

        stop music fadeout 1.0

        play music "music/epilogue/ost-1.mp3"

        python:
            _preferences.set_volume('music', 0.2)

        if war_IsWon == True and player_IsAlive == True and tribe_alan == True:
            jump alan_victory_playerIsAlive

        elif war_IsWon == True and player_IsAlive == False and tribe_alan == True:
            jump alan_victory_playerIsDead

        elif war_IsWon == False and player_IsAlive == True and tribe_alan == True:
            jump alan_lost_playerIsAlive

        elif war_IsWon == True and player_IsAlive == True and tribe_saxon == True:
            jump saxon_victory_playerIsAlive

        elif war_IsWon == True and player_IsAlive == False and tribe_saxon == True:
            jump saxon_victory_playerIsDead

        elif war_IsWon == False and player_IsAlive == True and tribe_saxon == True:
            jump saxon_lost_playerIsAlive

        if war_IsWon == True and player_IsAlive == True and tribe_vandal == True:
            jump vandal_victory_playerIsAlive

        elif war_IsWon == True and player_IsAlive == False and tribe_vandal == True:
            jump vandal_victory_playerIsDead

        elif war_IsWon == False and player_IsAlive == True and tribe_vandal == True:
            jump vandal_lost_playerIsAlive

        else:
            jump worst_ending

        return

    return