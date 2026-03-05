from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/api/v1", tags=["video"])


@router.get("/video-link")
async def get_upload_video_link_page():
    # Đường dẫn đến file HTML của bạn
    HTML_PATH = os.path.join(
        "public", "assets", "pages", "upload-video-link", "main.html"
    )
    if os.path.exists(HTML_PATH):
        return FileResponse(HTML_PATH)
    return {"error": "File HTML không tồn tại tại đường dẫn chỉ định."}
