def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    # Ensure both tuples have at least 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Add the first elements of the tuples
    sum_a = tuple_a[0] + tuple_b[0]

    # Add the second elements of the tuples
    sum_b = tuple_a[1] + tuple_b[1]

    # Return the result as a tuple
    return (sum_a, sum_b)
