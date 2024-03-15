def minimax_alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = minimax_alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minimax_alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

if __name__ == "__main__":
    MAX = float('inf')
    MIN = float('-inf')
    values = [10, 9, 14, 18, 5, 4, 50, 3]
    print("The optimal value is:", minimax_alpha_beta(0, 0, True, values, MIN, MAX))
