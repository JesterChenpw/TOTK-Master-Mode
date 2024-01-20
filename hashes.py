import mmh3

# Whatever you want here
actor_list = ["Enemy_Bokoblin_Gold_R",
              "Enemy_Moriblin_Gold_R",
              "Enemy_Lizalfos_Gold_R",
              "Enemy_Lynel_Gold_R",
              "Enemy_Horablin_Gold_R",
              "Enemy_Bokoblin_Boss_Gold_R",
              "Enemy_Drake_Lord",
              "Enemy_Zonau_BlockMaster_Gold",
              "Enemy_Sandworm_Gold",
              "Enemy_Golem_Gold",
              "Enemy_Mogurudo_Gold",
              "Enemy_Giant_Gold",
              "Enemy_Bokoblin_Gold",
              "Enemy_Moriblin_Gold",
              "Enemy_Lizalfos_Gold",
              "Enemy_Lynel_Gold",
              "Enemy_Bokoblin_Boss_Gold",
              "Enemy_Horablin_Gold"]

points = {
    "Enemy_Bokoblin_Gold": 40,
    "Enemy_Moriblin_Gold": 55,
    "Enemy_Lizalfos_Gold": 55,
    "Enemy_Lynel_Gold": 150,
    "Enemy_Horablin_Gold": 55,
    "Enemy_Bokoblin_Boss_Gold": 70,
    "Enemy_Zonau_Robot_Gold": 35,
    "Enemy_Zonau_Golem_Gold": 70,
    "Enemy_Drake_Lord": 400,
    "Enemy_Zonau_BlockMaster_Gold": 60,
    "Enemy_Sandworm_Gold": 80,
    "Enemy_Golem_Gold": 60,
    "Enemy_Mogurudo_Gold": 110,
    "Enemy_Giant_Gold": 60,
    "Enemy_Bokoblin_Gold_R": 60,
    "Enemy_Moriblin_Gold_R": 75,
    "Enemy_Lizalfos_Gold_R": 75,
    "Enemy_Horablin_Gold_R": 75,
    "Enemy_Bokoblin_Boss_Gold_R": 90,
    "Enemy_Lynel_Gold_R": 250
}

def hash(value):
    hash = hex(mmh3.hash(value, signed=False))
    while len(hash) != 10:
        hash = hash[:2] + '0' + hash[2:] # add 0's to pad to the right length, just remove if unwanted
    return hash

# Just bump the value after the < if you want it to be further to the right
def format(actor, prefix='', suffix=''):
    return f"{prefix + actor + suffix:<80}{': ' + hash(prefix + actor + suffix)}"

def generate_basic():
    with open('hashes.txt', 'w') as file:
        for actor in actor_list:
            print(format(actor, 'EnemyBattleData.', '.DefeatedNoDamageCount'), file=file)
            print(format(actor, 'DefeatedEnemyNum.'), file=file)
            print(format(actor, 'EnemyBattleData.', '.GuardJustCount'), file=file)
            print(format(actor, 'EnemyBattleData.', '.HeadShotCount'), file=file)
            print(format(actor, 'EnemyBattleData.', '.JustAvoidCount'), file=file)
            print('', file=file) # add a newline to separate individual actors

def generate_for_xp():
    with open('hashes.txt', 'w') as file:
        for actor in points.keys():
            print(str(
                '  - LevelSensorGameDataElement: {ActorName: '
                + actor + ', DefeatedNoDamageCountHash: !u ' + hash('EnemyBattleData.' + actor + '.DefeatedNoDamageCount')
                + ', DefeatedNumGameDataHash: !u ' + hash('DefeatedEnemyNum.' + actor)
                + ', GuardJustCountHash: !u ' + hash('EnemyBattleData.' + actor + '.GuardJustCount')
                + ', HeadShotCountHash: !u ' + hash('EnemyBattleData.' + actor + '.HeadShotCount')
                + ', JustAvoidCountHash: !u ' + hash('EnemyBattleData.' + actor + '.JustAvoidCount')
                + '}\n    Point: ' + str(points[actor]) + '.0'
                + ''
                ), file = file
            )

#generate_basic()
generate_for_xp()