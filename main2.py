from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/aici_primim_paine_calda")
def talk2me(message: str):

    print(message)

    return ("HAI CEAU " * 3) + message
