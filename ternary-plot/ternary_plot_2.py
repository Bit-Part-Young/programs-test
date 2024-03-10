import matplotlib.pyplot as plt
import mpltern

ax = plt.subplot(projection="ternary")
# ax = plt.subplot(projection="ternary", ternary_sum=50.0)
# ax = plt.subplot(projection="ternary", ternary_sum=100.0)

ax.set_tlabel("Top (%)")
ax.set_llabel("Left (%)")
ax.set_rlabel("Right (%)")

ax.taxis.set_ticks([0.1, 0.2, 0.3, 0.4, 0.5])
ax.laxis.set_ticks([0.6, 0.7, 0.8, 0.9, 1.0])
ax.raxis.set_ticks([0.1, 0.2, 0.3, 0.4, 0.5])


ax.grid()

# plt.show()

plt.savefig("figure_2.png")
