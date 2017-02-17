import frikanalen

from unittest import TestCase


class TestScheduleItem(TestCase):
    def test_from_response(self):
        progs = frikanalen.today_programs().sort()
        assert len(progs) > 0

