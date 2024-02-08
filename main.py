# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 30 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 16 -> 5, 65 -> 44 , 78 -> 67, 72 -> 61
# -- sarkanas kāpnes ved uz augšu, 13 -> 22, 37 -> 46, 31 -> 50, 85 -> 94 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import random 
player_location=1
computer_location=1
x=0
print("Welcome to the circus")
#while,pārliecinās, ka ir ne vairāk kā 30 kustības
while x<=30:
#if,ja spēlētāja vai datora pozīcija ir mazāka par 100, spēle turpinās
  if player_location<=100 or computer_location<=100:
   x=x+1

   print("Your turn to roll to dice type anything")
   a=input()
   dice=random.randint(1,6)
   print("You rolled", dice)
   player_location=player_location+dice
   #ja spēlētāja pozīcija atrodas uz kāda no iepriekšminētajām vietām, viņš tiks novietots uz kāpnēm un viņa pozīcija var pacelties vai pazemināties
   if player_location == 16:
     player_location = 5
     print("unlucky you ended up on the blue stairs")
   elif player_location == 13:
     player_location = 22
     print("lucky you got on the red stairs")
   elif player_location == 37:
     player_location = 46
     print("lucky you got on the red stairs")
   elif player_location == 31:
     player_location = 50
     print("lucky you got on the red stairs")
   elif player_location == 85:
     player_location = 94
     print("lucky you got on the red stairs")
   elif player_location == 65:
     player_location = 44
     print("unlucky you ended up on the blue stairs")
   elif player_location == 78:
     player_location = 67 
     print("unlucky you ended up on the blue stairs")
   elif player_location == 72:
     player_location = 61
     print("unlucky you ended up on the blue stairs")
   print("Your location ", player_location)

   print("Oponents turn ")
   dice=random.randint(1,6)
   print("Oponents rolled", dice )
   computer_location=computer_location+dice
   #ja datora pozīcija atrodas uz kāda no iepriekšminētajām vietām, viņš tiks novietots uz kāpnēm un viņa pozīcija var pacelties vai pazemināties
   if computer_location == 16:
     computer_location = 5
     print("lucky computer got on the blue stairs")
   elif computer_location == 13:
     computer_location = 22
     print("unlucky computer got on the red stairs")
   elif computer_location == 37:
     computer_location = 46
     print("unlucky computer got on the red stairs")
   elif computer_location == 31:
     computer_location = 50
     print("unlucky computer got on the red stairs")
   elif computer_location == 85:
     computer_location = 94
     print("unlucky computer got on the red stairs")
   elif computer_location == 65:
     computer_location = 44
     print("lucky computer got on the blue stairs")
   elif computer_location == 78:
     computer_location = 67
     print("lucky computer got on the blue stairs") 
   elif computer_location == 72:
     computer_location = 61
     print("lucky computer got on the blue stairs")
   print("Oponents location",computer_location)
#ja spēlētājs sasniedz 100 ātrāk nekā dators, viņš uzvar
   if player_location>=100: 
       print("You won")
       break
   elif computer_location>=100:
       print("You lost")
       break
if player_location<100 and computer_location<100:
    print("draw")

