import numpy as np


def calculate_stats(value_list, index_list, normalized_index_list):
    # Handling binary values specifically
    A_value = value_list[0]
    B_value = value_list[1]
    A_index = index_list[0]
    B_index = index_list[1]

    # Basic statistics
    max_value = value_list.max()
    min_value = value_list.min()
    avg_value = value_list.mean()

    A_weighted = A_value * A_index
    B_weighted = B_value * B_index

    stats = {
        "A": A_value,
        "B": B_value,
        "A+B": A_value + B_value,
        "A+B_weighted": A_weighted + B_weighted,
        "A-B": A_value - B_value,
        "A-B_weighted": A_weighted - B_weighted,
        "A*B": A_value * B_value,
        "A*B_weighted": A_weighted * B_weighted,
        "A/B": A_value / B_value if B_value != 0 else float("inf"),
        "A/B_weighted": A_weighted / B_weighted
        if B_weighted != 0
        else float("inf"),
        "avg": avg_value,
        "max": max_value,
        "min": min_value,
        "std_dev": np.std(value_list),
        "variance": np.var(value_list),
    }

    # Round all statistics to three decimal places
    stats = {key: round(value, 3) for key, value in stats.items()}

    return stats
