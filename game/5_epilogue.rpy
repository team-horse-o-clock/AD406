# Oyunun tüm sonlarını "Anlatıcı" anlatıyor.

label alan_victory_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Mezopotamya.")

    scene bg alan_1
    with flash
    
    # İran'a doğru yola çıkarlar. Anadolu'dan geçerler.

    play sound "sounds/anlatici/anlatici d2-1.mp3"
    anlatici "Savaşı kazanan Alan kabilesinin lideri [player], bu zamana kadar verdiği mücadeleyi de kazanmıştı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-2.mp3"
    anlatici "Liderlerine olan güveni artan Alan halkı, efendilerini takip etmekten gurur duyuyorlardı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-3.mp3"
    anlatici "Savaştan sonra uzun yollar kat eden Alanlar, Anadolu'yu geçerek İran topraklarına yerleşti."
    stop sound

    play sound "sounds/anlatici/anlatici d2-4.mp3"
    anlatici "Burada refah ve huzur içinde yaşayan Alanlar, günümüz devletlerine kadar soyunu sürdürmeyi başardı."
    stop sound
    
    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits

    return

label alan_victory_playerIsDead:

    $ renpy.notify("BAŞARIM KAZANILDI: Geri vites.")

    scene bg alan_2
    with flash
    
    # Liderleri öldüğü için, ne yapacaklarını bilemeyip geriye dönerler. Kısa süre sonra dağılırlar.
    play sound "sounds/anlatici/anlatici d2-9.mp3"
    anlatici "Savaşı kazanan Alan kabilesi, liderleri [player]'ın ölmesiyle birlikte büyük bir yasa gömüldü."
    stop sound

    play sound "sounds/anlatici/anlatici d2-10.mp3"
    anlatici "Savaşı kazanmış olsalar bile ne yapacaklarını bilmeyen Alanlar, en doğru yolun geri dönmek olduğuna karar verdi."
    stop sound

    play sound "sounds/anlatici/anlatici d2-11.mp3"
    anlatici "Ancak bu karar, belki de verdikleri en kötü karar olacaktı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-13.mp3"
    anlatici "Uzun süre kendilerine lider seçemeyen Alanlar, çok fazla süre dayanamadı ve dağıldılar."
    stop sound

    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label alan_lost_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Sürgün hayatı.")

    scene bg alan_3
    with flash

    # Lider esir düşer. Oradan oraya giderken ölür.
    play sound "sounds/anlatici/anlatici d2-14.mp3"
    anlatici "Büyük bir yenilgiye uğrayan [player], bütün dostlarını ve ailesini savaşta kaybetmişti."
    stop sound

    play sound "sounds/anlatici/anlatici d2-15.mp3"
    anlatici "Savaş alanının ortasında yakalanan yenilmiş Alan lideri, yıllarca Roma askerleri tarafından, oradan oraya taşındı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-16.mp3"
    anlatici "Kalan ömrünü sürgünde geçiren [player], yılların verdiği yorgunluğa dayanamadı ve öldü."
    stop sound

    play sound "sounds/anlatici/anlatici d2-6.mp3"
    anlatici "Ona bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound
    
    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label saxon_victory_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Denizlerin efendileri.")

    scene bg sakson_1
    with flash
    
    # Denize açılıp Britanya yarımadasına doğru yola çıkarlar.

    play sound "sounds/anlatici/anlatici d2-17.mp3"
    anlatici "Savaşı kazanan Sakson kabilesinin lideri [player], bu zamana kadar verdiği mücadeleyi de kazanmıştı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-18.mp3"
    anlatici "Liderlerine olan güveni artan Sakson halkı, efendilerini takip etmekten gurur duyuyorlardı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-19.mp3"
    anlatici "Savaştan sonra denizlere açılan Sakson halkı, günlerce yolculuk etti."
    stop sound

    play sound "sounds/anlatici/anlatici d2-20.mp3"
    anlatici "En sonunda Britanya yarımadasına varan Saksonlar, küçük bir kasabaya yerleştiler."
    stop sound

    play sound "sounds/anlatici/anlatici d2-21.mp3"
    anlatici "Liderleri [player]'ın da sayesinde oldukça gelişen Sakson halkı, kendilerine bir krallık kurdu."
    stop sound

    play sound "sounds/anlatici/anlatici d2-22.mp3"
    anlatici "Burada refah ve huzur içinde yaşayan Saksonlar, günümüz devletlerine kadar soyunu sürdürmeyi başardı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label saxon_victory_playerIsDead:

    $ renpy.notify("BAŞARIM KAZANILDI: Kaptansız bir gemi.")

    scene bg sakson_2
    with flash

    # Denizlere açılan Saxon'lar yollarını kaybederler ve bir çok kabile üyesi ölür.
    play sound "sounds/anlatici/anlatici d2-23.mp3"
    anlatici "Savaşı kazanan Sakson kabilesi, liderleri [player]'ın ölmesiyle birlikte büyük bir yasa gömüldü."
    stop sound

    play sound "sounds/anlatici/anlatici d2-24.mp3"
    anlatici "Savaşı kazanmış olsalar bile ne yapacaklarını bilmeyen Saksonlar, en doğru yolun denizlere açılmak olduğuna karar verdi."
    stop sound

    play sound "sounds/anlatici/anlatici d2-25.mp3"
    anlatici "Ancak liderleri olmayan bir toplum, kaptansız bir gemiye benzer."
    stop sound

    play sound "sounds/anlatici/anlatici d2-26.mp3"
    anlatici "Hangi yöne yelken açacaklarına karar vermeyen Saksonlar, kendi içlerinde kavgaya tutuştular."
    stop sound

    play sound "sounds/anlatici/anlatici d2-27.mp3"
    anlatici "En sonunda birbirlerini öldürmeye kadar giden durum, Saksonlar'ın dağılmasına sebep oldu."
    stop sound

    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label saxon_lost_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Denize olan özlem.")

    scene bg sakson_3
    with flash

    # Esir düşen lider, denize ayağı bağlanarak atılır.

    play sound "sounds/anlatici/anlatici d2-28.mp3"
    anlatici "Büyük bir yenilgiye uğrayan [player], bütün dostlarını ve ailesini savaşta kaybetmişti."
    stop sound

    play sound "sounds/anlatici/anlatici d2-29.mp3"
    anlatici "Savaş alanının ortasında yakalanan yenilmiş Sakson lideri, savaş suçlusu sıfatıyla, ölüm cezasına çarptırılmaya karar verildi."
    stop sound

    play sound "sounds/anlatici/anlatici d2-30.mp3"
    anlatici "Ayağına ağır bir taş bağlanarak denize atılan [player], hedefi olan denizlere açılmayı, farklı bir şekilde başarmış oldu."
    stop sound

    play sound "sounds/anlatici/anlatici d2-6.mp3"
    anlatici "Ona bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label vandal_victory_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Çöllerin içindeki bir krallık.")

    scene bg vandal_1
    with flash
    
    # Çölleri geçerek Kuzey Afrika'da bir krallık kurarlar.

    play sound "sounds/anlatici/anlatici d2-31.mp3"
    anlatici "Savaşı kazanan Vandal kabilesinin lideri [player], bu zamana kadar verdiği mücadeleyi de kazanmıştı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-2.mp3"
    anlatici "Liderlerine olan güveni artan Vandal halkı, efendilerini takip etmekten gurur duyuyorlardı."
    stop sound

    play sound "sounds/anlatici/yenikayit21.mp3"
    anlatici "Ren Nehri'ni aşarak İspanya'ya kadar ilerleyen Vandallar, daha sonrasında Kuzey Afrika topraklarına yerleştiler."
    stop sound

    play sound "sounds/anlatici/yenikayit23.mp3"
    anlatici "Yönetimi tek elden sağlamak isteyen [player], kendini kral ilan etti ve güçlü bir krallık kurmak için çalışmalara başladı."
    stop sound

    play sound "sounds/anlatici/yenikayit24.mp3"
    anlatici "Burada refah ve huzur içinde yaşayan Vandallar, günümüz devletlerine kadar soyunu sürdürmeyi başardı."
    stop sound

    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label vandal_victory_playerIsDead:

    $ renpy.notify("BAŞARIM KAZANILDI: İç savaşın ortasında.")

    scene bg vandal_2
    with flash

    # Kabile içi savaş çıkar ve kral olabilmek için birbirlerini öldürürler.

    play sound "sounds/anlatici/yenikayit25.mp3"
    anlatici "Savaşı kazanan Vandal kabilesi, liderleri [player]'ın ölmesiyle birlikte büyük bir yasa gömüldü."
    stop sound

    play sound "sounds/anlatici/yenikayit26.mp3"
    anlatici "Savaşı kazanmış olsalar bile ne yapacaklarını bilmeyen Vandallar, kendi aralarında güç kavgasına tutuştu."
    stop sound

    play sound "sounds/anlatici/yenikayit27.mp3"
    anlatici "Gruplara bölünüp birbirlerini öldürmeye başlayan halk, bir iç savaşın ortasında kalmıştı."
    stop sound

    play sound "sounds/anlatici/yenikayit28.mp3"
    anlatici "Ve bu durum, maalesef onlar için güzel bitmedi."
    stop sound

    play sound "sounds/anlatici/anlatici d2-5.mp3"
    anlatici "Onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label vandal_lost_playerIsAlive:

    $ renpy.notify("BAŞARIM KAZANILDI: Kafasız lider.")

    scene bg vandal_3
    with flash

    # Asi davranışlar sergileyen liderimiz kafası kesilerek idam edilir.
    play sound "sounds/anlatici/yenikayit29.mp3"
    anlatici "Büyük bir yenilgiye uğrayan [player], bütün dostlarını ve ailesini savaşta kaybetmişti."
    stop sound

    play sound "sounds/anlatici/yenikayit30.mp3"
    anlatici "Savaş alanının ortasında yakalanan yenilmiş Vandal lideri, birkaç kez kaçmaya çalıştı."
    anlatici "Ancak başaramadı."
    stop sound

    play sound "sounds/anlatici/yenikayit31.mp3"
    anlatici "Asi tavırlar sergileyen [player], en sonunda susturuldu."
    stop sound

    play sound "sounds/anlatici/yenikayit32.mp3"
    anlatici "Çünkü, konuşacak bir kafası kalmamıştı artık."
    stop sound

    play sound "sounds/anlatici/anlatici d2-6.mp3"
    anlatici "Ona bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits
    
    return

label worst_ending:

    $ renpy.notify("BAŞARIM KAZANILDI: Her hikaye mutlu bitmez.")

    scene bg worst_ending
    with flash

    # İmparator'un Senato'ya yaptığı konuşmada nasıl yendiklerini, övüne övüne anlatır.

    play sound "sounds/anlatici/yenikayit33.mp3"
    anlatici "Doğu'dan gelen barbar tehditini savuşturmayı başaran Roma İmparatorluğu, kutlamalar yapmaya başlamıştı bile."
    stop sound

    play sound "sounds/anlatici/yenikayit34.mp3"
    anlatici "Kaybeden kabilenin tüm halkı kılıçtan geçirilmiş ve eşyalarına el konulmuştu."
    stop sound

    play sound "sounds/anlatici/yenikayit35.mp3"
    anlatici "Yağmaladıkları yiyecek ve içeceklerle askerlere ziyafetler düzenlendi."
    stop sound

    play sound "sounds/anlatici/yenikayit36.mp3"
    anlatici "İmparator Honorius ise, bu zafer sayesinde Senato'nun güvenini kazandı."
    stop sound

    play sound "sounds/anlatici/yenikayit37.mp3"
    anlatici "En iyi sona ulaşamadın sanırım, değil mi?"
    stop sound

    play sound "sounds/anlatici/yenikayit38.mp3"
    anlatici "Yine de, onlara bu yolculuğunda eşlik ettiğiniz için sizlere teşekkür ediyoruz."
    stop sound

    play sound "sounds/anlatici/anlatici d2-7.mp3"
    anlatici "Başka oyunlarımızda görüşmek dileğiyle :)"
    stop sound

    play sound "sounds/anlatici/anlatici d2-8.mp3"
    anlatici "Team Horse O'Clock ❤ You"
    stop sound

    anlatici "Unutmadan,"

    anlatici "[proverb] -[player]"

    jump credits

    return

label credits:

    stop music fadeout 1.0

    scene bg black
    with dissolve

    python:
        _preferences.set_volume('music', 0.8)

    # Credits için video hazırlanabilir.

    $ renpy.notify("BAŞARIM KAZANILDI: Oyunu bitirdiniz :) Teşekkür ederiz!")

    $ renpy.movie_cutscene('videos/credits.webm')

    $ MainMenu(confirm=False)()

    return