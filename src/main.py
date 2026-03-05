from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.routes.video_route import router as video_router

app = FastAPI(title="YouTube Subtitle Tool")

# 1. Cấu hình phục vụ file tĩnh (CSS, JS, Images)
# Người dùng có thể truy cập qua: http://localhost:8000/static/...
app.mount("/static", StaticFiles(directory="public"), name="static")

# 2. Nhúng router từ thư mục routes vào app chính
app.include_router(video_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Subtitle Tool API. Go to /docs for more info."}
