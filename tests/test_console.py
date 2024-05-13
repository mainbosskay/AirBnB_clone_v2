#!/usr/bin/python3
"""Unittest module for console.py has been established"""
import unittest
import json
import models
import MySQLdb
from os import getenv
from io import StringIO
from models import storage
from unittest.mock import patch
from sqlalchemy.exc import OperationalError
from console import HBNBCommand
from tests.__init__ import clearfilecontents


class TestHBNBCommand(unittest.TestCase):
    """Unittest for the HBNBCommand class is defined"""
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def testcreateFS(self):
        """test 'create' command with FileStorage"""
        with patch('sys.stdout', new=StringIO()) as result:
            cmdinterp = HBNBCommand()
            cmdinterp.onecmd('create City name="Chicago"')
            expctmsg = result.getvalue().strip()
            clearfilecontents(result)
            self.assertIn(f'City.{expctmsg}', storage.all().keys())
            cmdinterp.onecmd(f'show City {expctmsg}')
            self.assertIn("'name': 'Chicago'", result.getvalue().strip())
            clearfilecontents(result)
            cmdinterp.onecmd('create User name="Jide" age=30 height=6.1')
            expctmsg = result.getvalue().strip()
            self.assertIn(f'User.{expctmsg}', storage.all().keys())
            clearfilecontents(result)
            cmdinterp.onecmd(f'show User {expctmsg}')
            self.assertIn("'name': 'Jide'", result.getvalue().strip())
            self.assertIn("'age': 30", result.getvalue().strip())
            self.assertIn("'height': 6.1", result.getvalue().strip())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def testcreateDB(self):
        """test 'create' command with Database Storage"""
        with patch('sys.stdout', new=StringIO()) as result:
            cmdinterp = HBNBCommand()
            with self.assertRaises(OperationalError):
                cmdinterp.onecmd('creatte User')
            clearfilecontents(result)
            cmdinterp.onecmd('create User email="jitu89@a.com" password="j89"')
            expctmsg = result.getvalue().strip()
            dbconnct = MySQLdb.connect(
                    user=getenv('HBNB_MYSQL_USER'),
                    passwd=getenv('HBNB_MYSQL_PWD'),
                    host=getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    dbname=getenv('HBNB_MYSQL_DB')
            )
            dbcurrnt = dbconnct.cursor()
            dbquery = f'SELECT * FROM users WHERE id="{expctmsg}"'
            dbcurrnt.execute(dbquery)
            quryres = dbcurrnt.fetchone()
            self.assertTrue(quryres is not None)
            self.assertIn('jitu89@a.com', quryres)
            self.assertIn('j89', quryres)
            dbcurrnt.close()
            dbconnct.close()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def testshowDB(self):
        """test 'show' command with Database Storage"""
        with patch('sys.stdout', new=StringIO()) as res:
            cmdinterp = HBNBCommand()
            usrinst = User(email="jitu89@gmail.com", password="j1tu89")
            dbconnct = MySQLdb.connect(
                    user=getenv('HBNB_MYSQL_USER'),
                    passwd=getenv('HBNB_MYSQL_PWD'),
                    host=getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    dbname=getenv('HBNB_MYSQL_DB')
            )
            dbcurrnt = dbconnct.cursor()
            dbquery = f'SELECT * FROM users WHERE id="{usrinst.id}"'
            dbcurrnt.execute(dbquery)
            quryres = dbcurrnt.fetchone()
            self.assertTrue(quryres is None)
            cmdinterp.onecmd(f'show User {usrinst.id}')
            self.assertEqual(res.getvalue().strip(), '** no instance found **')
            usrinst.save()
            dbconnct = MySQLdb.connect(
                    user=getenv('HBNB_MYSQL_USER'),
                    passwd=getenv('HBNB_MYSQL_PWD'),
                    host=getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    dbname=getenv('HBNB_MYSQL_DB')
            )
            dbcurrnt = dbconnct.cursor()
            dbquery = f'SELECT * FROM users WHERE id="{usrinst.id}"'
            dbcurrnt.execute(dbquery)
            clearfilecontents(res)
            cmdinterp.onecmd(f'show User {usrinst.id}')
            quryres = dbcurrnt.fetchone()
            self.assertTrue(quryres is not None)
            self.assertIn('jitu89@gmail.com', quryres)
            self.assertIn('j1tu89', quryres)
            self.assertIn('jitu89@gmail.com', res.getvalue())
            self.assertIn('j1tu89', res.getvalue())
            dbcurrnt.close()
            dbconnct.close()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def testcountDB(self):
        """test 'count' command with Database Storage"""
        with patch('sys.stdout', new=StringI0()) as result:
            cmdinterp = HBNBCommand()
            dbconnct = MySQLdb.connect(
                    user=getenv('HBNB_MYSQL_USER'),
                    passwd=getenv('HBNB_MYSQL_PWD'),
                    host=getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    dbname=getenv('HBNB_MYSQL_DB')
            )
            dbcurrnt = dbconnct.cursor()
            dbquery = f'SELECT COUNT(*) FROM states;'
            dbcurrnt.execute(dbquery)
            quryres = dbcurrnt.fetchone()
            prevcnt = int(quryres[0])
            cmdinterp.onecmd('create State name="Enugu"')
            clearfilecontents(result)
            cmdinterp('count State')
            newcnt = result.getvalue().strip()
            self.assertEqual(int(newcnt), prevcnt + 1)
            clearfilecontents(result)
            cmdinterp.onecmd('count State')
            dbcurrnt.close()
            dbconnct.close()
