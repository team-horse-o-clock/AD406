label medium:

    play music "music/chapter one/ost-1.mp3"

    $ renpy.notify("BAŞARIM KAZANILDI: Giriş bölümü tamamlandı.")

    scene bg tribe flags # Kabilelerin bayrakları.
    with dissolve

    call medium_txt1 from _call_medium_txt1

    menu flags:

        "Lideri olmak istediğiniz kabileyi seçiniz."

        "Saksonlar":
            "Denizciliğin üstâdı, birebir dövüşlerin ustası, korkusuz Sakson kabilesini mi yönetmek istiyorsun?"

            menu choice_saxon:
                "Saksonları seçmek istediğinden emin misin? Bu kararın geri dönüşü olmayacaktır!"

                "Evet":
                    "Sakson halkı olarak sizi başımızda görmek, bizim için bir onurdur, Efendim."
                    $ tribe_saxon = True

                    python:
                        tribe_name = "Sakson"

                "Hayır":
                    jump flags

        "Vandallar":
            "Silahları altınlarla kaplı, madenciliğin ve kuyumculuğun ustası, zenginliğiyle bilinen Vandal kabilesini mi yönetmek istiyorsun?"

            menu choice_vandal:
                "Vandalları seçmek istediğinizden emin misin? Bu kararın geri dönüşü olmayacaktır!"
                
                "Evet":
                    "Vandal halkı olarak sizi başımızda görmek, bizim için bir onurdur, Efendim."
                    $ tribe_vandal = True

                    python:
                        tribe_name = "Vandal"

                "Hayır":
                    jump flags

        "Alanlar":
            "Kültürleri ve bilgeliğiyle tanınan, keşfedilmedik, gezilmedik yer bırakmayan, akılcı Alan kabilesini mi yönetmek istiyorsun?"

            menu choice_alan:
                "Alanları seçmek istediğinizden emin misin? Bu kararın geri dönüşü olmayacaktır!"
                
                "Evet":
                    "Alan halkı olarak sizi başımızda görmek, bizim için bir onurdur, Efendim."
                    $ tribe_alan = True

                    python:
                        tribe_name = "Alan"

                "Hayır":
                    jump flags

    $ renpy.notify("BAŞARIM KAZANILDI: Kabile lideri oldunuz. Tebrikler!")

    scene bg medium meeting # Karakterimizin, Medium ile olan görüşmesi.
    with fade

    play sound "sounds/medyum/medyum_1.mp3"

    medyum "Günaydın, Efendim. Dışarıda harika bir savaş atmosferi var, konuşmamız bittikten sonra kesinlikle bakmalısınız."

    stop sound

    play sound "sounds/medyum/medyum_2.mp3"

    medyum "Ama ilk önce kendimi tanıtmama izin verin. Ben, serüveniniz boyunca sizin emrinizde olacak bir Medyum’um. Bu maceranızda size yardımcı olmak için burada bulunmaktayım."

    stop sound

    python:
        player = renpy.input("Başlamadan önce, liderimizin adını öğrenebilir miyim?") 
        player = player.strip()

        if not player:
            player = "Çocuk Adam"

        player = player.capitalize()

    call medium_question1 from _call_medium_question1

    menu q_1:

        medyum "Bu durumda, liderimiz [player] ne yapardı?"

        "Trenin yönünü değiştirirdim.":
            $ med_q1_IsActive = True

        "Trenin yönünü değiştirmezdim.":
            $ med_q1_IsPassive = True

        "Tren mi...? O da ne??":
            $ med_q1_IsStupid = True

    call medium_question2 from _call_medium_question2

    menu q_2:

        medyum "Bu durumda, beş kişiyi kurtarmak adına, normalde raylara düşmeyecek olan ve müdahale etmemeniz durumunda beş kişinin ölmesine neden olacak olan şişman adamı, kendi ellerinizle raylara iter miydiniz?"

        "İterdim.":
            $ med_q2_IsActive = True

        "İtmezdim.":
            $ med_q2_IsPassive = True

        "Yine mi trenler, raylar!? Neyden bahsettiğini bir türlü anlayamıyorum, Medyum.":
            $ med_q2_IsStupid = True

    play sound "sounds/medyum/medyum_12.mp3"

    medyum "Bir odanın içerisindesiniz ve odada durduramayacağınız bir yangın çıkıyor. Bu oda içerisinde orjinal Mona Lisa tablosu ve ufak bir köpek yavrusu bulunuyor."

    stop sound

    menu q_3:

        medyum "Sadece birini kurtarabileceksiniz ve kurtarmayı seçmediğiniz yanacak. Efendimiz [player], hangisini seçerdi?"

        "Mona Lisa tablosunu.":
            $ monalisa_IsTrue = True

        "Yavru köpeği.":
            $ puppy_IsTrue = True

    python:
        proverb = renpy.input("Son olarak, çok sevdiğiniz bir sözü benimle paylaşır mısınız, Efendim?")
        proverb = proverb.strip()

        if not proverb:
            proverb = "Bir ulus sımsıkı birbirine bağlı olmayı bildikçe, yeryüzünde onu dağıtabilecek bir güç düşünülemez."

        proverb = proverb.capitalize()

    $ renpy.notify("BAŞARIM KAZANILDI: Medyumla tanıştın ve bütün sorularını cevapladın.")

    play sound "sounds/medyum/medyum_14.mp3"

    medyum "Sorularımı cevaplandırdığınız için teşekkür ederim, Efendim."

    stop sound

    play sound "sounds/medyum/medyum_15.mp3"

    medyum "Askerleriniz dışarıda sizleri bekliyor, isterseniz onları daha fazla heyecanlandırmayın."

    stop sound

    stop music fadeout 1.0

    if jerome_IsDeath == True:
        jump preparation
    else:
        jump palatine_hill

    return

#--------------------------------------------------------------------------DİYALOGLAR-----------------------------------------------------------------------------------------------#

label medium_txt1:

    play sound "sounds/anlatici/anlatici (simdisirasizde).mp3"
    anlatici "Şimdi sıra sizde. Oyun boyunca yönetmek istediğiniz kabileyi seçmeniz gerekiyor."
    stop sound

    play sound "sounds/anlatici/yenikayit22.mp3"
    anlatici "Seçmiş olduğunuz kabilenin, belli avantajları ve dezavantajları bulunuyor. Bunları, oyunu oynadığınız süre boyunca göreceksiniz."
    stop sound

    play sound "sounds/anlatici/anlatici (unutmayinn 23).mp3"
    anlatici "Unutmayın! Dikkatli bir şekilde karar vermelisiniz, çünkü bu seçimin geri dönüşü olmayacak."
    stop sound
    
    return

label medium_question1:

    play sound "sounds/medyum/medyum_3.mp3"

    medyum "Efendi [player], sizinle tanışmış olmak benim için çok büyük bir onurdur. İzin verirseniz, şimdi size birkaç soru sormak istiyorum."

    stop sound

    play sound "sounds/medyum/medyum_4.mp3"

    medyum "Bir tren, raylardan kaçamayacak durumda olan beş kişinin üzerine doğru gitmektedir. Siz, tamamen güvenli bir konumda bulunuyorsunuz ve trenin hangi yöne gideceğine karar verebilecek konumdasınız."

    stop sound

    play sound "sounds/medyum/medyum_5.mp3"

    medyum "Ancak, eğer ki bunu seçerseniz ve rayları değiştirecek olursanız, bu defa da yeni rotada bulunan, yine kaçamayacak durumda olan diğer bir kişi var ve bu defa da o kesinlikle ölecek."

    stop sound

    return

label medium_question2:

    play sound "sounds/medyum/medyum_7.mp3"

    medyum "Bir tren, tek bir ray hattı üzerinde, kesinlikle kaçamayacak ve trenin çarpması durumunda tamamı kesinlikle ölecek konumda olan beş kişinin üzerine gitmektedir."
    
    stop sound

    play sound "sounds/medyum/medyum_8.mp3"

    medyum "Bu sırada siz, trenin altından geçeceği bir köprünün üzerindesiniz ve yanınızda, sizinle beraber trenin beş kişinin üzerine gelişini izleyen devasa boyutlarda, şişman bir adam var."

    stop sound

    play sound "sounds/medyum/medyum_9.mp3"

    medyum "Bu adamın, o beş kişiyi raylara bağlayan insan olduğundan eminsiniz ve kendisi de bunu kabul ediyor."

    stop sound

    play sound "sounds/medyum/medyum_10.mp3"

    medyum "Aynı zamanda, şişman adamın raylarda bulunması durumunda, trenin ona çarparak kesinlikle durabileceğinden eminsiniz."

    stop sound

    return

