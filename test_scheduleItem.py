# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Alexander Alemayhu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import frikanalen

from unittest import TestCase


class TestScheduleItem(TestCase):
    def test_from_response(self):
        progs = sorted(frikanalen.today_programs())
        for p in progs:
            if p.video is not None:
                print(str(p.video.name.encode('utf-8')))
            print(str(p.starttime))

        assert len(progs) > 0
        frikanalen.whats_on()

