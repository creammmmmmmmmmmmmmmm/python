# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time

player_list=['bersaka','archer','saber','rider','avenger','foreingner']
enemy_list=['assasian','lancer','altergo','pretender','caster']
players=random.sample(player_list,3)
enemys=random.sample(enemy_list,3)
player_info={}
enemy_info={}

def born_role():
    life=random.randint(100,180)
    attack=random.randint(30,50)
    return life,attack

def show_role():
    for i in range(3):
        player_info[players[i]]=born_role()
        enemy_info[enemys[i]]=born_role()

    print("your servants:")
    for i in range(3):
        print('%s: hp=%s, attack=%s' % (players[i],player_info[players[i]][0],player_info[players[i]][1]))
    print("enemy servants:")
    for i in range(3):
        print('%s: hp=%s, attack=%s' % (enemys[i],enemy_info[enemys[i]][0],enemy_info[enemys[i]][1]))
    return

def order_role():
    global players
    order_dict={}
    for i in range(3):
        order=int(input('you want to put %s in which place?'%players[i]))
        order_dict[order]=players[i]

    players=[]
    for i in range(i,4):
        players.append(order_dict[i])

    print('your servant will attend in this way:%s %s %s'%(players[0],players[1],players[2]))
    print('enemy will attend in this way:%s %s %s'%(enemys[0],enemys[1],enemys[2]))
    return

def pk_role():
    round=1
    score=0
    for i in range(3):
        player_name=players[i]
        enemy_name=enemys[i]
        player_life=player_info[players[i]][0]
        enemy_life=enemy_info[enemys[i]][0]
        player_attack=player_info[players[i]][1]
        enemy_attack=enemy_info[enemys[i]][1]

        print('your servant: %s VS enemy servant: %s'%(players[i],enemys[i]))
        print('hp=%s hp=%s'%(player_info[players[i]][0],enemy_info[enemys[i]][0]))
        print('atk=%s atk=%s'%(player_info[players[i]][1],enemy_info[enemys[i]][1]))

        while player_life>0 and enemy_life>0:
            enemy_life-=player_attack
            player_life-=enemy_attack
            print('%s attack %s,%s hp=%s'%(players[i],enemys[1],enemys[i],enemy_info[enemys[i]][0]))
            print('%s attack %s,%s hp=%s'%(enemys[i],players[i],players[i],player_info[players[i]][0]))
            print('---------------------------------------------------------------------------------------------------------------------------')
            time.sleep(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
