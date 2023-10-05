# def maxIndex(steps, badIndex):
#     max_distance = steps * (steps + 1) // 2
#
#     if max_distance == badIndex:
#         strategy1 = max_distance - steps
#     elif max_distance > badIndex:
#         strategy1 = max_distance - (badIndex - (steps - 1)) + steps
#     else:
#         strategy1 = max_distance
#
#     max_distance -= 1
#     if max_distance == badIndex:
#         strategy2 = max_distance - (steps - 1)
#     elif max_distance > badIndex:
#         strategy2 = max_distance - (badIndex - (steps - 2)) + (steps - 1)
#     else:
#         strategy2 = max_distance
#
#     return max(strategy1, strategy2)

def maxIndex(steps, badIndex):
    position = 0
    next_move = 1

    for _ in range(steps):
        if position + next_move == badIndex:
            next_move += 1
            continue
        position += next_move
        next_move += 1

    return position


if __name__ == '__main__':
    steps = int(input().strip())
    badIndex = int(input().strip())
    result = maxIndex(steps, badIndex)
    print(result)


def balancedOrNot(expressions, maxReplacements):
    results = []

    for i, expr in enumerate(expressions):
        stack = []
        replacements_needed = 0

        for char in expr:
            if char == '<':
                stack.append(char)
            elif char == '>':
                if stack:
                    stack.pop()
                else:
                    replacements_needed += 1

        if len(stack) <= maxReplacements[i] - replacements_needed:
            results.append(1)
        else:
            results.append(0)

    return results


def balancedOrNot(expressions, maxReplacements):
    results = []

    for i, expr in enumerate(expressions):
        stack = []
        replacements_needed = 0

        for char in expr:
            if char == '<':
                stack.append(char)
            elif char == '>':
                if stack:
                    stack.pop()
                else:
                    replacements_needed += 1

        if len(stack) <= maxReplacements[i] - replacements_needed:
            results.append(1)
        else:
            results.append(0)

    return results


if __name__ == "__main__":
    expressions_count = int(input().strip())
    expressions = [input().strip() for _ in range(expressions_count)]

    maxReplacements_count = int(input().strip())
    maxReplacements = [int(input().strip()) for _ in range(maxReplacements_count)]

    result = balancedOrNot(expressions, maxReplacements)

    for r in result:
        print(r)
