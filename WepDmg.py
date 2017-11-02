# Wow

lowend = int(input("Please enter the low end of the base weapon damage: "))
highend = int(input("Please enter the high end of the base weapon damage: "))

weapon_speed = float(input("Please enter the weapon speed: "))
attack_power = int(input("Please enter your attack power: "))

damage = lowend + (weapon_speed * attack_power / 14)
damage2 = highend + (weapon_speed * attack_power / 14)

print("You're calculated Damage should be: %.2f to %.2f" % (damage, damage2))
