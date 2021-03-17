from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse

from app.models.requests import TextRequest
# from app.resources.settings import apies_logger
# from app.resources.utils import log_event
from app.resources.elasticsearch import es, es_text_index

router = APIRouter()

no_feature_msg = "Search word features is not available yet, " \
                 "please try later."


def elastic_search_words(channel: str, words: str,
                         start_time: str, stop_time: str) -> dict:

    searched_value = words
    hits = []
    searched_timestamp = ''
    previous = ''
    nexts = ''
    total_matches = 0

    es_response = {"search_value": searched_value,
                   "hits": [{
                       "searched_timestamp": searched_timestamp,
                       "previuos": previous,
                       "next": nexts
                   }],
                   "total_matches": total_matches
                   }
    return es_response


@router.get("/words", tags=["words"])
async def read_words(text_request: TextRequest,
                     background_tasks: BackgroundTasks):
    channel = text_request.channel_id
    words = text_request.text
    start_time = text_request.start_time
    stop_time = text_request.stop_time

    es_response = elastic_search_words(channel, words, start_time, stop_time)

    """
    total_matches = es_response['total_matches']
    if total_matches > 0:
        code = 200
        description = f"'{words}' found {total_matches} " \
                      f"times in the {channel} video."
    else:
        code = 404
        description = f"'{words}' was not found in the {channel} video."
    """

    code = 404
    description = no_feature_msg
    es_response = {}

    level = "error" if code == 404 else "info"
    msg = f"HTTP status code {code} - {description} " \
          f"- elasticsearch response {es_response}"

    # background_tasks.add_task(log_event, logger=apies_logger,
    #                           level=level, msg=msg)

    return JSONResponse(
        status_code=code,
        content={"code": code, "description": description,
                 "data": es_response}
    )


@router.get("/words/most-searched ", tags=["words"])
async def read_words_most_searched(background_tasks: BackgroundTasks):
    code = 404
    description = no_feature_msg
    data = {}

    level = "error" if code == 404 else "info"
    msg = f"HTTP status code {code} - {description} " \
          f"- elasticsearch response {data}"

    # background_tasks.add_task(log_event, logger=apies_logger,
    #                          level=level, msg=msg)

    return JSONResponse(
        status_code=code,
        content={"code": code, "description": description, "data": data},
    )
