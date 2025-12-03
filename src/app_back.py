from fastapi import FastAPI 
from routers.user_router import router_user

app = FastAPI()  

app.include_router(router_user)

@app.get('/')  
def read_root():  
    return {'message': 'Olá Mundo!'}