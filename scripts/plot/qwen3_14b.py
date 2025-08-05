import matplotlib.pyplot as plt
import numpy as np

def rescale(x, start_hr, end_hr):
    x = np.array(x)
    return start_hr + (x - x[0]) / (x[-1] - x[0]) * (end_hr - start_hr)

x1_steps = list(range(0, 7000, 200))
y1 = [30.30, 47.35, 50.51, 51.39, 49.49, 50.51, 51.77, 52.27, 53.16, 53.79, 53.16, 55.18, 53.16, 56.19, 53.79, 54.42, 54.92, 54.29, 52.15, 51.52, 55.30, 52.90, 54.67, 54.92, 52.53, 54.80, 56.44, 54.04, 53.28, 52.40, 54.04, 54.92, 53.16, 51.64, 54.17]
y1_1 = [41.29, 39.52, 50.38, 48.86, 52.40, 57.07, 56.31, 54.42, 55.43, 57.58, 58.33, 59.72, 58.21, 58.33, 58.84, 61.11, 58.33, 57.70, 58.96, 58.84, 61.11, 60.48, 59.72, 60.73, 59.47, 61.11, 59.72, 59.85, 60.48, 60.10, 59.60, 62.12, 60.23, 61.62, 60.73]
w1 = [0.00, 17.93, 85.48, 96.34, 98.11, 98.48, 98.74, 98.99, 99.62, 99.12, 99.24, 99.12, 99.49, 99.37, 99.37, 99.12, 99.24, 99.37, 99.12, 99.37, 99.24, 99.49, 99.75, 99.49, 99.24, 99.75, 98.74, 99.62, 99.49, 99.24, 99.62, 99.62, 99.75, 99.62, 99.12]
z1 = [823.7, 18532.8, 17104.8, 19021.7, 21197.2, 22954.4, 23395.0, 24240.7, 24102.5, 24948.8, 25147.8, 24931.1, 26222.0, 25209.9, 25548.7, 26557.9, 26336.1, 26565.3, 25690.5, 26068.2, 26304.7, 26072.6, 25991.6, 26451.8, 25903.8, 25155.6, 25348.8, 25214.8, 24811.3, 25210.3, 24890.1, 25371.7, 25349.6, 25262.4, 24810.0]

x2_steps = list(range(0, 310, 10))
y2 = [30.30, 40.15, 43.43, 44.32, 47.98, 46.84, 47.85, 46.59, 45.83, 47.60, 49.12, 48.99, 51.01, 52.27, 51.14, 48.74, 51.39, 50.38, 49.49, 49.49, 49.49, 48.99, 51.89, 50.76, 51.01, 51.26, 50.88, 53.41, 50.13, 49.87, 47.85]
y2_1 = [41.29, 41.92, 42.42, 45.58, 44.44, 46.84, 48.23, 49.37, 48.48, 49.62, 47.60, 48.74, 50.13, 51.64, 48.48, 50.88, 49.62, 51.77, 51.14, 49.37, 50.88, 51.52, 50.13, 50.76, 50.25, 50.76, 52.27, 49.37, 51.01, 51.14, 49.24]
w2 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
z2 = [823.7, 796.2, 1016.0, 981.9, 1186.8, 1274.9, 1260.0, 1280.1, 1383.9, 1477.0, 1536.2, 1574.3, 1433.7, 1416.0, 1642.2, 1776.2, 1695.5, 1579.8, 1813.4, 1716.4, 1721.5, 1727.9, 1761.3, 1758.1, 1690.3, 1760.3, 1831.6, 1859.5, 1702.9, 1821.9, 1711.5]

x3_steps = list(range(0, 48, 3))
y3 = [47.35, 48.74, 53.79, 56.57, 56.44, 54.67, 58.21, 54.42, 56.82, 58.21, 58.08, 58.59, 58.46, 58.21, 55.56, 55.56]
y3_1 = [39.52, 43.31, 43.69, 44.82, 40.91, 39.77, 38.13, 37.12, 35.48, 35.23, 34.97, 35.23, 35.73, 34.34, 32.95, 33.71]
w3 = [17.93, 14.90, 13.51, 12.75, 11.87, 11.24, 11.74, 7.58, 7.70, 8.33, 7.95, 8.84, 7.07, 8.84, 7.95, 7.95]
z3 = [18532.8, 15580.9, 13347.3, 10407.7, 10314.4, 8892.6, 8000.1, 9340.4, 9070.4, 8275.7, 8439.5, 8030.2, 7996.3, 8088.6, 7892.1, 7345.6]

x4_steps = list(range(0, 48, 3))
y4 = [50.51, 56.31, 55.05, 57.07, 57.32, 58.21, 56.94, 57.95, 57.07, 55.43, 55.56, 58.46, 57.45, 57.95, 56.57, 56.94]
y4_1 = [50.38, 48.48, 46.21, 45.33, 43.18, 42.55, 43.06, 39.77, 39.90, 39.02, 38.89, 38.64, 37.37, 36.99, 33.21, 35.23]
w4 = [85.48, 83.08, 80.68, 80.68, 79.80, 73.61, 72.60, 73.99, 72.60, 76.77, 72.22, 77.90, 76.01, 74.37, 75.51, 71.59]
z4 = [17104.8, 13580.9, 11880.7, 10144.1, 9341.1, 8519.2, 8612.1, 9458.9, 8683.1, 9594.5, 8705.5, 9541.4, 9122.2, 8154.5, 8266.6, 8485.1]

x5_steps = list(range(0, 48, 3))
y5 = [49.49, 53.91, 54.92, 56.31, 55.30, 57.83, 60.23, 57.07, 58.96, 58.08, 57.95, 56.57, 57.07, 58.71, 57.32, 58.21]
y5_1 = [52.40, 52.27, 52.53, 50.63, 47.47, 41.92, 42.17, 43.18, 43.56, 40.66, 39.27, 37.25, 38.76, 37.25, 37.50, 35.35]
w5 = [98.11, 97.73, 98.11, 98.23, 98.36, 98.23, 97.98, 98.23, 98.23, 98.48, 98.48, 98.86, 98.48, 98.48, 98.48, 98.61]
z5 = [21197.2, 19797.8, 17845.8, 16337.2, 15747.6, 14639.2, 14021.8, 14142.6, 13402.6, 15615.0, 15559.3, 15733.0, 15111.5, 15158.3, 14272.5, 14584.9]

x6_steps = list(range(0, 48, 3))
y6 = [53.16, 54.92, 56.82, 56.31, 55.43, 59.09, 57.45, 55.56, 58.84, 59.22, 58.08, 59.60, 57.20, 60.98, 58.59, 58.21]
y6_1 = [55.43, 55.56, 56.57, 52.90, 53.41, 50.51, 50.00, 48.11, 48.74, 48.48, 44.07, 44.19, 46.09, 47.10, 45.83, 45.45]
w6 = [99.62, 98.86, 99.87, 99.62, 99.62, 99.87, 99.75, 99.24, 99.87, 99.49, 99.87, 99.62, 99.62, 99.75, 99.37, 99.62]
z6 = [24102.5, 24537.3, 24987.0, 24573.6, 24832.0, 23638.9, 24027.6, 23694.5, 22107.9, 20219.5, 19561.4, 20030.2, 20705.9, 17280.7, 17262.2, 17062.8]

x7_steps = list(range(0, 48, 3))
y7 = [54.92, 52.02, 56.06, 52.78, 55.93, 56.94, 57.70, 57.20, 57.83, 58.96, 60.10, 59.72, 59.22, 56.69, 60.35, 60.23]
y7_1 = [58.33, 59.97, 59.97, 59.72, 59.34, 55.43, 56.19, 54.80, 55.05, 55.05, 52.65, 53.28, 53.16, 50.76, 50.38, 50.38]
w7 = [99.24, 98.36, 98.74, 98.86, 99.12, 99.37, 99.62, 99.49, 99.24, 99.49, 99.75, 99.75, 99.49, 99.75, 99.62, 99.62]
z7 = [26336.1, 26333.4, 24104.5, 23564.8, 23737.1, 25608.9, 25630.4, 26437.3, 27025.8, 27308.9, 27097.2, 27252.6, 27303.2, 27495.6, 28547.2, 28721.9]

x8_steps = list(range(0, 27, 3)) # 0.25x
y8 = [46.72, 47.60, 49.37, 50.00, 53.91, 53.66, 55.18, 55.30, 55.68]
y8_1 = [38.01, 39.02, 37.37, 37.63, 38.13, 36.62, 36.11, 33.96, 33.71]

x9_steps = list(range(0, 39, 3)) # 0.125x
y9 = [40.40, 41.54, 39.65, 46.46, 48.48, 48.11, 50.25, 51.39, 53.66, 53.16, 53.66, 52.65, 55.68]
y9_1 = [29.80, 31.06, 32.58, 31.19, 33.84, 30.43, 31.82, 31.19, 30.81]

x10_steps = list(range(0, 55, 5)) # 0.05x
y_10 = [27.02, 28.91, 37.37, 44.19, 46.97, 47.10, 49.62, 48.86, 50.76, 49.87, 48.99]
y_10_1 = [39.52, 43.31, 44.32, 42.42, 39.90, 40.91, 43.43, 42.68, 43.56, 45.33, 45.58]

x11_steps = list(range(0, 140, 10)) # 0.025x
y11 = [27.15, 39.27, 44.32, 45.71, 45.45, 47.35, 48.61, 48.36, 48.74, 48.86, 51.01, 48.11, 50.63]
y11_1 = [42.42, 43.18, 44.19, 42.80, 43.56, 46.72, 42.42, 46.34, 47.85, 47.73, 47.60, 49.12, 47.73, 45.96]

# ========================= w/ generation time =========================
# Rescale x-values to new time ranges
x1 = rescale(x1_steps, 0, x1_steps[-1] / 1000 * 4)
x1_1 = x1
x2 = rescale(x2_steps, 0, x2_steps[-1] / 16 * 4)
x2_1 = x2
x3 = rescale(x3_steps, 0.8, 0.8 + x3_steps[-1] / 3 * 4)
x3_1 = x3
x4 = rescale(x4_steps, 1.6, 1.6 + x4_steps[-1] / 3 * 4)
x4_1 = x4
x5 = rescale(x5_steps, 3.2, 3.2 + x5_steps[-1] / 3 * 4)
x5_1 = x5
x6 = rescale(x6_steps, 6.4, 6.4 + x6_steps[-1] / 3 * 4)
x6_1 = x6
x7 = rescale(x7_steps, 12.8, 12.8 + x7_steps[-1] / 3 * 4)
x7_1 = x7
x_max = max(x1.max(), x2.max(), x3.max(), x4.max(), x5.max(), x6.max(), x7.max())


# Plot high + recommended with generation time
plt.figure(figsize=(14, 8))

def plot_pair(x, y, x1, y1, label1, color, label2=None):
    plt.plot(x, y, label=label1, linewidth=3, color=color)
    plt.plot(x1, y1, label=label2,linestyle='--', linewidth=2.5, color=color)

plot_pair(x1, y1, x1_1, y1_1, "SFT (high)", 'blue', label2="SFT (recommended)")
plot_pair(x2, y2, x2_1, y2_1, "GRPO (128x32, lr: 1e-6, high)", 'green')
plot_pair(x3, y3, x3_1, y3_1, "200 step SFT + GRPO (128x32, lr: 1e-6, high)", 'pink')
plot_pair(x4, y4, x4_1, y4_1, "400 step SFT + GRPO (128x32, lr: 1e-6, high)", 'red')
plot_pair(x5, y5, x5_1, y5_1, "800 step SFT + GRPO (128x32, lr: 1e-6, high)", 'orange')
plot_pair(x6, y6, x6_1, y6_1, "1600 step SFT + GRPO (128x32, lr: 1e-6, high)", 'cyan')
plot_pair(x7, y7, x7_1, y7_1, "3200 step SFT + GRPO (128x32, lr: 1e-6, high)", 'purple')

# Horizontal baselines
for y_val, label in [
    (64.77, "Qwen 3 14B (Reproduced)"),
    (42.93, "Qwen 3 14B Base (Reproduced)"),
    (64.0, "Qwen 3 14B (Official)"),
    (39.9, "Qwen 3 14B Base (Official)")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/ RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA pass@1", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(25, 65)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high+recommended.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high+recommended.png")


# Plot high with generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, y1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, y2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, y3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, y4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, y5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, y6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, y7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Horizontal baselines
for y_val, label in [
    (64.77, "Qwen 3 14B (Reproduced)"),
    (42.93, "Qwen 3 14B Base (Reproduced)"),
    (64.0, "Qwen 3 14B (Official)"),
    (39.9, "Qwen 3 14B Base (Official)")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/ RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA pass@1", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(25, 65)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high.png")


# Plot think tag ratio (high) with generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, w1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, w2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, w3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, w4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, w5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, w6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, w7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Axes and labels
plt.xlabel("training time (w/ RL generation) (hrs)", fontsize=20)
plt.ylabel("<think> tags (%)", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(0, 100)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high_think_tag.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high_think_tag.png")


# Plot length (high) with generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, z1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, z2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, z3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, z4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, z5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, z6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, z7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Horizontal baselines
for y_val, label in [
    (16384, "SFT & GRPO training cutoff"),
    (32768, "GPQA inference cutoff")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/ RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA generation length (#tokens)", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(0, 32768)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high_length.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high_length.png")


# ========================= w/o generation time =========================
# Rescale x-values to new time ranges
x1 = rescale(x1_steps, 0, x1_steps[-1] / 1000 * 4)
x1_1 = x1
x2 = rescale(x2_steps, 0, x2_steps[-1] / 61.9 * 4)
x2_1 = x2
x3 = rescale(x3_steps, 0.8, 0.8 + x3_steps[-1] / 9.1 * 4)   
x3_1 = x3
x4 = rescale(x4_steps, 1.6, 1.6 + x4_steps[-1] / 9.0 * 4)
x4_1 = x4
x5 = rescale(x5_steps, 3.2, 3.2 + x5_steps[-1] / 7.2 * 4)
x5_1 = x5
x6 = rescale(x6_steps, 6.4, 6.4 + x6_steps[-1] / 4.6 * 4)
x6_1 = x6
x7 = rescale(x7_steps, 12.8, 12.8 + x7_steps[-1] / 5.0 * 4)
x7_1 = x7
x_max = max(x1.max(), x2.max(), x3.max(), x4.max(), x5.max(), x6.max(), x7.max())


# Plot high + recommended without generation time
plt.figure(figsize=(14, 8))

plot_pair(x1, y1, x1_1, y1_1, "SFT (high)", 'blue', label2="SFT (recommended)")
plot_pair(x2, y2, x2_1, y2_1, "GRPO (128x32, lr: 1e-6, high)", 'green')
plot_pair(x3, y3, x3_1, y3_1, "200 step SFT + GRPO (128x32, lr: 1e-6, high)", 'pink')
plot_pair(x4, y4, x4_1, y4_1, "400 step SFT + GRPO (128x32, lr: 1e-6, high)", 'red')
plot_pair(x5, y5, x5_1, y5_1, "800 step SFT + GRPO (128x32, lr: 1e-6, high)", 'orange')
plot_pair(x6, y6, x6_1, y6_1, "1600 step SFT + GRPO (128x32, lr: 1e-6, high)", 'cyan')
plot_pair(x7, y7, x7_1, y7_1, "3200 step SFT + GRPO (128x32, lr: 1e-6, high)", 'purple')

# Horizontal baselines
for y_val, label in [
    (64.77, "Qwen 3 14B (Reproduced)"),
    (42.93, "Qwen 3 14B Base (Reproduced)"),
    (64.0, "Qwen 3 14B (Official)"),
    (39.9, "Qwen 3 14B Base (Official)")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/o RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA pass@1", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(25, 65)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high+recommended_wo_generation.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high+recommended_wo_generation.png")


# Plot high without generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, y1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, y2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, y3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, y4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, y5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, y6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, y7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Horizontal baselines
for y_val, label in [
    (64.77, "Qwen 3 14B (Reproduced)"),
    (42.93, "Qwen 3 14B Base (Reproduced)"),
    (64.0, "Qwen 3 14B (Official)"),
    (39.9, "Qwen 3 14B Base (Official)")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/o RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA pass@1", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(25, 65)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high_wo_generation.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high_wo_generation.png")


# Plot think tag ratio (high) without generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, w1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, w2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, w3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, w4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, w5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, w6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, w7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Axes and labels
plt.xlabel("training time (w/o RL generation) (hrs)", fontsize=20)
plt.ylabel("<think> tags (%)", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(0, 100)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high_think_tag_wo_generation.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high_think_tag_wo_generation.png")


# Plot length (high) without generation time
plt.figure(figsize=(14, 8))

plt.plot(x1, z1, label="SFT (high)", linewidth=3, color='blue')
plt.plot(x2, z2, label="GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='green')
plt.plot(x3, z3, label="200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='pink')
plt.plot(x4, z4, label="400 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='red')
plt.plot(x5, z5, label="800 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='orange')
plt.plot(x6, z6, label="1600 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='cyan')
plt.plot(x7, z7, label="3200 step SFT + GRPO (128x32, lr: 1e-6, high)", linewidth=3, color='purple')

# Horizontal baselines
for y_val, label in [
    (16384, "SFT & GRPO training cutoff"),
    (32768, "GPQA inference cutoff")
]:
    plt.axhline(y=y_val, color='gray', linestyle='--', linewidth=1.5)
    plt.text(x_max + 0.5, y_val, label, va='center', ha='left', fontsize=14, color='gray')

# Axes and labels
plt.xlabel("training time (w/o RL generation) (hrs)", fontsize=20)
plt.ylabel("GPQA generation length (#tokens)", fontsize=20)
plt.title("Qwen 3 14B Base\npost-trained on SCP_v2", fontsize=24)
plt.xlim(0, x_max)
plt.ylim(0, 32768)
plt.legend(loc='lower right', fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("plots/grpo_vs_sft_qwen3_14b_high_length_wo_generation.png")
print("Saving plots to plots/grpo_vs_sft_qwen3_14b_high_length_wo_generation.png")