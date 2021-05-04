def solution(numbers, hand):
    answer = ''

    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *(10), #(11)
    keypad = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]

    left_point = 10
    right_point = 11

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left_point = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right_point = i
        else:
            a, b = keypad[i]
            l1, l2 = keypad[left_point]
            r1, r2 = keypad[right_point]
            dist_l = abs(a - l1) + abs(b - l2)
            dist_r = abs(a - r1) + abs(b - r2)
            if dist_l < dist_r:  # 왼쪽이 더 가깝다면,
                answer += 'L'
                left_point = i
            elif dist_l > dist_r:  # 오른쪽이 더 가깝다면,
                answer += 'R'
                right_point = i
            else:  # 둘이 거리가 같다면,
                if hand == 'left':  # 왼손잡이라면,
                    answer += 'L'
                    left_point = i
                else:  # 오른손잡이라면,
                    answer += 'R'
                    right_point = i

    return answer