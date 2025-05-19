def avg_weighted_norm(parsed_formula, property_name, db):
    return sum([i[1] * db[i[0]][property_name] for i in parsed_formula]) / sum(
        [i[1] for i in parsed_formula]
    )


def avg_value(parsed_formula, property_name, db):
    return sum([db[i[0]][property_name] for i in parsed_formula]) / len(
        parsed_formula
    )


def max_value(parsed_formula, property_name, db):
    return max([db[i[0]][property_name] for i in parsed_formula])


def min_value(parsed_formula, property_name, db):
    return min([db[i[0]][property_name] for i in parsed_formula])


def max_by_min_value(parsed_formula, property_name, db):
    return max_value(parsed_formula, property_name, db) / min_value(
        parsed_formula, property_name, db
    )


def first_element_value(parsed_formula, property_name, db):
    return db[parsed_formula[0][0]][property_name]


def last_element_value(parsed_formula, property_name, db):
    return db[parsed_formula[-1][0]][property_name]
