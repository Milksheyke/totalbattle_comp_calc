# Define a dictionary for each category with units and their silver value per casualty
# Example values are placeholders; you should replace them with the actual values from the sheet
def calculate_guards_total_cost(casualties, temple_factor, prod_cost, rez_cost):
    to_be_rebuild = casualties * 0.1
    to_be_rez = casualties * 0.9
    total_cost = (to_be_rebuild * prod_cost) + (to_be_rez * rez_cost / temple_factor)
    return total_cost


def calculate_monster_cost(casualties, prod_cost, dragon_coins, assumed_cost_dc, rez_cost, temple_factor):
    to_be_rebuild = casualties * 0.1
    to_be_rez = casualties * 0.9
    rebuild_cost = to_be_rebuild * (prod_cost + dragon_coins * assumed_cost_dc)
    rez_cost_total = (to_be_rez * rez_cost) / temple_factor
    total_cost = rebuild_cost + rez_cost_total
    return total_cost


def calculate_merc_cost(casualties, rez_cost, temple_factor, compensation_price):
    to_be_rebuild = casualties * 0.1
    to_be_rez = casualties * 0.9
    rez_cost_total = (to_be_rez * rez_cost) / temple_factor
    rebuild_cost = to_be_rebuild * compensation_price
    total_cost = rez_cost_total + rebuild_cost
    return total_cost


resources = {
    "Tree": lambda x: x / 10,
    "Iron": lambda x: x / 10,
    "Stone": lambda x: x / 10,
    "Metal": lambda x: x / 10,
    "Silver": lambda x: x,
    "Tar": lambda x: x * 10,
    "Portal": lambda x: x * 1000000,
    "Forts": lambda x: x * 5000000,
    "Walls Level": lambda x: x * 125,
    "Hero Level": lambda x: x * 100,
    "Sum of Captains' Levels": lambda x: x * 50,
}

guardsmen = {
    "Archers I-IV": lambda x: x * 100,
    "Spearmen I-IV": lambda x: x * 100,
    "Riders I-IV": lambda x: x * 200,
    "Archers V+": lambda x: x * 200,
    "Spearmen V+": lambda x: x * 200,
    "Riders V+": lambda x: x * 400,
    "Griffin": lambda x: x * 4000,
    "TI Purifier": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.02, prod_cost=1700, rez_cost=40
    ),
    "TI Punisher": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.02, prod_cost=1700, rez_cost=40
    ),
    "TI Smiter": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.02, prod_cost=3400, rez_cost=80
    ),
    "TI Corax": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.02, prod_cost=34000, rez_cost=800
    ),
    "TII Purifier": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.91, prod_cost=1900, rez_cost=40
    ),
    "TII Punisher": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.91, prod_cost=1900, rez_cost=40
    ),
    "TII Smiter": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.91, prod_cost=3800, rez_cost=80
    ),
    "TII Corax": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.91, prod_cost=38000, rez_cost=800
    ),
}

specialists = {
    "Swordsmen": lambda x: x * 100,
    "Spies": lambda x: x * 100,
    "T5 Deadshots": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=4400, rez_cost=40
    ),
    "T5 Lion riders": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=4800, rez_cost=80
    ),
    "T5 Vultures": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=5200, rez_cost=40
    ),
    "T6 Deadshots": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=5600, rez_cost=40
    ),
    "T6 Lion riders": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=6000, rez_cost=80
    ),
    "T6 Vultures": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=6400, rez_cost=40
    ),
    "T6 Heavy knight": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.13, prod_cost=6800, rez_cost=40
    ),
    "T6 Swift jaeger": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.13, prod_cost=7200, rez_cost=200
    ),
    "T7 Deadshots": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=7600, rez_cost=40
    ),
    "T7 Lion riders": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=8000, rez_cost=80
    ),
    "T7 Vultures": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=8400, rez_cost=40
    ),
    "T7 Heavy knight": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=8800, rez_cost=40
    ),
    "T7 Swift jaeger": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=9200, rez_cost=200
    ),
    "TI Legitimist": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=9600, rez_cost=40
    ),
    "TI Duelist": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.13, prod_cost=10000, rez_cost=40
    ),
    "TI Whitemane": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.13, prod_cost=10400, rez_cost=80
    ),
    "TI Royal lion": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=10800, rez_cost=800
    ),
    "TI Panoptic": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.33, prod_cost=11200, rez_cost=200
    ),
    "TII Legitimist": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=11600, rez_cost=40
    ),
    "TII Duelist": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.53, prod_cost=12000, rez_cost=40
    ),
    "TII Whitemane": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=12400, rez_cost=80
    ),
    "TII Royal lion": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.81, prod_cost=12800, rez_cost=800
    ),
    "TII Panoptic": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=1.13, prod_cost=13200, rez_cost=200
    ),
}

engineers = {
    "Catapults I-IV": lambda x: x * 1000,
    "Catapults V+": lambda x: x * 2000,
    "T6 Ballistae": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=3.84, prod_cost=13000, rez_cost=400
    ),
    "T7 Ballistae": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=4.34, prod_cost=15000, rez_cost=400
    ),
    "TI Josephine": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.02, prod_cost=17000, rez_cost=400
    ),
    "TII Josephine": lambda casualties: calculate_guards_total_cost(
        casualties=casualties, temple_factor=5.91, prod_cost=19000, rez_cost=400
    ),
}

monsters = {
    "T3 Emerald Dragon": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=19600,
        dragon_coins=280,
        assumed_cost_dc=450,
        rez_cost=1120,
        temple_factor=1.53,
    ),
    "T3 Water Elemental": lambda casualties: calculate_monster_cost(
        casualties=casualties, prod_cost=8400, dragon_coins=120, assumed_cost_dc=450, rez_cost=480, temple_factor=1.53
    ),
    "T3 Stone Gargoyle": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=22400,
        dragon_coins=320,
        assumed_cost_dc=450,
        rez_cost=1280,
        temple_factor=1.53,
    ),
    "T3 Battle Boar": lambda casualties: calculate_monster_cost(
        casualties=casualties, prod_cost=16760, dragon_coins=240, assumed_cost_dc=450, rez_cost=960, temple_factor=1.53
    ),
    "T4 Magic Dragon": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=46800,
        dragon_coins=520,
        assumed_cost_dc=350,
        rez_cost=2080,
        temple_factor=1.81,
    ),
    "T4 Ice Phoenix": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=54000,
        dragon_coins=600,
        assumed_cost_dc=350,
        rez_cost=2400,
        temple_factor=1.81,
    ),
    "T4 Many-Armed Guardian": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=39600,
        dragon_coins=440,
        assumed_cost_dc=350,
        rez_cost=1760,
        temple_factor=1.81,
    ),
    "T4 Gorgon Medusa": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=35920,
        dragon_coins=400,
        assumed_cost_dc=350,
        rez_cost=1600,
        temple_factor=1.81,
    ),
    "T5 Desert Vanquisher": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=87900,
        dragon_coins=800,
        assumed_cost_dc=250,
        rez_cost=3200,
        temple_factor=2.51,
    ),
    "T5 Flaming Centaur": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=92400,
        dragon_coins=840,
        assumed_cost_dc=250,
        rez_cost=3360,
        temple_factor=2.51,
    ),
    "T5 Ettin": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=101130,
        dragon_coins=920,
        assumed_cost_dc=250,
        rez_cost=3680,
        temple_factor=2.51,
    ),
    "T5 Fearsome Manticore": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=96760,
        dragon_coins=880,
        assumed_cost_dc=250,
        rez_cost=3520,
        temple_factor=2.51,
    ),
    "T6 Crystal Dragon": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=171600,
        dragon_coins=1320,
        assumed_cost_dc=150,
        rez_cost=5280,
        temple_factor=3.84,
    ),
    "T6 Ruby Golem": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=182000,
        dragon_coins=1400,
        assumed_cost_dc=150,
        rez_cost=5600,
        temple_factor=3.84,
    ),
    "T6 Troll Rider": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=156000,
        dragon_coins=1200,
        assumed_cost_dc=150,
        rez_cost=4800,
        temple_factor=3.84,
    ),
    "T6 Jungle Destroyer": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=176800,
        dragon_coins=1360,
        assumed_cost_dc=150,
        rez_cost=5440,
        temple_factor=3.84,
    ),
    "T7 Black Dragon": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=180000,
        dragon_coins=1760,
        assumed_cost_dc=100,
        rez_cost=7040,
        temple_factor=4.34,
    ),
    "T7 Wind Lord": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=190000,
        dragon_coins=1800,
        assumed_cost_dc=100,
        rez_cost=7200,
        temple_factor=4.34,
    ),
    "T7 Destructive Colossus": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=180000,
        dragon_coins=1720,
        assumed_cost_dc=100,
        rez_cost=6880,
        temple_factor=4.34,
    ),
    "T7 Ancient Terror": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=168000,
        dragon_coins=1640,
        assumed_cost_dc=100,
        rez_cost=6560,
        temple_factor=4.34,
    ),
    "TI Devastator": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=360400,
        dragon_coins=2120,
        assumed_cost_dc=75,
        rez_cost=8480,
        temple_factor=5.02,
    ),
    "TI Fire Phoenix": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=367200,
        dragon_coins=2160,
        assumed_cost_dc=75,
        rez_cost=8640,
        temple_factor=5.02,
    ),
    "TI Kraken": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=374000,
        dragon_coins=2200,
        assumed_cost_dc=75,
        rez_cost=8800,
        temple_factor=5.02,
    ),
    "TI Trickster": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=353600,
        dragon_coins=2080,
        assumed_cost_dc=75,
        rez_cost=8320,
        temple_factor=5.02,
    ),
    "TII Devastator": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=402800,
        dragon_coins=2120,
        assumed_cost_dc=75,
        rez_cost=8480,
        temple_factor=5.91,
    ),
    "TII Fire Phoenix": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=410400,
        dragon_coins=2160,
        assumed_cost_dc=75,
        rez_cost=8640,
        temple_factor=5.91,
    ),
    "TII Kraken": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=418000,
        dragon_coins=2200,
        assumed_cost_dc=75,
        rez_cost=8800,
        temple_factor=5.91,
    ),
    "TII Trickster": lambda casualties: calculate_monster_cost(
        casualties=casualties,
        prod_cost=395200,
        dragon_coins=2080,
        assumed_cost_dc=75,
        rez_cost=8320,
        temple_factor=5.91,
    ),
}


mercs = {
    "T5 Swift Marksman": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=50400, temple_factor=1.53, compensation_price=504000
    ),
    "T5 Epic Mercs": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=50400, temple_factor=1.53, compensation_price=504000
    ),
    "T5 Scorpion": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=504000, temple_factor=1.53, compensation_price=5040000
    ),
    "T5 Gargoyle": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=945000, temple_factor=1.53, compensation_price=9450000
    ),
    "T5 Bear": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1008000, temple_factor=1.53, compensation_price=10080000
    ),
    "T5 Unicorn Rider": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1260000, temple_factor=1.53, compensation_price=12600000
    ),
    "T5 Bull Rider": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1386000, temple_factor=1.53, compensation_price=13860000
    ),
    "T5 Giant Zombie": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1575000, temple_factor=1.53, compensation_price=15750000
    ),
    "T5 Scorpion Rider": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1764000, temple_factor=1.53, compensation_price=17640000
    ),
    "T5 Ifrit": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=2079000, temple_factor=1.53, compensation_price=20790000
    ),
    "T5 Cyclops": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=2142000, temple_factor=1.53, compensation_price=21420000
    ),
    "T5 Fireworm Rider": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=2394000, temple_factor=1.53, compensation_price=23940000
    ),
    "T6 Arbalester-Trailseeker": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=36000, temple_factor=1.81, compensation_price=360000
    ),
    "T6 Epic Mercs": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=36000, temple_factor=1.81, compensation_price=360000
    ),
    "T6 Legionary-Knight": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=36000, temple_factor=1.81, compensation_price=360000
    ),
    "T6 Chariot-Rhino Rider": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=72000, temple_factor=1.81, compensation_price=720000
    ),
    "T6 Sphinx-Shedu": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1440000, temple_factor=1.81, compensation_price=14400000
    ),
    "T6 Pathfinder-Pionnier": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=180000, temple_factor=1.81, compensation_price=1800000
    ),
    "T6 Trebuchet": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=360000, temple_factor=1.81, compensation_price=3600000
    ),
    "T6 Death Chariots": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1080000, temple_factor=1.81, compensation_price=10800000
    ),
    "T6 Bone Golem": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1350000, temple_factor=1.81, compensation_price=13500000
    ),
    "T6 Ent": lambda casualties: calculate_merc_cost(
        casualties=casualties, rez_cost=1395000, temple_factor=1.81, compensation_price=13950000
    ),
    "T6 Cursed Dendroids": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=2025000, temple_factor=1.81, compensation_price=20250000
    ),
    "T6 Abomination": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=2430000, temple_factor=1.81, compensation_price=24300000
    ),
    "T6 Archdemons": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=3420000, temple_factor=1.81, compensation_price=34200000
    ),
    "T7 Palintone": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=90000, temple_factor=2.51, compensation_price=900000
    ),
    "T7 Epic Mercs": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=90000, temple_factor=2.51, compensation_price=900000
    ),
    "T7 Jungle King": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=2970000, temple_factor=2.51, compensation_price=29700000
    ),
    "T7 Sea Lord": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=360000, temple_factor=2.51, compensation_price=3600000
    ),
    "T7 Lighting Lord": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=405000, temple_factor=2.51, compensation_price=4050000
    ),
    "T7 Golden Dragon": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=450000, temple_factor=2.51, compensation_price=4500000
    ),
    "T7 Overlord": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=540000, temple_factor=2.51, compensation_price=5400000
    ),
    "T7 Life Dragon": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=630000, temple_factor=2.51, compensation_price=6300000
    ),
    "T7 Cursed Dragon": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=832500, temple_factor=2.51, compensation_price=8325000
    ),
    "T7 Sandworm": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=1147500, temple_factor=2.51, compensation_price=11475000
    ),
    "T7 Fire Lord": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=1473750, temple_factor=2.51, compensation_price=14737500
    ),
    "TII Highlander-Pounder": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=57000, temple_factor=3.84, compensation_price=570000
    ),
    "TII Epic Mercs": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=57000, temple_factor=3.84, compensation_price=570000
    ),
    "TII Slavic Warrior-Scarface": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=57000, temple_factor=3.84, compensation_price=570000
    ),
    "TII Quicksand-Galloper": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=114000, temple_factor=3.84, compensation_price=1140000
    ),
    "TII Warregal-Jago": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=114000, temple_factor=3.84, compensation_price=1140000
    ),
    "TII Grace": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=28500, temple_factor=3.84, compensation_price=285000
    ),
    "TII Ariel": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=57000, temple_factor=3.84, compensation_price=570000
    ),
    "TII Wardens": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=242250, temple_factor=3.84, compensation_price=2422500
    ),
    "TII Demonic Salamanders": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=213750, temple_factor=3.84, compensation_price=2137500
    ),
    "TII Eternal Cannoneers": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=228000, temple_factor=3.84, compensation_price=2280000
    ),
    "TII Wyverns": lambda x: calculate_merc_cost(
        casualties=x, rez_cost=356250, temple_factor=3.84, compensation_price=3562500
    ),
}

categories = {
    "Resources": resources,
    "Guardsmen": guardsmen,
    "Specialists": specialists,
    "Monsters": monsters,
    "Mercenaries": mercs,
}


def calculate_category_total(category_dict, casualties_dict):
    total_silver = 0
    for unit, casualties in casualties_dict.items():
        if unit in category_dict:
            # Call the lambda function or the specific calculation function for the unit
            total_silver += category_dict[unit](casualties)
    return total_silver


def calculate_total_silver(**kwargs):
    grand_total_silver = 0
    for category, casualties_dict in kwargs.items():
        if category in categories:
            category_dict = categories[category]
            grand_total_silver += calculate_category_total(category_dict, casualties_dict)
    return int(grand_total_silver)
