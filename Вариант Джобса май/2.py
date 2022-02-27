# 𝑎 ∧ ¬𝑏 ∨ (𝑎 ∨ 𝑏) ∧ 𝑐 ∨ 𝑑
print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                if (a and not(b) or (a or b) and c or d) == False:
                    print(a, b, c, d)
