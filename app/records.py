from contextvars import ContextVar

records = ContextVar("records")
invalid_records = ContextVar("invalid_records")
