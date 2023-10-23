import yaml

class Node:
    with open('config/c3dc-model.yml', 'r') as file:
        _NODEDEFS = yaml.safe_load(file)['Nodes']
    with open('config/c3dc-model-props.yml', 'r') as file:
        _PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    _ENUMS = {}
    _PROPER_NAMES = {}
    _REQS = {}
    _TYPES = {}
    _TYPE_MAP = {
        'integer': int,
        'string': str,
    }

    def _determine_attr_type(yaml_node):
        if not 'Type' in yaml_node.keys():
            raise ValueError(f'Invalid typing in Model Description YAML')
        else:
            type_desc = yaml_node['Type']

            if isinstance(type_desc, str):
                if not type_desc in Node._TYPE_MAP:
                    raise LookupError(f'Unexpected type')
                else:
                    return Node._TYPE_MAP[type_desc]
            # From here on, we expect to be working with a dict
            # elif not isinstance(type_desc, dict):
            elif not isinstance(type_desc, dict):
                raise ValueError(f'Invalid typing in Model Description YAML')
            elif not 'enum' in (item.lower() for item in type_desc.keys()):
                raise ValueError(f'Invalid typing in Model Description YAML')
            else:
                return 'enum'

    # Figures out whether an attribute has prescribed values
    # If so, then returns the list of prescribed values
    # If not, then returns false
    def _determine_attr_enum(self, yaml_node):
        type = self._determine_attr_type(yaml_node)

        if type != 'enum':
            raise TypeError(f'Attribute is not an enum')
        else:
            return yaml_node['Type']['Enum']

    def _validate_attr(self, attr_name, value):
        enum = self._ENUMS.get(attr_name, False) or None
        is_required = self._REQS[attr_name]
        # type = Node._TYPE_MAP[self._TYPES[attr_name]]
        type = Node._determine_attr_type(self._PROPDEFS[attr_name])

        if is_required and value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        if is_required and type == str and value == '':
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        # We don't have to check the type of an enum, because it must match one of the prescribed values anyway
        if type != 'enum' and not isinstance(value, type) and not value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be of type {type}')

        if not enum is None and value not in enum:
            raise ValueError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be one of the specified values')

class Participant(Node):
    _ENUMS = {
        'ethnicity': Node._PROPDEFS['ethnicity']['Type']['Enum'],
        'gender': Node._PROPDEFS['gender']['Type']['Enum'],
        'race': Node._PROPDEFS['race']['Type']['Enum'],
    }
    _PROPER_NAMES = {
        'alternate_participant_id': 'Alternate Participant ID',
        'ethnicity': 'Ethnicity',
        'gender': 'Gender',
        'participant_id': 'Participant ID',
        'race': 'Race',
    }
    _REQS = {
        'alternate_participant_id': Node._PROPDEFS['alternate_participant_id']['Req'],
        'ethnicity': Node._PROPDEFS['ethnicity']['Req'],
        'gender': Node._PROPDEFS['gender']['Req'],
        'participant_id': Node._PROPDEFS['participant_id']['Req'],
        'race': Node._PROPDEFS['race']['Req'],
    }
    _TYPES = {
        'alternate_participant_id': Node._PROPDEFS['alternate_participant_id']['Type'],
        'ethnicity': 'string',
        'gender': 'string',
        'participant_id': 'string',
        'race': 'string',
    }

    def __init__(self, alternate_participant_id, ethnicity, gender, participant_id, race, model_file_path=None, props_file_path=None):
        self.alternate_participant_id = alternate_participant_id or None
        self.ethnicity = ethnicity or None
        self.gender = gender or None
        self.participant_id = participant_id or None
        self.race = race or None

        if (not model_file_path is None):
            with open(model_file_path, 'r') as file:
                self._NODEDEFS = yaml.safe_load(file)['Nodes']

        if (not props_file_path is None):
            with open(props_file_path, 'r') as file:
                self._PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    def __str__(self):
        return ' | '.join([
            self._participant_id or '',
            self._alternate_participant_id or '',
            self._gender or '',
            self._ethnicity or '',
            self._race or '',
        ])

    @property
    def alternate_participant_id(self):
        return self._alternate_participant_id

    @alternate_participant_id.setter
    def alternate_participant_id(self, value):
        self._validate_attr('alternate_participant_id', value)
        self._alternate_participant_id = value

    @property
    def ethnicity(self):
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, value):
        self._validate_attr('ethnicity', value)
        self._ethnicity = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._validate_attr('gender', value)
        self._gender = value

    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._validate_attr('participant_id', value)
        self._participant_id = value

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._validate_attr('race', value)
        self._race = value

    def to_list(self):
        return [
            'participant',
            self._participant_id,
            self._race,
            self._gender,
            self._ethnicity,
            self._alternate_participant_id,
        ]

class Study(Node):
    _ENUMS = {

        'ethnicity': Node._PROPDEFS['ethnicity']['Type']['Enum'],
        'gender': Node._PROPDEFS['gender']['Type']['Enum'],
        'race': Node._PROPDEFS['race']['Type']['Enum'],
    }
    _REQS = {
        'acl': Node._PROPDEFS['acl']['Req'],
        'consent': Node._PROPDEFS['consent']['Req'],
        'consent_number': Node._PROPDEFS['consent_number']['Req'],
        'external_url': Node._PROPDEFS['external_url']['Req'],
        'phs_accession': Node._PROPDEFS['phs_accession']['Req'],
        'study_acronym': Node._PROPDEFS['study_acronym']['Req'],
        'study_description': Node._PROPDEFS['study_description']['Req'],
        'study_id': Node._PROPDEFS['study_id']['Req'],
        'study_name': Node._PROPDEFS['study_name']['Req'],
        'study_short_title': Node._PROPDEFS['study_short_title']['Req'],
    }
    _TYPES = {
        'acl': Node._PROPDEFS['acl']['Type'],
        'consent': Node._PROPDEFS['consent']['Type'],
        'consent_number': Node._PROPDEFS['consent_number']['Type'],
        'external_url': Node._PROPDEFS['external_url']['Type'],
        'phs_accession': Node._PROPDEFS['phs_accession']['Type'],
        'study_acronym': Node._PROPDEFS['study_acronym']['Type'],
        'study_description': Node._PROPDEFS['study_description']['Type'],
        'study_id': Node._PROPDEFS['study_id']['Type'],
        'study_name': Node._PROPDEFS['study_name']['Type'],
        'study_short_title': Node._PROPDEFS['study_short_title']['Type'],
    }

    def __init__(self, acl, consent, consent_number, external_url,
            phs_accession, study_acronym, study_description,
            study_id, study_name, study_short_title):
        self.acl = acl or ''
        self.consent = consent or ''
        self.consent_number = consent_number or ''
        self.external_url = external_url or ''
        self.phs_accession = phs_accession or ''
        self.study_acronym = study_acronym or ''
        self.study_description = study_description or ''
        self.study_id = study_id or ''
        self.study_name = study_name or ''
        self.study_short_title = study_short_title or ''

    def __str__(self):
        return ' | '.join([
            self.acl,
            self.consent,
            self.consent_number,
            self.external_url,
            self.phs_accession,
            self.study_acronym,
            self.study_description,
            self.study_id,
            self.study_name,
            self.study_short_title,
        ])

    @property
    def acl(self):
        return self._acl

    @acl.setter
    def acl(self, value):
        is_required = self._REQS['acl']
        type = Node._TYPE_MAP[self._TYPES['acl']]

        if is_required and value is None:
            raise TypeError(f'ACL is missing')
        elif not isinstance(value, type):
            raise TypeError(f'ACL `{value}` must be of type <{type}>')
        else:
            self._acl = value

    @property
    def consent(self):
        return self._consent

    @consent.setter
    def consent(self, value):
        is_required = self._REQS['consent']
        type = Node._TYPE_MAP[self._TYPES['consent']]

        if is_required and value is None:
            raise TypeError(f'Consent is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Consent `{value}` must be of type <{type}>')
        else:
            self._consent = value

    @property
    def consent_number(self):
        return self._consent

    @consent_number.setter
    def consent_number(self, value):
        is_required = self._REQS['consent_number']
        type = Node._TYPE_MAP[self._TYPES['consent_number']]

        if is_required and value is None:
            raise TypeError(f'Consent Number is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Consent Number `{value}` must be of type <{type}>')
        else:
            self._consent_number = value

    @property
    def external_url(self):
        return self._external_url

    @external_url.setter
    def external_url(self, value):
        is_required = self._REQS['external_url']
        type = Node._TYPE_MAP[self._TYPES['external_url']]

        if is_required and value is None:
            raise TypeError(f'External URL is missing')
        elif not isinstance(value, type):
            raise TypeError(f'External URL `{value}` must be of type <{type}>')
        else:
            self._external_url = value

    @property
    def phs_accession(self):
        return self._phs_accession

    @phs_accession.setter
    def phs_accession(self, value):
        is_required = self._REQS['phs_accession']
        type = Node._TYPE_MAP[self._TYPES['phs_accession']]

        if is_required and value is None:
            raise TypeError(f'PHS Accession is missing')
        elif not isinstance(value, type):
            raise TypeError(f'PHS Accession `{value}` must be of type <{type}>')
        else:
            self._phs_accession = value

    @property
    def study_acronym(self):
        return self._study_acronym

    @study_acronym.setter
    def study_acronym(self, value):
        is_required = self._REQS['study_acronym']
        type = Node._TYPE_MAP[self._TYPES['study_acronym']]

        if is_required and value is None:
            raise TypeError(f'Study Acronym is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Study Acronym `{value}` must be of type <{type}>')
        else:
            self._study_acronym = value

    @property
    def study_description(self):
        return self._study_description

    @study_description.setter
    def study_description(self, value):
        is_required = self._REQS['study_description']
        type = Node._TYPE_MAP[self._TYPES['study_description']]

        if is_required and value is None:
            raise TypeError(f'Study Description is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Study Description `{value}` must be of type <{type}>')
        else:
            self._study_description = value

    @property
    def study_id(self):
        return self._study_id

    @study_id.setter
    def study_id(self, value):
        is_required = self._REQS['study_id']
        type = Node._TYPE_MAP[self._TYPES['study_id']]

        if is_required and value is None:
            raise TypeError(f'Study ID is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Study ID `{value}` must be of type <{type}>')
        else:
            self._study_id = value

    @property
    def study_name(self):
        return self._study_name

    @study_name.setter
    def study_name(self, value):
        is_required = self._REQS['study_name']
        type = Node._TYPE_MAP[self._TYPES['study_name']]

        if is_required and value is None:
            raise TypeError(f'Study Name is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Study Name `{value}` must be of type <{type}>')
        else:
            self._study_name = value

    @property
    def study_short_title(self):
        return self._study_short_title

    @study_short_title.setter
    def study_short_title(self, value):
        is_required = self._REQS['study_short_title']
        type = Node._TYPE_MAP[self._TYPES['study_short_title']]

        if is_required and value is None:
            raise TypeError(f'Study Short Title is missing')
        elif not isinstance(value, type):
            raise TypeError(f'Study Short Title `{value}` must be of type <{type}>')
        else:
            self._study_short_title = value

    def to_list(self):
        return [
            'study',
            self.study_id,
            self.phs_accession,
            self.acl,
            self.study_name,
            self.study_short_title,
            self.study_acronym,
            self.study_description,
            self.consent,
            self.consent_number,
            self.external_url,
        ]
