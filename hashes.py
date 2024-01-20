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
              "Enemy_Giant_Gold"]

def hash(value):
    hash = hex(mmh3.hash(value, signed=False))
    while len(hash) != 10:
        hash = hash[:2] + '0' + hash[2:] # add 0's to pad to the right length, just remove if unwanted
    return hash

# Just bump the value after the < if you want it to be further to the right
def format(actor, prefix='', suffix=''):
    return f"{prefix + actor + suffix:<80}{': ' + hash(prefix + actor + suffix)}"

with open('hashes.txt', 'w') as file:
    for actor in actor_list:
        print(format(actor, 'EnemyBattleData.', '.DefeatedNoDamageCount'), file=file)
        print(format(actor, 'DefeatedEnemyNum.'), file=file)
        print(format(actor, 'EnemyBattleData.', '.GuardJustCount'), file=file)
        print(format(actor, 'EnemyBattleData.', '.HeadShotCount'), file=file)
        print(format(actor, 'EnemyBattleData.', '.JustAvoidCount'), file=file)
        print('', file=file) # add a newline to separate individual actors