from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

file_list = []

@app.get("/", response_class=HTMLResponse)
async def index():
    html = "<html><head><title>Shared Files</title></head><body>"
    html += "<h1>Shared Files</h1><ul>"
    for idx, f in enumerate(file_list):
        html += f'<li><a href="/download/{idx}">{f["name"]}</a></li>'
    html += "</ul></body></html>"
    return HTMLResponse(content=html)

@app.get("/download/{index}")
async def download(index: int):
    f = file_list[index]
    return FileResponse(f["path"], filename=f["name"])