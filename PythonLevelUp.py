#!/usr/bin/env python3

# Main variables here
practice_xp = 30
class_xp = 20
reading_xp = 15
audio_xp = 10
work_class_xp = 5

lvl = 6
xp = 599
Nextlvl = 826


########## Daily Work ###########
quests_today = (practice_xp * 4) + (class_xp * 20) + (reading_xp * 15) + (audio_xp * 15) + (work_class_xp * 15)

########## Daily Work ###########

xp = xp + quests_today


while xp >= Nextlvl:
	lvl = lvl+1
	xp = (xp - Nextlvl)
	Nextlvl = round(Nextlvl * 1.75)
	
Needed_xp = (Nextlvl - xp)
current_lvl_percent = (xp / Nextlvl)
needed_xp_percent = (Needed_xp / Nextlvl)
bar_1 = "|" + (int((xp/5)) * '#') + "|"
bar_2 = "|" + (int((Needed_xp/5))) * '#' + "|"


print(" ")
print(" ")
print(" ")
print(" ")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
print("__________________________________________________")
print('| | | Good work! You earned: ' + str(quests_today) + " XP today | | |")
print("__________________________________________________")
print('Current Level: ', lvl)
print('Current XP: ', xp, 'XP','|', "{:.0%}".format(current_lvl_percent), 'percent to the next level')
print(bar_1)
print('XP for the Next Level: ', Nextlvl,'XP' ,' | ','XP remaining: ', Needed_xp, "|" , "{:.0%}".format(needed_xp_percent))
print(bar_2)
print("__________________________________________________")

print(" ")
print("Huzzah! You are a level: " + str(lvl) + " Tech-Knight!")
print("__________________________________________________")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")

########## Journey ###########
