from datetime import datetime
from models import *
from services import *
import os

class addAccountBook:

    def setUp(self, name):
        """
        Set up the test environment. Initialize the services and create test data.
        """
        self.cred_path = 'src/Firebase_credit/moneytrackerplus-firebase-adminsdk-aqbar-596c204702.json'
        self.db_url = 'https://moneytrackerplus-default-rtdb.firebaseio.com/'
        self.cloud_service = CloudSyncService(self.cred_path, self.db_url)
        self.file_path = 'test_account_books.json'
        self.data_service = DataService(self.file_path)

        self.account_book = AccountBook(name = name)
        self.cloud_service.upload_account_book(self.account_book)
        return True