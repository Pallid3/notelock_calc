

#AR < 5: preempt = 1200ms + 120ms * (5 - AR)
#AR = 5: preempt = 1200ms
#AR > 5: preempt = 1200ms - 150ms * (AR - 5)

ar = 9
def ar_calc(ar):
    if ar < 5:
        preempt = 1200 + 120 * (5 - ar)
    elif ar == 5:
        preempt = 1200
    elif ar > 5:
        preempt = 1200 - 150 * (ar - 5)
    return preempt

print(ar_calc(ar))
