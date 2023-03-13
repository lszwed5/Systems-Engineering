def generate_data():
    """Generate data according to the plot from assignment."""
    i = 0

    X_data = []
    for _ in range(12):
        X_data.append(i)
        i += 1 / 3
    Y_data = [-0.6, -0.58, -0.5, -0.3, 0, 0.4, 0.75, 1, 0.85, 0.25, -0.5, -1]
    return X_data, Y_data


def ask_for_input_to_interpolate(X_data):
    """Ask for an x to be interpolated.

    :param X_data: The original X dataset that limits the interpolation.
    :type X_data: list"""
    print("\n" + 50 * "=")
    x = float(input(f"Enter the x to which a value should be interpolated\n"
                    f"(Keep in mind, that the value must be between\n"
                    f"{min(X_data): 0.2f} and {max(X_data): 0.2f}): "))
    print("\n")

    if x < min(X_data) or x > max(X_data):
        raise ValueError("Value outside of the original set.")
    return x
