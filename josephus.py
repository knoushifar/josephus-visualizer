def josephus_order(n: int, k: int):
    """
    Returns the elimination order and survivor for the Josephus problem.
    People are numbered from 1 to n.
    """
    if n <= 0:
        raise ValueError("Number of people must be greater than 0.")

    if k <= 0:
        raise ValueError("Step size must be greater than 0.")

    people = list(range(1, n + 1))
    elimination_order = []
    index = 0

    while len(people) > 1:
        index = (index + k - 1) % len(people)
        eliminated = people.pop(index)
        elimination_order.append(eliminated)

    survivor = people[0]
    return elimination_order, survivor