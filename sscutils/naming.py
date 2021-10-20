from pathlib import Path

COMPLETE_ENV_NAME = "complete"
DEFAULT_BRANCH_NAME = "main"

FEATURES_CLS_SUFFIX = "features"
INDEX_CLS_SUFFIX = "index"

PIPELINE_STEP_SEPARATOR = "|>"

CONFIG_DIR = Path("conf")
METADATA_DIR = Path("metadata")


class NamespaceMetadataPaths:
    def __init__(self, local_name: str = "") -> None:
        def _p(s) -> Path:
            return METADATA_DIR / local_name / s

        self.composite_types = _p("composite-types.yaml")
        self.entity_classes = _p("entity-classes.yaml")
        self.table_schemas = _p("tables.yaml")


DATASET_METADATA_PATHS = NamespaceMetadataPaths()
IMPORTED_NAMESPACES_PATH = METADATA_DIR / "imported-namespaces.yaml"
DEFAULT_REMOTES_PATH = CONFIG_DIR / "default-remotes.yaml"


class DatasetConfigPaths:

    CREATED_ENVS = CONFIG_DIR / "created-envs.yaml"


class ProjectConfigPaths:

    CURRENT_ENV = CONFIG_DIR / "project-env.yaml"
    PARAMS = Path("params.yaml")


DATA_PATH = Path("data")
SRC_PATH = Path("src")
IMPORTED_NAMESPACES_MODULE_NAME = "imported_namespaces"
NAMESPACE_METADATA_MODULE_NAME = "namespace_metadata"
UPDATE_DATA_MODULE_NAME = "update_data"
UPDATE_DATA_FUNCTION_NAME = "update_data"
ENV_CREATION_MODULE_NAME = "create_environments"
ENV_CREATION_FUNCTION_NAME = "create_environments"
