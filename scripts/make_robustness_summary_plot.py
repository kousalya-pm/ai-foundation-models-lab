# Renders results/robustness_summary.png from the already-computed MAE/RMSE
# values in notebooks/02_ctsm_robustness.ipynb's summary_df output.
# These numbers are copied, not recomputed -- this script does not run CTSM
# and does not change any experimental result.
import matplotlib.pyplot as plt
import numpy as np

labels = [
    "Baseline\n(clean)",
    "Noise\nsigma=6",
    "Noise\nsigma=10",
    "Noise\nsigma=15",
    "Missing\n5%",
    "Missing\n10%",
    "Missing\n25%",
    "Anomaly\nspike",
]
mae = [2.176, 4.305, 7.170, 10.811, 3.011, 4.105, 3.624, 3.679]
rmse = [2.854, 5.622, 9.371, 14.088, 3.658, 4.888, 4.384, 4.411]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(x - width / 2, mae, width, label="MAE", color="tab:blue")
ax.bar(x + width / 2, rmse, width, label="RMSE", color="tab:red")
ax.axhline(2.176, color="tab:blue", linestyle=":", linewidth=1, alpha=0.6)
ax.axhline(2.854, color="tab:red", linestyle=":", linewidth=1, alpha=0.6)

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Error (percentage points of CPU)")
ax.set_title("CTSM Robustness Summary: MAE / RMSE Across All Experiments\n(dotted lines = clean baseline)")
ax.legend()
plt.tight_layout()
plt.savefig("results/robustness_summary.png", dpi=150)
print("wrote results/robustness_summary.png")
