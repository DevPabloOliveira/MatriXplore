from fastapi import FastAPI, UploadFile, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from typing import List
import os
# Importação da função process_matrices
from app.utils import process_matrices

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Monta a pasta 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Caminho da pasta com os arquivos de matrizes para download
BASE_PATH = "base-test"

def get_matrix_files():
    """Lê os arquivos CSV na pasta BASE_PATH e retorna uma lista de nomes de arquivos."""
    return [f for f in os.listdir(BASE_PATH) if f.endswith(".csv")]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

# Página para Download de Matrizes
@app.get("/matrices", response_class=HTMLResponse)
async def matrices_page(request: Request):
    files = get_matrix_files()
    return templates.TemplateResponse("matrices.html", {"request": request, "title": "Bases para Download", "files": files})

# Rota para Download de Arquivo
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join(BASE_PATH, file_name)
    return FileResponse(file_path, media_type="text/csv", filename=file_name)

@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request, "title": "Upload de Matrizes"})

@app.post("/process", response_class=HTMLResponse)
async def process_files(request: Request, files: List[UploadFile]):
    matrices_data = []
    for file in files:
        content = await file.read()
        matrices_data.append(content.decode())  # Assume que o conteúdo é texto simples
    
    # Processa os dados do arquivo
    results = process_matrices(matrices_data)
    
    # Retorna o template 'result.html' com os dados processados
    return templates.TemplateResponse("result.html", {"request": request, "results": results, "title": "Resultados"})

# Corrija aqui a rota "/manual" para que o FastAPI possa reconhecer
@app.get("/manual", response_class=HTMLResponse)
async def manual_page(request: Request):
    return templates.TemplateResponse("manual.html", {"request": request, "title": "Inserção Manual de Matrizes e Relações"})

@app.post("/process_manual", response_class=HTMLResponse)
async def process_manual(request: Request, matrix: str = Form(...), set: str = Form(...), relation: str = Form(...)):
    # Converte as entradas para uma lista de strings
    input_data = [matrix, set, relation]
    
    # Processa os dados
    results = process_matrices(input_data)
    
    # Retorna o template 'result.html' com os dados processados
    return templates.TemplateResponse("result.html", {"request": request, "results": results, "title": "Resultados"})
