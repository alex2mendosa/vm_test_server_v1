from fastapi import FastAPI 
import uvicorn 

app = FastAPI()

def test_api_upcase(query: str):
    buff = query.upper() 
    return {"agent_response": buff}

app.add_api_route(
    path = "/test/{query}", 
    endpoint=test_api_upcase,
    methods = ["GET"]
)

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8002)
