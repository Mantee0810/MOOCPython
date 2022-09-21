'''
        双人击球比赛，回合制，五局三胜
        发球-判分-胜者发球
        只能在发球局得1分，15分一局
        从能力值求胜率
'''
import random

def Info():
    print('体育竞技胜率分析')

def Get_Num():
    Cap_A = eval(input('输入A的能力值：'))
    Cap_B = eval(input('输入B的能力值：'))
    n = int(eval(input('输入要分析的场数：')))
    return Cap_A,Cap_B,n

def Game_Over(win_A,win_B):
    if win_A>=3 or win_B>=3:
        return True
    else:
        return False

# 一场比赛五局三胜
def Play5Win3(Cap_A,Cap_B):
    win_A = 0
    win_B = 0
    serve = random.choice(['A','B'])
    while not Game_Over(win_A,win_B):
        num = random.random()
        if serve=='A':
            if Cap_A>num:
                win_A += 1
            else:
                serve = 'B'
        else:
            if Cap_B>num:
                win_B += 1
            else:
                serve = 'A'
    if win_A==3:
        winner = 'A'
    else:
        winner = 'B'
    return winner

# 模拟n场比赛
def Sim_Games(Cap_A,Cap_B,n):
    win_A,win_B = 0,0
    for i in range(n):
        if Play5Win3(Cap_A,Cap_B)=='A':
            win_A += 1
        else:
            win_B +=1
    return win_A,win_B


def End(win_A,win_B):
    print('共模拟{}场比赛'.format(win_A+win_B))
    print('A胜率为{}'.format(win_A/(win_A+win_B)))
    print('B胜率为{}'.format(win_B/(win_A+win_B)))

def main():
    Info()
    Cap_A,Cap_B,n = Get_Num()
    win_A,win_B = Sim_Games(Cap_A,Cap_B,n)
    End(win_A,win_B)

if __name__ == '__main__':
    main()


