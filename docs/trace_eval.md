# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Hoàng Ngọc Đức    
> **Mã Sinh Viên / Mã Học viên:** 2A202602380  
> **Chủ đề Lựa chọn:** 4.1: Trợ lý Tuyển dụng & Sàng lọc CV: Tra cứu tiêu chí tuyển dụng vị trí và gửi thông báo lịch phỏng vấn.  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** |3/ 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 4/ 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4/ 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 3/ 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **14/ 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Chào bạn, bạn có thể giới thiệu quy chế học vụ cơ bản của Đại học VinUni không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Xin lỗi bạn, mình là Trợ lý Tuyển dụng Nhân sự và chỉ có thể hỗ trợ các tác vụ liên quan đến **Tuyển dụng & Sàng lọc CV** (tra cứu vị trí tuyển dụng, đánh giá hồ sơ ứng viên, kiểm tra lịch phỏng vấn và đặt lịch phỏng vấn).\n\nCác thông tin về **quy chế học vụ, chương trình đào tạo hay quy chế sinh viên** không thuộc phạm vi hỗ trợ của mình. Bạn vui lòng liên hệ **Phòng Quản lý Đào tạo / Bộ phận Dịch vụ Sinh viên (Student Affairs / Registrar Office)** của Đại học VinUni để được tư vấn và hỗ trợ chi tiết nhất nhé.",
    "latency_ms": 3364.85
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Xin lỗi bạn, tôi là Trợ lý Tuyển dụng Nhân sự nên chỉ có thể hỗ trợ các tác vụ liên quan đến **tuyển dụng, sàng lọc CV và lịch phỏng vấn**. \n\nYêu cầu tra cứu thông tin học vụ của sinh viên nằm ngoài phạm vi hỗ trợ của tôi. Bạn vui lòng liên hệ **Phòng Quản lý Đào tạo** hoặc **Phòng Công tác Sinh viên** để được hỗ trợ tốt nhất nhé!",
    "latency_ms": 3364.42
  },
  {
    "step": 1,
    "query": "Hãy gửi thông báo lịch phỏng vấn cho ứng viên Nguyễn Văn A (Mã Ứng viên: UV2024001) vào lúc 9h sáng ngày 20/10/2026.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_interview",
    "arguments": {
      "candidate_id": "UV2024001",
      "datetime_str": "09:00 20/10/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-UV2024001-99",
      "candidate_id": "UV2024001",
      "datetime": "09:00 20/10/2026",
      "interviewer": "Nguyễn Văn A",
      "message": "Đặt lịch thành công cho ứng viên UV2024001 với Nguyễn Văn A vào lúc 09:00 20/10/2026."
    },
    "latency_ms": 3493.53
  },
  {
    "step": 2,
    "query": "Hãy gửi thông báo lịch phỏng vấn cho ứng viên Nguyễn Văn A (Mã Ứng viên: UV2024001) vào lúc 9h sáng ngày 20/10/2026.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đặt lịch thành công cho ứng viên UV2024001 với Nguyễn Văn A vào lúc 09:00 20/10/2026.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Bạn hãy tra cứu tiêu chí tuyển dụng cho vị trí Data Scientist, sau đó đặt lịch phỏng vấn cho ứng viên Trần Thị B vào lúc 14h ngày mai.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Để thực hiện tra cứu tiêu chí tuyển dụng và đặt lịch phỏng vấn, tôi cần bạn cung cấp thêm một số thông tin chi tiết sau:\n\n1. **Mã vị trí tuyển dụng (`job_id`)** của vị trí Data Scientist (ví dụ: `DS001`).\n2. **Mã ứng viên (`candidate_id`)** của ứng viên Trần Thị B (ví dụ: `UV2024002`).\n3. **Ngày cụ thể** (định dạng DD/MM/YYYY) cho lịch hẹn phỏng vấn vào lúc 14:00.\n\nBạn vui lòng bổ sung thông tin trên để tôi có thể hỗ trợ bạn nhanh chóng và chính xác nhé!",
    "latency_ms": 7264.67
  },
  {
    "step": 1,
    "query": "Hãy tra cứu tiêu chí tuyển dụng cho vị trí Kỹ sư hàng không vũ trụ (Mã vị trí: AE999).",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "search_job_requirements",
    "arguments": {
      "job_id": "AE999"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy vị trí mã 'AE999'"
    },
    "latency_ms": 3171.52
  },
  {
    "step": 2,
    "query": "Hãy tra cứu tiêu chí tuyển dụng cho vị trí Kỹ sư hàng không vũ trụ (Mã vị trí: AE999).",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Không tìm thấy vị trí mã 'AE999'",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 3 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
