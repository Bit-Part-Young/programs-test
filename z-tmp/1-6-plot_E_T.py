import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mchammer import DataContainer
from plot_params import set_plot_params

set_plot_params(font_size=18, legend_frameon=False, legend_fontsize=16)


def get_data():
    Ts = np.arange(300, 3100, 100)
    df = pd.read_csv("csv/csro_300.csv")
    # fig, axes = plt.subplots(2, 3)

    records = []
    for c in [0.10]:
        dft = df[(df.Nb == c) & (df.Zr == c) & (df.Al != 0)]
        dft = dft.sort_values("Al")
        for d in dft.dirs:
            c_Al = dft[dft.dirs == d]["Al"].values[0]
            print(
                d,
            )
            for T in Ts:
                print(
                    T,
                    "K",
                )
                dc = DataContainer.read(
                    "data2/pos/{}/canonical_ensemble/canonical_ensemble_T{}.dc".format(
                        d, T
                    )
                )
                mean_E = dc.data["potential"][-2000:].mean() / 2000
                records.append({"dirs": d, "Al": c_Al, "Ts": T, "mean_E": mean_E})

    df = pd.DataFrame(records)
    df.to_csv("d1-6-cAl_E.csv", index=False)


os.path.exists("d1-6-cAl_E.csv") or get_data()
df = pd.read_csv("d1-6-cAl_E.csv")

fig, ax = plt.subplots(figsize=(8, 6))
markers = ["o", "s", "^", "*", "+", "x", "D", "h", "H", "p", "X"]
for c_Al in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]:
    dft = df[df.Al == c_Al]
    plt.plot(dft.Ts, dft.mean_E, marker=".", label="{:.2f}".format(c_Al))

plt.ylim([-0.43, -0.05])
plt.xlabel("Temperature (K)")
plt.ylabel("Mixing Energy (eV/atom)")

plt.legend(ncol=3, columnspacing=0.5)
plt.savefig("f1-6-E.jpg")
plt.close()
