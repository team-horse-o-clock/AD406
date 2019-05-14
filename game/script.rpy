# Oyunun başlaması için gereken script dosyası. #

label start:

    scene bg play_with_headphone # Kulaklık ile oynayın uyarısı.
    with dissolve
    pause 5.0

    scene bg story_based # Hikayenin önemli olduğunun uyarısı.
    with dissolve
    pause 5.0

    scene bg developer # Geliştirici ekip.
    with dissolve
    pause 5.0

    stop music fadeout 1.0

    play music "music/prologue/ost-2.mp3"

    call prologue from _call_prologue # Prologue'u çağırıyor ve oyun başlıyor.

    return # Son return komutu oyunu bitirir.



#/******************************************************************************************************************************************************************************/#



# Oyun içinde kullanılacak olan değişkenler tanımlandı. #
#--------------------------------------------------------#

define flash = Fade(.25, 0, .75, color="#fff") # Saldırı efekti.

define diff_md = 0 # Oyun sonundaki düellonun zorluğunu belirleyen değişken.

default jerome_IsDeath = False # Jerome'nin ölüp ölmediğini belirleyen değişken.

# Oyuncunun seçtiği kabileyi tutan değişkenler. #
default tribe_saxon = False
default tribe_vandal = False
default tribe_alan = False

# Medyum'un ilk sorusuna verilen cevabı tutan değişkenler. #
default med_q1_IsActive = False
default med_q1_IsPassive = False
default med_q1_IsStupid = False

# Medyum'un ikinci sorusuna verilen cevabı tutan değişkenler. #
default med_q2_IsActive = False 
default med_q2_IsPassive = False
default med_q2_IsStupid = False

# Oyuncunun yavru köpek/tablo seçimini tutan değişkenler. #
default monalisa_IsTrue = False 
default puppy_IsTrue = False

# İmparator'un, oyunun sonundaki düelloda olup olmayacağını belirleyen değişken. #
default emperor_IsAngry = False 

# Okçu komutanının sorduğu soruların cevaplarını tutan değişkenler. #
default bowm_IsCorrect = False
default bowm_EscapeRoute = False
default bowm_ProtectTent = False

# Süvari komutanının sorduğu soruların cevaplarını tutan değişken. #
default cav_IsCorrect = False 

# Öncü birliklerin hangisi olduğunu tutan değişkenler.#
default spears_OnFront = False
default swords_OnFront = False
default shields_OnFront = False

default war_IsWon = False # Bütün savaşın zafer/yenilgi durumunu tutan değişken.

default player_IsAlive = False # Oyuncunun düellodan sağ çıkıp çıkmadığını kontrol eden değişken.



#/******************************************************************************************************************************************************************************/#



# Oyun içinde kullanılacak olan karakterler tanımlandı. #
#--------------------------------------------------------#

define anlatici = Character("Anlatıcı") # ÖFC

define jerome = Character("Aziz Jerome", image="jerome", color="#0f2f66") # Erkek, yaşlı ve bilge din adamı

define haydut_1 = Character("Haydut", image="haydut_1", color="#ffffff") # Erkek, kaba, haydut işte

define haydut_2 = Character("Haydut", image="haydut_2", color="#ffffff") # Erkek, kaba, haydut işte

define horse = Character("Roach", color="#490701") # Bildiğimiz at

define medyum = Character("Medyum", image="medyum", color="#01300d") # Kadın, cadı, bilge

define nobetci = Character("Nöbetçi", image="nobetci", color="#ffffff") # Erkek, gür sesli, emreder şekilde konuşma

define imparator = Character("İmparator Honorius", image="imparator", color="#593a01") # Erkek, orta yaşlı

define general = Character("[general]", image = "[general]", color="#01594c") # Erkek, yaşlı, tecrübeli

define okcu_komutan = Character("Komutan Vel Decumius", image = "okcu_komutan", color="#52129b") # Erkek, genç

define suvari_komutan = Character("Komutan Vibius Canius", image = "suvari_komutan", color="#5b084d") # Erkek, genç

define imparator_boss = Character("Kanlı Honorius", image = "imparator_boss", color="#6b0000") # İmparator'un daha sert ve güçlenmiş hali

define puppy = Character("Cesur Köpek", color="#0f2f66")


#/******************************************************************************************************************************************************************************/#



#--------------------------GİRİŞ UYARILARI----------------------------#
image bg play_with_headphone = "uyarilar/1.png"
image bg story_based = "uyarilar/2.png"
image bg developer = "uyarilar/3.png"


#--------------------------PROLOGUE----------------------------#
#label prologue
image bg jerome riding_horse = "prologue/label prologue/1.png"
image bg world europe_map = "prologue/label prologue/2.jpg"
image bg jerome from_face = "prologue/label prologue/3.jpg"
image bg jerome choose_path = "prologue/label prologue/4.png"
#label lakeside
image bg jerome near_lakeside = "prologue/label prologue/label lakeside/1.png"
#label ridgeway
image bg jerome on_ridgeway = "prologue/label prologue/label ridgeway/1.png"
image bg jerome with_bandits = "prologue/label prologue/label ridgeway/2.png"
#label jerome_escape
image bg jerome try_escape = "prologue/label prologue/label ridgeway/label jerome_escape/1.jpg"
#label escaped
image bg jerome escaping = "prologue/label prologue/label ridgeway/label jerome_escape/2.png" # -----------------------> label not_escaped ile aynı görsel.
#label not_escaped
image bg black = "#000"
image bg jerome hit_arrow = "prologue/label prologue/label ridgeway/label jerome_escape/label not_escaped/1.png"
image bg jerome killed = "prologue/label prologue/label ridgeway/label jerome_escape/label not_escaped/2.png"


#--------------------------MEDIUM----------------------------#
#label medium
image bg tribe flags = "chapter one/1.jpg"
image bg medium meeting = "chapter one/2.jpg"


#--------------------------PALATINE HILL----------------------------#
#label palatine_hill
image bg palatine_hill gates = "chapter two/1.png"
image bg palatine_hill watchers = "chapter two/2.png"
image bg palatine_hill jerome = "chapter two/3.jpeg"
image bg palatine_hill throne_room = "chapter two/4.png"
image bg palatine_hill garden_hill = "chapter two/5.png"
image bg palatine_hill jerome_giving_parchument = "chapter two/6.png"
image bg palatine_hill parchument = "chapter two/7.png"


#-----------------------------------PREPARATION----------------------------#
image bg pre tent = "chapter three/1.png"
image bg pre speech = "chapter three/2.jpg"
image bg pre meet_general = "chapter three/3.png"
image bg pre headquarters = "chapter three/4.png"


#-----------------------------------ENDGAME----------------------------#
image bg two_army = "chapter four/1.png"
image bg pre boss_fight = "chapter four/2.png"
image bg firstmen_war = "chapter four/war scene/1.png"
image bg cavalry_war = "chapter four/war scene/2.png"
image bg archery_war = "chapter four/war scene/3.png"
image bg duello = "chapter four/duello scene/1.png"
image bg lvl1_boss = "chapter four/boss/1.png"
image bg lvl3_boss = "chapter four/boss/3.png"


#-----------------------------------EPILOGUE----------------------------#
image bg worst_ending = "epilogue/1.png"
image bg alan_1 = "epilogue/alan/1.jpg"
image bg alan_2 = "epilogue/alan/2.jpg"
image bg alan_3 = "epilogue/alan/3.png"
image bg sakson_1 = "epilogue/sakson/1.jpg"
image bg sakson_2 = "epilogue/sakson/2.jpg"
image bg sakson_3 = "epilogue/sakson/3.jpg"
image bg vandal_1 = "epilogue/vandal/1.jpg"
image bg vandal_2 = "epilogue/vandal/2.jpg"
image bg vandal_3 = "epilogue/vandal/3.jpg"


#-----------------------KARAKTERLER---------------------------------#
image ch bandit1 = "characters/bandit1.png"
image ch bandit2 = "characters/bandit2.png"
image ch jerome = "characters/jerome.png"
image ch emperor = "characters/emperor.png"
image ch general = "characters/general.png"
image ch veL_decumius = "characters/veL_decumius.png"
image ch vibius_canius = "characters/vibius_canius.png"
image ch lvl2_boss = "chapter four/boss/2.png"
image ch emperor_boss = "chapter four/boss/4.png"

#----------------------SIDE IMAGES--------------------------------------#
image side haydut_1 = "characters/side images/bandit1.png"
image side haydut_2 = "characters/side images/bandit2.png"
image side medyum = "characters/side images/medium.png"
image side jerome = "characters/side images/jerome.png"
image side nobetci = "characters/side images/watcher.png"
image side imparator = "characters/side images/emperor.png"
image side okcu_komutan = "characters/side images/vel_decumius.png"
image side suvari_komutan = "characters/side images/vibius_canius.png"
image side general = "characters/side images/general.png"