def naive_levenshtein_distance(word1, word2):
    """Наивная функция нахождения расстояния Левенштейна."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )
    return dp[m][n]


def levenshtein_distance(word1, word2):
    """Функция нахождения расстояния Левенштейна."""
    if len(word1) < len(word2):
        return levenshtein_distance(word2, word1)
    # Инициализация матрицы
    previous_row = list(range(len(word2) + 1))
    current_row = [0] * (len(word2) + 1)
    for i, c1 in enumerate(word1):
        current_row[0] = i + 1
        for j, c2 in enumerate(word2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row[j + 1] = min(insertions, deletions, substitutions)
            if i > 0 and j > 0 and c1 == word2[j - 1] and c2 == word1[i - 1]:
                current_row[j + 1] = min(
                                        current_row[j + 1],
                                        previous_row[j - 1] + 1
                                    )

        # Обновляем предыдущую строку
        previous_row, current_row = current_row, previous_row
    return previous_row[-1]
