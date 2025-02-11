import yaml

class Node:
    with open('c3dc-model/model-desc/c3dc-model.yml', 'r', encoding='utf8') as file:
        _NODEDEFS = yaml.safe_load(file)['Nodes']
    with open('c3dc-model/model-desc/c3dc-model-props.yml', 'r', encoding='utf8') as file:
        _PROPDEFS = yaml.safe_load(file)['PropDefinitions']

    _PROPER_NAMES = {}
    _TYPE_MAP = {
        'integer': int,
        'list': list,
        'string': str,
    }

    # Retrieves an attribute's list of prescribed values
    def _get_permissible_values(self, yaml_node):
        # Enum PVs are found under "Enum"
        if self._is_enum(yaml_node):
            return yaml_node['Enum']

        # List PVs are found under "Type"->"item_type"
        if self._is_list(yaml_node):
            return yaml_node['Type']['item_type']

        # At this point, the attribute is neither an Enum nor a list
        raise ValueError('Trying to get prescribed values of a non-enum or non-list')

    # Determines whether a list/enum has permissible values
    def _has_permissible_values(self, yaml_node):
        if self._is_enum(yaml_node):
            pv_list = yaml_node['Enum'] # Enums have the "Enum" key by definition

            if not isinstance(pv_list, list) or len(pv_list) == 0:
                return False

            return True

        if self._is_list(yaml_node):
            type_desc = yaml_node['Type'] # Lists have the "Type"->"value_type" keys by definition

            if 'item_type' not in type_desc.keys() or len(type_desc['item_type']) == 0:
                return False

            return True

        # Should not reach this code if list or enum
        raise RuntimeError('Cannot check permissible values for a non-enum or non-list')

    # Determines whether an attribute is an enum
    def _is_enum(self, yaml_node):
        # We know it's an enum if there's an "Enum" key
        if 'Enum' in yaml_node.keys():
            return True

        return False

    # Determines whether an attribute is a list
    def _is_list(self, yaml_node):
        type_desc = None

        # "Enum" is reserved to specifically not be a list, even if both can have PVs
        if self._is_enum(yaml_node):
            return False

        if 'Type' not in yaml_node.keys():
            raise ValueError('Attribute isn\'t an enum, but MDF is missing the \'Type\' key')

        type_desc = yaml_node['Type']

        # Primitives are not lists
        if isinstance(type_desc, str):
            return False

        if 'value_type' not in type_desc.keys():
            raise ValueError('Attribute isn\'t an enum, but MDF is missing the \'value_type\' key')

        # Lists are explicitly called "list"
        if type_desc['value_type'] == 'list':
            return True

        # We shouldn't reach this code
        raise RuntimeError('Can\'t determine attribute type - unknown MDF format')

    # Returns a boolean indicating whether the attribute is required
    def _is_req(self, yaml_node):
        # Early error to catch invalid YAML
        if 'Req' not in yaml_node.keys():
            raise ValueError('Missing `Req` key in Model Description YAML')

        return yaml_node['Req']

    # Figures out the Python type that an attribute should be
    def _get_type(self, yaml_node):
        type_literal = None

        # Don't bother with the types of enums or lists. Just make sure their values are allowed.
        if self._is_enum(yaml_node) or self._is_list(yaml_node):
            raise RuntimeError('Invalid type check. For enums and lists, just make sure their values are permissible')

        type_literal = yaml_node['Type']

        # Handle undefined type mapping
        if type_literal not in self._TYPE_MAP.keys():
            raise LookupError(f'No type mapped to string literal {type_literal}')

        return self._TYPE_MAP[type_literal]

    def _validate_attr(self, attr_name, value):
        prop_def = self._PROPDEFS[attr_name]
        is_required = self._is_req(prop_def)

        if is_required and value is None:
            raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

        if not is_required and value is None:
            return

        # Validation for primitives
        if not self._is_enum(prop_def) and not self._is_list(prop_def):
            type = self._get_type(prop_def)

            if is_required and type == str and value == '':
                raise TypeError(f'{self._PROPER_NAMES[attr_name]} is missing')

            # Check that the value is the right type
            if value is not None and not isinstance(value, type):
                raise TypeError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be of type {type}')

            return

        # Validation for enums
        if self._is_enum(prop_def):
            if not self._has_permissible_values(prop_def):
                raise RuntimeError(f'{self._PROPER_NAMES[attr_name]} is an enum, but it has no permissible values')

            if value not in self._get_permissible_values(prop_def):
                raise ValueError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be one of the specified values')

            return


        # Validation for lists
        if self._is_list(prop_def):
            # In rare cases, the MDF specifies no permissible values for a list
            if not self._has_permissible_values(prop_def):
                return

            if not all(item in self._get_permissible_values(prop_def) for item in value):
                raise ValueError(f'{self._PROPER_NAMES[attr_name]} `{value}` must be a subset of the specified values')

            return

        # Shouldn't reach this code
        raise RuntimeError('Unknown validation error')

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
        'participant_id': 'Participant ID',
        'race': 'Race',
        'sex_at_birth': 'Sex at Birth',
    }

    def __init__(self, id, participant_id, race, sex_at_birth, model_file_path=None, props_file_path=None):
        self.id = id
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
    def sex_at_birth(self):
        return self._sex_at_birth

    @sex_at_birth.setter
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
        ]

class Study(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'consent': 'Consent',
        'consent_number': 'Consent Number',
        'external_url': 'External URL',
        'dbgap_accession': 'dbGaP Accession',
        'study_description': 'Study Description',
        'study_id': 'Study ID',
        'study_name': 'Study Name',
    }

    def __init__(self, id, consent, consent_number, external_url,
            dbgap_accession, study_description, study_id, study_name):
        self.id = id
        self.consent = consent
        self.consent_number = consent_number
        self.external_url = external_url
        self.dbgap_accession = dbgap_accession
        self.study_description = study_description
        self.study_id = study_id
        self.study_name = study_name

    def __str__(self):
        return ' | '.join([
            self._id,
            self._consent,
            self._consent_number,
            self._external_url,
            self._dbgap_accession,
            self._study_description,
            self._study_id,
            self._study_name,
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

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
    def dbgap_accession(self):
        return self._dbgap_accession

    @dbgap_accession.setter
    def dbgap_accession(self, value):
        self._validate_attr('dbgap_accession', value)
        self._dbgap_accession = value

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
            self._dbgap_accession,
            self._study_name,
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
            self._diagnosis_basis,
            self._diagnosis_comment,
            self._disease_phase,
            self._anatomic_site,
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
        'cause_of_death': 'Cause of Death',
        'event_free_survival_status': 'Event Free Survival Status',
        'first_event': 'First Event',
        'last_known_survival_status': 'Last Known Survival Status',
        'survival_id': 'Survival ID',
    }

    def __init__(self, id, age_at_event_free_survival_status,
            age_at_last_known_survival_status, cause_of_death,
            event_free_survival_status, first_event, last_known_survival_status,
            survival_id):
        self.id = id
        self.age_at_event_free_survival_status = age_at_event_free_survival_status
        self.age_at_last_known_survival_status = age_at_last_known_survival_status
        self.cause_of_death = cause_of_death
        self.event_free_survival_status = event_free_survival_status
        self.first_event = first_event
        self.last_known_survival_status = last_known_survival_status
        self.survival_id = survival_id

    def __str__(self):
        return ' | '.join([
            self.id,
            self.age_at_event_free_survival_status,
            self.age_at_last_known_survival_status,
            self.cause_of_death,
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
    def cause_of_death(self):
        return self._cause_of_death

    @cause_of_death.setter
    def cause_of_death(self, value):
        self._validate_attr('cause_of_death', value)
        self._cause_of_death = value

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
            self.cause_of_death,
        ]

class Treatment(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'age_at_treatment_end': 'Age at Treatment End',
        'age_at_treatment_start': 'Age at Treatment Start',
        'treatment_agent': 'Treatment Agent',
        'treatment_id': 'Treatment ID',
        'treatment_type': 'Treatment Type',
    }

    def __init__(self, id, age_at_treatment_end, age_at_treatment_start,
            treatment_agent, treatment_id, treatment_type):
        self.id = id
        self.age_at_treatment_end = age_at_treatment_end
        self.age_at_treatment_start = age_at_treatment_start
        self.treatment_agent = treatment_agent
        self.treatment_id = treatment_id
        self.treatment_type = treatment_type

    def __str__(self):
        return ' | '.join([
            self.id,
            self.treatment_id,
            self.age_at_treatment_start,
            self.age_at_treatment_end,
            self.treatment_type,
            self.treatment_agent
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

    @property
    def age_at_treatment_end(self):
        return self._age_at_treatment_end

    @age_at_treatment_end.setter
    def age_at_treatment_end(self, value):
        self._validate_attr('age_at_treatment_end', value)
        self._age_at_treatment_end = value

    @property
    def age_at_treatment_start(self):
        return self._age_at_treatment_start

    @age_at_treatment_start.setter
    def age_at_treatment_start(self, value):
        self._validate_attr('age_at_treatment_start', value)
        self._age_at_treatment_start = value

    @property
    def treatment_agent(self):
        return self._treatment_agent

    @treatment_agent.setter
    def treatment_agent(self, value):
        self._validate_attr('treatment_agent', value)
        self._treatment_agent = value

    @property
    def treatment_id(self):
        return self._treatment_id

    @treatment_id.setter
    def treatment_id(self, value):
        self._validate_attr('treatment_id', value)
        self._treatment_id = value

    @property
    def treatment_type(self):
        return self._treatment_type

    @treatment_type.setter
    def treatment_type(self, value):
        self._validate_attr('treatment_type', value)
        self._treatment_type = value

    def to_list(self):
        return [
            'treatment',
            self.id,
            self.treatment_id,
            self.age_at_treatment_start,
            self.age_at_treatment_end,
            self.treatment_type,
            ';'.join(self.treatment_agent),
        ]

class TreatmentResponse(Node):
    _PROPER_NAMES = {
        'id': 'ID',
        'age_at_response': 'Age at Response',
        'response': 'Response',
        'response_category': 'Response Category',
        'response_system': 'Response System',
        'treatment_response_id': 'Treatment Response ID',
    }

    def __init__(self, id, age_at_response, response, response_category,
            response_system, treatment_response_id):
        self.id = id
        self.age_at_response = age_at_response
        self.response = response
        self.response_category = response_category
        self.response_system = response_system
        self.treatment_response_id = treatment_response_id

    def __str__(self):
        return ' | '.join([
            self.id,
            self.age_at_response,
            self.response,
            self.response_category,
            self.response_system,
            self.treatment_response_id
        ])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._validate_attr('id', value)
        self._id = value

    @property
    def age_at_response(self):
        return self._age_at_response

    @age_at_response.setter
    def age_at_response(self, value):
        self._validate_attr('age_at_response', value)
        self._age_at_response = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._validate_attr('response', value)
        self._response = value

    @property
    def response_category(self):
        return self._response_category

    @response_category.setter
    def response_category(self, value):
        self._validate_attr('response_category', value)
        self._response_category = value

    @property
    def response_system(self):
        return self._response_system

    @response_system.setter
    def response_system(self, value):
        self._validate_attr('response_system', value)
        self._response_system = value

    @property
    def treatment_response_id(self):
        return self._treatment_response_id

    @treatment_response_id.setter
    def treatment_response_id(self, value):
        self._validate_attr('treatment_response_id', value)
        self._treatment_response_id = value

    def to_list(self):
        return [
            'treatment_response',
            self.id,
            self.treatment_response_id,
            self.response,
            self.age_at_response,
            self.response_category,
            self.response_system
        ]
