from cryptography.fernet import Fernet
import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the Dynacorp API</h1>" \
           "<div>" \
           "Try it: <a href='/api/cloudclass'>/api/cloudclass</a>" \
           "</div>" \
           "</body>" \
           "</html>"

    return fastapi.responses.HTMLResponse(content=body)


@app.get('/api/cloudclass')
def cloudclass():
    key = 'hZ-1hxcfvZgtFDPcaAAHDy66bJF7VtAwcfU3rCYt06k='
    f = Fernet(key.encode())

    message = "gAAAAABhrVg92NBPiny0SKPJT8f9u-SXslGm_3L8QjM_XgLpQrVEWNs7Sqsmii6HtUKb5jKjMG-zjW0T5_6WXBzXvsMdoAkkOv1oBvBkp3r9MCmBoR_eF9a8ojdIDmACkNj_FSw_l14x8rjCtvF-HX1KcYxxteb0Lk3E4ioI6rAefqAIF8QYfEA="  # noqa
    decrypted_message = f.decrypt(message.encode())

    return fastapi.responses.JSONResponse(
        content={"message": decrypted_message.decode()},
        status_code=200
    )


@app.get('/api/healthcheck')
def healthcheck():

    return fastapi.responses.JSONResponse(
        content={"health": "ok"},
        status_code=200
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
