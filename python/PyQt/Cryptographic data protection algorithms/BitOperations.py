def is_binary(number):
    return set(number) <= set('01')


def get_bit(value, n):
    return (value >> n & 1) != 0


def set_bit(value, n):
    return value | (1 << n)


def clear_bit(value, n):
    return value & ~(1 << n)


def swap_bits(value, i, j):
    bit1 = (value >> i) & 1
    bit2 = (value >> j) & 1
    x = (bit1 ^ bit2)
    x = (x << i) | (x << j)
    result = value ^ x
    return result


def swap_bytes(value, i, j):
    mask_m = 0xFF << (i << 3)
    mask_n = 0xFF << (j << 3)
    mask = (mask_m | mask_n) ^ 0xFFFFFFFF

    xi = value >> (i << 3)
    xi = xi & 0xFF
    xj = value >> (j << 3)
    xj = xj & 0xFF

    x_swapped = (value & mask) | (xj << (i << 3)) | (xi << (j << 3))
    return x_swapped


def clear_junior_bits(number, m):
    return number >> m << m


def concat_bits(number, i):
    binary_number = str(bin(int(number)))
    binary_number = binary_number[2:]
    length = len(binary_number)

    eMask = (1 << i) - 1
    left = (number >> (length - (i * 2))) & (eMask << i)
    right = number & eMask
    result = left | right
    return result


def cut_bits(number, i):
    binary_number = str(bin(int(number)))
    binary_number = binary_number[2:]
    length = len(binary_number)

    eMask = (1 << (length - i * 2)) - 1
    result = (number & (eMask << i)) >> i
    return result

    # public static int MixBytes(int number, int[] mass)
    # {
    #     int answer = 0;
    #     int offset = 0;
    #     int mask = (1 << 8) - 1;
    #     foreach(int index in mass)
    #     {
    #         var hit = (number & (mask << (index * 8))) >> (index * 8);
    #         answer = answer | (hit << offset*8);
    #         offset++;
    #     }
    #     return answer;
    # }