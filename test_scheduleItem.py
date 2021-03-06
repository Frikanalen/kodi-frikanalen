#!/usr/bin/python
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
import unittest


class TestScheduleItem(unittest.TestCase):
    def test_from_response(self):
        progs = sorted(frikanalen.today_programs())
        for p in progs:
            if p.video is not None:
                print(str(p.video.name.encode('utf-8')))
            print(str(p.starttime))

        assert len(progs) > 0
        frikanalen.whats_on()

    def test_category_listing(self):
        categories = frikanalen.categories()
        assert 0 < len(categories)
        for category in categories:
            print("Looking up cateogry %s" % category)
            videos = frikanalen.in_category(category)
            assert 0 < len(videos)


    def test_iso_dates(self):
        examples = (
            '2017-04-06T09:11:27+0100',
            '2017-04-06T09:11:27.469588+0100',
            '2017-04-06T09:11:27Z',
            '2017-04-06T09:11:27.469588Z',
        )
        for d in examples:
            conv = frikanalen.iso2datetime(d)

if __name__ == '__main__':
    unittest.main()
