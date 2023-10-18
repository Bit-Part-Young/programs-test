import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_params import set_plot_params

set_plot_params(font_size=18, legend_frameon=False, legend_fontsize=16)
# set_plot_params(font_size=18, legend_frameon=False, legend_fontsize=15)

markers = {
    "AlAl": "+",
    "AlTi": "^",
    "AlNb": "o",
    "AlMo": "s",
    "AlZr": ">",
    "TiTi": "x",
    "TiNb": "d",
    "TiMo": "<",
    "TiZr": "p",
    "NbNb": "+",
    "NbMo": "v",
    "NbZr": "h",
    "MoMo": "1",
    "MoZr": "2",
    "ZrZr": "3",
}

colors = {
    "AlTi": (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
    "AlNb": (1.0, 0.4980392156862745, 0.054901960784313725),
    "AlMo": (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
    "AlZr": (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
    "TiNb": (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
    "TiMo": (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
    "TiZr": (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
    "NbMo": (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
    "NbZr": (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
    "MoZr": (0.09019607843137255, 0.7450980392156863, 0.8117647058823529),
    "AlAl": (0.4980392156862745, 0.788235294117647, 0.4980392156862745),
    "TiTi": (0.7450980392156863, 0.6823529411764706, 0.8313725490196079),
    "NbNb": (0.9921568627450981, 0.7529411764705882, 0.5254901960784314),
    "MoMo": (0.9411764705882353, 0.00784313725490196, 0.4980392156862745),
    "ZrZr": (0.3196078431372549, 0.7235294117647059, 0.7901960784313725),
}

cs = [0.1]
# cs = [0.1, 0.15, 0.2]
df = pd.read_csv("./csro_300.csv")
# df = pd.read_csv("csv/csro_300.csv")
# pairs = ['AlAl', 'AlTi', 'AlNb', 'AlZr', 'TiTi', 'TiNb', 'TiZr', 'NbNb', 'NbZr', 'ZrZr']
pairs = [
    "AlTi",
    "AlNb",
    "AlZr",
    "TiNb",
    "TiZr",
    "NbZr",
]
Al13 = {
    "AlAl": -0.251372,
    "AlTi": 0.265012,
    "AlNb": 0.600106,
    "AlZr": -1.38674,
    "TiTi": -0.09904,
    "TiNb": -0.20908,
    "TiZr": 0.353724,
    "NbNb": -0.53790,
    "NbZr": 0.801694,
    "ZrZr": -0.92824,
}

# fig, ax = plt.subplots()
fig, axes = plt.subplots(
    2, 1, gridspec_kw={"height_ratios": [2, 4]}, sharex=True, figsize=(9, 7)
)
plt.subplots_adjust(
    hspace=0.00,
)
for c in cs:
    print("Tne conc is {}".format(c))
    dft = df[(df.Nb == c) & (df.Zr == c) & (df.Al != 0)]
    dft = dft.sort_values("Al")

    ax = axes[0]
    ax.set_ylabel("$T_c (K)$")
    ax.plot(
        100 * dft.Al,
        dft["Tc"],
        linestyle="-",
        marker="o",
    )
    ax.scatter(13, 666, marker="x", label="Al13")
    # ax.text(11.5, 1000, 'Al13', fontsize=14)
    # ax.legend()
    ax.set_ylim([150, 1400])

    ax = axes[1]
    for pair in pairs:
        print("The pair is {}".format(pair))
        if dft[pair].isna().all():
            continue
        plt.plot(
            100 * dft.Al,
            dft[pair],
            color=colors[pair],
            label=pair,
            marker=markers[pair],
        )
        plt.scatter(13, Al13[pair], color=colors[pair], marker="x")

    # plt.legend(ncol=3)
    plt.ylim([-2, 1.1])
    # plt.xlim([2, 33])
    # plt.xticks(np.arange(0, 0.35, 0.05))
    plt.xlabel("Al (at%)")
    plt.ylabel("CSRO")
    plt.legend(ncol=2, columnspacing=0.5)
    # plt.show()
    plt.savefig("f7-5-5-csro_cNb{}_300.jpg".format(c))
    plt.close()
