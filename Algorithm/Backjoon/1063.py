

















# dict_={
#     'R' : (0, 1),
#     'L' : (0, -1),
#     'B' : (1, 0),
#     'T' : (-1, 0),
#     'RT' : (-1, 1),
#     'LT' : (-1, -1),
#     'RB' : (1, 1),
#     'LB' : (1, -1)
# }

# king, stone, N = input().split()

# king_row, king_col = 8 - int(king[1]), ord(king[0])-65 
# stone_row, stone_col = 8 - int(stone[1]), ord(stone[0])-65 

# for _ in range(int(N)):
#     move = input()
#     n_king_row = king_row + dict_[move][0]
#     n_king_col = king_col + dict_[move][1]
    
#     if 0 <= n_king_row < 8 and 0 <= n_king_col < 8:
#         if stone_row == n_king_row and stone_col == n_king_col:
#             n_stone_row = stone_row + dict_[move][0]
#             n_stone_col = stone_col + dict_[move][1]
#             if 0 <= n_stone_row < 8 and 0 <= n_stone_col < 8:
#                 stone_row = stone_row + dict_[move][0]
#                 stone_col = stone_col + dict_[move][1]
#                 king_row = n_king_row
#                 king_col = n_king_col
#         else:
#             king_row = n_king_row
#             king_col = n_king_col

# ans_king = chr(int(king_col)+65) + str(8-king_row)
# ans_stone = chr(int(stone_col)+65) + str(8-stone_row)

# print(ans_king)
# print(ans_stone)