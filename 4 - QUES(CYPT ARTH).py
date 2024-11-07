def solve_cryptarithmetic():
    for S in range(10):
        for E in range(10):
            for N in range(10):
                for D in range(10):
                    for M in range(10):
                        for O in range(10):
                            for R in range(10):
                                for Y in range(10):
                                    if S != 0 and M != 0:  # S and M cannot be 0
                                        send = S * 1000 + E * 100 + N * 10 + D
                                        more = M * 1000 + O * 100 + R * 10 + E
                                        money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
                                        if send + more == money:
                                            return S, E, N, D, M, O, R, Y
    return None

solution = solve_cryptarithmetic()
if solution:
    S, E, N, D, M, O, R, Y = solution
    print("S = {}, E = {}, N = {}, D = {}, M = {}, O = {}, R = {}, Y = {}".format(S, E, N, D, M, O, R, Y))
    print("SEND + MORE = MONEY")
    print("{}{}{}{} + {}{}{}{} = {}{}{}{}{}".format(S, E, N, D, M, O, R, E, M, O, N, E, Y))
else:
    print("No solution found")