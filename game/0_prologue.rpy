# Giriş bölümü için düşünülen mevsim: Sonbahar

label prologue:

    $ renpy.notify("BAŞARIM KAZANILDI: Oyuna hoşgeldin :)")

    scene bg jerome riding_horse # Yağmurlu bir havada, yan kamera açısından, Jerome'nin at üzerindeki görseli.
    with fade

    call prologue_txt1 from _call_prologue_txt1

    scene bg world europe_map # Avrupa haritası ekrana gelir, kabilelerin ilerleyişi için animasyon yapılabilir. 
    with dissolve

    call prologue_txt2 from _call_prologue_txt2

    scene bg jerome from_face # Jerome'nin ön taraftan yüzünün belli olduğu görsel.
    with dissolve

    call prologue_txt3 from _call_prologue_txt3

    scene bg jerome choose_path # Jerome'nin karşısına iki seçenekli yol ayrımı gelir, ya yolunu kısaltmak için tehlikeli dağdan geçecek, ya da uzunluğuna bakmadan gölün kenarından ilerleyecektir.
    with dissolve

    call prologue_txt4 from _call_prologue_txt4

    menu palatine_hill_path:

        "Sanırım gölün kenarından gitmek, benim için daha güvenli olacaktır.":
            jump lakeside
        
        "Bu raporun önemi çok büyük, en kısa yolu tercih edip dağlardan geçmek zorundayım!":
            jump ridgeway

    label lakeside:

        $ renpy.notify("BAŞARIM KAZANILDI: İlk seçim her zaman çok özeldir <3")

        scene bg jerome near_lakeside # Jerome'nin göl kenarında yolculuk yaptığı bir görsel.
        with fade

        call prologue_lakeside_txt1 from _call_prologue_lakeside_txt1

        stop music fadeout 1.0

        call intro from _call_intro

        return

    #-------------------------------------------------------------------------------------------------------------#

    label ridgeway:

        $ renpy.notify("BAŞARIM KAZANILDI: İlk seçim her zaman çok özeldir <3")

        scene bg jerome on_ridgeway # Jerome'nin dağ yolunda yolculuk yaptığı bir görsel.
        with fade

        play sound "sounds/anlatici/yenikayit18.mp3"
        anlatici "Raporun zamanında İmparator'a verilmesinin, imparatorluğun kaderini etkileyeceğini düşünen Aziz Jerome, tüm riskleri göze alarak dağlara giden patikaya saptı."
        stop sound

        stop music fadeout 1.0

        play music "music/prologue/ost-3.mp3"

        scene bg jerome with_bandits # Patikanın karanlık ve az aydınlanan bir yerinde, karşısına iki haydut çıkar
        with dissolve

        call prologue_bandits_txt1 from _call_prologue_bandits_txt1

        menu ridgeway_path:

            "{b}(HAYDUTLARA SALDIR){/b}":
                jump jerome_fight

            "{b}(KAÇMAYA ÇALIŞ){/b}":
                jump jerome_escape

        label jerome_fight:

            stop music fadeout 1.0

            python:
                _preferences.set_volume('music', 0.8)

            play music "music/prologue/ost-4.mp3"

            call jeromeVSbandits from _call_jeromeVSbandits

            stop music fadeout 1.0

            call intro from _call_intro_1

        #*********************************************************************#

        label jerome_escape:

            scene bg jerome try_escape # Jerome'nin atıyla haydutlardan kaçmaya çalıştığını gösteren bir görsel.
            with fade

            play music "music/prologue/ost-5.mp3"

            play sound "sounds/jerome/jerome_3.mp3"
            jerome "Deeeh, Roach! Buradan hemen uzaklaşmamız gerekiyor!"
            stop sound

            play sound "sounds/horse/1.mp3"
            horse "Aaghihihih !!!"
            stop sound

            $ a = renpy.random.choice(['success', 'fail'])
            
            if (a == 'fail'):
                jump not_escaped
            else:
                jump escaped

            label escaped:

                scene bg jerome escaping # Jerome ve Roach'un, haydutları arkada bırakarak mağaranın çıkışına doğru gittiği görülür.
                with dissolve

                play sound "sounds/anlatici/yenikayit19.mp3"
                anlatici "Atını tam zamanında şaha kaldıran Aziz Jerome, haydutları arkasında bırakarak mağaranın çıkışına doğru yöneldi."
                stop sound

                scene bg jerome near_lakeside # Jerome'nin at üzerinde gittiği bir görsel.
                with fade

                $ renpy.notify("BAŞARIM KAZANILDI: Şans kapıyı çalınca.")
                
                call prologue_jerome_escaped from _call_prologue_jerome_escaped

                stop music fadeout 1.0

                $ diff_md += 1

                call intro from _call_intro_2

                return

            #//////////////////////////////////////////////////////////////////#

            label not_escaped:

                scene bg jerome escaping # Jerome ve Roach'un, haydutları arkada bırakarak mağaranın çıkışına doğru gittiği görülür.
                with dissolve

                play sound "sounds/anlatici/yenikayit19.mp3"
                anlatici "Atını tam zamanında şaha kaldıran Aziz Jerome, haydutları arkasında bırakarak mağaranın çıkışına doğru yöneldi."
                stop sound

                scene bg black
                with fade

                stop music fadeout 1.0

                play music "music/prologue/ost-6.mp3"

                anlatici "Ancak...."

                scene bg jerome hit_arrow # Jerome'nin sırtından ok yediğini gösteren bir sahne.
                with flash

                play sound "sounds/jerome/jerome_6.mp3"
                jerome "AAAAAAH !!!"
                stop sound

                play sound "sounds/horse/3.mp3"
                horse "Ioohoho !!!"
                stop sound

                scene bg jerome killed # Jerome'nin cesedine bakan iki haydut.
                with fade
                
                play sound "sounds/haydutlar/haydut_1_3.mp3"
                $ renpy.notify("BAŞARIM KAZANILDI: Jerome! Jerome!! Jeromeeeeee!!!")
                haydut_1 "Bizden kaçmaya çalışmayacaktın, seni yaşlı bunak! Şimdi gördün mü gününü, he? GÖRDÜN MÜ??"
                stop sound

                play sound "sounds/haydutlar/haydut_2_2.mp3"
                haydut_2 "Bağırmayı kes, seni salak. Hemen üzerindekilerini toplayalım ve buradan kaybolalım."
                stop sound

                $ jerome_IsDeath = True

                stop music fadeout 1.0

                call intro from _call_intro_3

                return

        return

    return

label intro:

    # Oyun için hazırlanmış özel görsel ve müzik girer.

    stop music fadeout 1.0

    scene bg black
    with dissolve

    $ renpy.movie_cutscene('videos/intro.webm')

    call medium from _call_medium

    return

#--------------------------------------------------------------------------DİYALOGLAR-----------------------------------------------------------------------------------------------#

label prologue_txt1:

    play sound "sounds/anlatici/yenikayit5.mp3"
    anlatici "Yaşlı bir adam, atının üzerinde nefes nefese kalmış bir şekilde, Roma İmparatoru'nun yaşadığı Palatine Hill'e doğru son sürat yol almaktaydı."
    stop sound 
    play sound "sounds/anlatici/yenikayit6.mp3"
    anlatici "Güneş takvimine göre, yılın sonlarına doğru yaklaşılmaktaydı. Havalar her zamankinden daha soğuktu, rüzgarlar ise çok şiddetli esiyordu."
    stop sound 
    play sound "sounds/anlatici/yenikayit7.mp3"
    anlatici "Ancak önümüzdeki kış, Doğu'dan yaklaşan barbarların saldırıları yüzünden, hiç beklenmedik kadar karanlık ve kanlı olacaktı."
    stop sound 

    return

label prologue_txt2:

    play sound "sounds/anlatici/yenikayit8.mp3"
    anlatici "Yıllardır sürmekte olan barbar istilaları, her zamankinden daha sık yaşanmaya başlamıştı."
    stop sound 
    play sound "sounds/anlatici/yenikayit9.mp3"
    anlatici "Roma İmparatorluğu'nun sınırlarında, Ren ve Tuna nehirlerinin ötesinde yaşayan insanlar, kabileler halinde toplanmış ve yetersiz kaynaklarla, yoksul topraklarla geçimlerini sağlamaya çalışıyorlardı."
    stop sound 
    play sound "sounds/anlatici/yenikayit10.mp3"
    anlatici "Fakat Doğu'dan gelen Hun baskısına artık dayanamayan üç kabile, {b}Saksonlar, Vandallar{/b} ve {b}Alanlar,{/b} bağımsızlıklarını sürdürebilmek için Roma İmparatorluğu'nun sınırlarına akın etmekteydi."
    stop sound 
    play sound "sounds/anlatici/yenikayit11.mp3"
    anlatici "Konseyin verdiği kesin karar sonucu, bu kabilelerin imparatorluk sınırlarına sığınmasına izin vermeyen Roma'yı, önümüzdeki kış aylarında büyük bir savaş bekliyordu."
    stop sound 

    return

label prologue_txt3:

    play sound "sounds/anlatici/yenikayit12.mp3"
    anlatici "Aziz Jerome, atın üzerindeki yaşlı adam, elindeki raporu bir an önce İmparator Honorius'a göstermesi gerekiyordu."
    stop sound

    play sound "sounds/anlatici/soluksoluga.mp3"
    anlatici "Soluk soluğa dedi ki,"
    stop sound

    play sound "sounds/jerome/jerome_1.mp3"
    jerome "Rrrrr, havalar ne kadar da soğudu. Artık at üzerinde yolculuk yapamayacak kadar yaşlı olduğumu kabul etmem gerekiyor. Bir sonraki sefer, genç ulaklardan birini yollarsam daha iyi olacak sanırım."
    stop sound

    play sound "sounds/jerome/jerome_2.mp3"
    jerome "Ah, neler saçmalıyorum! Bu raporda geçenleri İmparator'a izah edebilecek bir tek ben varım bu dünyada. Yapılması gerekeni yapmak için, bir tek benim sözüme güveneceğini biliyorum."
    stop sound

    return

label prologue_txt4:

    play sound "sounds/anlatici/yenikayit14.mp3"
    anlatici "Aziz Jerome kendi kendine konuşurken önüne, seçim yapması gereken bir yol ayrımı gelmişti."
    stop sound

    play sound "sounds/anlatici/yenikayit15.mp3"
    anlatici "Ya yolunu kısaltmak için zorlu bir dağ yolculuğunu seçecekti, ya da mesafesine bakmadan gölün kenarından ilerleyecekti."
    stop sound
    
    return

label prologue_lakeside_txt1:

    play sound "sounds/anlatici/yenikayit16.mp3"
    anlatici "Atını son sürat Palatine Hill'e sürmeye devam eden Aziz Jerome, kendisi için daha güvenli olduğunu düşündüğü sahil yolunu tercih etmişti."
    stop sound

    play sound "sounds/anlatici/yenikayit17.mp3"
    anlatici "Daha huzur dolu bir yolculuk yapabilmek için yolunu günlerce uzatan yaşlı adam, önümüzdeki günlerde bu kararından çok pişman olacaktı."
    stop sound

    return

label prologue_bandits_txt1:

    show ch bandit1 at right
    with dissolve

    play sound "sounds/haydutlar/haydut_1_1.mp3"
    haydut_1 "HEEEY!"
    stop sound

    show ch bandit2 at right
    with dissolve

    play sound "sounds/haydutlar/haydut_2_1.mp3"
    haydut_2 "Ha ha ha. Bak sen şu işe. Sanırım Tanrı bize, soyabilmemiz için kutsanmış bir Aziz yollamış. Değil mi, kardeşim?"
    stop sound

    show ch bandit1 at right
    with dissolve

    play sound "sounds/haydutlar/haydut_1_2.mp3"
    haydut_1 "Ha ha ha. Katılıyorum, kardeşim. Hey yaşlı adam, hemen atından in ve üzerindeki değerli tüm eşyaları bize teslim et!"
    stop sound

    return

label prologue_jerome_escaped:

    play sound "sounds/jerome/jerome_4.mp3"
    jerome "(derin bir nefes verir) Çok ucuz atlattık, değil mi Roach?"
    stop sound

    play sound "sounds/horse/2.mp3"
    horse "Brüffss"
    stop sound

    play sound "sounds/jerome/jerome_5.mp3"
    jerome "(gülerek) Ben de öyle düşünmüştüm, dostum. Acele etmeliyiz. Bu raporun bir an önce, İmparator'a ulaşması lazım."
    stop sound

    play sound "sounds/anlatici/yenikayit20.mp3"
    anlatici "Diyen Jerome, Roach ile birlikte, Palatine Hill'e doğru olan yolculuğuna devam eder..."
    stop sound

    return