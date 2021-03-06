import os
from pathlib import Path

"""
This file has global application specific configuration stored as properties
"""


def fetch_all_jobs_path():
    """
    This method creates (if doesnot exists) a folder where all jobs will be stored
    :return: return all jobs folder path
    """
    prnt_fld = Path.home()
    fld_path = os.path.join(prnt_fld, "ml_olfa", "all_jobs")

    if not os.path.exists(fld_path):
        os.makedirs(fld_path, exist_ok=True)

    return fld_path


def fetch_app_config_path():
    prnt_fld = Path.home()
    fld_path = os.path.join(prnt_fld, "ml_olfa", ".app_config")

    if not os.path.exists(fld_path):
        os.makedirs(fld_path, exist_ok=True)

    return fld_path


ALL_JOBS_FOLDER = fetch_all_jobs_path()

JOB_INIT_STATUS = "job_created"
STEP0_STATUS = "read_data"
STEP1_STATUS = "feature_generation"
STEP2_STATUS = "preprocessing"
STEP3_STATUS = "feature_selection"
STEP4_STATUS = "feature_extraction"
STEP5_STATUS = "classification"
STEP6_STATUS = "test_set_generation"
STEP6_1_STATUS = "test_set_preprocessing"
STEPS_COMPLETED_STATUS = "job_completed"

JOB_STATUS_LABELS = {
    "job_created": "Job Created",
    "read_data": "Read User Data",
    "feature_generation": "Feature Generation",
    "preprocessing": "Pre-Processing",
    "feature_selection": "Feature Selection",
    "feature_extraction": "Feature Extraction",
    "classification": "Classification",
    "test_set_generation": "Test Set Generation",
    "test_set_preprocessing": "Test Set Pre-Processing",
    "job_completed": "Job Completed"
}

JOB_CONFIG_FLD_NAME = ".config"
JOB_DATA_FLD_NAME = "data"
JOB_RESULTS_FLD_NAME = "results"
JOB_LOGS_FLD_NAME = "logs"
JOB_CONFIG_FNAME = "ml_ip_config.json"
JOB_OTHER_CONFIG_FNAME = "other_config.json"

USER_IP_FLD_NAME = "step0"
USER_IP_FNAME = "user_data.csv"

FG_FLD_NAME = "step1"
FG_PADEL_FNAME = "FG_Padel.csv"
FG_MORDRED_FNAME = "FG_Mordred.csv"
FG_PADEL_FLD_NAME = "PaDEL"
FG_MORDRED_FLD_NAME = "Mordred"

PP_FLD_NAME = "step2"
PP_FLD_PREFIX = "PP_"
PP_INIT_DATA_FNAME = "PP_init_data.csv"
PP_INIT_COL_PRUNED_FNAME = "PP_cols_pruned.csv"
PP_NORM_DUMP_NAME = "PP_data_normalization.joblib"
PP_FIN_XTRAIN_FNAME = "PP_train.csv"
PP_FIN_XTEST_FNAME = "PP_test.csv"
PP_FIN_YTRAIN_FNAME = "PP_train_labels.csv"
PP_FIN_YTEST_FNAME = "PP_test_labels.csv"

FS_FLD_NAME = "step3"
FS_FLD_PREFIX = "FS_"
FS_XTRAIN_FNAME = "FS_train.csv"
FS_XTEST_FNAME = "FS_test.csv"
FS_YTRAIN_FNAME = "FS_train_labels.csv"
FS_YTEST_FNAME = "FS_test_labels.csv"

FE_FLD_NAME = "step4"
FE_FLD_PREFIX = "FE_"
FE_PCA_DUMP_FNAME = "FE_PCA.joblib"

CLF_FLD_NAME = "step5"
CLF_FLD_PREFIX = "clf_"

TSG_FLD_NAME = "step6"
TSG_TEST_FLD_NAME = "test"
TSG_RAW_FLD_NAME = "raw"
TSG_PP_FLD_NAME = "preprocessed"
TSG_CMPND_FLD_NAME = "test_compounds"
TSG_PP_LIME_FLD_NAME = "pp_lime"

CLF_RESULTS_FLD_NAME = "classifiers"
CV_RESULTS_FLD_NAME = "cross-validation"
NOVEL_RESULTS_FLD_NAME = "novel_predictions"

TEMP_TTS_FLD_NAME = ".temp"
TEMP_XTRAIN_FNAME = "train.csv"
TEMP_XTEST_FNAME = "test.csv"
TEMP_YTRAIN_FNAME = "train_labels.csv"
TEMP_YTEST_FNAME = "test_labels.csv"
