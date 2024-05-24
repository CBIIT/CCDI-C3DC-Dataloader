# Generates a Version 5 UUID

import uuid

def make_uuid(node_type, study_id, record_id):
    uuid_name = "".join([
        node_type,
        study_id,
        record_id
    ])

    return str(uuid.uuid5(uuid.NAMESPACE_URL, uuid_name))
