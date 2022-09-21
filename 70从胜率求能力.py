import random

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

def From_Cap_to_Rate(Cap_A,Cap_B,n):
    win_A, win_B = Sim_Games(Cap_A,Cap_B,n)
    rate_A = win_A/n
    rate_B = win_B/n
    return rate_A,rate_B

def End_Adj(rate_A,rate_A_gt):
    if abs(rate_A-rate_A_gt)<0.05:
        return True
    else:
        return False

def Adj_Cap(rate_A_gt,n=10):
    Cap_A = 0.5
    Cap_B = 0.5
    rate_A, rate_B = From_Cap_to_Rate(Cap_A,Cap_B,n)
    while not End_Adj(rate_A,rate_A_gt):
        if rate_A>rate_A_gt:
            Cap_B += 0.01
            rate_A, rate_B = From_Cap_to_Rate(Cap_A, Cap_B,n)
        else:
            Cap_A += 0.01
            rate_A, rate_B = From_Cap_to_Rate(Cap_A, Cap_B,n)
    return Cap_A,Cap_B

def main():
    rate_A_gt = eval(input('输入牛逼方的胜率：'))
    n = int(eval(input('每次验证通过的比赛轮数：')))
    Cap_A,Cap_B = Adj_Cap(rate_A_gt,n)
    print('强势方的能力值为：{:.3f}，弱势方的能力值为：{:.3f}，能力值之差为：{:.3f}'.format(Cap_A,Cap_B,abs(Cap_A-Cap_B)))

if __name__ == '__main__':
    main()


