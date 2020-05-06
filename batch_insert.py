import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



class FirestorePush:
    def __init__(self):
        # Login with your Firestore credentials
        cred = credentials.Certificate('./data/firebasekey.json')
        self.db_admin = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        # My sample DB
        with open('./data/areas_data.json', 'r') as f:
            self.records_db = json.load(f)

    # Method to push bulk records to Firestore
    def push(self):
        # Get a ref to Firestore database.
        records_collection = self.db.collection('academic-areas')
        
        # This is just for logging purposes.        
        total = len(self.records_db)
        idx = 0
        
        # Start a batch
        batch = self.db.batch()
        for record in self.records_db:
            
            # Commit the batch at every 500th record.
            if idx % 500 == 0:
                if idx > 0:
                    print('Committing..')
                    batch.commit()
                    
                # Start a new batch for the next iteration.
                batch = self.db.batch()
            idx += 1
            print(str(idx) + str('/') + str(total) + ': ' + str(record['id']))
            record_ref = records_collection.document(record['id'])
            # Include current record in batch
            batch.set(record_ref, record)
        # Include current record in batch
        if idx % 500 != 0:
            print('Committing..')
            batch.commit()
if __name__ == '__main__':
    f = FirestorePush()
    f.push()