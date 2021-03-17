import argparse
import uvicorn
from fastapi import FastAPI

from app.routers import measurements, words

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help',
                    action='help',
                    default=argparse.SUPPRESS,
                    help='Show this help message and exit.')

parser.add_argument("--ip",
                    default='0.0.0.0',
                    help="If set, api will run in its address")

parser.add_argument("--port",
                    default=8000,
                    help="If set, api will run in its address")


args = parser.parse_args()

host, port = args.ip, int(args.port)

app = FastAPI()

app.include_router(measurements.router)
app.include_router(words.router)


@app.get("/")
async def root():
    return {"message": "Welcome to APIes!"}

if __name__ == "__main__":
    print(f"Starting welo-API-es in {host}:{port} address")
    uvicorn.run(app, host=host, port=port)
