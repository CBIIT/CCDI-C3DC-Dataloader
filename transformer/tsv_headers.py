# Column headers for the TSV files

DIAGNOSIS_HEADERS = [
    'type',
    'id',
    'diagnosis_id',
    'diagnosis',
    'diagnosis_classification_system',
    'diagnosis_basis',
    'diagnosis_comment',
    'disease_phase',
    'anatomic_site',
    'age_at_diagnosis',
    'toronto_childhood_cancer_staging',
    'tumor_classification',
    'tumor_grade',
    'tumor_stage_clinical_t',
    'tumor_stage_clinical_n',
    'tumor_stage_clinical_m',
    'participant.id',
]

PARTICIPANT_HEADERS = [
    'type',
    'id',
    'participant_id',
    'race',
    'sex_at_birth',
    'ethnicity',
    'study.id',
]

REFERENCE_FILE_HEADERS = [
    'type',
    'id',
    'reference_file_id',
    'file_category',
    'file_name',
    'file_type',
    'file_description',
    'file_size',
    'md5sum',
    'reference_file_url',
    'dcf_indexd_guid',
    'study.id',
]

STUDY_HEADERS = [
    'type',
    'id',
    'study_id',
    'phs_accession',
    'acl',
    'study_short_title',
    'study_acronym',
    'study_description',
    'consent',
    'consent_number',
    'external_url',
]

SURVIVAL_HEADERS = [
    'type',
    'id',
    'survival_id',
    'last_known_survival_status',
    'event_free_survival_status',
    'first_event',
    'age_at_last_known_survival_status',
    'age_at_event_free_survival_status',
    'participant.id',
]