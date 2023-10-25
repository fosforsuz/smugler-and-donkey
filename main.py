import random

def read_input_data():
    """
    Reads input data from the user and returns the processed decision variable ranges, n1 and n2 values.

    Returns:
    decision_variable_ranges_processed (list): A list of tuples representing the processed decision variable ranges.
    n1_input (int): The value of n1 entered by the user.
    n2_input (int): The value of n2 entered by the user.
    """
    decision_variable_ranges_input = input("Karar değişkenlerinin aralıklarını girin (örneğin, 0-10, 20-30): ").split(',')
    n1_input = int(input("n1 değerini girin: "))
    n2_input = int(input("n2 değerini girin: "))
    
    decision_variable_ranges_processed = []
    for var_range in decision_variable_ranges_input:
        start, end = var_range.strip().split('-')
        decision_variable_ranges_processed.append((float(start), float(end)))
    
    return decision_variable_ranges_processed, n1_input, n2_input


def generate_initial_population(decision_variable, row, column):
    initial_population = []

    for _ in range(1, row + 1):
        row_values = []
        for _ in range(1, column + 1):
            # Her hücre için rastgele bir değer üret
            rand_value = random.uniform(decision_variable[0][0], decision_variable[0][1])
            row_values.append(rand_value)
        initial_population.append(row_values)

    return initial_population


if __name__ == "__main__":
    decision_variable_ranges, n1, n2 = read_input_data()
    