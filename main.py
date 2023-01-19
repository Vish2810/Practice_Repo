from fastapi import FastAPI, HTTPException
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

sold_epc = ["30361fac68253e4000000024", "30361f6ad811bcc000000001"]
unsold_epc = ["30361f56b40141c000000001", "30361fac682d3340000000f8"]


app = FastAPI(title="Eas Alarm_Count",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/eas/alarm/{epc}", tags=["EAS Alarm"])
def get_alarm_count(epc: str):
    try:
        if epc in sold_epc:
            logger.debug(f'EPC is sold {epc}')
            raise HTTPException(status_code=400)
        elif epc in unsold_epc:
            logger.info(f'EPC is un-sold {epc}', detail=f'epc is Sold')
            raise HTTPException(status_code=200, detail=f'epc is un-sold')
        else:
            logger.critical(f'EPC is un-sold/other {epc}')
            raise HTTPException(status_code=200, detail=f'epc is un-sold')
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f'{e}')
        raise HTTPException(status_code=500, detail=f'Error in get_epc: {e}')


if __name__ == '__main__':
    logger.info("Started main")

    run("main:app", host="0.0.0.0", port=5010, reload=True)
