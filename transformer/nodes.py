import yaml

class Node:
    with open('config/c3dc-model.yml', 'r') as file:
        _NODEDEFS = yaml.safe_load(file)['Nodes']
    with open('config/c3dc-model-props.yml', 'r') as file:
        _PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    _PROPER_NAMES = {}
    _TYPE_MAP = {
        'integer': int,
        'list': list,
        'string': str,
    }

    # Figures out an attribute's list of prescribed values
    def _determine_attr_enum(self, yaml_node):
        # Early error to catch not being an enum
        if not self._determine_attr_is_enum(yaml_node):
            raise ValueError('Trying to get prescribed values of a non-enum')

        return yaml_node['Type']['Enum']

    # Determines whether an attribute is an enum/list
    def _determine_attr_is_enum(self, yaml_node):
        type_desc = None

        # Early error to catch invalid YAML
        if not 'Type' in yaml_node.keys():
            raise ValueError('Missing `Type` key in Model Description YAML')

        type_desc = yaml_node['Type']

        # Not en enum, because the type is expressed with a string literal
        if isinstance(type_desc, str):
            return False

        # Error if it should be enum but doesn't have an Enum key
        if 'Enum' not in (key for key in type_desc.keys()):
            raise ValueError('Missing `Enum` field in Model Description YAML')

        return True

    # Returns a boolean indicating whether the attribute is required
    def _determine_attr_req(self, yaml_node):
        # Early error to catch invalid YAML
        if not 'Req' in yaml_node.keys():
            raise ValueError('Missing `Req` key in Model Description YAML')

        return yaml_node['Req']

    # Figures out the Python type that an attribute should be
    def _determine_attr_type(self, yaml_node):
        type_literal = None

        # Is not an enum or list
        if not self._determine_attr_is_enum(yaml_node):
            type_literal = yaml_node['Type']
        elif 'value_type' not in (key for key in yaml_node['Type'].keys()):
            raise ValueError('Missing `value_type` field in Model Description YAML')
        elif yaml_node['Type']['value_type'] == 'list':
            type_literal = 'list'
        else:
            type_literal = yaml_node['Type']['value_type']

        # Handle undefined type mapping
        if type_literal not in self._TYPE_MAP.keys():
            raise LookupError(f'No type mapped to string literal {type_literal}')

        return self._TYPE_MAP[type_literal]

    def _validate_attr(self, attr_name, value):
        prop_def = self._PROPDEFS[attr_name]
        is_required = self._determine_attr_req(prop_def)
        type = self._determine_attr_type(prop_def)

        if is_required and value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        if is_required and type == str and value == '':
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        if not is_required and value is None:
            return

        # Check that the value is the right type
        if value is not None and not isinstance(value, type):
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be of type {type}')

        # Checks for enum/list
        if self._determine_attr_is_enum(prop_def):
            enum = self._determine_attr_enum(prop_def)

            # For list
            if type == list and not all(item in enum for item in value):
                raise ValueError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be a subset of the specified values')

            # For enum
            if type != list and value not in enum:
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
            ';'.join(self._race),
            self._gender,
            ';'.join(self._ethnicity),
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

class Diagnosis(Node):
    _PROPER_NAMES = {
        'age_at_diagnosis': 'Age at Diagnosis',
        'anatomic_site': 'Anatomic Site',
        'diagnosis_finer_resolution': 'Diagnosis Finer Resolution',
        'diagnosis_id': 'Diagnosis ID',
        'diagnosis_icd_cm': 'Diagnosis ICD-10-CM',
        'diagnosis_icd_o': 'Diagnosis ICD-O',
        'disease_phase': 'Disease Phase',
        'toronto_childhood_cancer_staging': 'Toronto Childhood Cancer Staging',
        'tumor_grade': 'Tumor Grade',
        'tumor_stage_clinical_m': 'Tumor Clinical M Stage',
        'tumor_stage_clinical_n': 'Tumor Clinical N Stage',
        'tumor_stage_clinical_t': 'Tumor Clinical T Stage',
    }

    def __init__(self, age_at_diagnosis, anatomic_site,
            diagnosis_finer_resolution, diagnosis_icd_cm,
            diagnosis_icd_o, diagnosis_id, disease_phase,
            toronto_childhood_cancer_staging, tumor_grade,
            tumor_stage_clinical_m, tumor_stage_clinical_n,
            tumor_stage_clinical_t):
        self.age_at_diagnosis = age_at_diagnosis or None
        self.anatomic_site = anatomic_site or None
        self.diagnosis_finer_resolution = diagnosis_finer_resolution or None
        self.diagnosis_icd_cm = diagnosis_icd_cm or None
        self.diagnosis_icd_o = diagnosis_icd_o or None
        self.diagnosis_id = diagnosis_id or None
        self.disease_phase = disease_phase or None
        self.toronto_childhood_cancer_staging = toronto_childhood_cancer_staging or None
        self.tumor_grade = tumor_grade or None
        self.tumor_stage_clinical_m = tumor_stage_clinical_m or None
        self.tumor_stage_clinical_n = tumor_stage_clinical_n or None
        self.tumor_stage_clinical_t = tumor_stage_clinical_t or None

    def __str__(self):
        return ' | '.join([
            self._age_at_diagnosis,
            self._anatomic_site,
            self._diagnosis_finer_resolution,
            self._diagnosis_icd_cm,
            self._diagnosis_icd_o,
            self._diagnosis_id,
            self._disease_phase,
            self._toronto_childhood_cancer_staging,
            self._tumor_grade,
            self._tumor_stage_clinical_m,
            self._tumor_stage_clinical_n,
            self._tumor_stage_clinical_t,
        ])

    @property
    def age_at_diagnosis(self):
        return self._age_at_diagnosis

    @age_at_diagnosis.setter
    def age_at_diagnosis(self, value):
        self._validate_attr('age_at_diagnosis', value)
        self._age_at_diagnosis = value

    @property
    def anatomic_site(self):
        return self._anatomic_site

    @anatomic_site.setter
    def anatomic_site(self, value):
        self._validate_attr('anatomic_site', value)
        self._anatomic_site = value

    @property
    def diagnosis_finer_resolution(self):
        return self._diagnosis_finer_resolution

    @diagnosis_finer_resolution.setter
    def diagnosis_finer_resolution(self, value):
        self._validate_attr('diagnosis_finer_resolution', value)
        self._diagnosis_finer_resolution = value

    @property
    def diagnosis_icd_cm(self):
        return self._diagnosis_icd_cm

    @diagnosis_icd_cm.setter
    def diagnosis_icd_cm(self, value):
        self._validate_attr('diagnosis_icd_cm', value)
        self._diagnosis_icd_cm = value

    @property
    def diagnosis_icd_o(self):
        return self._diagnosis_icd_o

    @diagnosis_icd_o.setter
    def diagnosis_icd_o(self, value):
        self._validate_attr('diagnosis_icd_o', value)
        self._diagnosis_icd_o = value

    @property
    def diagnosis_id(self):
        return self._diagnosis_id

    @diagnosis_id.setter
    def diagnosis_id(self, value):
        self._validate_attr('diagnosis_id', value)
        self._diagnosis_id = value

    @property
    def disease_phase(self):
        return self._disease_phase

    @disease_phase.setter
    def disease_phase(self, value):
        self._validate_attr('disease_phase', value)
        self._disease_phase = value

    @property
    def toronto_childhood_cancer_staging(self):
        return self._toronto_childhood_cancer_staging

    @toronto_childhood_cancer_staging.setter
    def toronto_childhood_cancer_staging(self, value):
        self._validate_attr('toronto_childhood_cancer_staging', value)
        self._toronto_childhood_cancer_staging = value

    @property
    def tumor_grade(self):
        return self._tumor_grade

    @tumor_grade.setter
    def tumor_grade(self, value):
        self._validate_attr('tumor_grade', value)
        self._tumor_grade = value

    @property
    def tumor_stage_clinical_m(self):
        return self._tumor_stage_clinical_m

    @tumor_stage_clinical_m.setter
    def tumor_stage_clinical_m(self, value):
        self._validate_attr('tumor_stage_clinical_m', value)
        self._tumor_stage_clinical_m = value

    @property
    def tumor_stage_clinical_n(self):
        return self._tumor_stage_clinical_n

    @tumor_stage_clinical_n.setter
    def tumor_stage_clinical_n(self, value):
        self._validate_attr('tumor_stage_clinical_n', value)
        self._tumor_stage_clinical_n = value

    @property
    def tumor_stage_clinical_t(self):
        return self._tumor_stage_clinical_t

    @tumor_stage_clinical_t.setter
    def tumor_stage_clinical_t(self, value):
        self._validate_attr('tumor_stage_clinical_t', value)
        self._tumor_stage_clinical_t = value

    def to_list(self):
        return [
            'diagnosis',
            self._age_at_diagnosis,
            self._anatomic_site,
            self._diagnosis_finer_resolution,
            self._diagnosis_icd_cm,
            ';'.join(self._diagnosis_icd_o),
            self._diagnosis_id,
            self._disease_phase,
            self._toronto_childhood_cancer_staging,
            self._tumor_grade,
            self._tumor_stage_clinical_m,
            self._tumor_stage_clinical_n,
            self._tumor_stage_clinical_t,
        ]
