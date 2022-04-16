from fastapi import FastAPI, Response
#import uvicorn

app = FastAPI()


@app.get("/test-ping")
async def test_ping():
    return {"message": "Pong!"}

@app.post("/get-cookie")
async def send_cookie(response: Response):
    response.set_cookie(key="cookie1", value="Something1")
    return {"message": "Requesting 1 cookie"}

@app.post("/get-cookies")
async def send_cookies(response: Response):
    response.set_cookie(key="cookieA", value="SomethingA")
    response.set_cookie(key="cookieB", value="SomethingB")
    return {"message": "Requesting 2 cookies"}

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)
