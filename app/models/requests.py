from pydantic import BaseModel, root_validator

from app.resources.utils import str_to_isoformat


class MeasurementRequest(BaseModel):
    # API expects a json object like:
    start_time: str  # YYYY-MM-DDThh:mm:ss+00:00
    stop_time: str  # YYYY-MM-DDThh:mm:ss+00:00

    @root_validator(pre=True)
    def check_required_items(cls, values):

        start_time = values.get("start_time")
        stop_time = values.get("stop_time")

        if not start_time:
            raise ValueError("Field 'start_time' required")
        if not stop_time:
            raise ValueError("Field 'end_time' required")
        if not isinstance(start_time, str):
            raise ValueError("Field 'start_time' must be a str")
        str_to_isoformat(start_time)
        if not isinstance(stop_time, str):
            raise ValueError("Field 'stop_time' must be a str")
        str_to_isoformat(stop_time)

        return values


class TextRequest(BaseModel):
    # API expects a json object like:
    channel_id: str  # welo channel to search in
    start_time: str  # YYYY-MM-DDThh:mm:ss+00:00.
    stop_time: str  # YYYY-MM-DDThh:mm:ss+00:00.
    text: str  # to search

    @root_validator(pre=True)
    def check_required_items(cls, values):

        channel_id = values.get("channel")
        start_time = values.get("start_time")
        stop_time = values.get("stop_time")
        text = values.get("text")

        if not channel_id:
            raise ValueError("Field 'channel_id' required")
        if not isinstance(channel_id, str):
            raise ValueError("Field 'channel_id' must be a str")
        if not start_time:
            raise ValueError("Field 'start_time' required")
        if not isinstance(start_time, str):
            raise ValueError("Field 'start_time' must be a str")
        str_to_isoformat(start_time)

        if not stop_time:
            raise ValueError("Field 'end_time' required")
        if not isinstance(stop_time, str):
            raise ValueError("Field 'stop_time' must be a str")
        str_to_isoformat(stop_time)

        if not text:
            raise ValueError("Field 'text' required")
        if not isinstance(text, str):
            raise ValueError("Field 'text' must be a str")
        return values
