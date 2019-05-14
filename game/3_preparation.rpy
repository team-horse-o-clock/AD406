label preparation:

    $ renpy.notify("BAŞARIM KAZANILDI: İkinci bölüm tamamlandı.")

    play music "music/chapter three/ost-1.mp3"

    python:
        _preferences.set_volume('music', 0.2)

    scene bg pre tent # Çadırın parlayan girişi, iç kısımdan görülür.
    with dissolve

    play sound "sounds/medyum/medyum_16.mp3"

    medyum "Nasıl hissediyorsunuz, Efendim?"

    stop sound

    menu how_to_feel:

        "Ölmek için güzel bir gün":
            jump speech

        "Şanlı Roma askerleri, mutlak gücümüzün tadına bugün bakacaklar!":
            jump speech

        "Kan! Daha çok kanın dökülmesini istiyorum":
            jump speech

    label speech:

        scene bg pre speech # Kabilenin askerleri ve flamalarının gözüktüğü, herkesin hazır durumda olduğu bir sahne gelir. Oyuncu yani kabile lideri konuşma yapacaktır.
        with fade

        play sound "sounds/anlatici/32.mp3"
        anlatici "Çadırından dışarıya çıkan [player], askerlerine gaz vermek için bir konuşma yapmaya hazırlanıyordu."
        stop sound
        
        menu speech_ch:

            "Ey yurttaşlarım! Çok uzun zamandır yollardaydık. Yeri geldi yorgun düştük, yeri geldi sefa sürdük.":
                jump speech_ch2

            "Siz kendini asker zanneden çaylaklar, beni dinleyin! Bugün sizin ya ölüm ya zafer gününüz olacak.":
                jump speech_ch2

                menu speech_ch2:

                    "Sizlere olan güvenim tamdır, sonsuzdur. Bugün bu Romalı caniler, [tribe_name] gücümüzün tadına bakacaklar. Yürüyün!":
                        jump meet_the_general

                    "Korkaklığa, savaşmayana bu topraklarda ölüm yakışmaz. Ne duruyorsunuz, ölmeye gidiyoruz!":
                        jump meet_the_general

    label meet_the_general:

        $ renpy.notify("BAŞARIM KAZANILDI: Askerlerine konuşma yap.")

        scene bg pre meet_general 
        with dissolve

        show ch general at left
        with dissolve

        python:
            general = renpy.input("Günaydın, Efendi [player]! Ben sizin askeri danışmanınızım. İstediğiniz bir şekilde bana seslenebilirsiniz.")
            general = general.strip()

            if not general:
                general = "M. Kemal Atatürk"

            general = general.capitalize()

        play sound "sounds/general/general_1.mp3"

        general "[general]. İlginç ve bir o kadar da güzel bir takma isim olduğunu kabul etmek gerekiyor, Efendim. İzninizle, şimdi size nasıl aksiyona gireceğinizi öğretmek istiyorum. Başlayabilir miyim?"

        stop sound

        menu tutorial:
            "Dinliyorum.":
                jump tutorial_true
            "İhtiyacım olduğunu sanmıyorum.":
                jump tutorial_false


    label tutorial_true:

        stop music fadeout 1.0

        python:
            _preferences.set_volume('music', 0.8)

        play music "music/chapter three/ost-2.mp3"

        call trainingVS from _call_trainingVS

        stop music fadeout 1.0

        python:
            _preferences.set_volume('music', 0.2)

        play music "music/chapter three/ost-1.mp3"

        play sound "sounds/general/general_2.mp3"

        general "Beni dinlediğiniz için teşekkür ederim, Efendi [player]. Önümüzde zorlu bir savaşın olduğunu hatırlatmak istiyorum."

        stop sound

        $ renpy.notify("BAŞARIM KAZANILDI: General için küçük bir ders.")

        play sound "sounds/general/general_3.mp3"

        general "İsterseniz, savaş stratejimizi konuşmak için askeri karargaha geçelim. Komutanlarınız sizleri bekliyor."

        stop sound

        jump war_room

    label tutorial_false:

        play sound "sounds/general/general_4.mp3"

        $ renpy.notify("BAŞARIM KAZANILDI: Korkak.")

        general "Liderimiz en iyisini bilir."

        stop sound

        play sound "sounds/general/general_3.mp3"

        general "İsterseniz, savaş stratejimizi konuşmak için askeri karargaha geçelim. Komutanlarınız sizleri bekliyor."

        stop sound

        jump war_room

    label war_room:

        scene bg pre headquarters # Askeri karargah
        with dissolve

        call preparation_war_room_txt1 from _call_preparation_war_room_txt1

        menu bowmans:
            "Bir meydan savaşı olacağını düşünürsek, sizce asıl okçu birliğimizi nereye yerleştirmeliyiz?"

            "Meydanı gören tepelere yerleştirin!":
                $ bowm_IsCorrect = False

            "Kalkanlı birliklerin arkasına yerleştirin!":
                $ bowm_IsCorrect = True

            "Öncü birliklerin yanına yerleştirin!":
                $ bowm_IsCorrect = False

        play sound "sounds/okcu_komutan/okcu_komutan_4.mp3"

        okcu_komutan "Oldukça iyi bir strateji olduğunu söylemem gerekiyor, Efendim."

        stop sound

        menu bowmans_repl:
            "Peki, yardımcı okçuları nereye konuşlandırmak istersiniz?"

            "Düşman askerlerin kaçma ihtimaline karşılık, kaçış rotalarını tutsunlar!":
                $ bowm_EscapeRoute= True

            "Benim çadırımı korusunlar!":
                $ bowm_ProtectTent = True

        call preparation_war_room_txt2 from _call_preparation_war_room_txt2

        menu cavalries_repl:
            "Sizce, nasıl bir strateji izlemeliyiz?"

            "Okçuların korunması için kullan!":
                $ cav_IsCorrect = True

            "En ön kısımda hücum edip, düşman askerlerine zorluk çıkarttır!":
                $ cav_IsCorrect = True

            "Dost ya da düşman, kaçan askerleri öldürmek için kullan!":
                $ cav_IsCorrect = False

        menu gen_repl:
            "Ve son olarak, baş komutanımız [player], öncü birliklerimizin hangi askeri sınıftan oluşmasını ister?"

            "Mızraklı birlikleri en ileriye sürün!":
                $ spears_OnFront = True

            "Kılıçlı birlikleri en ileriye sürün!":
                $ swords_OnFront = True

            "Kalkanlı birlikleri en ileriye sürün!":
                $ shields_OnFront = True

        show ch general at left
        with dissolve

        general "Bu kararınıza kesinlikle katılıyorum, Efendim."

        python:
            _preferences.set_volume('music', 0.2)

        stop music fadeout 1.0

        $ renpy.notify("BAŞARIM KAZANILDI: Savaşa hazır!")

        menu war_dec:
            "Savaş alanına hem geçmek ister misiniz?"

            "Evet, savaşmak için sabırsızlanıyorum!":
                call endgame from _call_endgame

            "Hayır, verdiğim kararları tekrar gözden geçirmek istiyorum.":
                $ bowm_IsCorrect = False
                $ bowm_EscapeRoute= False
                $ bowm_ProtectTent = False
                $ cav_IsCorrect = False
                $ spears_OnFront = False
                $ swords_OnFront = False
                $ shields_OnFront = False

                jump war_room

    return

#--------------------------------------------------------------------------DİYALOGLAR-----------------------------------------------------------------------------------------------#

label preparation_war_room_txt1:

    show ch general at left
    with dissolve

    play sound "sounds/general/general_5.mp3"

    general "Savaşın en kritik kısmına sıra geldi, değil mi Efendim?"

    stop sound

    play sound "sounds/general/general_6.mp3"

    general "Size hatırlatmama izin verin. Burada alacağınız kararlar, askerlerimizin ve elbette kabilemizin geleceğinde çok önemli bir rol oynayacak."

    stop sound

    play sound "sounds/general/general_7.mp3"

    general "Roma İmparatorluğu’nun sınır güçleri, her ne kadar eskisi kadar güçlü olmasa da, eğer ki yanlış bir strateji izlersek, bizi büyük bir yenilgiye uğratabilir."

    stop sound

    play sound "sounds/general/general_8.mp3"

    general "Seçimlerinizi yaparken iki kere düşünmenizi ve dikkatli karar vermenizi öneriyorum, Yüce [player]."

    stop sound

    hide ch general

    show ch veL_decumius at right
    with dissolve

    play sound "sounds/okcu_komutan/okcu_komutan_1.mp3"

    okcu_komutan "İyi günler, Efendim. Ben okçularınızın komutanı, Vel Decumius."

    stop sound

    play sound "sounds/okcu_komutan/okcu_komutan_2.mp3"

    okcu_komutan "Okçu birliğimizin, nasıl bir taktik izlemesini istediğiniz hakkında size birkaç sorum olacak. Hemen başlayalım."

    stop sound

    play sound "sounds/okcu_komutan/okcu_komutan_3.mp3"

    okcu_komutan "Ren Nehri’nin civar koşullarına baktığımızda, yükseltilerin az, düzlüklerin fazla olduğunu rahatlıkla söyleyebilirim, Efendim."

    stop sound

    return


label preparation_war_room_txt2:

    play sound "sounds/okcu_komutan/okcu_komutan_5.mp3"

    okcu_komutan "Bu taktik ile yenilmemizin imkansız olduğunu söyleyebilirim, Efendi [player]! İzninizle, çekiliyorum."

    stop sound

    hide ch veL_decumius

    show ch vibius_canius at right
    with dissolve

    play sound "sounds/suvari_komutan/suvari_komutan_1.mp3"

    suvari_komutan "Günaydın, Komutanım. Ben atlı birliklerinizin komutanı, Vibius Canius."

    stop sound

    play sound "sounds/suvari_komutan/suvari_komutan_2.mp3"

    suvari_komutan "Süvari birliğimizin, nasıl bir taktik izlemesini istediğiniz hakkında size birkaç sorum olacak. Hemen başlayalım."

    stop sound

    play sound "sounds/suvari_komutan/suvari_komutan_3.mp3"

    suvari_komutan "Meydan savaşlarının atlı birlikler için çok zor olduğunu söylemem gerekiyor."

    stop sound

    play sound "sounds/suvari_komutan/suvari_komutan_4.mp3"

    suvari_komutan "Özellikle çok askerin aynı alanda bulunması ve daralan bölge sebebiyle, süvarilerimizin nasıl bir yol izleyeceğine tam emin olamıyorum."
    
    stop sound

    hide ch vibius_canius

    return