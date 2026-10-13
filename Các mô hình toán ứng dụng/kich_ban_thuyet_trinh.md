# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO TIỂU LUẬN (PHIÊN BẢN TINH GỌN)
## ĐỀ TÀI: ỨNG DỤNG MÔ HÌNH LOTKA–VOLTERRA MỞ RỘNG CHO HỆ SINH THÁI ATLANTIC MENHADEN – STRIPED BASS
* **Môn học:** Các mô hình toán ứng dụng  
* **Giảng viên hướng dẫn:** TS. Nguyễn Trọng Hiếu  
* **Nhóm sinh viên thực hiện (K68A2):** Tạ Tiến Nam – Tạ Văn Nghĩa – Trần Đức Kiên  
* **Định dạng:** Thuyết trình nhanh, súc tích (~15 giây / slide)  
* **Tổng thời lượng:** ~5.5 – 6 phút (+ Q&A thảo luận)  
* **Tiêu chí trọng tâm:** Tập trung vào **Mục đích – Ý nghĩa sinh thái – Kết quả thực tiễn – Khuyến nghị chính sách**; lược bỏ các diễn giải biến đổi toán học chi tiết.

---

## TỔNG QUAN PHÂN CHIA 3 PHẦN THUYẾT TRÌNH

| Phần | Nội dung chính | Slide | Người trình bày | Thời gian |
| :--- | :--- | :---: | :---: | :---: |
| **Phần 1** | Bối cảnh Vịnh Chesapeake & Đặt vấn đề quản lý | Slide 1 – 7 | **Tạ Tiến Nam** | ~1.5 – 2.0 phút |
| **Phần 2** | Mô hình sinh thái, Khớp dữ liệu thực tế & Dự báo | Slide 8 – 15 | **Tạ Văn Nghĩa** | ~2.0 phút |
| **Phần 3** | Độ đàn hồi phục hồi, Chính sách khai thác & Hàm ý quản lý | Slide 16 – 24 | **Trần Đức Kiên** | ~2.5 phút |

---

# CHI TIẾT LỜI THOẠI 15 GIÂY TỪNG SLIDE

---

### SLIDE 1: TRANG TIÊU ĐỀ
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Mục đích:** Giới thiệu đề tài và định vị nghiên cứu.
> *"Kính thưa thầy TS. Nguyễn Trọng Hiếu và các bạn! Hôm nay nhóm K68A2 xin báo cáo đề tài: **Ứng dụng mô hình Lotka–Volterra mở rộng cho hệ sinh thái cá mòi dầu và cá vược sọc tại Vịnh Chesapeake** – một nghiên cứu giải quyết bài toán mâu thuẫn giữa khai thác kinh tế và bảo tồn sinh thái biển."*

---

### SLIDE 2: NỘI DUNG BÁO CÁO (MỤC LỤC)
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Mục đích:** Khái quát lộ trình 5 phần của bài báo cáo.
> *"Bài báo cáo của nhóm gồm 5 nội dung chính: Khởi đầu từ bối cảnh sinh thái Vịnh Chesapeake; tiếp đến là thiết lập mô hình Lotka–Volterra mở rộng; thứ ba là đối chứng dữ liệu 23 năm thực tế; thứ tư là phân tích độ đàn hồi phục hồi 13 năm; và cuối cùng là đánh giá 3 chính sách khai thác thực tiễn."*

---

### SLIDE 3: BỐI CẢNH NGHIÊN CỨU: HỆ SINH THÁI VỊNH CHESAPEAKE
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Ý nghĩa:** Giới thiệu ngư trường lớn nhất Bắc Mỹ và xung đột lợi ích.
> *"Vịnh Chesapeake là cửa sông lớn nhất Bắc Mỹ với hơn 3.600 loài sinh vật. Tại đây đang diễn ra mâu thuẫn gay gắt: Nhu cầu đánh bắt thương mại ngắn hạn đang đe dọa làm suy thoái nguồn tài nguyên sinh khối vĩnh viễn, đặc biệt là mối tương tác dinh dưỡng sống còn giữa cá mòi dầu và cá vược sọc."*

---

### SLIDE 4: HAI LOÀI SINH VẬT TRỌNG YẾU TRONG HỆ SINH THÁI VỊNH
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Ý nghĩa:** Làm rõ vai trò sinh thái và kinh tế của 2 loài.
> *"Cá mòi dầu là 'loài cá quan trọng nhất vịnh' – chúng vừa ăn lọc làm sạch nước vịnh, vừa là thức ăn nuôi sống toàn bộ chuỗi thức ăn. Ở đầu kia, cá vược sọc là loài săn mồi đỉnh cao, biểu tượng của nghề cá giải trí mang lại doanh thu hàng tỷ USD cho nền kinh tế ven biển."*

---

### SLIDE 5: KHỦNG HOẢNG KHAI THÁC & BI KỊCH TÀI NGUYÊN CHUNG
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Ý nghĩa:** Chỉ ra sai lầm của tư duy quản lý đơn loài truyền thống.
> *"Áp lực đánh bắt công nghiệp khiến cả hai loài suy giảm nghiêm trọng. Đáng nói, các cơ quan quản lý trước đây chỉ dùng **mô hình đánh giá đơn loài**, kết luận cá mòi vẫn an toàn mà hoàn toàn bỏ qua việc đàn cá vược sọc đang chết đói vì cạn kiệt nguồn thức ăn này."*

---

### SLIDE 6: NHU CẦU CHUYỂN DỊCH SANG QUẢN LÝ DỰA TRÊN HỆ SINH THÁI (EBFM)
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam
* **Mục đích:** Đặt ra mục tiêu nghiên cứu của nhóm.
> *"Để không làm sụp đổ chuỗi thức ăn, nghề cá bắt buộc phải chuyển sang **Quản lý dựa trên hệ sinh thái (EBFM)**. Mục tiêu của đề tài chúng em là dùng mô hình toán học để định lượng chính xác sự tương tác giữa hai loài và tìm ra hạn ngạch khai thác an toàn cho hệ thống."*

---

### SLIDE 7: SƠ ĐỒ CẤU TRÚC TƯƠNG TÁC SINH THÁI – KINH TẾ
* **Thời lượng:** ~15s
* **Người nói:** Tạ Tiến Nam $\to$ chuyển giao cho Tạ Văn Nghĩa
* **Ý nghĩa:** Khái quát bức tranh liên ngành Sinh thái – Kinh tế.
> *"Sơ đồ trên màn hình mô tả sự tích hợp giữa động lực học tự nhiên của hai loài với hoạt động khai thác và hàm lợi nhuận thị trường. Sau đây, bạn Tạ Văn Nghĩa sẽ trình bày chi tiết về mô hình toán học và kết quả khớp dữ liệu thực tế."*

---

### SLIDE 8: HỆ PHƯƠNG TRÌNH VI PHÂN LOTKA–VOLTERRA TỔNG QUÁT
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Ý nghĩa toán học & sinh học:** Cải tiến mô hình để phù hợp thực tế.
> *"Thay vì mô hình cổ điển chỉ dao động vô hạn kém thực tế, mô hình mở rộng bổ sung hai số hạng tự giới hạn logistic $-ax^2$ và $-cy^2$. Điều này phản ánh sức chứa hữu hạn của vịnh, đảm bảo các quần thể tăng trưởng có kiểm soát và hội tụ ổn định."*

---

### SLIDE 9: Ý NGHĨA SINH HỌC CỦA 6 THAM SỐ MÔ HÌNH
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Ý nghĩa:** Định lượng các quá trình sinh thái.
> *"Mô hình bao gồm 6 tham số sinh học đại diện cho: tốc độ sinh sản $r$, tỷ lệ tử vong $e$, sự cạnh tranh nội bộ $a, c$ và hiệu quả săn bắt chuyển hóa dinh dưỡng $b, d$. Toàn bộ dữ liệu sinh khối được chuẩn hóa theo đơn vị **tỷ cá thể** để tối ưu tính toán số học."*

---

### SLIDE 10: 5 GIẢ THIẾT NỀN TẢNG & ƯU THẾ CỦA MÔ HÌNH
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Ý nghĩa:** Ưu thế tinh gọn của mô hình.
> *"Với 5 giả thiết sinh học tập trung vào chuỗi thức ăn chính, ưu thế lớn nhất của mô hình là vừa đủ tinh gọn để giải tích rõ ràng các điểm cân bằng, vừa tránh được hiện tượng quá khớp (overfitting) khi đối chiếu với số liệu lịch sử."*

---

### SLIDE 11: NGUỒN DỮ LIỆU THỰC NGHIỆM & PHƯƠNG PHÁP HỒI QUY (NLS)
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Ý nghĩa:** Nguồn gốc dữ liệu chuẩn xác.
> *"Nhóm tác giả sử dụng chuỗi dữ liệu độ phong phú thực tế trong suốt **23 năm (1995–2017)** từ Ủy ban Nghề cá ASMFC, đã tính thêm lượng đánh bắt thực tế. Phương pháp bình phương tối thiểu phi tuyến (NLS) được áp dụng để tìm ra bộ tham số thực nghiệm tối ưu."*

---

### SLIDE 12: BỘ THAM SỐ TỐI ƯU & ĐÁNH GIÁ ĐỘ CHÍNH XÁC
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Ý nghĩa:** Khẳng định độ tin cậy của mô hình.
> *"Bộ tham số tìm được cho thấy tốc độ tăng trưởng của cá mòi $r = 0.513$ trùng khớp hoàn toàn với các quan sát sinh học độc lập. Sai số chuẩn phần dư chỉ là $S = 0.11$, chứng minh mô hình khớp rất sát với biến động thực tế của vịnh Chesapeake."*

---

### SLIDE 13: ĐỒ THỊ KHỚP MÔ HÌNH & HIỆN TƯỢNG DAO ĐỘNG TRỄ PHA (FIG. 1)
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Kết quả:** Phân tích trực quan Hình 1.
> *"Hình 1 do nhóm lập trình tái hiện cho thấy sự phù hợp tuyệt vời giữa đường cong mô hình và dữ liệu thực tế. Đồ thị phản ánh rõ **hiện tượng trễ pha**: Khi cá mòi bùng nổ thì 1–2 năm sau cá vược mới tăng theo; và khi cá vược đạt đỉnh săn bắt thì đàn cá mòi sẽ sụt giảm chu kỳ."*

---

### SLIDE 14: DỰ BÁO ĐỘNG THÁI QUẦN THỂ ĐẾN NĂM 2100 (FIG. 2)
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa
* **Kết quả:** Phân tích trực quan Hình 2.
> *"Tại Hình 2, mô hình dự báo dài hạn đến năm 2100. Các dao động suy giảm biên độ theo cơ chế **dao động tắt dần** và hội tụ hoàn toàn về trạng thái cân bằng tự nhiên sau năm 2050 mà không xảy ra hiện tượng hỗn loạn hay tuyệt chủng."*

---

### SLIDE 15: TÍNH TOÁN TRẠNG THÁI CÂN BẰNG DỪNG TỰ NHIÊN $Q(x^*, y^*)$
* **Thời lượng:** ~15s
* **Người nói:** Tạ Văn Nghĩa $\to$ chuyển giao cho Trần Đức Kiên
* **Ý nghĩa ứng dụng:** Con số nền tảng cho quản lý.
> *"Tại điểm cân bằng dừng, trữ lượng cá mòi dầu đạt **136.3 triệu con** và cá vược sọc đạt **288.6 triệu con**. Đây chính là mốc chuẩn sinh thái tự nhiên của vịnh. Tiếp theo, bạn Trần Đức Kiên sẽ trình bày về khả năng tự phục hồi của hệ thống và các chính sách khai thác."*

---

### SLIDE 16: KHÁI NIỆM ĐỘ ĐÀN HỒI SINH HỌC (RESILIENCE)
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Ý nghĩa:** Định nghĩa thước đo sức chống chịu sinh thái.
> *"Độ đàn hồi sinh học ($R$) đo lường tốc độ hệ sinh thái tự phục hồi về trạng thái cân bằng sau một cú sốc môi trường. Độ đàn hồi tỷ lệ nghịch với thời gian hồi phục $\tau$ và được xác định qua phần thực của giá trị riêng ma trận Jacobian."*

---

### SLIDE 17: MA TRẬN JACOBIAN & TÍNH ỔN ĐỊNH TIỆM CẬN
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Ý nghĩa:** Kết luận tính ổn định tự nhiên của vịnh.
> *"Khảo sát ma trận Jacobi chứng minh hệ luôn thỏa mãn tiêu chuẩn Routh–Hurwitz. Điều này khẳng định trạng thái cân bằng đồng tồn tại giữa cá mòi dầu và cá vược sọc là **ổn định tiệm cận**, tức hệ thống luôn có xu hướng tự phục hồi nếu không bị can thiệp quá mức."*

---

### SLIDE 18: GIÁ TRỊ RIÊNG & THỜI GIAN PHỤC HỒI CỦA VỊNH CHESAPEAKE
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Kết quả quan trọng:** Con số then chốt 13 năm.
> *"Với các tham số thực tế của vịnh, giá trị riêng có phần thực là $-0.0768$. Từ đó tính ra thời gian hồi phục tự nhiên của hệ sinh thái vịnh là **khoảng 13 năm** – một con số mang thông điệp sinh thái vô cùng quan trọng."*

---

### SLIDE 19: Ý NGHĨA SINH THÁI SÂU SẮC CỦA CHỈ SỐ ĐỘ ĐÀN HỒI
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Ý nghĩa thực tiễn & Cảnh báo:** Sức chống chịu của vịnh rất chậm.
> *"13 năm nghĩa là: Nếu vịnh gặp một cú sốc lớn như tràn dầu hay dịch bệnh, phải mất hơn một thập kỷ hệ sinh thái mới cân bằng lại! Sức chống chịu tự nhiên của vịnh là rất mong manh, đòi hỏi các chính sách khai thác phải luôn duy trì một ngưỡng đệm an toàn cao."*

---

### SLIDE 20: MỞ RỘNG BIONOMIC: SO SÁNH 3 CHIẾN LƯỢC KHAI THÁC
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Ứng dụng chính sách then chốt:** Bác bỏ MSY đơn loài.
> *"So sánh 3 chính sách cho thấy: Nếu khai thác tối đa sản lượng (MSY) cá mòi theo kiểu đơn loài, **đàn cá vược sọc sẽ bị tuyệt chủng vì đói**! Để cả hai loài cùng tồn tại bền vững, mô hình khuyến nghị bắt buộc phải **cắt giảm 50% hạn ngạch khai thác cá mòi dầu**."*

---

### SLIDE 21: TỔNG KẾT CÁC KẾT QUẢ CHÍNH ĐẠT ĐƯỢC CỦA ĐỀ TÀI
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Tổng kết:** 4 đóng góp cốt lõi.
> *"Tóm lại, đề tài đã chứng minh tính đặt đúng của mô hình toán học, khớp chính xác số liệu lịch sử 23 năm, cung cấp luận cứ bác bỏ chính sách MSY đơn loài cho cá mồi và định lượng được thời gian hồi phục 13 năm của hệ sinh thái vịnh."*

---

### SLIDE 22: HÀM Ý CHÍNH SÁCH QUẢN LÝ CHO VỊNH CHESAPEAKE
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Ứng dụng thực tiễn:** Khuyến nghị hành động cụ thể.
> *"Nghiên cứu đưa ra thông điệp chính sách cốt lõi: Chuyển dịch dứt khoát sang EBFM, áp dụng Điểm tham chiếu sinh thái để lại ít nhất 50% cá mòi trong biển. **Bảo vệ cá mòi dầu chính là bảo vệ ngành kinh tế câu cá giải trí hàng tỷ USD của cá vược sọc!**"*

---

### SLIDE 23: ĐÁNH GIÁ HẠN CHẾ & HƯỚNG PHÁT TRIỂN TIẾP THEO
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên
* **Mở rộng nghiên cứu:** Hướng đi tương lai.
> *"Dù đạt kết quả thực tiễn cao, mô hình hiện tại vẫn bỏ qua cấu trúc tuổi và yếu tố ngẫu nhiên khí hậu. Trong tương lai, nhóm dự kiến mở rộng mô hình phân lớp tuổi kết hợp lưới thức ăn đa loài và phương trình vi phân ngẫu nhiên (SDE)."*

---

### SLIDE 24: KẾT LUẬN & HỎI ĐÁP (Q&A)
* **Thời lượng:** ~15s
* **Người nói:** Trần Đức Kiên (đại diện nhóm)
* **Kết thúc:** Cảm ơn và mở màn Q&A.
> *"Trên đây là toàn bộ báo cáo của nhóm K68A2. Chúng em xin chân thành cảm ơn thầy TS. Nguyễn Trọng Hiếu và các bạn đã chú ý lắng nghe. Nhóm rất mong nhận được những câu hỏi và đóng góp quý báu từ thầy và các bạn!"*

---

# GỢI Ý TRẢ LỜI NHANH CÁC CÂU HỎI THƯỜNG GẶP (QUICK Q&A CHEATSHEET)

* **Hỏi: Tại sao lại đề xuất cắt giảm 50% hạn ngạch cá mòi dầu?**  
  $\rightarrow$ **Đáp:** Vì nếu đánh bắt cá mòi ở mức tối đa sản lượng đơn loài ($E \approx 1.02$), sinh khối cá mòi còn lại không đủ cung cấp thức ăn tối thiểu, khiến cá vược suy dinh dưỡng và tuyệt chủng. Cắt giảm 50% ($E = 0.5$) là ngưỡng tối ưu để giữ cá vược không bị suy giảm quá 50% quần thể.

* **Hỏi: Con số 13 năm hồi phục có ý nghĩa gì trong thực tế?**  
  $\rightarrow$ **Đáp:** Nghĩa là khả năng tự phục hồi của vịnh rất chậm trước các cú sốc môi trường. Các nhà quản lý không thể điều chỉnh tăng hạn ngạch tùy tiện theo từng năm mà phải có chính sách ổn định đa niên hạn.

* **Hỏi: Tại sao mô hình này tốt hơn mô hình Lotka–Volterra cổ điển?**  
  $\rightarrow$ **Đáp:** Mô hình cổ điển chỉ dao động điều hòa vĩnh viễn không tắt. Mô hình mở rộng có số hạng tự giới hạn logistic $-ax^2, -cy^2$, giúp mô tả đúng sức chứa hữu hạn của vịnh và tạo ra trạng thái cân bằng ổn định tiệm cận.
