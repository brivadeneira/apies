from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse

from app.models.requests import MeasurementRequest
from app.resources.elasticsearch import es, es_mon_index
# from app.resources.settings import apies_logger
# from app.resources.utils import log_event

router = APIRouter()


@router.get("/measurements/all", tags=["measurements"])
async def read_measurements(background_tasks: BackgroundTasks):
    es_response = await es.search(
        index=es_mon_index,
        body={"query": {"match_all": {}}},
    )
    if es_response["hits"]["total"]["value"] > 0:
        status_code, code = status.HTTP_200_OK, 200
        description, data = "measurements found", es_response
    else:
        status_code, code = status.HTTP_404_NOT_FOUND, 404
        description, data = "measurements not found", {}

    level = "error" if code == 404 else "info"
    msg = f"HTTP status code {code} - {description} "\
          f"- elasticsearch response {data}"

    # background_tasks.add_task(log_event, logger=apies_logger,
    #                          level=level, msg=msg)

    return JSONResponse(
        status_code=status_code,
        content={"code": code, "description": description, "data": data},
    )


@router.post("/measurements", tags=["measurements"])
async def read_measurements_range(
    measure_request: MeasurementRequest, background_tasks: BackgroundTasks
):
    es_response = await es.search(
        index=es_mon_index,
        body={
            "query": {
                "range": {
                    "measurement_time": {
                        "gte": measure_request.start_time,
                        "lte": measure_request.stop_time,
                    }
                }
            }
        },
    )
    if es_response["hits"]["total"]["value"] > 0:
        status_code, code = status.HTTP_200_OK, 200
        description = (
            f"measurements found in range "
            f"{measure_request.start_time} "
            f"to {measure_request.stop_time}"
        )
        data = es_response
    else:
        status_code, code = status.HTTP_404_NOT_FOUND, 404
        description, data = (
            f"measurements not found in range "
            f"{measure_request.start_time} "
            f"to {measure_request.stop_time}",
            {},
        )

    level = "error" if code == 404 else "info"
    msg = f"HTTP status code {code} - {description} " \
          f"- elasticsearch response {data}"

    # background_tasks.add_task(log_event, logger=apies_logger,
    #                          level=level, msg=msg)

    return JSONResponse(
        status_code=status_code,
        content={"code": code, "description": description, "data": data},
    )
