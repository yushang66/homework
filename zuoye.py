import numpy as np  # 导入实现游戏所需的库

rows, cols = 4, 5# 游戏板尺寸 4x5

board = np.full((rows, cols), '.')# 创建游戏板，初始化为 '.'

players = ['X', 'O', 'T']# 初始化玩家及其符号
scores = {player: 0 for player in players}  # 初始化每个玩家的罚分

total_moves = rows * cols# 总移动次数
move_count = 0  # 当前的移动次数

while move_count < total_moves:# 显示当前游戏板状态
    current_player = players[move_count % len(players)]  # 轮流选择当前玩家
    
    for row in board: # 显示当前棋盘
        print(' '.join(row))
    print()

    while True:# 获取玩家的移动输入
        try:
            x, y = map(int, input(f"玩家 {current_player}，请输入坐标 (行 列): ").split())
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == '.':
                break
            else:
                print("无效移动，该位置已被占用或坐标超出范围。")
        except ValueError:
            print("请输入两个空格分隔的数字。")

    board[x][y] = current_player    # 执行移动

    penalty = 0  # 计算罚分
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == current_player:
            penalty += 1

    scores[current_player] += penalty

    move_count += 1# 增加移动次数

for row in board:# 游戏结束，输出结果
    print(' '.join(row))
print()

print("游戏结束！结果如下：")
for player, score in scores.items():
    print(f"玩家 {player}: 罚分 {score}")

winner = min(scores, key=scores.get)# 判断获胜者
print(f"获胜者：玩家 {winner}，罚分 {scores[winner]} 分！")