from fastapi import FastAPI, HTTPException
import uuid
import redis


app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.post("/create/")
async def post(url: str = ""):
    corr_id = str(uuid.uuid4()) + str(uuid.uuid4())

    r.set(corr_id, url)

    return {"item_id": corr_id}


@app.get("/link/{id}")
async def get(id: str = ""):
    url = r.get(id)
    if not url:
        raise HTTPException(
            status_code=404, detail="Id {} has not founded in database".format(id)
        )

    return {"url": url}
