import math

# Nakamoto's C Poisson Distribution logic re-written in python
def attackerSuccessProbability(q, z):
    p = 1.0 - q
    Lambda = z * (q / p)
    sum = 1.0

    i, k = 0, 0
    for k in range(z+1):
        poisson = math.exp(-Lambda)
        for i in range(1, k+1):
            poisson *= (Lambda / i)
        sum -= poisson * (1 - pow(q/p, z-k))
    
    return float(sum)

def attackerSuccessProbabilityRevised(q, z):
    p = 1.0 - q
    Lambda = z * (q / p)
    sum = 1.0

    i, k = 0, 0
    for k in range((z+1)+1):
        poisson = math.exp(-Lambda)
        for i in range(1, k+1):
            poisson *= (Lambda / i)
        sum -= poisson * (1 - pow(q/p, (z+1)-k))
    
    return float(sum)

if __name__ == "__main__":
    qInput = float(input("q value (attacker mining power): "))
    zInput = int(input("z value (block deficit): "))

    attackerSuccess = attackerSuccessProbability(qInput, zInput)
    print(f"Attacker Success Probability to catch-up: {attackerSuccess:10f}")

    attackerOvertake = attackerSuccessProbabilityRevised(qInput, zInput)
    print(f"Attacker Success Probability to overtake: {attackerOvertake:10f}")