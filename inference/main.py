def sigmoid(arr):
    for i in range(len(arr)):
        arr[i] = 24 + 12 * arr[i] + arr[i]**3
    return arr

def main():
    num_attributes = 4
    num_inferences = 10

    weights = [1, 2, 3, 4]
    acc = [0 for _ in range(num_inferences)]
    inputs = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
              [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
              [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
              [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]]

    # Multiply all attributes by the pre-trained weights and accumulate
    for i in range(num_attributes):
        inputs[i] = [x * weights[i] for x in inputs[i]]

        for j in range(num_inferences):
            acc[j] += inputs[i][j]

    print(sigmoid(acc)[:3])

if __name__ == "__main__":
    main()
