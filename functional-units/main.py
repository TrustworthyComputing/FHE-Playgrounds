# 4 bit adder

def half_adder(a, b):
    sum_out = a ^ b
    carry_out = a & b
    return sum_out, carry_out


def full_adder(a, b, Cin):
    sum_out1, carry_out1 = half_adder(a, b)
    sum_out2, carry_out2 = half_adder(sum_out1, Cin)
    final_sum = sum_out2
    final_carry = carry_out1 | carry_out2
    return final_sum, final_carry


def four_bit_adder(a, b):
    assert len(a) == 4 and len(b) == 4, "Input vectors must be 4 bits long"
    sum_out = [0] * 4
    carry = 0
    for i in range(3, -1, -1):
        sum_out[i], carry = full_adder(a[i], b[i], carry)
    return sum_out, carry


def main():
    # Test the 4-bit adder
    a = [1, 0, 1, 1]
    b = [0, 0, 0, 1]
    sum_result, carry_out = four_bit_adder(a, b)
    print("Sum:", sum_result)
    print("Carry:", carry_out)


if __name__ == "__main__":
    main()
