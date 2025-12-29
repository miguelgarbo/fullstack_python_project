from fastapi import FastAPI, Depends
from routers.user import router as u_router
from routers.login import router as l_router

app = FastAPI()  

app.include_router(u_router)
app.include_router(l_router)

@app.get('/')  
def read_root():  
    print("opa")
    return {'message': 'hello world from app_back'}

