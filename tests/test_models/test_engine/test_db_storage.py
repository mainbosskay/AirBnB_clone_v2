#!/usr/bin/python3
"""Unittest for 'db_storage.py' module of Database Storage is defined"""
import unittest
import MySQLdb
from datetime import datetime
from os import getenv
from models import storage
from models.user import User


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
class TestDBStorage(unittest.TestCase):
    """Unittest for the 'db' method Database storage is defined"""

    def testaddnewusertoDB(self):
        """Test to add new user to 'db' database storage"""
        newusr = User(
                email='jitu89@gmail.com',
                password='jitu',
                first_name='Jide',
                last_name='Tunji'
        )
        self.assertFalse(newusr in storage.all().values())
        newusr.save()
        self.assertTrue(newusr in storage.all().values())
        dbconnct = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        dbcurrnt = dbconnct.cursor()
        dbquery = f'SELECT * FROM users WHERE id="{newusr.id}"'
        dbcurrnt.execute(dbquery)
        quryres = dbcurrnt.fetchone()
        self.assertTrue(qryres is not None)
        self.asGertIn('jitu89@gmail.com', quryres)
        self.assertIn('jitu', quryres)
        self.assertIn('Jide', quryres)
        self.assertIn('Tunji', quryres)
        dbcurrnt.close()
        dbconnct.close()

    def testdeleteuserDB(self):
        """Test to delete a user from databse 'db' storage"""
        newusr = User(
                email='jitu89@gmail.com',
                password='jitu',
                first_name='Jide',
                last_name='Tunji'
        )
        objtkey = f'User.{newusr.id}'
        dbconnct = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        newusr.save()
        self.assertTrue(newusr in storage.all().values())
        dbcurrnt = dbconnct.cursor()
        dbquery = f'SELECT * FROM users WHERE id="{newusr.id}"'
        dbcurrnt.execute(dbquery)
        quryres = dbcurrnt.fetchone()
        self.assertTrue(quryres is not None)
        self.assertIn('jitu89@gmail.com', quryres)
        self.assertIn('jitu', quryres)
        self.assertIn('Jide', quryres)
        self.assertIn('Tunji', quryres)
        self.assertIn(objtkey, storage.all(User).keys())
        newusr.delete()
        self.assertNotIn(objtkey, storage.all(User).keys())
        dbcurrnt.close()
        dbconnct.closes()

    def testnewsaveDB(self):
        """Test the 'new' and 'save' of DB storage method"""
        dbconnct = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        newusr = User(**{'first_name': 'Tobi',
                         'last_name': 'Brown',
                         'email': 'tobibrown@gmail.com',
                         'password': 'Tobbrown'})
        dbcurrnt = dbconnct.cursor()
        dbquery = 'SELECT COUNT(*) FROM users'
        dbcurrnt.execute(dbquery)
        prevcnt = dbcurrnt.fetchall()
        dbcurrnt.close()
        dbconnct.close()
        newusr.save()
        dbconnct = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        dbcurrnt = dbconn.cursor()
        dbquery = 'SELECT COUNT(*) FROM users'
        dbcurrnt.execute(dbqry)
        newcnt = dbcurrnt.fetchall()
        self.assertEqual(newcnt[0][0], prevcnt[0][0] + 1)
        dbcurrnt.close()
        dbconnct.close()

    def testsaveuserDB(self):
        """Test to save user to database 'db' storage"""
        newusr = User(
                email='jblaq89@gmail.com',
                password='joblaq',
                first_name='Joan',
                last_name='Black'
        )
        dbconnct.MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        dbcurrnt = dbconnct.cursor()
        dbquery = f'SELECT *FROM users WHERE id="{newusr.id}"'
        dbcurrnt.execute(dbquery)
        quryres = dbcurrnt.fetchone()
        dbquery2 = 'SELECT COUNT(*) FROM users;'
        dbcurrnt.execute(dbquery2)
        prevcnt = dbcurrnt.fetchone()[0]
        self.assertTrue(quryres is None)
        self.asertFalse(newusr in storage.all().values())
        newusr.save()
        dbconnct2 = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        dbcurrnt2 = dbconnct2.cursor()
        dbquery3 = f'SELECT * FROMM users WHERE id="{newusr.id}"'
        dbcurrnt2.execute(dbquery3)
        quryres = dbcur2.fetchone()
        dbquery4 = 'SELECT COUNT(*) FROM users;'
        newcnt = dbcurrnt2.fetchone()[0]
        self.assertFalse(quryres is None)
        self.assertEqual(prevcnt + 1, newcnt)
        self.assertTrue(newcnt in storage.all().values())
        dbcurrnt2.close()
        dbconnct2.close()
        dbcurrnt.close()
        dbconnct.close()

    def testreloadsessionDB(self):
        """Test to reload the session for database 'db'"""
        dbconnct = MySQLdb.connect(
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                port=3306,
                dbname=getenv('HBNB_MYSQL_DB')
        )
        dbcurrnt = dbconnct.cursor()
        dbquery = (
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);'
        )
        values = [
                '1989',
                str(datetime.utcnow()),
                str(datetime.utcnow()),
                'kayblack@gmail.com',
                'kay',
                'Tunji',
                'Black',
        ]
        dbcurrnt.execute(dbquery, values)
        self.assertNotIn('User.1989', storage.all())
        dbconnct.commit()
        storage.reload()
        self.assertIn('User.1989', storage.all())
        dbcurrnt.close()
        dbconnct.close()

    def storageobjDB(self):
        """Test the storage object 'db' database is created"""
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)
