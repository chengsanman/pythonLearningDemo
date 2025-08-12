####### 题目1： 3x4改成4x3的矩阵
# 原始的 3x4 矩阵
list_second = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 1. 获取原矩阵的行数和列数
original_rows = len(list_second)
original_cols = len(list_second[0]) # 假设矩阵不为空

# 2. 创建一个空的 4x3 矩阵 (用 0 作为占位符)
# 新矩阵有 original_cols 行, original_rows 列
transposed_list = []
for i in range(original_cols):
    # 为新矩阵的每一行创建一个空列表
    new_row = []
    for j in range(original_rows):
        # 用 0 填充新矩阵的每一列
        new_row.append(0)
    # 将创建好的新行添加到转置矩阵中
    transposed_list.append(new_row)

# 此时 transposed_list 的结构是:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 3. 遍历原矩阵，将元素填充到新矩阵的正确位置
# 外层循环遍历原矩阵的行
for i in range(original_rows):
    # 内层循环遍历原矩阵的列
    for j in range(original_cols):
        # 将原矩阵在 (i, j) 的元素放到新矩阵的 (j, i) 位置
        transposed_list[j][i] = list_second[i][j]

# 打印最终结果
print(transposed_list)

