"""
Tái hiện 2 đồ thị ở Mục 2 (Fig. 1 và Fig. 2) trong bài báo:
"Bioeconomic analysis of harvesting within a predator-prey system: A case study in the Chesapeake Bay fisheries"
(Panayotova et al., Ecological Modelling 480 (2023) 110330)

Yêu cầu:
- Fig. 1: Đường cong khớp mô hình Lotka-Volterra với dữ liệu thực tế giai đoạn 1995 - 2017.
- Fig. 2: Dự báo mô hình động thái quần thể của hai loài đến năm 2100.
"""

import sys
import os

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 1. DỮ LIỆU THỰC TẾ & THAM SỐ MÔ HÌNH
# ==========================================

# Chuỗi thời gian quan sát từ 1995 đến 2017 (23 năm)
years_obs = [
    1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017
]

# Dữ liệu độ phong phú thực tế (đơn vị: tỷ con - Billions) trích xuất chính xác từ bài báo
# Con mồi: Cá mòi dầu Đại Tây Dương (Atlantic Menhaden)
menhaden_obs = [
    0.1221, 0.1021, 0.0964, 0.1518, 0.1287, 0.0933, 0.1160, 0.1273,
    0.1138, 0.1081, 0.1542, 0.1594, 0.1120, 0.1420, 0.1368, 0.2338,
    0.1463, 0.1117, 0.1268, 0.1313, 0.2083, 0.2243, 0.0997
]

# Kẻ săn mồi: Cá vược sọc (Striped Bass)
bass_obs = [
    0.3411, 0.3844, 0.4298, 0.3337, 0.3120, 0.2716, 0.3260, 0.3774,
    0.2850, 0.4633, 0.3492, 0.3046, 0.2252, 0.2489, 0.1893, 0.1903,
    0.2106, 0.3045, 0.1912, 0.1697, 0.2341, 0.3402, 0.2385
]

# Bộ tham số tối ưu thu được từ quá trình khớp mô hình (Table 1 trong bài báo)
r = 0.513   # Tốc độ tăng trưởng nội tại của cá mòi dầu
a = 0.026   # Hệ số tự giới hạn của cá mòi dầu
b = 1.765   # Tác động săn bắt của cá vược sọc lên cá mòi dầu
e = 1.213   # Tỷ lệ tử vong tự nhiên của cá vược sọc
c = 0.520   # Hệ số tự giới hạn của cá vược sọc
d = 9.999   # Hiệu quả chuyển đổi sinh khối con mồi của cá vược sọc

# Giá trị ban đầu tại năm 1995 (t = 0) thu được sau khi khớp đường cong
x0 = 0.1645  # Menhaden ban đầu
y0 = 0.3108  # Striped Bass ban đầu

# ==========================================
# 2. GIẢI HỆ PHƯƠNG TRÌNH VI PHÂN (ODE)
# ==========================================

def derivatives(x, y):
    """
    Hệ Lotka-Volterra tổng quát:
    dx/dt = x * (r - a*x - b*y)
    dy/dt = y * (-e - c*y + d*x)
    """
    dxdt = x * (r - a * x - b * y)
    dydt = y * (-e - c * y + d * x)
    return dxdt, dydt

def solve_lotka_volterra(t_start, t_end, dt=0.01):
    """
    Giải hệ vi phân bằng phương pháp Runge-Kutta bậc 4 (RK4).
    Thuật toán thuần Python, không phụ thuộc thư viện ngoài.
    """
    t_values = []
    x_values = []
    y_values = []
    
    t = t_start
    x = x0
    y = y0
    
    num_steps = int(round((t_end - t_start) / dt))
    for _ in range(num_steps + 1):
        t_values.append(t)
        x_values.append(x)
        y_values.append(y)
        
        # RK4
        k1x, k1y = derivatives(x, y)
        k2x, k2y = derivatives(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = derivatives(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
        k4x, k4y = derivatives(x + dt * k3x, y + dt * k3y)
        
        x += (dt / 6.0) * (k1x + 2 * k2x + 2 * k3x + k4x)
        y += (dt / 6.0) * (k1y + 2 * k2y + 2 * k3y + k4y)
        t += dt
        
    return t_values, x_values, y_values

# Giải cho giai đoạn 1995 - 2017 (Fig. 1)
t_fig1, x_fig1, y_fig1 = solve_lotka_volterra(1995.0, 2017.0, dt=0.02)

# Giải cho giai đoạn 1995 - 2100 (Fig. 2)
t_fig2, x_fig2, y_fig2 = solve_lotka_volterra(1995.0, 2100.0, dt=0.05)


# ==========================================
# 3. VẼ ĐỒ THỊ BẰNG MATPLOTLIB
# ==========================================

def plot_with_matplotlib():
    import matplotlib.pyplot as plt

    # Thiết lập style giống đồ thị MATLAB trong bài báo gốc của Elsevier
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 10
    plt.rcParams['mathtext.fontset'] = 'stix'

    # ------------------------------------------
    # VẼ HÌNH 1: Giai đoạn 1995 - 2017
    # ------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(6.2, 4.6), dpi=300)

    # 1. Dữ liệu quan sát thực tế (vòng tròn rỗng)
    ax1.plot(years_obs, menhaden_obs, 'o', color='red', markerfacecolor='none',
             markeredgewidth=1.2, markersize=5.5, label='Menhaden')
    ax1.plot(years_obs, bass_obs, 'o', color='blue', markerfacecolor='none',
             markeredgewidth=1.2, markersize=5.5, label='Striped Bass')

    # 2. Đường cong khớp mô hình lý thuyết
    ax1.plot(t_fig1, x_fig1, '-', color='red', linewidth=1.6)
    ax1.plot(t_fig1, y_fig1, '-', color='blue', linewidth=1.6)

    # Định dạng trục
    ax1.set_xlim(1994, 2018)
    ax1.set_ylim(0, 0.5)
    ax1.set_xticks(range(1995, 2018, 2))
    ax1.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax1.set_xlabel('Time (Years)', fontsize=11)
    ax1.set_ylabel('Abundance (Billions)', fontsize=11)

    # MATLAB style: vạch chia hướng vào trong (inward ticks), có tick ở cả 4 cạnh
    ax1.tick_params(direction='in', top=True, right=True, length=4, width=0.8)

    # Chú thích góc trên bên phải
    ax1.legend(loc='upper right', frameon=True, edgecolor='black', fancybox=False,
               framealpha=1.0, borderpad=0.5, handletextpad=0.4)

    plt.tight_layout()
    output_fig1 = 'fig1_fitted_curves.png'
    fig1.savefig(output_fig1, dpi=300)
    print(f"Đã lưu Hình 1 vào file: {output_fig1}")

    # ------------------------------------------
    # VẼ HÌNH 2: Dự báo đến năm 2100
    # ------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(6.2, 4.6), dpi=300)

    # 1. Dữ liệu quan sát thực tế 1995-2017
    ax2.plot(years_obs, menhaden_obs, 'o', color='red', markerfacecolor='none',
             markeredgewidth=1.2, markersize=5.5, label='Menhaden')
    ax2.plot(years_obs, bass_obs, 'o', color='blue', markerfacecolor='none',
             markeredgewidth=1.2, markersize=5.5, label='Striped Bass')

    # 2. Đường cong dự báo đến 2100
    ax2.plot(t_fig2, x_fig2, '-', color='red', linewidth=1.6)
    ax2.plot(t_fig2, y_fig2, '-', color='blue', linewidth=1.6)

    # Định dạng trục
    ax2.set_xlim(1994, 2101)
    ax2.set_ylim(0, 0.5)
    ax2.set_xticks([1995, 2010, 2025, 2040, 2055, 2070, 2085, 2100])
    ax2.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax2.set_xlabel('Time (Years)', fontsize=11)
    ax2.set_ylabel('Abundance (Billions)', fontsize=11)

    # Vạch chia hướng vào trong (inward ticks)
    ax2.tick_params(direction='in', top=True, right=True, length=4, width=0.8)

    # Chú thích
    ax2.legend(loc='upper right', frameon=True, edgecolor='black', fancybox=False,
               framealpha=1.0, borderpad=0.5, handletextpad=0.4)

    plt.tight_layout()
    output_fig2 = 'fig2_model_prediction.png'
    fig2.savefig(output_fig2, dpi=300)
    print(f"Đã lưu Hình 2 vào file: {output_fig2}")


# ==========================================
# 4. HÀM XUẤT SVG THUẦN (STANDALONE SVG)
# ==========================================

def export_svg(filename, t_curve, x_curve, y_curve, x_range, x_ticks, title=""):
    """
    Tạo file SVG chuẩn vector chất lượng cao không cần thư viện đồ họa phụ trợ.
    """
    width = 600
    height = 450
    margin_left = 75
    margin_right = 35
    margin_top = 40
    margin_bottom = 60

    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    xmin, xmax = x_range
    ymin, ymax = 0.0, 0.5

    def to_pixel(x, y):
        px = margin_left + (x - xmin) / (xmax - xmin) * plot_w
        py = margin_top + plot_h - (y - ymin) / (ymax - ymin) * plot_h
        return px, py

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" style="background-color: white; font-family: Helvetica, Arial, sans-serif;">')

    # Khung chữ nhật bao quanh (MATLAB box)
    svg.append(f'  <rect x="{margin_left}" y="{margin_top}" width="{plot_w}" height="{plot_h}" fill="white" stroke="black" stroke-width="1.2"/>')

    # Vạch chia trục Y (0, 0.1, 0.2, 0.3, 0.4, 0.5)
    for y_val in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
        _, py = to_pixel(xmin, y_val)
        # Inward ticks (cả 2 bên)
        svg.append(f'  <line x1="{margin_left}" y1="{py:.2f}" x2="{margin_left + 6}" y2="{py:.2f}" stroke="black" stroke-width="1"/>')
        svg.append(f'  <line x1="{margin_left + plot_w - 6}" y1="{py:.2f}" x2="{margin_left + plot_w}" y2="{py:.2f}" stroke="black" stroke-width="1"/>')
        svg.append(f'  <text x="{margin_left - 10}" y="{py + 4:.2f}" font-size="12" text-anchor="end" fill="black">{y_val:.1f}</text>')

    # Vạch chia trục X
    for xt in x_ticks:
        px, _ = to_pixel(xt, ymin)
        # Inward ticks (cả trên và dưới)
        svg.append(f'  <line x1="{px:.2f}" y1="{margin_top + plot_h - 6}" x2="{px:.2f}" y2="{margin_top + plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'  <line x1="{px:.2f}" y1="{margin_top}" x2="{px:.2f}" y2="{margin_top + 6}" stroke="black" stroke-width="1"/>')
        svg.append(f'  <text x="{px:.2f}" y="{margin_top + plot_h + 20}" font-size="12" text-anchor="middle" fill="black">{xt}</text>')

    # Nhãn trục
    svg.append(f'  <text x="{margin_left + plot_w / 2:.2f}" y="{margin_top + plot_h + 46}" font-size="14" text-anchor="middle" fill="black">Time (Years)</text>')
    svg.append(f'  <text x="{22}" y="{margin_top + plot_h / 2:.2f}" font-size="14" text-anchor="middle" fill="black" transform="rotate(-90 22 {margin_top + plot_h / 2:.2f})">Abundance (Billions)</text>')

    # Vẽ đường cong Menhaden (đỏ)
    d_red = " ".join([f"{'M' if i == 0 else 'L'} {to_pixel(t, x)[0]:.2f} {to_pixel(t, x)[1]:.2f}" for i, (t, x) in enumerate(zip(t_curve, x_curve))])
    svg.append(f'  <path d="{d_red}" fill="none" stroke="red" stroke-width="1.8"/>')

    # Vẽ đường cong Striped Bass (xanh)
    d_blue = " ".join([f"{'M' if i == 0 else 'L'} {to_pixel(t, y)[0]:.2f} {to_pixel(t, y)[1]:.2f}" for i, (t, y) in enumerate(zip(t_curve, y_curve))])
    svg.append(f'  <path d="{d_blue}" fill="none" stroke="blue" stroke-width="1.8"/>')

    # Vẽ điểm dữ liệu Menhaden (vòng tròn rỗng đỏ)
    for yr, obs in zip(years_obs, menhaden_obs):
        px, py = to_pixel(yr, obs)
        svg.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.2" fill="none" stroke="red" stroke-width="1.4"/>')

    # Vẽ điểm dữ liệu Striped Bass (vòng tròn rỗng xanh)
    for yr, obs in zip(years_obs, bass_obs):
        px, py = to_pixel(yr, obs)
        svg.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.2" fill="none" stroke="blue" stroke-width="1.4"/>')

    # Legend box ở góc trên bên phải
    leg_x = margin_left + plot_w - 125
    leg_y = margin_top + 15
    svg.append(f'  <rect x="{leg_x}" y="{leg_y}" width="115" height="52" fill="white" stroke="black" stroke-width="0.8"/>')
    # Mục 1: Menhaden
    svg.append(f'  <circle cx="{leg_x + 18}" cy="{leg_y + 18}" r="3.2" fill="none" stroke="red" stroke-width="1.4"/>')
    svg.append(f'  <text x="{leg_x + 32}" y="{leg_y + 22}" font-size="12" fill="black">Menhaden</text>')
    # Mục 2: Striped Bass
    svg.append(f'  <circle cx="{leg_x + 18}" cy="{leg_y + 38}" r="3.2" fill="none" stroke="blue" stroke-width="1.4"/>')
    svg.append(f'  <text x="{leg_x + 32}" y="{leg_y + 42}" font-size="12" fill="black">Striped Bass</text>')

    svg.append('</svg>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg))
    print(f"Đã xuất đồ thị vector SVG: {filename}")


# ==========================================
# 5. CHẠY CHƯƠNG TRÌNH CHÍNH
# ==========================================

if __name__ == '__main__':
    # Luôn xuất 2 file SVG vector (chạy được trên mọi hệ điều hành không cần cài thêm thư viện)
    export_svg("fig1_fitted_curves.svg", t_fig1, x_fig1, y_fig1, 
               (1994, 2018), list(range(1995, 2018, 2)), "Fig 1: Fitted Curves (1995-2017)")
    export_svg("fig2_model_prediction.svg", t_fig2, x_fig2, y_fig2, 
               (1994, 2101), [1995, 2010, 2025, 2040, 2055, 2070, 2085, 2100], "Fig 2: Model Prediction to 2100")

    # Thử xuất bằng Matplotlib nếu máy đã cài đặt
    try:
        plot_with_matplotlib()
    except Exception as e:
        print(f"\n[Lưu ý] Không thể xuất PNG qua Matplotlib ({e}).")
        print("Đã tạo sẵn 2 file SVG chuẩn vector chất lượng cao (fig1_fitted_curves.svg và fig2_model_prediction.svg) hoàn toàn không cần thư viện ngoài.")
