from api.lib.db import conn, cursor
from api.lib.orm import build_from_record, build_from_records, save
import api.models as models


class Candidate:

    columns = ['id', 'locality_name', 'office_title', 'jurisdiction_on_ballot', 'incumbent', 'candidate_name', 'candidate_status', 'campaign_address_line1', 'campaign_address_line2', 'campaign_city', 'campaign_state', 'campaign_zip', 'campaign_email', 'campaign_website' ]

    __table__ = 'candidates'

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_id(self, id, cursor):
        cursor.execute('SELECT * FROM candidates WHERE id = %s', (id,))
        record = cursor.fetchone()
        if not record: 
            return None
        else:
            return build_from_record(Vehicle, record)

