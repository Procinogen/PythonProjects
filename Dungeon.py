import math
PlayerHealth = 3
EnemHealth = 2
PlayerAmmo = 0
PlayerBlocked = False
EnemBlocked = False
"""
Initial Print
"""
def Display():
        print PlayerHealth
        print PlayerAmmo
        print '[ ]'
        print '/|\ '
        print '|||'
        print '/ \ '
        print '| |'
        
        print ' '
        print ' '
    
        print EnemHealth
        print '{ }'
        print '/|\ '
        print '|||'
        print '/ \ '
        print '| |'
        return

def Reload():
        PlayerAmmo += 1
        return

def Fire():
        if PlayerAmmo > 0:
            PlayerAmm0 -= 1
            if EnemBlocked == False:
                EnemHealth -= 1
        return

def Block():
    PlayerBlocked = True
    return

def EnemAttack():
    if PlayerBlocked == False:
        PlayerHealth -= 1
    return

def EnemBlock():
    EnemBlocked = True
    return

def TurnCycle():
    PlayerChoice = raw_input('Reload, Fire, or Block?')
    if PlayerChoice == 'Fire':
        Fire()
    if PlayerChoice == 'Reload':
        Relaod()
    if PlayerChoice == 'Block':
        Block()
    return

Display()
TurnCycle()
