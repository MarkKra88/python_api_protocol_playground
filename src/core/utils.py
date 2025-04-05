import logging
import json
import uuid
import inspect
from functools import wraps
from datetime import datetime

# Error log config
logging.basicConfig(
    level=logging.ERROR,
    format='%(message)s'
)

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler("app_errors.log")
error_formatter = logging.Formatter('%(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
error_logger.propagate = False

input_logger = logging.getLogger("input_logger")
input_logger.setLevel(logging.INFO)
input_handler = logging.FileHandler("app_input.log")
input_formatter = logging.Formatter('%(message)s')
input_handler.setFormatter(input_formatter)
input_logger.addHandler(input_handler)
input_logger.propagate = False

def log_input():
    """
    Decorator to log function input to app_input.log
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            trace_id = str(uuid.uuid4())
            timestamp = datetime.now().isoformat()
            module = func.__module__
            func_name = func.__name__

            try:
                arg_names = inspect.getfullargspec(func).args
                input_data = dict(zip(arg_names, args))
                input_data.update(kwargs)
            except Exception:
                input_data = "Unavailable"

            log_entry = {
                "timestamp": timestamp,
                "trace_id": trace_id,
                "module": module,
                "function": func_name,
                "input": input_data
            }

            # Attach trace_id to function call for error logging
            wrapper._trace_id = trace_id
            wrapper._input_data = input_data

            input_logger.error(json.dumps(log_entry))

            return func(*args, **kwargs)
        return wrapper
    return decorator

def log_errors(func):
    """
    Decorator to catch, log, and structure any error raised by the wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            timestamp = datetime.now().isoformat()
            module = func.__module__
            func_name = func.__name__

            # Extract clean error info
            error_type = type(e).__name__
            error_msg = str(e).replace("\n", " ").replace("\r", "")

            trace_id = getattr(wrapper, "_trace_id", str(uuid.uuid4()))
            input_data = getattr(wrapper, "_input_data", "Unavailable")

            log_entry = {
                "timestamp": timestamp,
                "type": "ERROR",
                "trace_id": trace_id,
                "file": module,
                "function": func_name,
                "error_short": error_type,
                "error_message": error_msg,
                "input": input_data
            }

            error_logger.error(json.dumps(log_entry))
            print("⚠️  An error occurred. Please check the log (app_errors.log).")
    return wrapper