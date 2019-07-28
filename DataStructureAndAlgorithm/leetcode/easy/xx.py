def Cross_subarray(a, start, mid, end):
    left_sum = -1
    sum = 0
    cross_left = mid
    for i in range(mid, start - 1, -1):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            cross_left = i

    right_sum = -1
    sum = 0
    cross_right = mid
    for i in range(mid + 1, end + 1):
        sum += a[i]
        if sum > right_sum:
            right_sum = sum
            cross_right = i
    print(left_sum + right_sum, cross_left, cross_right)
    return left_sum + right_sum, cross_left, cross_right


def Max_subarray(a, start, end):
    if start == end:
        return a[start], start, end
    else:
        mid = int((start + end) / 2)
        left_sum, left_start, left_end = Max_subarray(a, start, mid)
        right_sum, right_start, right_end = Max_subarray(a, mid + 1, end)
        cross_sum, cross_start, cross_end = Cross_subarray(a, start, mid, end)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_start, left_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_start, right_end
    else:
        return cross_sum, cross_start, cross_end


if __name__ == '__main__':
    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Max_subarray(x, 0, len(x) - 1))
