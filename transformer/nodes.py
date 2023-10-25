import yaml

class Node:
    with open('config/c3dc-model.yml', 'r') as file:
        _NODEDEFS = yaml.safe_load(file)['Nodes']
    with open('config/c3dc-model-props.yml', 'r') as file:
        _PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    _PROPER_NAMES = {}
    _TYPE_MAP = {
        'integer': int,
        'string': str,
    }

    # Figures out whether an attribute has prescribed values
    # If so, then returns the list of prescribed values
    # If not, then returns false
    def _determine_attr_enum(self, yaml_node):
        type = self._determine_attr_type(yaml_node)

        if type != 'enum':
            raise TypeError('Attribute is not an enum')
        else:
            return yaml_node['Type']['Enum']
    
    # Returns a boolean indicating whether the attribute is required
    def _determine_attr_req(self, yaml_node):
        if not 'Req' in yaml_node.keys():
            raise ValueError('Missing `Req` field in Model Description YAML')
        else:
            return yaml_node['Req']

    # Figures out the type of an attribute
    # If it's not an enum, then returns a Python type
    # If it's an enum, then returns the string 'enum'
    def _determine_attr_type(self, yaml_node):
        if not 'Type' in yaml_node.keys():
            raise ValueError('Invalid typing in Model Description YAML')
        else:
            type_desc = yaml_node['Type']

            if isinstance(type_desc, str):
                if not type_desc in self._TYPE_MAP:
                    raise LookupError('Unexpected type')
                else:
                    return self._TYPE_MAP[type_desc]
            # From here on, we expect to be working with a dict
            # elif not isinstance(type_desc, dict):
            elif not isinstance(type_desc, dict):
                raise ValueError('Invalid typing in Model Description YAML')
            elif not 'enum' in (item.lower() for item in type_desc.keys()):
                raise ValueError('Invalid typing in Model Description YAML')
            else:
                return 'enum'

    def _validate_attr(self, attr_name, value):
        enum = None
        is_required = self._determine_attr_req(self._PROPDEFS[attr_name])
        type = self._determine_attr_type(self._PROPDEFS[attr_name])

        if type == 'enum':
            enum = self._determine_attr_enum(self._PROPDEFS[attr_name])

        if is_required and value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        if is_required and type == str and value == '':
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        # We don't have to check the type of an enum, because it must match one of the prescribed values anyway
        if type != 'enum' and not isinstance(value, type) and not value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be of type {type}')

        if not enum is None and value not in enum:
            raise ValueError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be one of the specified values')

    # Combine data with an existing Node
    def merge(other_node):
        pass

class Participant(Node):
    _PROPER_NAMES = {
        'alternate_participant_id': 'Alternate Participant ID',
        'ethnicity': 'Ethnicity',
        'gender': 'Gender',
        'participant_id': 'Participant ID',
        'race': 'Race',
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
    _PROPER_NAMES = {
        'acl': 'ACL',
        'consent': 'Consent',
        'consent_number': 'Consent Number',
        'external_url': 'External URL',
        'phs_accession': 'PHS Accession',
        'study_acronym': 'Study Acronym',
        'study_description': 'Study Description',
        'study_id': 'Study ID',
        'study_name': 'Study Name',
        'study_short_title': 'Study Short Title',
    }

    def __init__(self, acl, consent, consent_number, external_url,
            phs_accession, study_acronym, study_description,
            study_id, study_name, study_short_title):
        self.acl = acl or None
        self.consent = consent or None
        self.consent_number = consent_number or None
        self.external_url = external_url or None
        self.phs_accession = phs_accession or None
        self.study_acronym = study_acronym or None
        self.study_description = study_description or None
        self.study_id = study_id or None
        self.study_name = study_name or None
        self.study_short_title = study_short_title or None

    def __str__(self):
        return ' | '.join([
            self._acl,
            self._consent,
            self._consent_number,
            self._external_url,
            self._phs_accession,
            self._study_acronym,
            self._study_description,
            self._study_id,
            self._study_name,
            self._study_short_title,
        ])

    @property
    def acl(self):
        return self._acl

    @acl.setter
    def acl(self, value):
        self._validate_attr('acl', value)
        self._acl = value

    @property
    def consent(self):
        return self._consent

    @consent.setter
    def consent(self, value):
        self._validate_attr('consent', value)
        self._consent = value

    @property
    def consent_number(self):
        return self._consent_number

    @consent_number.setter
    def consent_number(self, value):
        self._validate_attr('consent_number', value)
        self._consent_number = value

    @property
    def external_url(self):
        return self._external_url

    @external_url.setter
    def external_url(self, value):
        self._validate_attr('external_url', value)
        self._external_url = value

    @property
    def phs_accession(self):
        return self._phs_accession

    @phs_accession.setter
    def phs_accession(self, value):
        self._validate_attr('phs_accession', value)
        self._phs_accession = value

    @property
    def study_acronym(self):
        return self._study_acronym

    @study_acronym.setter
    def study_acronym(self, value):
        self._validate_attr('study_acronym', value)
        self._study_acronym = value

    @property
    def study_description(self):
        return self._study_description

    @study_description.setter
    def study_description(self, value):
        self._validate_attr('study_description', value)
        self._study_description = value

    @property
    def study_id(self):
        return self._study_id

    @study_id.setter
    def study_id(self, value):
        self._validate_attr('study_id', value)
        self._study_id = value

    @property
    def study_name(self):
        return self._study_name

    @study_name.setter
    def study_name(self, value):
        self._validate_attr('study_name', value)
        self._study_name = value

    @property
    def study_short_title(self):
        return self._study_short_title

    @study_short_title.setter
    def study_short_title(self, value):
        self._validate_attr('study_short_title', value)
        self._study_short_title = value

    def merge(self, other_study):
        # Make sure that they share identifiers
        if (self.study_id != other_study.study_id):
            raise ValueError("Studies have different ID's")
        
        for participant_id in other_study._participant_ids:
            if participant_id not in self._participant_ids:
                self._participant_ids.append(participant_id)

    def to_list(self):
        return [
            'study',
            self._study_id,
            self._phs_accession,
            self._acl,
            self._study_name,
            self._study_short_title,
            self._study_acronym,
            self._study_description,
            self._consent,
            self._consent_number,
            self._external_url,
        ]
