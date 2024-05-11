from abc import ABC

import pytest

from config import DATA
from src.GetAPIHH import GetApiHh
from src.AbstractApiHH import AbstractGetApiHh


def test_issubclass():
    assert issubclass(AbstractGetApiHh, ABC)
    assert issubclass(GetApiHh, AbstractGetApiHh)


def test_get_vacancy_from_api():
    vacancy1 = GetApiHh('tttttt')
    vacancy2 = GetApiHh(1)
    vacancy3 = GetApiHh('python')

    vacancy1.get_vacancy_from_api()
    vacancy2.get_vacancy_from_api()
    vacancy3.get_vacancy_from_api()

    assert vacancy1.message == "Vacancies found"
    assert vacancy2.message == "Vacancy not found"
    assert vacancy3.message == "Vacancies found"


def test_save_info_valid():
    vacancy1 = GetApiHh('python')

    assert isinstance(vacancy1.all_vacancy, list)
    assert len(vacancy1.all_vacancy) > 0


def test_save_info_zero_len():
    vacancy1 = GetApiHh(1)

    assert vacancy1.save_info() == "Vacancy not found"