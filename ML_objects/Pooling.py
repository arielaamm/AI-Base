class Pooling:
    def MaxPooling(input_matrix, pool_size = 2):
        output_rows = len(input_matrix) // pool_size
        output_cols = len(input_matrix[0]) // pool_size
        output_matrix = [[0 for _ in range(output_cols)] for _ in range(output_rows)]
        for row in range(output_rows):
            for col in range(output_cols):
                start_row = row * pool_size
                start_col = col * pool_size
                window = [
                    input_matrix[i][j]
                    for i in range(start_row, start_row + pool_size)
                    for j in range(start_col, start_col + pool_size)
                ]
                output_matrix[row][col] = max(window)
        return output_matrix

    def AvgPooling(input_matrix, pool_size = 2):
        output_rows = len(input_matrix) // pool_size
        output_cols = len(input_matrix[0]) // pool_size
        output_matrix = [[0 for _ in range(output_cols)] for _ in range(output_rows)]
        for row in range(output_rows):
            for col in range(output_cols):
                start_row = row * pool_size
                start_col = col * pool_size
                window = [
                    input_matrix[i][j]
                    for i in range(start_row, start_row + pool_size)
                    for j in range(start_col, start_col + pool_size)
                ]
                output_matrix[row][col] = sum(window) / pool_size*pool_size
        return output_matrix