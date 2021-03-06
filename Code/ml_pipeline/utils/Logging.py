import logging
import os
#
logger = logging.getLogger('main_logger')
if len(logger.handlers) == 0:
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

def get_job_logger(job_log_fld):
    jlogger = logging.getLogger("job_logger")

    if len(jlogger.handlers) == 0:
        jlogger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

        debug_log_fp = os.path.join(job_log_fld, 'run_debug.log')
        fh_debug = logging.FileHandler(debug_log_fp)
        fh_debug.setLevel(logging.DEBUG)
        fh_debug.setFormatter(formatter)
        jlogger.addHandler(fh_debug)

        info_log_fp = os.path.join(job_log_fld, 'run_info.log')
        fh_info = logging.FileHandler(info_log_fp)
        fh_info.setLevel(logging.INFO)
        fh_info.setFormatter(formatter)
        jlogger.addHandler(fh_info)

        error_log_fp = os.path.join(job_log_fld, 'run_error.log')
        fh_error = logging.FileHandler(error_log_fp)
        fh_error.setLevel(logging.ERROR)
        fh_error.setFormatter(formatter)
        jlogger.addHandler(fh_error)

    return jlogger
