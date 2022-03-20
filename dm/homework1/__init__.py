from .common import load_data_raw
from .data_digest import data_digest
from .none_value_process import run_contrast


def run_homework_1():
    data = load_data_raw(limit=-1)
    data_digest(data)
    run_contrast(data)
