from datetime import datetime
from models import *
from services import *
import os

class addTransaction:

    def setUp(self):
        """
        Set up the test environment. Initialize the services and create test data.
        """
        self.cred_path = './Firebase_credit/moneytrackerplus-firebase-adminsdk-aqbar-5c9acd5080.json'
        self.db_url = 'https://moneytrackerplus-default-rtdb.firebaseio.com/'
        self.cloud_service = CloudSyncService(self.cred_path, self.db_url)
        self.file_path = 'test_account_books.json'
        self.data_service = DataService(self.file_path)

        self.transaction = Transaction(
            id=1,
            amount=100.0,
            date=datetime.now(),
            description='Test transaction'
        )
        self.account_book = AccountBook(name='Test Account Book')
        self.account_book.add_transaction(self.transaction)