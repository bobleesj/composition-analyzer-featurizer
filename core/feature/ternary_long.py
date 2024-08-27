import numpy as np


def find_middle_value(value_list):
    middle_value = np.median(value_list)
    return middle_value


def calculate_stats(value_list, index_list, normalized_index_list):
    R_value = value_list[0]
    M_value = value_list[1]
    X_value = value_list[2]

    R_index = index_list[0]
    M_index = index_list[1]
    X_index = index_list[2]

    R_weighted = R_value * R_index
    M_weighted = M_value * M_index
    X_weighted = X_value * X_index

    max_value = value_list.max()
    min_value = value_list.min()
    avg_value = value_list.mean()
    mid_value = find_middle_value(value_list)

    stats = {
        # value
        "R": R_value,
        "M": M_value,
        "X": X_value,
        # +
        "R+M": R_value + M_value,
        "M+X": M_value + X_value,
        "R+X": R_value + X_value,
        "R+M_weighted": R_weighted + M_weighted,
        "M+X_weighted": M_weighted + X_weighted,
        "R+X_weighted": R_weighted + X_weighted,
        # -
        "R-M": R_value - M_value,
        "M-X": M_value - X_value,
        "R-X": R_value - X_value,
        "R-M_weighted": R_weighted - M_weighted,
        "M-X_weighted": M_weighted - X_weighted,
        "R-X_weighted": R_weighted - X_weighted,
        # /
        "R/M": R_value / M_value if M_value != 0 else float("inf"),
        "M/X": M_value / X_value if X_value != 0 else float("inf"),
        "R/X": R_value / X_value if X_value != 0 else float("inf"),
        # Weighted /
        "R/M_weighted": R_weighted / M_weighted if M_weighted != 0 else float("inf"),
        "M/X_weighted": M_weighted / X_weighted if X_weighted != 0 else float("inf"),
        "R/X_weighted": R_weighted / X_weighted if X_weighted != 0 else float("inf"),
        # avg
        "avg_RMX": avg_value,
        "avg_RM": np.mean([R_value, M_value]),
        "avg_MX": np.mean([M_value, X_value]),
        "avg_RX": np.mean([R_value, X_value]),
        # max, min, max_by_min
        "max": max_value,
        "min": min_value,
        # max and min difference & sum & ratio
        "max/min": max_value / min_value,
        "max-min": max_value - min_value,
        # max and mid difference & sum & ratio
        "max/mid": max_value / mid_value,
        "max-mid": max_value - mid_value,
        # mid and min difference & sum & ratio
        "mid/min": mid_value / min_value,
        "mid-min": mid_value - min_value,
        # std_dev, variance
        "std_dev": np.std(value_list),
        "variance": np.var(value_list),
    }

    # Round all statistics to three decimal places
    stats = {key: round(value, 3) for key, value in stats.items()}

    return stats
