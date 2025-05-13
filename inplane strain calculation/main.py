import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
def compute_ratio(Y, t, R):

    Y = np.array(Y, dtype=float)
    t = np.array(t, dtype=float)
    if Y.shape != t.shape:
        raise ValueError("Y 和 t 必须等长")

    prefix = np.concatenate(([0.], np.cumsum(t)[:-1]))
    mid = prefix + t/2.0
    numerator   = np.sum(Y * t * mid)
    denominator = R * np.sum(Y * t)
    return numerator / denominator

if __name__ == "__main__":
    #BTO: 67 GPa
    #STO: 150 GPa
    #CIPS: 25 GPa
    #Al2O3: 300 GPa
    #PDMS: 1200 kPa
    #PET: 3GPa
    #MoS2: 265 GPa
    Y = [265,1.2e-3,3]#Unit: GPa
    t = [1e-9, 100e-6, 1e-3]#Unit: m

    R_list = np.linspace(0.001, 0.03, 200).tolist()

    # 计算所有 R 对应的 ratio
    ratios = [compute_ratio(Y, t, R) for R in R_list]

    R_list_mm = [R * 1000 for R in R_list]  # 转成 mm
    plt.figure(figsize=(6,4))
    plt.plot(R_list_mm, ratios, '-', color='C0', lw=2)
    plt.xlabel('R (mm)', fontsize=12)
    plt.ylabel('strain', fontsize=12)
    plt.title('strain vs. R', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))


    # plt.xscale('log')
    # plt.gca().set_xticks(R_list)
    # plt.gca().get_xaxis().set_major_formatter(plt.FormatStrFormatter('%.1f'))

    plt.tight_layout()
    plt.show()
