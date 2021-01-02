def sum_of_multiples(limit: int, multiples: list) -> int:
    """Give sum of all the multiples of given numbers untill given limit"""
    list_of_multiples = [i
            for i in range(limit)
            if any(i % factor == 0
                for factor in multiples if factor != 0
                )
            ]
    return sum(list_of_multiples)
