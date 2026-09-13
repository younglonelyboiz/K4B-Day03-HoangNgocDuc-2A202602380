"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    {
        "name": "search_job_requirements",
        "description": "Tra cứu yêu cầu tuyển dụng của một vị trí.",
        "parameters": {
            "type": "object",
            "properties": {
                "job_id": {"type": "string", "description": "Mã vị trí tuyển dụng"}
            },
            "required": ["job_id"],
        },
    },
    {
        "name": "screen_candidate",
        "description": "Đánh giá mức độ phù hợp giữa CV ứng viên và yêu cầu tuyển dụng.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_id": {"type": "string"},
                "job_id": {"type": "string"},
            },
            "required": ["candidate_id", "job_id"],
        },
    },
    {
        "name": "check_interview_availability",
        "description": "Kiểm tra các khung giờ phỏng vấn còn trống.",
        "parameters": {
            "type": "object",
            "properties": {
                "interviewer_id": {"type": "string"},
                "date": {"type": "string"},
            },
            "required": ["interviewer_id", "date"],
        },
    },
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - student_id (string): Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')
    #    - datetime_str (string): Thời gian hẹn (ví dụ: '14:00 15/09/2026')
    #    - advisor_name (string): Tên cố vấn học tập
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
        "name": "schedule_interview",
        "description": "Gửi thông báo và đặt lịch phỏng vấn với ứng viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_id": {
                    "type": "string",
                    "description": "Mã ứng viên (ví dụ: 'UV2024001')",
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn phỏng vấn (ví dụ: '09:00 20/10/2026')",
                },
            },
            "required": ["candidate_id", "datetime_str"],
        },
    },
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "UV2024001": {
        "full_name": "Nguyễn Văn A",
        "email": "an.nv@gmail.com",
        "skills": ["Python", "Machine Learning", "Data Analysis"],
        "experience": "2 years",
    },
    "UV2024002": {
        "full_name": "Trần Thị B",
        "email": "binh.tt@gmail.com",
        "skills": ["Java", "Spring Boot", "SQL"],
        "experience": "3 years",
    },
    "DS001": {
        "job_title": "Data Scientist",
        "requirements": ["Python", "Machine Learning", "SQL"],
        "experience_required": "1+ years",
        "status": "Open",
    },
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps(
            {"status": "SUCCESS", "student_id": student_id, "data": student},
            ensure_ascii=False,
        )
    else:
        return json.dumps(
            {
                "status": "NOT_FOUND",
                "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'",
            },
            ensure_ascii=False,
        )


def execute_search_job_requirements(job_id: str) -> str:
    job = MOCK_DATABASE.get(job_id.strip().upper())
    if job:
        return json.dumps(
            {"status": "SUCCESS", "job_id": job_id, "data": job}, ensure_ascii=False
        )
    else:
        return json.dumps(
            {"status": "NOT_FOUND", "message": f"Không tìm thấy vị trí mã '{job_id}'"},
            ensure_ascii=False,
        )


def execute_screen_candidate(candidate_id: str, job_id: str) -> str:
    candidate = MOCK_DATABASE.get(candidate_id.strip().upper())
    job = MOCK_DATABASE.get(job_id.strip().upper())
    if candidate and job:
        return json.dumps(
            {"status": "SUCCESS", "match_score": "85%", "message": "Ứng viên phù hợp."},
            ensure_ascii=False,
        )
    return json.dumps(
        {"status": "NOT_FOUND", "message": "Không tìm thấy dữ liệu."},
        ensure_ascii=False,
    )


def execute_check_interview_availability(interviewer_id: str, date: str) -> str:
    return json.dumps(
        {"status": "SUCCESS", "available_slots": ["09:00", "14:00"]}, ensure_ascii=False
    )


def execute_schedule_interview(
    candidate_id: str, datetime_str: str, interviewer_name: str = "Nguyễn Văn A"
) -> str:
    """Thực thi đặt lịch hẹn phỏng vấn"""
    return json.dumps(
        {
            "status": "SUCCESS",
            "booking_id": f"BK-{candidate_id}-99",
            "candidate_id": candidate_id,
            "datetime": datetime_str,
            "interviewer": interviewer_name,
            "message": f"Đặt lịch thành công cho ứng viên {candidate_id} với {interviewer_name} vào lúc {datetime_str}.",
        },
        ensure_ascii=False,
    )


# Router gọi tool thực tế
TOOL_ROUTER = {
    "search_job_requirements": execute_search_job_requirements,
    "screen_candidate": execute_screen_candidate,
    "check_interview_availability": execute_check_interview_availability,
    "schedule_interview": execute_schedule_interview,
}


def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps(
                {"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False
            )
    return json.dumps(
        {"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"},
        ensure_ascii=False,
    )
