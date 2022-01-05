from pathlib import Path

import vivarium_conic_vitamin_a_supp_gbd2019
from vivarium_conic_vitamin_a_supp_gbd2019.constants import metadata

BASE_DIR = Path(vivarium_conic_vitamin_a_supp_gbd2019.__file__).resolve().parent

ARTIFACT_ROOT = Path(f"/share/costeffectiveness/artifacts/{metadata.PROJECT_NAME}/")
MODEL_SPEC_DIR = BASE_DIR / 'model_specifications'
RESULTS_ROOT = Path(f'/share/costeffectiveness/results/{metadata.PROJECT_NAME}/')
