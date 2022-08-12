from matplotlib import pyplot as pl

t = [3.24, 3.22, 3.194, 3.14, 3.09, 3.03, 3.00, 2.95, 2.91, 2.87, 2.83]  # 1000/T
logp = [
    2.5,
    2.49,
    2.45,
    2.30,
    2.19,
    2.07,
    2.00,
    1.93,
    1.83,
    1.74,
    1.65,
]  # log of resistivity

pl.plot(t, logp, marker="o", markerfacecolor="green")
pl.grid()
pl.title("Logρ vs 1000/T")

pl.xlabel("1000/T")
pl.ylabel("logρ")

pl.show()
