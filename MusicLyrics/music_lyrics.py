import pygame
import time 


pygame.mixer.init()

pygame.mixer.music.load("C:/Data Science/Timepass/MusicLyrics/Boyfriend.mp3")
pygame.mixer.music.play()

lyrics = [
    (0,"🎵 Starting the music..."),
    (10,"Tai nu keh, rakh hun bidka’an na"),
    (13,"Tu vi mainu, mhari maai jhidka’an na"),
    (15,"Dekh ke munde nu, haan kar hogyi"),
    (18,  "Tu vi ohde kehndi si, umar ho gayi"),
    (20,"Ni piche pae gaya, naal khae gaya, kaule beh gaya koyi"),
    (25,"Ni maaye dil le gaya, le gaya, le gaya koyi"),
    (29,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi"),
    (35,"Main akad’an vi kar gayi’an, hun har gayi’an, ni seh gaya koyi"),
    (40,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi"),
    (45,"Labda pyaar kehnda, phone’an cho ni main"),
    (48,"Haan aashiq’an, veliya’an, dona cho ni main"),
    (50,"Jinni rehgi tere na’ batauni aakhda"),
    (52,"Haan taimpass karu, kehnda ohna cho ni main"),
    (55,"Hogi haan meri, tu hai jaan meri, mainu keh gaya koyi"),
    (59,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi"),
    (64,"Main akad’an vi kar gayi’an, hun har gayi’an, ni seh Gaya koyi"),
    (69,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi"),
    (85,"Sir utte kehnda chunni rakhya karo (haan)"),
    (88,"Pehla vi si, or oh shareef kargya (ahaan)"),
    (90,"Maa-peyya ne kehnda, bada sohna paali aa"),
    (93,"Janda-janda thaudi vi tareef kargya"),
    (95,"Agli vaari main aau ghardya na"),
    (98,"Karni ni gal kehnda, pardey’an na"),
    (100,"Maitho hun honi naiyo deek lagda"),
    (103,"Bhabhi nu dikhaata, kehndi theek lagda"),
    (105,"Kehnda na’an dassi, bas naal rakhi, de sheh gaya koyi"),
    (109,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi (le gaya koyi)"),
    (115,"Main akad’an vi kar gayi’an, hun har gayi’an, ni seh Gaya koyi (seh gaya koyi)"),
    (119,"Ni maaye dil le gaya, dil le gaya, dil le gaya koyi"),
    (125,"Main akad’an vi kar gayi’an, hun har gayi’an, ni seh Gaya koyi (seh gaya koyi)"),
    (130,"Oh dekh mera mukh janda khilKhabhi ankh thal’on til"),
    (133,"dil mera dil, mera le gaya koyi"),
    (135,"Kehnda tere utte dil aa still mera"),
    (137,"Aida kehke dil, mera dil, mera le gaya koyi"),
    (140,"Oh dekh mera mukh janda khil"),
    (142,"Khabhi ankh thal’on til, mera dil, mera le gaya koyi"),
    (145,"Kehnda tere utte dil aa still mera"),
    (147,"Aida kehke dil, mera dil, mera le gaya koyi")

]


start_time = time.time()

for timestamp, line in lyrics:
    while time.time() - start_time < timestamp:
        time.sleep(0.1)
    print(line)


while pygame.mixer.music.get_busy():
    time.sleep(3)

print("🎵 Music Finished!")