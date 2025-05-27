from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
import qrcode
import io

app = FastAPI()

@app.get("/qrcode")
def generate_qrcode(data: str = Query(...)):
    qr = qrcode.make(data)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
