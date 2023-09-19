### Master Mode project attempt for Tears of the Kingdom (works only on 1.1.0)

##### Regular gameplay changes
- Gloom damage went from 0.3x damage to 0.8x damage
- Almost all Link's attacks do not interrupt enemies' actions
- Charged attacks are slower and take more stamina
- Hitting a Lynel when on its back does less damage for one handed and two handed weapons
- Flurry rush only does 0.25x damage
- Spin to win only does 0.5x damage

##### Scaling
- All enemies that have golden variants (so not counting Constructs) will go up a rank (like in BotW). There will still be one of each base enemy for the compendium. Each tier of enemy will use the XP threshold of the previous rank, like in BotW as well. e.g. Silver Lizalfos -> Golden Lizalfos will occur when Black Lizalfos -> Silver Lizalfos would have occured in Normal Mode.
  - [Red Bokoblin](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,G-4,0xb485726697bc4505)
  - [Red Armored Bokoblin](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Depths?id=MinusField,D-6,0x8f761f61db5ed24e)
  - [Red Moblin](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,E-7,0xb33392917f6dfb14)
  - [Green Lizalfos](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,C-1,0xb9172ba12f4c5007)
  - [Red Lynel](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,I-2,0x6b549b34c4879128)
  - [Red Armored Lynel](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Depths?id=MinusField,F-6,0x13737102680c78dc)
  - [Red Horriblin](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,Cave__Cave_Hebra_0035_GroupSet_000%20,0xf6653dfe76458d9e)
  - [Red Boss Bokoblin](https://objmap-totk.zeldamods.org/#/map/z2,0,0,Surface?id=MainField,G-1,0x3d8aa5f4040846fb)

##### New enemies

###### Golden Bokoblin (Enemy_Bokoblin_Gold )(fully implemented)
- Base Attack Power: 56
- Base Attack Power (melee): 80
- Base Attack Power (ranged): 56
- HP: 1,620
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Bokoblin or Majora's Masks
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Golden Moblin (Enemy_Moriblin_Gold) (fully implemented)
- Base Attack Power: 64
- Base Attack Power (melee): 92
- Base Attack Power (ranged): 56
- HP: 2,880
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Moblin or Majora's Masks
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Golden Lizalfos (Enemy_Lizalfos_Gold) (fully implemented)
- Base Attack Power: 60
- Base Attack Power (melee): 86
- Base Attack Power (ranged): 86
- HP: 2,260
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Lizalfos or Majora's Masks
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Golden Lynel (Enemy_Lynel_Gold) (fully implemented)
- Base Attack Power: 104
- Base Attack Power (melee): 130
- Base Attack Power (ranged): 104
- HP: 10,000
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Lynel or Majora's Masks
- Arrows only do 20% of damage
- Can't headshot

###### Golden Bokoblin (armored) (Enemy_Bokoblin_Armor_Gold) (fully implemented)

###### Golden Lynel (armored) (Enemy_Lynel_Boss_Gold) (fully implemented)

###### Golden Horriblin (Enemy_Horablin_Gold) (fully implemented)
- Base Attack Power: 50
- Base Attack Power (melee): 76
- Base Attack Power (ranged): 50
- HP: 1,840
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Horriblin or Majora's Masks
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Golden Boss Bokoblin (Enemy_Bokoblin_Boss_Gold) (fully implemented)
- Base Attack Power: 76
- Base Attack Power (melee): 96
- Base Attack Power (ranged): 76
- HP: 4,000
- No cooldown
- Faster speed
- Better awareness
- Can not be tricked with Bokoblin or Majora's Masks
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Soldier Construct V (Enemy_Zonau_Robot_Gold) (fully implemented)
- Base Attack Power: 56
- Base Attack Power (melee): 80
- Base Attack Power (ranged): 56
- HP: 1,620
- No cooldown
- Faster speed
- Better awareness
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

###### Captain Construct V (Enemy_Zonau_Golem_Gold) (fully implemented)
- Base Attack Power: 64
- Base Attack Power (melee): 86
- Base Attack Power (ranged): 64
- HP: 2,400
- No cooldown
- Faster speed
- Better awareness
- Immune to all elements and confusion
- Arrows only do 20% of damage
- Harder to headshot, headshots only deal 150% damage

Check minibosses_spoilers.md for new mini bosses variants. If you're only a player and not actually a modder, you better not click on that for a better surprise!

##### New enemy materials

###### Golden Lizalfos Tail (Item_Enemy_900) (fully implemented)
- Fuse Damage: 49
- Sell Price: 150
- Buy Price: 600
- Crit chance: 60%
- Cook time: 5:20

###### Golden Bokoblin Horn (Item_Enemy_901) (fully implemented, waiting for model/texture)
- Fuse Damage: 52
- Sell Price: 175
- Buy Price: 700
- Cook time: 2:00

###### Golden Moblin Horn (Item_Enemy_902) (fully implemented, waiting for model/texture)
- Fuse Damage: 57
- Sell Price: 200
- Buy Price: 800
- Cook time: 2:30

###### Golden Lizalfos Horn (Item_Enemy_903) (fully implemented)
- Fuse Damage: 60
- Sell Price: 250
- Buy Price: 1000
- Cook time: 3:00

###### Golden Horriblin Horn (Item_Enemy_904) (fully implemented, waiting for model/texture)
- Fuse Damage: 62
- Sell Price: 300
- Buy Price: 1200
- Cook time: 4:00

###### Golden Boss Bokoblin Horn (Item_Enemy_905) (fully implemented, waiting for model/texture)
- Fuse Damage: 70
- Sell Price: 400
- Buy Price: 1600
- Cook time: 5:00

###### Golden Lynel Saber Horn (Item_Enemy_906) (fully implemented)
- Fuse Damage: 85
- Sell Price: 650
- Buy Price: 2600
- Cook time: 9:00

###### Golden Lynel Mace Horn (Item_Enemy_907) (fully implemented)
- Fuse Damage: 78
- Sell Price: 650
- Buy Price: 2600
- Cook time: 9:00

###### Soldier Construct V Horn (Item_Enemy_908) (fully implemented, waiting for model/texture)
- Fuse Damage: 50
- Sell Price: 200
- Buy Price: 800

###### Captain Construct V Horn (Item_Enemy_909) (fully implemented, waiting for model/texture)
- Fuse Dmaage: 65
- Sell Price: 300
- Buy Price: 1200

##### New weapons

###### Lynel Sword (Weapon_Sword_016) (fully implemented, waiting for model/texture)
- Damage: 18
- Durability: 20
- Fuse durability: 10
- Able to guard by itself

###### Lynel Crusher (Weapon_Lsword_016) (not started yet)
- Damage: 26
- Durability: 18
- Fuse durability: 10
- Able to guard by itself

###### Lynel Spear (Weapon_Spear_016) (not started yet)
- Damage: 10
- Durability: 25
- Fuse durability: 10
- Able to guard by itself

###### Mighty Lynel Sword (Weapon_Sword_017) (not started yet)
- Damage: 28
- Durability: 25
- Fuse durability: 10
- Able to guard by itself

###### Mighty Lynel Crusher (Weapon_Lsword_017) (not started yet)
- Damage: 40
- Durability: 21
- Fuse durability: 10
- Able to guard by itself

###### Mighty Lynel Spear (Weapon_Lsword_017) (not started yet)
- Damage: 16
- Durability: 30
- Fuse durability: 10
- Able to guard by itself

###### Savage Lynel Sword (Weapon_Sword_018) (not started yet)
- Damage: 42
- Durability: 30
- Fuse durability: 10
- Able to guard by itself

###### Savage Lynel Crusher (Weapon_Lsword_018) (not started yet)
- Damage: 58
- Durability: 24
- Fuse durability: 10
- Able to guard by itself

###### Savage Lynel Spear (Weapon_Spear_018) (not started yet)
- Damage: 34
- Durability: 35
- Fuse durability: 10
- Able to guard by itself

###### Seized Construct Sword (Weapon_Sword_200) (not started yet)
- Damage: 30
- Durability: 54
- Zonai bonus: 25

###### Seized Construct Longsword (Weapon_Lsword_200) (not started yet)
- Damage: 45
- Durability: 50
- Zonai bonus: 25

###### Seized Construct Spear (Weapon_Spear_200) (not started yet)
- Damage: 21
- Durability: 50
- Zonai bonus: 25

###### Seized Construct Shield (Weapon_Shield_200) (not started yet)
- Guard: 70
- Durability: 40
- Fuse Damage: 15

###### Seized Construct Bow (Weapon_Bow_200) (not started yet)
- Damage: 45
- Durability: 60
- Range: 40
- Arrow gravity: -5.0
- Fuse Damage: 11