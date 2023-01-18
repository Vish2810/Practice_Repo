from http.client import HTTPException

from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

# from src.route.all_routes import router as all_routes

app = FastAPI(
    title="Eas Alarm_Count",

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


# app.include_router(all_routes)


@app.get("/eas/alarm/{epc}", tags=["EAS Alarm"])
def get_alarm_count(
        epc: str

):
    try:
        logger.debug(epc)
        if epc == '0000000000000000000001e1':
            raise HTTPException(status_code=400, detail=f'epc is not valid {epc}')
        return epc

    except HTTPException as e:
        logger.debug(f'{e}')
        raise e
    except Exception as e:
        logger.debug(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')

    # @app.on_event("startup")


# async def init_processes():
#     start_new_thread(stock_take_processing_thread, ())
#     pass

if __name__ == '__main__':
    logger.info("Started main")

    run("main:app", host="0.0.0.0", port=5010, reload=True)
