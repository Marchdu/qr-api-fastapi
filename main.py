from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import qrcode
import io

app = FastAPI()

@app.get("/qrcode")
def generate_qr(data: str):
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
