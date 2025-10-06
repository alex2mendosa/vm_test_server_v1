from fastapi import FastAPI 
import uvicorn 
from pydantic import BaseModel

app = FastAPI()

class query_result( BaseModel ): 
     query:str 


def test_api_upcase(request: query_result):
    buff = request.query.upper() 
    return {"agent_response": buff}

app.add_api_route(
    path = "/test", 
    endpoint=test_api_upcase,
    methods = ["POST"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
