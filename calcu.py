def calcular_factores(i, n):
    i = i / 100  # convertir porcentaje a decimal
    F_P = (1 + i)**n
    P_F = 1 / F_P
    F_A = ((1 + i)**n - 1) / i
    A_F = i / ((1 + i)**n - 1)
    P_A = ((1 + i)**n - 1) / (i * (1 + i)**n)
    A_P = (i * (1 + i)**n) / ((1 + i)**n - 1)
    F_G = (((1 + i)**n - 1) / i**2) - (n / i)
    P_G = (((1 + i)**n - 1) / (i**2 * (1 + i)**n)) - (n / (i * (1 + i)**n))
    A_G = (1 / i) - (n / ((1 + i)**n - 1))
    return {
        "F/P": round(F_P, 4),
        "P/F": round(P_F, 4),
        "F/A": round(F_A, 4),
        "A/F": round(A_F, 4),
        "P/A": round(P_A, 4),
        "A/P": round(A_P, 4),
        "F/G": round(F_G, 4),
        "P/G": round(P_G, 4),
        "A/G": round(A_G, 4)
    }
