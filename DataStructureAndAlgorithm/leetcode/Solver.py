
#给定两个排序的数组a,b，长度分别为m和n,找出这两个数组中第k小的数
def the_k_least(A, m, B, n, k):
    # 重新排序
    if m > n:
        return the_k_least(B, n, A, m, k)
    # 数组A元素为零
    if m == 0:
        return B[k - 1]
    # k==1
    if k == 1:
        return min([A[0], B[0]])

    ia = min([k // 2, m])
    ib = k - ia
    if A[ia - 1] < B[ib - 1]:
        return the_k_least(A[ia:], m - ia, B, n, k - ia)
    elif A[ia - 1] > B[ib - 1]:
        return the_k_least(A, m, B[ib:], n - ib, k - ib)
    else:
        return A[ia - 1]


A = [1, 3, 5]
B = [2, 4, 6, 8]

print(the_k_least(A,len(A),B,len(B), 7))
