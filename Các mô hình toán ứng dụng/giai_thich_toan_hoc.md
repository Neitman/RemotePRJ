# TỔNG HỢP CÁC NỘI DUNG GIẢI THÍCH TOÁN HỌC CHUYÊN SÂU
## ĐỀ TÀI: MÔ HÌNH LOTKA–VOLTERRA MỞ RỘNG (MENHADEN & STRIPED BASS)
**Dự án:** Tiểu luận môn học *Các mô hình toán ứng dụng*  
**Nhóm sinh viên thực hiện (K68A2):** Tạ Tiến Nam – Tạ Văn Nghĩa – Trần Đức Kiên  
**Giảng viên hướng dẫn:** TS. Nguyễn Trọng Hiếu  
**Tài liệu tham khảo chính:** I. N. Panayotova et al., *Ecological Modelling* 480 (2023) 110330

---

> **Mục đích của tài liệu này:**  
> File này đóng vai trò là **tài liệu kỹ thuật đồng hành (companion technical document)** cùng với [kich_ban_thuyet_trinh.md](file:///D:/HUS-PRJ/RemotePRJ/C%C3%A1c%20m%C3%B4%20h%C3%ACnh%20to%C3%A1n%20%E1%BB%A9ng%20d%E1%BB%A5ng/kich_ban_thuyet_trinh.md) và các slide báo cáo [slide.tex](file:///D:/HUS-PRJ/RemotePRJ/C%C3%A1c%20m%C3%B4%20h%C3%ACnh%20to%C3%A1n%20%E1%BB%A9ng%20d%E1%BB%A5ng/slide/slide.tex). Toàn bộ các phép biến đổi, chứng minh, tính toán ma trận và lý giải giải tích chi tiết được tổng hợp tại đây nhằm phục vụ việc đào sâu nghiên cứu và trả lời các câu hỏi phản biện của Hội đồng.

---

## MỤC LỤC
1. [Hệ phương trình vi phân Lotka–Volterra mở rộng & Cơ chế tự giới hạn](#1-hệ-phương-trình-vi-phân-lotka-volterra-mở-rộng--cơ-chế-tự-giới-hạn)
2. [Hàm mất mát và Phương pháp hồi quy phi tuyến (NLS)](#2-hàm-mất-mát-và-phương-pháp-hồi-quy-phi-tuyến-nls)
3. [Tính không âm và Tính bị chặn của nghiệm (Tập bất biến sinh học $\Omega$)](#3-tính-không-âm-và-tính-bị-chặn-của-nghiệm-tập-bất-biến-sinh-học-omega)
4. [Tính toán Điểm cân bằng dừng tự nhiên $Q(x^*, y^*)$](#4-tính-toán-điểm-cân-bằng-dừng-tự-nhiên-qx-y)
5. [Tuyến tính hóa Jacobian & Khảo sát Tính ổn định tiệm cận](#5-tuyến-tính-hóa-jacobian--khảo-sát-tính-ổn-định-tiệm-cận)
6. [Độ đàn hồi sinh học (Resilience) & Thời gian hồi phục 13 năm](#6-độ-đàn-hồi-sinh-học-resilience--thời-gian-hồi-phục-13-năm)
7. [Mô hình kinh tế sinh thái (Bionomic) & 4 trường hợp cân bằng](#7-mô-hình-kinh-tế-sinh-thái-bionomic--4-trường-hợp-cân-bằng)
8. [Cơ sở toán học của 3 chính sách khai thác (MSY, MEY, RMY)](#8-cơ-sở-toán-học-của-3-chính-sách-khai-thác-msy-mey-rmy)
9. [Phương pháp phân tích độ nhạy vi phân trực tiếp (DDM)](#9-phương-pháp-phân-tích-độ-nhạy-vi-phân-trực-tiếp-ddm)

---

## 1. HỆ PHƯƠNG TRÌNH VI PHÂN LOTKA–VOLTERRA MỞ RỘNG & CƠ CHẾ TỰ GIỚI HẠN

### 1.1. Dạng phương trình vi phân
Hệ gồm hai phương trình vi phân thường phi tuyến bậc nhất mô tả tốc độ biến thiên sinh khối con mồi $x(t)$ (Cá mòi dầu) và kẻ săn mồi $y(t)$ (Cá vược sọc):

$$\left\{
\begin{aligned}
\frac{dx}{dt} &= x(r - ax - by) \\
\frac{dy}{dt} &= y(-e - cy + dx)
\end{aligned}
\right. \quad (1)$$

* Trong đó: $x(t) \ge 0, y(t) \ge 0$ tính theo đơn vị **tỷ cá thể** ($10^9$ con).
* Mọi tham số $r, a, b, e, c, d$ đều là các hằng số thực dương.

### 1.2. So sánh với mô hình Lotka–Volterra cổ điển (1925)
* **Hệ cổ điển:** $\dot{x} = x(r - by), \;\dot{y} = y(-e + dx)$.
  * Tồn tại hàm thế bảo toàn (tích phân thứ nhất):
    $$V(x, y) = d x - e \ln x + b y - r \ln y = \text{const}$$
  * Điểm cân bằng là một **tâm (center)** với hai giá trị riêng thuần ảo $\lambda = \pm i \sqrt{rd}$. Quỹ đạo pha là các đường cong đóng kín tuần hoàn mãi mãi quanh tâm, biên độ phụ thuộc điều kiện ban đầu.
  * **Hạn chế sinh học:** Không phản ánh được sức chứa hữu hạn của môi trường, không có khả năng tiêu tán nhiễu loạn để tự ổn định.
* **Hệ mở rộng (Panayotova et al., 2023):** Bổ sung hai số hạng bậc hai $-ax^2$ và $-cy^2$.
  * $-ax^2$: Tự cạnh tranh nội bộ loài cá mòi dầu (cạnh tranh tảo phù du, không gian bơi). Sức chứa riêng: $K_x = r/a$.
  * $-cy^2$: Tự cạnh tranh nội bộ loài cá vược sọc (cạnh tranh bãi đẻ nước ngọt và vùng lãnh thổ).
  * Hai số hạng này đưa cơ chế **tiêu tán năng lượng (dissipative mechanism)** vào hệ, phá vỡ tính bảo toàn của $V(x, y)$, biến tâm thành **tiêu điểm ổn định (stable focus)**.

---

## 2. HÀM MẤT MÁT VÀ PHƯƠNG PHÁP HỒI QUY PHI TUYẾN (NLS)

### 2.1. Công thức hàm mất mát
Bài toán tìm véctơ tham số tối ưu $\theta = (r, a, b, e, c, d)^T$ được phát biểu dưới dạng bài toán quy hoạch phi tuyến:

$$\min_{\theta \in \Theta} L(\theta) = \sum_{k=1}^{N} \left[ \left(x(t_k; \theta) - x_k^{\text{obs}}\right)^2 + \left(y(t_k; \theta) - y_k^{\text{obs}}\right)^2 \right]$$

* $N = 23$: Số mốc thời gian quan sát thực nghiệm từ năm 1995 đến 2017 ($t_k \in \{1995, 1996, \dots, 2017\}$).
* $x_k^{\text{obs}}, y_k^{\text{obs}}$: Dữ liệu thực tế quan sát được của hai loài cá (đã cộng thêm nỗ lực khai thác đánh bắt thương mại và giải trí).
* $x(t_k; \theta), y(t_k; \theta)$: Giá trị số nghiệm của hệ vi phân (1) tại thời điểm $t_k$ khi tích phân từ điều kiện ban đầu $(x_0, y_0)$ với bộ tham số $\theta$.
* Không gian tìm kiếm: $\Theta = (0, 10]^6$.

### 2.2. Lý giải chuyên sâu về mặt tối ưu hóa
1. **Khớp nối đồng thời (Joint Fitting):**  
   Hàm mất mát cộng gộp bình phương sai số của cả con mồi và kẻ săn mồi. Vì hai phương trình ràng buộc chặt chẽ qua các số hạng ghép $-bxy$ và $+dxy$, việc tối ưu hóa phải tiến hành đồng thời trên không gian 6 chiều.
2. **Tại sao sử dụng bình phương sai số $L_2$:**  
   * Triệt tiêu dấu của sai số, tránh hiện tượng lệch dương ở năm này bù trừ cho lệch âm ở năm khác.
   * Tính khả vi cấp hai liên tục ($\mathcal{C}^2$), cho phép áp dụng hiệu quả các thuật toán tối ưu bậc cao như **Levenberg–Marquardt** hoặc **Trust-Region Reflective**.
3. **Tại sao phải áp đặt chặn trên $\theta_i \le 10$:**  
   * Hệ (1) là phi tuyến cao. Với 46 điểm quan sát (23 năm $\times$ 2 loài) để xác định 6 tham số, đây là **hệ toán học quá xác định (over-determined system)**.
   * Trên bề mặt hàm mất mát $L(\theta)$ tồn tại vô số cực tiểu cục bộ (*local minima*). Nếu không có chặn trên, các thuật toán tối ưu gradient dễ rơi vào những hố cục bộ cho ra tham số có giá trị khổng lồ nhưng vô nghĩa về mặt sinh thái.
   * Chặn trên $\theta_i \le 10$ đóng vai trò như một **kỹ thuật điều chuẩn biên (Box-constraint Regularization)**. Ràng buộc này giữ thuật toán trong phạm vi sinh học thực tế, giúp ước lượng được $r = 0.513\text{ năm}^{-1}$ – con số trùng khớp với ước lượng thống kê độc lập của Drew et al. (2021).

### 2.3. Sai số chuẩn phần dư (Residual Standard Error - $S$)
Độ chính xác hồi quy được đo lường bằng:

$$S = \sqrt{\frac{1}{2N - p} \sum_{k=1}^N \left[ \left(x(t_k) - x_k^{\text{obs}}\right)^2 + \left(y(t_k) - y_k^{\text{obs}}\right)^2 \right]}$$

* Tổng số bậc tự do của dữ liệu: $2N = 46$.
* Số tham số ước lượng: $p = 6$.
* Bậc tự do còn lại của phần dư: $2N - p = 40$.
* Kết quả: $S = 0.11$ (tỷ con) $= 110\text{ triệu con}$. Điều này chứng minh khoảng cách trung bình từ các điểm quan sát đến đường cong mô hình chỉ khoảng 110 triệu con, một độ lệch rất nhỏ so với quy mô hàng tỷ con của vịnh.

---

## 3. TÍNH KHÔNG ÂM VÀ TÍNH BỊ CHẶN CỦA NGHIỆM (TẬP BẤT BIẾN SINH HỌC $\Omega$)

Để mô hình có ý nghĩa thực tế, các nghiệm bắt đầu từ miền dương phải luôn luôn dương và không được bùng nổ ra vô cùng (*no blow-up*).

### 3.1. Tính không âm (Positivity)
Viết lại phương trình thứ nhất dưới dạng:

$$\frac{dx}{x} = \phi_1(x, y) dt \quad \text{với } \phi_1(x, y) = r - ax - by$$

Tích phân hai vế từ $0$ đến $t$:

$$x(t) = x(0) \exp\left( \int_0^t \phi_1(x(s), y(s)) ds \right)$$

Vì hàm mũ luôn dương $\exp(\cdot) > 0$, nếu điều kiện ban đầu $x(0) > 0$ thì $x(t) > 0$ với mọi $t \ge 0$.  
Chứng minh hoàn toàn tương tự cho $y(t)$:

$$y(t) = y(0) \exp\left( \int_0^t (-e - cy(s) + dx(s)) ds \right) > 0, \quad \forall t \ge 0$$

Do đó, góc phần tư thứ nhất $\mathbb{R}^2_+ = \{(x, y) \mid x \ge 0, y \ge 0\}$ là một tập bất biến dương.

### 3.2. Tính bị chặn toàn cục (Boundedness)
1. **Chặn trên của $x(t)$:**  
   Do $y(t) \ge 0$ và $b > 0$, từ phương trình thứ nhất ta có bất đẳng thức vi phân:
   $$\frac{dx}{dt} = x(r - ax - by) \le x(r - ax)$$
   Giải phương trình vi phân Bernoulli/logistic so sánh $\dot{u} = u(r - au)$ bằng phương pháp tách biến, ta thu được:
   $$x(t) \le \frac{x(0) r}{a x(0) + (r - a x(0)) e^{-rt}}$$
   Khi $t \to \infty$, $e^{-rt} \to 0$, do đó:
   $$\limsup_{t \to \infty} x(t) \le \frac{r}{a}$$

2. **Chặn trên của $y(t)$ qua biến phụ $w(t)$:**  
   Đặt biến tổng hợp:
   $$w(t) = x(t) + \frac{y(t)}{\gamma} \quad \text{với } \gamma = \frac{d}{b} \iff d = \gamma b$$
   Đạo hàm theo thời gian:
   $$\frac{dw}{dt} = \frac{dx}{dt} + \frac{1}{\gamma} \frac{dy}{dt} = x(r - ax - by) + \frac{1}{\gamma} y(-e - cy + dx)$$
   Thay $dx = \gamma by$, các số hạng tương tác chéo triệt tiêu hoàn toàn:
   $$\frac{dw}{dt} = x(r - ax) - bxy - \frac{e}{\gamma}y - \frac{c}{\gamma}y^2 + bxy = x(r - ax) - \frac{e}{\gamma}y - \frac{c}{\gamma}y^2$$
   Vì $-\frac{c}{\gamma}y^2 \le 0$, ta có:
   $$\frac{dw}{dt} \le x(r - ax) - \frac{e}{\gamma}y$$
   Hàm bậc hai $f(x) = x(r - ax)$ đạt giá trị cực đại tại $x = \frac{r}{2a}$ với $f_{\max} = \frac{r^2}{4a}$.  
   Chọn hằng số $\delta = \min(e, r) > 0$, ta có:
   $$\frac{dw}{dt} \le \frac{r^2}{4a} - \delta\left(x + \frac{y}{\gamma}\right) = \frac{r^2}{4a} - \delta w$$
   Giải bất đẳng thức vi phân tuyến tính cấp một bằng thừa số tích phân $e^{\delta t}$:
   $$w(t) \le w(0) e^{-\delta t} + \frac{r^2}{4a\delta} (1 - e^{-\delta t})$$
   Lấy giới hạn khi $t \to \infty$:
   $$\limsup_{t \to \infty} w(t) \le L = \frac{r^2}{4a\delta}$$

### 3.3. Kết luận về tập bất biến sinh học $\Omega$
Hệ thống bị chặn toàn cục trong miền đa giác lồi:

$$\Omega = \left\{ (x, y) \in \mathbb{R}^2_+ \;\middle|\; 0 \le x \le \frac{r}{a}, \; 0 \le x + \frac{b}{d} y \le L \right\}$$

Mọi nghiệm xuất phát trong $\Omega$ sẽ tồn tại vĩnh viễn trong $\Omega$, đảm bảo quần thể không bao giờ bùng nổ vô hạn.

---

## 4. TÍNH TOÁN ĐIỂM CÂN BẰNG DỪNG TỰ NHIÊN $Q(x^*, y^*)$

### 4.1. Thiết lập hệ đại số tuyến tính
Tại trạng thái cân bằng đồng tồn tại tự nhiên $Q(x^*, y^*)$ với $x^* > 0, y^* > 0$, triệt tiêu các đạo hàm:

$$\left\{
\begin{aligned}
x^*(r - ax^* - by^*) &= 0 \\
y^*(-e - cy^* + dx^*) &= 0
\end{aligned}
\right.
\iff
\left\{
\begin{aligned}
ax^* + by^* &= r \\
dx^* - cy^* &= e
\end{aligned}
\right.$$

Viết dưới dạng ma trận:

$$\begin{pmatrix} a & b \\ d & -c \end{pmatrix} \begin{pmatrix} x^* \\ y^* \end{pmatrix} = \begin{pmatrix} r \\ e \end{pmatrix}$$

### 4.2. Giải hệ bằng định lý Cramer
Định thức chính của hệ:

$$D = \det \begin{pmatrix} a & b \\ d & -c \end{pmatrix} = -ac - bd = -(ac + bd) < 0$$

Định thức theo $x$:

$$D_x = \det \begin{pmatrix} r & b \\ e & -c \end{pmatrix} = -rc - be = -(rc + be)$$

Định thức theo $y$:

$$D_y = \det \begin{pmatrix} a & r \\ d & e \end{pmatrix} = ae - rd = -(rd - ae)$$

Theo quy tắc Cramer:

$$x^* = \frac{D_x}{D} = \frac{-(rc + be)}{-(ac + bd)} = \frac{rc + be}{ac + bd}$$

$$y^* = \frac{D_y}{D} = \frac{-(rd - ae)}{-(ac + bd)} = \frac{rd - ae}{ac + bd}$$

### 4.3. Điều kiện tồn tại sinh học
Để cả hai loài cùng tồn tại ($x^* > 0, y^* > 0$):
* $x^* > 0$ luôn thỏa mãn vì $r, c, b, e > 0$.
* $y^* > 0 \iff rd - ae > 0 \iff rd > ae \iff \frac{r}{a} > \frac{e}{d}$.
  * **Ý nghĩa:** Sức chứa môi trường của cá mòi $K_x = r/a$ phải lớn hơn ngưỡng sinh tồn tối thiểu của cá vược $e/d$.

### 4.4. Thay số thực nghiệm từ Bảng 1
Với $r = 0.513, a = 0.026, b = 1.765, e = 1.213, c = 0.520, d = 9.999$:
* $ac + bd = (0.026)(0.520) + (1.765)(9.999) = 0.01352 + 17.648235 = 17.661755$
* $rc + be = (0.513)(0.520) + (1.765)(1.213) = 0.26676 + 2.140945 = 2.407705$
* $rd - ae = (0.513)(9.999) - (0.026)(1.213) = 5.129487 - 0.031538 = 5.097949$

Do đó:

$$x^* = \frac{2.407705}{17.661755} \approx \mathbf{0.13632\text{ tỷ con}} \quad (136.3\text{ triệu con})$$

$$y^* = \frac{5.097949}{17.661755} \approx \mathbf{0.28864\text{ tỷ con}} \quad (288.6\text{ triệu con})$$

---

## 5. TUYẾN TÍNH HÓA JACOBIAN & KHẢO SÁT TÍNH ỔN ĐỊNH TIỆM CẬN

### 5.1. Ma trận Jacobi tổng quát
Hàm vế phải: $f_1(x, y) = rx - ax^2 - bxy$, $f_2(x, y) = -ey - cy^2 + dxy$.  
Ma trận Jacobi tại điểm bất kỳ $(x, y)$:

$$J(x, y) = \begin{pmatrix} \frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\ \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} \end{pmatrix} = \begin{pmatrix} r - 2ax - by & -bx \\ dy & -e - 2cy + dx \end{pmatrix}$$

### 5.2. Thu gọn tại điểm cân bằng $Q(x^*, y^*)$
Do tại $Q$, ta có $r - ax^* - by^* = 0$ và $-e - cy^* + dx^* = 0$, ma trận Jacobi rút gọn thành:

$$A = J(x^*, y^*) = \begin{pmatrix} (r - ax^* - by^*) - ax^* & -bx^* \\ dy^* & (-e - cy^* + dx^*) - cy^* \end{pmatrix} = \begin{pmatrix} -ax^* & -bx^* \\ dy^* & -cy^* \end{pmatrix}$$

### 5.3. Kiểm tra tính ổn định tiệm cận (Tiêu chuẩn Routh–Hurwitz)
Phương trình đặc trưng của ma trận $A$:

$$\det(\lambda I - A) = \lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$$

1. **Vết của ma trận $A$:**
   $$\text{tr}(A) = -ax^* - cy^* = -(ax^* + cy^*)$$
   Vì $a, c > 0$ và $x^*, y^* > 0$, ta có $\text{tr}(A) < 0$.
2. **Định thức của ma trận $A$:**
   $$\det(A) = (-ax^*)(-cy^*) - (-bx^*)(dy^*) = acx^*y^* + bdx^*y^* = (ac + bd)x^*y^*$$
   Vì $a, c, b, d > 0$ và $x^*, y^* > 0$, ta có $\det(A) > 0$.

Theo **Tiêu chuẩn Routh–Hurwitz** cho đa thức bậc 2:
* Điều kiện cần và đủ để mọi nghiệm của phương trình đặc trưng có phần thực âm là $\text{tr}(A) < 0$ và $\det(A) > 0$.
* Do cả hai điều kiện luôn thỏa mãn với mọi bộ tham số thực dương, **điểm cân bằng dừng $Q(x^*, y^*)$ luôn luôn ổn định tiệm cận cục bộ (locally asymptotically stable)**.

---

## 6. ĐỘ ĐÀN HỒI SINH HỌC (RESILIENCE) & THỜI GIAN HỒI PHỤC 13 NĂM

### 6.1. Định nghĩa toán sinh học theo Pimm & Lawton (1978)
Nghiệm của hệ tuyến tính hóa quanh điểm cân bằng có dạng:

$$\begin{pmatrix} x(t) - x^* \\ y(t) - y^* \end{pmatrix} = c_1 e^{\lambda_1 t} v_1 + c_2 e^{\lambda_2 t} v_2$$

* Nếu $\lambda_{1, 2} = \alpha \pm i\omega$ với $\alpha = \text{Re}(\lambda) < 0$:
  $$e^{\lambda t} = e^{\alpha t} (\cos \omega t + i \sin \omega t)$$
* Thành phần chi phối tốc độ suy giảm của bao hình dao động (*envelope decay*) là hàm mũ $e^{\alpha t}$.
* Thời gian để độ lệch suy giảm đi một thừa số $e^{-1} \approx 36.8\%$ được định nghĩa là **Thời gian hồi phục (Return Time to Equilibrium - $\tau$):**
  $$\tau = \frac{-1}{\text{Re}(\lambda_m)}$$
* **Độ đàn hồi sinh học (Resilience - $R$):**
  $$R = \frac{1}{\tau} = -\text{Re}(\lambda_m)$$

### 6.2. Tính toán chính xác giá trị riêng cho Vịnh Chesapeake
Thay giá trị từ Bảng 1 vào ma trận $A$:
* $A_{11} = -ax^* = -(0.026)(0.13632) \approx -0.003544$
* $A_{12} = -bx^* = -(1.765)(0.13632) \approx -0.240605$
* $A_{21} = dy^* = (9.999)(0.28864) \approx 2.886111$
* $A_{22} = -cy^* = -(0.520)(0.28864) \approx -0.150093$

Tính Vết và Định thức:
* $\text{tr}(A) = -0.003544 - 0.150093 = \mathbf{-0.153637}$
* $\det(A) = (-0.003544)(-0.150093) - (-0.240605)(2.886111) = 0.000532 + 0.694413 = \mathbf{0.694945}$

Phương trình đặc trưng:

$$\lambda^2 + 0.153637 \lambda + 0.694945 = 0$$

Biệt thức $\Delta$:

$$\Delta = (\text{tr}(A))^2 - 4\det(A) = (-0.153637)^2 - 4(0.694945) = 0.023604 - 2.779780 = \mathbf{-2.756176} < 0$$

Vì $\Delta < 0$, hệ có cặp giá trị riêng phức liên hợp:

$$\lambda_{1, 2} = \frac{\text{tr}(A) \pm i\sqrt{|\Delta|}}{2} = \frac{-0.153637 \pm i\sqrt{2.756176}}{2} \approx \mathbf{-0.07682 \pm 0.83009i}$$

Kết quả này trùng khớp chính xác tuyệt đối với công thức (2) trong bài báo gốc của Panayotova et al.:

$$\lambda_1 \approx -0.0768 + 0.8301i, \quad \lambda_2 \approx -0.0768 - 0.8301i$$

### 6.3. Giải mã ý nghĩa sinh thái của hai thành phần
1. **Phần ảo $\omega = 0.8301\text{ rad/năm}$:**  
   Quy định chu kỳ dao động lệch pha sinh học của quần thể:
   $$T = \frac{2\pi}{\omega} = \frac{2\pi}{0.8301} \approx \mathbf{7.57\text{ năm}}$$
   Cứ sau khoảng 7.5 năm, chu kỳ bùng nổ và suy thoái của hai loài lại hoàn thành một vòng lặp.
2. **Phần thực $\alpha = -0.0768\text{ năm}^{-1}$:**  
   Quy định tốc độ tắt dần của dao động:
   $$R = -\alpha \approx \mathbf{0.0768\text{ năm}^{-1}}$$
   Thời gian phục hồi:
   $$\tau = \frac{1}{R} = \frac{1}{0.07682} \approx \mathbf{13.02\text{ năm}}$$
   **Ý nghĩa:** Sau một biến cố môi trường lớn, hệ sinh thái vịnh cần khoảng **13 năm** để dập tắt các dao động hỗn loạn và quay trở lại trạng thái cân bằng dừng.

---

## 7. MÔ HÌNH KINH TẾ SINH THÁI (BIONOMIC) & 4 TRƯỜNG HỢP CÂN BẰNG

### 7.1. Hệ phương trình Bionomic
Tích hợp giả thuyết sản lượng trên một đơn vị nỗ lực khai thác (Catch-Per-Unit-Effort - CPUE) của Schaefer:

$$\left\{
\begin{aligned}
\frac{dx}{dt} &= x(r - ax - by) - q_1 E_1 x \\
\frac{dy}{dt} &= y(-e - cy + dx) - q_2 E_2 y \\
\pi(E_1, E_2) &= (p_1 q_1 x - c_1) E_1 + (p_2 q_2 y - c_2) E_2
\end{aligned}
\right. \quad (3)$$

* $E_1, E_2$: Nỗ lực đánh bắt (*fishing effort*) cá mòi dầu và cá vược sọc.
* $q_1, q_2$: Hệ số dễ bị bắt (*catchability coefficients*). Chọn $q_1 = 0.5$ (cá mòi đi theo đàn dễ bắt), $q_2 = 1.0$ (cá vược phân tán).
* $p_1, p_2$: Giá bán trên một đơn vị sinh khối ($/tỷ con).
* $c_1, c_2$: Chi phí trên một đơn vị nỗ lực đánh bắt.
* $\pi(E_1, E_2)$: Hàm tô kinh tế ròng (*net economic rent / profit*).

Cân bằng kinh tế sinh thái (Bionomic Equilibrium) đạt được khi đồng thời:
$$\frac{dx}{dt} = 0, \quad \frac{dy}{dt} = 0, \quad \pi(E_1, E_2) = 0$$

### 7.2. Bốn trường hợp cân bằng bionomic
* **Trường hợp 1: Chỉ đánh bắt cá vược sọc ($E_1 = 0, E_2 \ne 0$)**  
  Doanh thu cá mòi không bù đắp được chi phí ($c_1 > p_1 q_1 x$), ngư dân rút khỏi nghề cá mòi.  
  Tọa độ cân bằng:
  $$x_B = \frac{r}{a} - \frac{b c_2}{a p_2 q_2}, \quad y_B = \frac{c_2}{p_2 q_2}$$
  $$E_{2B} = -\frac{e}{q_2} - \frac{c c_2}{p_2 q_2^2} + \frac{d}{q_2}\left(\frac{r}{a} - \frac{b c_2}{a p_2 q_2}\right)$$
  Điều kiện tồn tại: $x_B > 0$ và $E_{2B} > 0$.

* **Trường hợp 2: Chỉ đánh bắt cá mòi dầu ($E_1 \ne 0, E_2 = 0$)**  
  Ngư dân rút khỏi nghề cá vược ($c_2 > p_2 q_2 y$).  
  Tọa độ cân bằng:
  $$x_B = \frac{c_1}{p_1 q_1}, \quad y_B = \frac{d c_1}{c p_1 q_1} - \frac{e}{c}$$
  $$E_{1B} = \frac{r}{q_1} - \frac{a c_1}{p_1 q_1^2} - \frac{b}{q_1}\left(\frac{d c_1}{c p_1 q_1} - \frac{e}{c}\right)$$
  Điều kiện tồn tại: $y_B > 0$ và $E_{1B} > 0$.

* **Trường hợp 3: Đóng cửa cả hai nghề cá ($E_1 = E_2 = 0$)**  
  Chi phí khai thác ở cả hai loài đều cao hơn doanh thu. Hệ quay về cân bằng sinh học tự nhiên $Q(x^*, y^*)$ với điều kiện $rd > ae$.

* **Trường hợp 4: Khai thác đồng thời cả hai loài ($E_1 \ne 0, E_2 \ne 0$)**  
  Tọa độ điểm dừng:
  $$x_B = \frac{c_1}{p_1 q_1}, \quad y_B = \frac{c_2}{p_2 q_2}$$
  Nỗ lực cân bằng tương ứng:
  $$E_{1B} = \frac{r}{q_1} - \frac{a c_1}{p_1 q_1^2} - \frac{b c_2}{p_2 q_1 q_2}, \quad E_{2B} = -\frac{e}{q_2} - \frac{c c_2}{p_2 q_2^2} + \frac{d c_1}{p_1 q_1 q_2}$$

---

## 8. CƠ SỞ TOÁN HỌC CỦA 3 CHÍNH SÁCH KHAI THÁC (MSY, MEY, RMY)

### 8.1. Chính sách Sản lượng bền vững tối đa (MSY)
Mục tiêu là tìm nỗ lực $E$ để cực đại hóa hàm tổng sản lượng $Y(E) = h_1 + h_2$.

1. **Khi chỉ khai thác cá vược sọc ($E_2 = E, E_1 = 0$):**
   * Điểm dừng theo $E$:
     $$\hat{x}(E) = \frac{be + rc}{ac + bd} + \frac{bq_2}{ac + bd} E, \quad \hat{y}(E) = \frac{rd - ae}{ac + bd} - \frac{aq_2}{ac + bd} E$$
   * Hàm sản lượng:
     $$Y(E) = E \hat{y}(E) = E\left(\frac{rd - ae}{ac + bd} - \frac{aq_2}{ac + bd} E\right)$$
   * Đây là một Parabola quay bề lõm xuống dưới. Lấy đạo hàm triệt tiêu $Y'(E) = 0$:
     $$E_{Y_m} = E_{\text{MSY}} = \frac{rd - ae}{2a q_2}$$
   * Vì $rd > ae$ thỏa mãn cho vịnh Chesapeake, chính sách MSY cho riêng cá vược luôn tồn tại và bền vững. Tại mức này, sinh khối cá vược giảm đúng một nửa: $\hat{y}(E_{\text{MSY}}) = \frac{1}{2} y^*$.

2. **Khi chỉ khai thác cá mòi dầu ($E_1 = E, E_2 = 0$) - NGHỊCH LÝ SINH THÁI:**
   * Điểm dừng:
     $$\bar{x}(E) = \frac{cr + be}{ac + bd} - \frac{cq_1}{ac + bd} E, \quad \bar{y}(E) = \frac{rd - ae}{ac + bd} - \frac{dq_1}{ac + bd} E$$
   * Hàm sản lượng:
     $$Y(E) = E \bar{x}(E) \implies E_{Y_m} = \frac{cr + be}{2c q_1}$$
   * **Điều kiện để cả hai loài cùng tồn tại tại đỉnh sản lượng:** Cần $\bar{y}(E_{Y_m}) > 0$, dẫn tới bất đẳng thức tham số:
     $$\frac{rd - ae}{cr + be} > \frac{d}{2c}$$
   * **Kiểm tra với số liệu thực tế Vịnh Chesapeake:**
     * Vế trái: $\frac{5.0979}{2.4077} \approx \mathbf{2.117}$
     * Vế phải: $\frac{9.999}{2(0.520)} \approx \mathbf{9.614}$
     * Do $2.117 \ll 9.614$, **điều kiện bị vi phạm nghiêm trọng!**
   * **Hệ quả:** Tại đỉnh sản lượng $E_{Y_m} = \frac{2.4077}{2(0.520)(0.5)} \approx \mathbf{4.63}$, giá trị $\bar{y}$ bị âm sâu. Thậm chí cá vược sẽ bị tuyệt chủng hoàn toàn ngay khi $E$ vượt qua ngưỡng:
     $$E_{\max} = \frac{rd - ae}{dq_1} = \frac{5.0979}{(9.999)(0.5)} \approx \mathbf{1.0198}$$
   * **Khuyến nghị chính sách:** Để tránh tuyệt chủng cá vược và giữ cho số lượng cá vược không giảm quá 50%, hạn ngạch phải bị cắt giảm 50% so với cận trên:
     $$E_{\text{MSY-recommended}} = \frac{E_{\max}}{2} = \frac{1.0198}{2} \approx \mathbf{0.5}$$

### 8.2. Chính sách Lợi nhuận kinh tế tối đa (MEY)
Mục tiêu là cực đại hóa hàm lợi nhuận ròng $\text{Rent}(E) = \hat{p} Y(E) - \hat{c} E$:

1. **Trường hợp chỉ đánh bắt cá vược:**
   $$\text{Rent}(E) = \hat{p} E \left(\frac{rd - ae}{ac + bd} - \frac{aq_2}{ac + bd} E\right) - \hat{c} E$$
   Lấy đạo hàm triệt tiêu $\frac{d(\text{Rent})}{dE} = 0$:
   $$E_{\text{MEY}} = \frac{\hat{p}(rd - ae) - \hat{c}(ac + bd)}{2\hat{p} a q_2} = E_{\text{MSY}} - \frac{\hat{c}(ac + bd)}{2\hat{p} a q_2}$$
   * **Tính chất cốt lõi:** Do $\hat{c}, \hat{p} > 0$, ta luôn có:
     $$E_{\text{MEY}} < E_{\text{MSY}}$$
   * Khai thác theo MEY luôn đòi hỏi nỗ lực thấp hơn MSY, vừa mang lại hiệu quả kinh tế cao hơn (tối đa hóa tiền lãi), vừa để lại nhiều sinh khối cá hơn trong tự nhiên.

### 8.3. Chính sách Tối đa hóa độ đàn hồi (RMY)
Khảo sát ma trận tuyến tính hóa $A(E_1)$ khi đánh bắt cá mòi:
* Phần thực của giá trị riêng: $\alpha(E_1) = -\frac{1}{2}(a\bar{x}(E_1) + c\bar{y}(E_1))$.
* Độ đàn hồi: $R(E_1) = -\alpha(E_1) = \frac{1}{2}(a\bar{x}(E_1) + c\bar{y}(E_1))$.
* Đạo hàm theo $E_1$:
  $$\frac{dR}{dE_1} = \frac{1}{2}\left( a \frac{d\bar{x}}{dE_1} + c \frac{d\bar{y}}{dE_1} \right) = \frac{1}{2}\left( -a \frac{cq_1}{ac + bd} - c \frac{dq_1}{ac + bd} \right) = -\frac{q_1(ac + cd)}{2(ac + bd)} < 0$$
* **Ý nghĩa:** $\frac{dR}{dE_1}$ luôn âm với mọi $E_1 > 0$. Hàm độ đàn hồi $R$ **giảm đơn điệu ngặt** theo nỗ lực đánh bắt cá mòi. Muốn hệ thống có độ đàn hồi tối đa thì bắt buộc $E_1 = 0$. Mọi hoạt động khai thác cá mòi đều phải trả giá bằng việc làm suy giảm sức chống chịu của hệ sinh thái vịnh.

---

## 9. PHƯƠNG PHÁP PHÂN TÍCH ĐỘ NHẠY VI PHÂN TRỰC TIẾP (DDM)

### 9.1. Thiết lập hệ phương trình vi phân độ nhạy
Xét hệ vector tổng quát: $\frac{du}{dt} = f(u, p)$ với $u = (x, y)^T$ và véctơ 8 tham số $p = (r, a, b, E_1, e, c, d, E_2)^T$.  
Đạo hàm riêng theo tham số $p_j$:

$$\frac{d}{dt} \left( \frac{\partial u}{\partial p_j} \right) = J(u, p) \cdot S_j + F_j$$

* $S_j = \left( \frac{\partial x}{\partial p_j}, \frac{\partial y}{\partial p_j} \right)^T$: Véctơ độ nhạy theo thời gian của tham số $p_j$.
* $J(u, p)$: Ma trận Jacobi của hệ.
* $F_j = \frac{\partial f}{\partial p_j}$: Đạo hàm riêng của vế phải theo tham số $p_j$.

Ma trận toàn phần $F$ gồm 2 hàng và 8 cột:

$$F = \begin{pmatrix} 
x & -x^2 & -xy & -q_1 x & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & -y & -y^2 & xy & -q_2 y
\end{pmatrix}$$

### 9.2. Chuẩn độ nhạy tương đối (Relative Sensitivity Norm)
Vì các tham số có đơn vị thứ nguyên và độ lớn khác nhau, ta chuẩn hóa theo độ nhạy tương đối:

$$\bar{S}_{ij}(t) = \frac{\partial u_i}{\partial p_j}(t) \cdot \frac{p_j}{u_i(t)}$$

Chỉ số độ nhạy tổng thể được đo bằng chuẩn $L_2$ trên khoảng thời gian ổn định (2050–2100):

$$\left\| \bar{S}_{ij} \right\|_2 = \sqrt{ \sum_{k=1}^M \left( \frac{\partial u_i}{\partial p_j}(t_k) \frac{p_j}{u_i(t_k)} \right)^2 }$$

### 9.3. Bảng xếp hạng độ nhạy và Ý nghĩa sinh thái
Dữ liệu trích từ Table 2 của bài báo:

| Tham số $p$ | Chuẩn độ nhạy Menhaden ($\|\bar{S}_{x}\|_2$) | Chuẩn độ nhạy Striped Bass ($\|\bar{S}_{y}\|_2$) |
| :---: | :---: | :---: |
| $r$ (tăng trưởng mòi) | 0.1079 | **1.0080 (Hạng 1)** |
| $b$ (săn bắt của bass) | 0.1098 | **1.0004 (Hạng 2)** |
| $d$ (chuyển hóa mòi sang bass) | **0.9985 (Hạng 1)** | 0.0093 |
| $e$ (tử vong bass) | **0.8886 (Hạng 2)** | 0.0133 |
| $E_1$ (khai thác mòi) | $0.2103 E_1 q_1$ | **$1.9647 E_1 q_1$ (Rất nhạy)** |
| $E_2$ (khai thác bass) | **$0.7328 E_2 q_2$** | $0.0110 E_2 q_2$ |

### 9.4. Kết luận sinh thái từ phân tích độ nhạy
1. **Cá vược sọc nhạy cảm bậc nhất với cá mòi dầu:**  
   Chuẩn độ nhạy của cá vược đối với $r$ lên tới $1.008$ và đối với $b$ là $1.0004$. Chỉ cần tốc độ tăng trưởng của cá mòi $r$ nhích nhẹ từ $0.513 \to 0.6$, điểm cân bằng của cá vược vọt ngay từ $0.29 \to 0.34$.
2. **Bất đối xứng trong nỗ lực khai thác:**  
   Nỗ lực đánh bắt cá mòi $E_1$ tác động tiêu cực lên cá vược ($\|S\| \approx 1.96$) mạnh gấp gần 10 lần so với tác động lên chính bản thân cá mòi ($\|S\| \approx 0.21$).  
   $\implies$ **Đánh bắt con mồi gây hủy diệt kẻ săn mồi nhanh hơn nhiều so với việc con mồi tự chịu đựng!** Đây là luận cứ toán học đanh thép nhất cho việc áp dụng Điểm tham chiếu sinh thái ERP.
