import random
print ("\nPokemon Calculator")
print ("\nCharizard VS. Feraligatr")
print ("\nCharizard LVL = 90, SAtt= 205")
print ("Feraligatr LVL = 95, SDef = 188 \nCharizard gamitan mo ng fireblast si Feraligatr ")

Level = 90
SAtt = 205
SDef = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
critical = 1,2
crit = random.choice(critical)
rand = .85,1
randoom = random.choice(rand)
Stab = 1
Type = 1
Burn = 1
Other = 1
Modifier = Targets * Weather * Badge * crit * randoom * Stab * Type * Burn * Other


if crit == 2:
    print ("        Lucky crit :D       ")
Damage = ((((((2*Level)/5)+2)* Power * SAtt / SDef)/50)+2) * Modifier
print ("\nCharizards Damage to Feraligatr is ", Damage , "\n\n\n\n")