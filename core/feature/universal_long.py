import numpy as np


def calculate_stats(value_list, index_list, normalized_index_list):
    # Calculate basic statistics
    avg = np.mean(value_list)
    max_value = np.max(value_list)
    min_value = np.min(value_list)
    max_by_min = max_value / min_value if min_value != 0 else float("inf")
    avg_weighted_norm = np.average(value_list, weights=normalized_index_list)
    stats = {
        "avg": avg,
        "avg_weighted_norm": avg_weighted_norm,
        "max": max_value,
        "max_by_min": max_by_min,
        "min": min_value,
        "std_dev": np.std(value_list),
        "variance": np.var(value_list),
    }

    # Round all statistics to three decimal places
    stats = {key: round(value, 3) for key, value in stats.items()}

    return stats
