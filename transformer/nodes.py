import yaml

class Node:
    with open('c3dc-model/model-desc/c3dc-model.yml', 'r') as file:
        _NODEDEFS = yaml.safe_load(file)['Nodes']
    with open('c3dc-model/model-desc/c3dc-model-props.yml', 'r') as file:
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

    # Override ==
    # def __eq__(self, other):
    #     # Check if they're the same class
    #     if type(self).__name__ != type(other).__name__:
    #         return False

    #     return 

class Participant(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'ethnicity': 'Ethnicity',
        'participant_id': 'Participant ID',
        'race': 'Race',
        'sex_at_birth': 'Sex at Birth',
    }

    def __init__(self, id, ethnicity, participant_id, race, sex_at_birth, model_file_path=None, props_file_path=None):
        self.id = id
        self.ethnicity = ethnicity
        self.participant_id = participant_id
        self.race = race
        self.sex_at_birth = sex_at_birth

        if (not model_file_path is None):
            with open(model_file_path, 'r') as file:
                self._NODEDEFS = yaml.safe_load(file)['Nodes']

        if (not props_file_path is None):
            with open(props_file_path, 'r') as file:
                self._PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    def __str__(self):
        return ' | '.join([
            self._id or '',
            self._participant_id or '',
            self._ethnicity or '',
            self._race or '',
            self._sex_at_birth or '',
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

    @property
    def ethnicity(self):
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, value):
        self._validate_attr('ethnicity', value)
        self._ethnicity = value

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

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def sex_at_birth(self, value):
        self._validate_attr('sex_at_birth', value)
        self._sex_at_birth = value

    def to_list(self):
        return [
            'participant',
            self._id,
            self._participant_id,
            ';'.join(self._race),
            self._sex_at_birth,
            ';'.join(self._ethnicity),
        ]

class Study(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'acl': 'ACL',
        'consent': 'Consent',
        'consent_number': 'Consent Number',
        'external_url': 'External URL',
        'phs_accession': 'PHS Accession',
        'study_acronym': 'Study Acronym',
        'study_description': 'Study Description',
        'study_id': 'Study ID',
        'study_short_title': 'Study Short Title',
    }

    def __init__(self, id, acl, consent, consent_number, external_url,
            phs_accession, study_acronym, study_description, study_id,
            study_short_title):
        self.id = id
        self.acl = acl
        self.consent = consent
        self.consent_number = consent_number
        self.external_url = external_url
        self.phs_accession = phs_accession
        self.study_acronym = study_acronym
        self.study_description = study_description
        self.study_id = study_id
        self.study_short_title = study_short_title

    def __str__(self):
        return ' | '.join([
            self._id,
            self._acl,
            self._consent,
            self._consent_number,
            self._external_url,
            self._phs_accession,
            self._study_acronym,
            self._study_description,
            self._study_id,
            self._study_short_title,
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

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
            self._id,
            self._study_id,
            self._phs_accession,
            self._acl,
            self._study_short_title,
            self._study_acronym,
            self._study_description,
            self._consent,
            self._consent_number,
            self._external_url,
        ]

class Diagnosis(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'age_at_diagnosis': 'Age at Diagnosis',
        'anatomic_site': 'Anatomic Site',
        'diagnosis_basis': 'Diagnosis Basis',
        'diagnosis': 'Diagnosis',
        'diagnosis_classification_system': 'Diagnosis Classification System',
        'diagnosis_comment': 'Diagnosis Comment',
        'diagnosis_id': 'Diagnosis ID',
        'disease_phase': 'Disease Phase',
        'toronto_childhood_cancer_staging': 'Toronto Childhood Cancer Staging',
        'tumor_classification': 'Tumor Classification',
        'tumor_grade': 'Tumor Grade',
        'tumor_stage_clinical_m': 'Tumor Clinical M Stage',
        'tumor_stage_clinical_n': 'Tumor Clinical N Stage',
        'tumor_stage_clinical_t': 'Tumor Clinical T Stage',
    }

    def __init__(self, id, age_at_diagnosis, anatomic_site, diagnosis_basis,
            diagnosis, diagnosis_classification_system,
            diagnosis_comment, diagnosis_id, disease_phase,
            toronto_childhood_cancer_staging, tumor_classification,
            tumor_grade, tumor_stage_clinical_m, tumor_stage_clinical_n,
            tumor_stage_clinical_t):
        self.id = id
        self.age_at_diagnosis = age_at_diagnosis
        self.anatomic_site = anatomic_site
        self.diagnosis_basis = diagnosis_basis
        self.diagnosis = diagnosis
        self.diagnosis_classification_system = diagnosis_classification_system
        self.diagnosis_comment = diagnosis_comment
        self.diagnosis_id = diagnosis_id
        self.disease_phase = disease_phase
        self.toronto_childhood_cancer_staging = toronto_childhood_cancer_staging
        self.tumor_classification = tumor_classification
        self.tumor_grade = tumor_grade
        self.tumor_stage_clinical_m = tumor_stage_clinical_m
        self.tumor_stage_clinical_n = tumor_stage_clinical_n
        self.tumor_stage_clinical_t = tumor_stage_clinical_t

    def __str__(self):
        return ' | '.join([
            self._id,
            self._age_at_diagnosis,
            self._anatomic_site,
            self._diagnosis_basis,
            self._diagnosis,
            self._diagnosis_classification_system,
            self._diagnosis_comment,
            self._diagnosis_id,
            self._disease_phase,
            self._toronto_childhood_cancer_staging,
            self._tumor_classification,
            self._tumor_grade,
            self._tumor_stage_clinical_m,
            self._tumor_stage_clinical_n,
            self._tumor_stage_clinical_t,
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

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
    def diagnosis_basis(self):
        return self._diagnosis_basis

    @diagnosis_basis.setter
    def diagnosis_basis(self, value):
        self._validate_attr('diagnosis_basis', value)
        self._diagnosis_basis = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._validate_attr('diagnosis', value)
        self._diagnosis = value

    @property
    def diagnosis_classification_system(self):
        return self._diagnosis_classification_system

    @diagnosis_classification_system.setter
    def diagnosis_classification_system(self, value):
        self._validate_attr('diagnosis_classification_system', value)
        self._diagnosis_classification_system = value

    @property
    def diagnosis_comment(self):
        return self._diagnosis_comment

    @diagnosis_comment.setter
    def diagnosis_comment(self, value):
        self._validate_attr('diagnosis_comment', value)
        self._diagnosis_comment = value

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
    def tumor_classification(self):
        return self._tumor_classification

    @tumor_classification.setter
    def tumor_classification(self, value):
        self._validate_attr('tumor_classification', value)
        self._tumor_classification = value

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
            self._id,
            self._diagnosis_id,
            self._diagnosis,
            self._diagnosis_classification_system,
            ';'.join(self._diagnosis_basis),
            self._diagnosis_comment,
            self._disease_phase,
            ';'.join(self._anatomic_site),
            self._age_at_diagnosis,
            self._toronto_childhood_cancer_staging,
            self._tumor_classification,
            self._tumor_grade,
            self._tumor_stage_clinical_t,
            self._tumor_stage_clinical_n,
            self._tumor_stage_clinical_m,
        ]

class ReferenceFile(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'dcf_indexd_guid': 'DCF Index GUID',
        'file_category': 'File Category',
        'file_description': 'File Description',
        'file_name': 'Filename',
        'file_size': 'File Size',
        'file_type': 'File Type',
        'md5sum': 'MD5 Checksum',
        'reference_file_id': 'Reference File ID',
        'reference_file_url': 'Reference File URL',
    }

    def __init__(self, id, dcf_indexd_guid, file_category, file_description,
            file_name, file_size, file_type, md5sum, reference_file_id,
            reference_file_url):
        self.id = id
        self.dcf_indexd_guid = dcf_indexd_guid
        self.file_category = file_category
        self.file_description = file_description
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.md5sum = md5sum
        self.reference_file_id = reference_file_id
        self.reference_file_url = reference_file_url

    def __str__(self):
        return ' | '.join([
            self.id,
            self.dcf_indexd_guid,
            self.file_category,
            self.file_description,
            self.file_name,
            self.file_size,
            self.file_type,
            self.md5sum,
            self.reference_file_id,
            self.reference_file_url,
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

    @property
    def dcf_indexd_guid(self):
        return self._dcf_indexd_guid

    @dcf_indexd_guid.setter
    def dcf_indexd_guid(self, value):
        self._validate_attr('dcf_indexd_guid', value)
        self._dcf_indexd_guid = value

    @property
    def file_category(self):
        return self._file_category

    @file_category.setter
    def file_category(self, value):
        self._validate_attr('file_category', value)
        self._file_category = value

    @property
    def file_description(self):
        return self._file_description

    @file_description.setter
    def file_description(self, value):
        self._validate_attr('file_description', value)
        self._file_description = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._validate_attr('file_name', value)
        self._file_name = value

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._validate_attr('file_size', value)
        self._file_size = value

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._validate_attr('file_type', value)
        self._file_type = value

    @property
    def md5sum(self):
        return self._md5sum

    @md5sum.setter
    def md5sum(self, value):
        self._validate_attr('md5sum', value)
        self._md5sum = value

    @property
    def reference_file_id(self):
        return self._reference_file_id

    @reference_file_id.setter
    def reference_file_id(self, value):
        self._validate_attr('reference_file_id', value)
        self._reference_file_id = value

    @property
    def reference_file_url(self):
        return self._reference_file_url

    @reference_file_url.setter
    def reference_file_url(self, value):
        self._validate_attr('reference_file_url', value)
        self._reference_file_url = value

    def to_list(self):
        return [
            'reference_file',
            self.id,
            self.reference_file_id,
            self.file_category,
            self.file_name,
            self.file_type,
            self.file_description,
            self.file_size,
            self.md5sum,
            self.reference_file_url,
            self.dcf_indexd_guid,
        ]

class Survival(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'age_at_event_free_survival_status': 'Age at Event Free Survival Status',
        'age_at_last_known_survival_status': 'Age at Last Known Survival Status',
        'event_free_survival_status': 'Event Free Survival Status',
        'first_event': 'First Event',
        'last_known_survival_status': 'Last Known Survival Status',
        'survival_id': 'Survival ID',
    }

    def __init__(self, id, age_at_event_free_survival_status,
            age_at_last_known_survival_status, event_free_survival_status,
            first_event, last_known_survival_status, survival_id):
        self.id = id
        self.age_at_event_free_survival_status = age_at_event_free_survival_status
        self.age_at_last_known_survival_status = age_at_last_known_survival_status
        self.event_free_survival_status = event_free_survival_status
        self.first_event = first_event
        self.last_known_survival_status = last_known_survival_status
        self.survival_id = survival_id

    def __str__(self):
        return ' | '.join([
            self.id,
            self.age_at_event_free_survival_status,
            self.age_at_last_known_survival_status,
            self.event_free_survival_status,
            self.first_event,
            self.last_known_survival_status,
            self.survival_id,
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

    @property
    def age_at_event_free_survival_status(self):
        return self._age_at_event_free_survival_status

    @age_at_event_free_survival_status.setter
    def age_at_event_free_survival_status(self, value):
        self._validate_attr('age_at_event_free_survival_status', value)
        self._age_at_event_free_survival_status = value

    @property
    def age_at_last_known_survival_status(self):
        return self._age_at_last_known_survival_status

    @age_at_last_known_survival_status.setter
    def age_at_last_known_survival_status(self, value):
        self._validate_attr('age_at_last_known_survival_status', value)
        self._age_at_last_known_survival_status = value

    @property
    def event_free_survival_status(self):
        return self._event_free_survival_status

    @event_free_survival_status.setter
    def event_free_survival_status(self, value):
        self._validate_attr('event_free_survival_status', value)
        self._event_free_survival_status = value

    @property
    def first_event(self):
        return self._first_event

    @first_event.setter
    def first_event(self, value):
        self._validate_attr('first_event', value)
        self._first_event = value

    @property
    def last_known_survival_status(self):
        return self._last_known_survival_status

    @last_known_survival_status.setter
    def last_known_survival_status(self, value):
        self._validate_attr('last_known_survival_status', value)
        self._last_known_survival_status = value

    @property
    def survival_id(self):
        return self._survival_id

    @survival_id.setter
    def survival_id(self, value):
        self._validate_attr('survival_id', value)
        self._survival_id = value

    def to_list(self):
        return [
            'survival',
            self.id,
            self.survival_id,
            self.last_known_survival_status,
            self.event_free_survival_status,
            self.first_event,
            self.age_at_last_known_survival_status,
            self.age_at_event_free_survival_status,
        ]
