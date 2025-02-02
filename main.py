from app import app
import database.models
from database import db_connect
import uvicorn


if __name__ == "__main__":
    db_connect.db_connect()
    uvicorn.run(app.app, host="0.0.0.0", port=8000)
    