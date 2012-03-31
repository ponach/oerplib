# -*- coding: UTF-8 -*-

import unittest

from args import ARGS

import oerplib


class TestInit(unittest.TestCase):

    def test_init1(self):
        # Server
        oerp = oerplib.OERP(ARGS.server)
        self.assertIsInstance(oerp, oerplib.OERP)
        self.assertIsNotNone(oerp)
        self.assertEqual(oerp.server, ARGS.server)
        self.assertIsNone(oerp.database)

    def test_init2(self):
        # Server + Database
        oerp = oerplib.OERP(ARGS.server, ARGS.database)
        self.assertIsInstance(oerp, oerplib.OERP)
        self.assertIsNotNone(oerp)
        self.assertEqual(oerp.server, ARGS.server)
        self.assertEqual(oerp.database, ARGS.database)

    def test_init3(self):
        # Server + Database + Protocol
        oerp = oerplib.OERP(ARGS.server, ARGS.database, ARGS.protocol)
        self.assertIsInstance(oerp, oerplib.OERP)
        self.assertIsNotNone(oerp)
        self.assertEqual(oerp.server, ARGS.server)
        self.assertEqual(oerp.database, ARGS.database)
        self.assertEqual(oerp.protocol, ARGS.protocol)

    def test_init4(self):
        # Server + Database + Protocol + Port
        oerp = oerplib.OERP(ARGS.server, ARGS.database,
                            ARGS.protocol, ARGS.port)
        self.assertIsInstance(oerp, oerplib.OERP)
        self.assertIsNotNone(oerp)
        self.assertEqual(oerp.server, ARGS.server)
        self.assertEqual(oerp.database, ARGS.database)
        self.assertEqual(oerp.protocol, ARGS.protocol)
        self.assertEqual(oerp.port, ARGS.port)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: