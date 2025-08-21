from pydantic import BaseModel
from typing import Optional


class StreamDelta(BaseModel):
    """
    Delta containing incremental changes in a streaming response.
    
    Parameters
    ----------
    text: `str`, optional
        Incremental text content
    """
    text: Optional[str] = None


class StreamChunk(BaseModel):
    """
    A single chunk from the streaming response.
    
    Parameters
    ----------
    rcid: `str`, optional
        Reply candidate ID for this chunk
    delta: `StreamDelta`
        The incremental content changes
    finish_reason: `str`, optional
        Reason why the stream finished (if applicable)
    """
    rcid: Optional[str] = None
    delta: StreamDelta
    finish_reason: Optional[str] = None