# Gece saatleri

label palatine_hill:

    $ renpy.notify("BAŞARIM KAZANILDI: Birinci bölüm tamamlandı.")

    play music "music/chapter two/ost-1.mp3"

    scene bg palatine_hill gates # Jerome'nin atıyla birlikte Palatine Hill'in kapısının önüne geldiği görülür.
    with dissolve

    call palatine_hill_txt1 from _call_palatine_hill_txt1

    scene bg palatine_hill watchers # Nöbetçilerin birbirine bakışması.
    with fade

    call palatine_hill_txt2 from _call_palatine_hill_txt2

    scene bg palatine_hill jerome # Aziz Jerome'nin gerçek bir görseli ekrana gelir.
    with fade

    $ renpy.notify("BAŞARIM KAZANILDI: Kim bu Jerome?")

    call palatine_hill_txt3 from _call_palatine_hill_txt3

    scene bg palatine_hill watchers
    with fade

    play sound "sounds/imparator_honorius/imparator_honorius_1.mp3"

    imparator "Neler oluyor orada? Gecenin bu saatinde, bu nasıl bir gürültüdür??"

    stop sound

    scene bg palatine_hill throne_room
    with fade

    show ch emperor at right
    with dissolve

    call palatine_hill_txt4 from _call_palatine_hill_txt4

    scene bg palatine_hill garden_hill # Jerome ve İmparator, çiçeklerle dolu bir bahçede yürümektedir.
    with dissolve

    play sound "sounds/imparator_honorius/imparator_honorius_6.mp3"

    imparator "Söyle bakalım Jerome, seni buraya, bu kadar hızlı bir şekilde geri döndüren durum nedir?"

    stop sound

    scene bg palatine_hill jerome_giving_parchument # Jerome'nin eli ve uzattığı parşömen görünür.
    with fade

    play sound "sounds/jerome/jerome_10.mp3"

    jerome "Kendi gözlerinizle görmenizde yarar var, Efendim."

    stop sound

    scene bg palatine_hill parchument # Ekrana mühürlü parşömen kağıdı ve üzerinde yazan yazılar gelir.
    with fade

    #------PARŞÖMENDE YAZANLAR--------#
    # Lucilius Bassus’un imzasıyla. Roma İmparatorluğu’nun ve imparatorluk topraklarının yüce sahibi, Batı Roma’nın hükümdarı ve Senato’nun yöneticisi  İmparator Honorius’a saygılarımı sunarım. 
    # Geçtiğimiz aylarda başlayan Ren sınırımızdaki barbar hareketlerinin, bu süre içerisinde zirve noktaya ulaştığını bildirmek istiyorum. 
    # Sınır birliklerimizin, olası bir savaş durumuna hazırlandığını, ancak askerlerimizin kış sebebiyle zor durumda olduklarını ve morallarinin düşük olduğunu belirtmek istiyorum. Yüce kararlarınıza sığınarak, 
    # Ren Köprüsü’nün bulunduğu 89. Askeri Garnizon’a askeri destek vermenizi rica ediyorum. 
    # Saygılarımla, Lucilius Bassus

    $ renpy.notify("BAŞARIM KAZANILDI: Yerine ulaştırılmış bir mektup.")

    play sound "sounds/jerome/jerome_11.mp3"

    jerome "Efendim, raporda yazdığı gibi, Doğu’dan gelen bu vahşi barbarlar, çoktan Ren Nehri’nin kıyılarına varmışlar bile."

    stop sound

    play sound "sounds/jerome/jerome_12.mp3"

    jerome "General Bassus, bu raporu yaklaşık bir ay önce yazdı ve ben bu önemli mesajı size iletebilmek için haftalardır at sürüyordum."

    stop sound

    scene bg palatine_hill throne_room
    with fade

    menu jerome_talking_emperor:
        "Ayrıca, size söylemek istediğim bir şey daha var ki..."

        "{b}(BLÖF YAP){/b}":
            jerome "Senato’nuz, bu fikri daha önceden görme şansı buldu ve kendileri kabul etmeye oldukça yakın durumdalar."

            menu jerome_talking_emperor_2:
                "Ve..."

                "{b}(BLÖF YAPMAYA DEVAM ET){/b}":
                    jerome "Kim bilir, belki de sizden önce davranıp büyük bir askeri birliği, çoktan Ren sınırlarına yollamışlardır."
                    jump emperor_angry

                "{b}(BLÖFÜ YUMUŞAT){/b}":
                    jerome "Lakin sizin verdiğiniz emir, Senato'dan daha önce gelir, Efendim."
                    jump emperor_accept

        "{b}(GERÇEĞİ SÖYLE){/b}":
            jerome "Benim fikrimi soracak olursanız, bu askeri desteği vermenizin en uygun seçenek olduğunu düşünüyorum."
            jump emperor_decline

    label emperor_accept:
        
        $ renpy.notify("BAŞARIM KAZANILDI: Görev başarılı.")

        call palatine_hill_emperor_accept from _call_palatine_hill_emperor_accept

        $ diff_md += 1

        call preparation from _call_preparation

    label emperor_decline:
        
        $ renpy.notify("BAŞARIM KAZANILDI: Görev başarısız.")

        call palatine_hill_emperor_decline from _call_palatine_hill_emperor_decline

        call preparation from _call_preparation_1

    label emperor_angry:
        
        $ renpy.notify("BAŞARIM KAZANILDI: Kızgın kumlar.")

        call palatine_hill_emperor_angry from _call_palatine_hill_emperor_angry

        $ emperor_IsAngry = True

        call preparation from _call_preparation_2
        
    return

#--------------------------------------------------------------------------DİYALOGLAR-----------------------------------------------------------------------------------------------#

label palatine_hill_txt1:

    play sound "sounds/anlatici/anlatici 24.mp3"
    anlatici "Aziz Jerome, haftalar süren yolculuğunun ardından, atı Roach ile birlikte Palatine Hill'e varmayı başarmıştı."
    stop sound

    play sound "sounds/anlatici/anlatici 25.mp3"
    anlatici "Daha fazla vakit kaybetmek istemeyen Jerome, elindeki raporu bir an önce İmparator'a vermek istiyordu."
    stop sound

    play sound "sounds/jerome/jerome_7.mp3"

    jerome "Nöbetçiler! Nöbetçiler! Elimde, Yüce İmparatorumuz Honorius için önemli bir mesaj bulunmaktadır."

    stop sound

    play sound "sounds/jerome/jerome_8.mp3"

    jerome "Hemen çanları çalın, kendisiyle bir an önce görüşmek istiyorum."
    
    stop sound

    return

label palatine_hill_txt2:

    nobetci "..."

    play sound "sounds/nobetci/1.mp3"

    nobetci "Hey, yaşlı adam! Orada dur bakalım. Bu kapıya gelip her bağıran kişiyi hemen içeriye alıyor olsaydık, işsiz kalırdık. Önce kim olduğunu, sonra da ne istediğini söyle!"

    stop sound

    play sound "sounds/jerome/jerome_9.mp3"

    jerome "Ah, sizi cahil itler! Beni, Yüce İmparator Honorius’un baş danışmanını, Katolik ve Batı Ortodoks kiliselerinin baş hekimini ve Anglikan Cemaati’nin kurucusu Aziz Jerome’yi nasıl tanımazsınız!?"

    stop sound

    return

label palatine_hill_txt3:

    play sound "sounds/anlatici/26.mp3"
    anlatici "Aziz Jerome, 347–420 yılları arasında yaşamış bir din adamı, ilahiyatçı, tarihçi ve hekimdir."
    stop sound

    play sound "sounds/anlatici/27.mp3"
    anlatici "Batı Roma’nın Hristiyanlaşmasında önemli bir rolü bulunan Jerome, hayatının son 15 yılında Batı Roma imparatorları için danışmanlık yapmıştır."
    stop sound

    play sound "sounds/anlatici/28.mp3"
    anlatici "İlahiyat alanında yaptığı araştırmalar ile birlikte, günümüzde birçok eseri bulunmaktadır. Ayrıca kendisi, A vitaminin kaşifi olarak da görülür."
    stop sound

    return

label palatine_hill_txt4:

    $ renpy.notify("BAŞARIM KAZANILDI: Eski bir dost.")

    play sound "sounds/imparator_honorius/imparator_honorius_2.mp3"

    imparator "Aaa, aziz dostum Jerome! Bu ne hoş bir sürpriz."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_3.mp3"

    imparator "Beklediğimden çok daha erken bir zamanda dönmüşsün."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_4.mp3"

    imparator "Ama bu kadar büyük bir heyecan ve korkuyla geri geldiğine göre, bana söylemen gereken çok önemli bir durumun olduğunu düşünüyorum."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_5.mp3"

    imparator "Gel, birlikte Garden Hill’e doğru yürüyelim. Bana neden bu kadar erken döndüğünü, yol boyunca anlatırsın."

    stop sound

    return

label palatine_hill_emperor_accept:

    play sound "sounds/anlatici/29.mp3"
    anlatici "Aziz Jerome'nin söylediği sözler, İmparator'un çok hoşuna gitmişti."
    stop sound

    show ch emperor at right
    with dissolve

    play sound "sounds/imparator_honorius/imparator_honorius_7.mp3"

    imparator "Yıllardır bana ve ülkene yaptığın hizmetleri de göz önünde bulundurursam, sana olan güvenim sonsuza yakın Jerome."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_8.mp3"

    imparator "Tavsiyeni onaylıyorum. Yarın sabah itibariyle, üç tane daha askeri garnizonun, Ren Nehri’nin yakınlarında konuşlanması için emir vereceğim."
    
    stop sound

    play sound "sounds/jerome/jerome_13.mp3"

    jerome "Teşekkürler, ekselansları. Pişman olmayacaksınız."

    stop sound

    return

label palatine_hill_emperor_decline:

    play sound "sounds/anlatici/30.mp3"
    anlatici "Aziz Jerome'nin söylediği sözler, İmparator'u etkilemeye yetmemişti."
    stop sound

    show ch emperor at right
    with dissolve

    play sound "sounds/imparator_honorius/imparator_honorius_7.mp3"

    imparator "Yıllardır bana ve ülkene yaptığın hizmetleri de göz önünde bulundurursam, sana olan güvenim sonsuza yakın Jerome."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_9.mp3"

    imparator "Ancak, bir takım barbarın, bizim güçlü lejyonerlerimizi yenebileceğini düşünmüyorum."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_10.mp3"

    imparator "Bu sebepten dolayı, tavsiyeni kulak ardı etmek zorundayım Jerome. Kusura bakma."

    stop sound

    play sound "sounds/jerome/jerome_14.mp3"

    jerome "Yüce İmparatorumuz nasıl buyurursa, ekselansları. Umarım bu kararınızdan pişman olmazsınız."

    stop sound

    return

label palatine_hill_emperor_angry:

    play sound "sounds/anlatici/31.mp3"
    anlatici "Aziz Jerome'nin yalanlarını fark eden İmparator, çok öfkelenmişti."
    stop sound
    
    show ch emperor at right
    with dissolve

    play sound "sounds/imparator_honorius/imparator_honorius_11.mp3"

    imparator "Benimle bu şekilde konuşmaya nasıl cesaret edebilirsin, Jerome!"

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_12.mp3"

    imparator "Bu zamana kadar sana, yaşından ve tecrübenden dolayı saygı gösteriyordum."

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_13.mp3"

    imparator "Ama bu yalanın beni cidden çok sinirlendirdi. Nöbetçiler!"

    stop sound

    play sound "sounds/imparator_honorius/imparator_honorius_14.mp3"

    imparator "Bu yaşlı bunağı zincirleyip zindana atın! Karanlıkta düşünmek için çok vakti olacak."

    stop sound

    play sound "sounds/jerome/jerome_15.mp3"

    jerome "Efend..."

    stop sound

    play sound "sounds/nobetci/2.mp3"

    nobetci "Yürü!"

    stop sound

    stop music fadeout 1.0

    return