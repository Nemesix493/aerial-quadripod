"""Module for loading and validating project information from a YAML file."""

import yaml
from cerberus import Validator

import settings


class ProjectInfo:
    """Class responsible for loading and validating project-related data from a YAML info file."""

    class ValidationError(Exception):
        """Exception raised when validation of the YAML data fails."""

    INFO_FILE_PATH = settings.INFO_FILE

    material_schema = {
        'id': {'type': 'string', 'required': True},
        'dim': {
            'type': 'list',
            'required': True,
            'schema': {
                'type': 'integer',
            }
        },
        'ref': {'type': 'string', 'required': True},
        'url': {'type': 'string', 'required': False},
    }

    construct_info_schema = {
        'cut_line_thickness': {
            'type': 'integer',
            'required': True
        },
        'cut_line_tolerance': {
            'type': 'integer',
            'required': True
        }
    }

    part_schema = {
        'name': {
            'type': 'string',
            'required': True
        },
        'quantity': {
            'type': 'integer',
            'required': True
        },
        'material_id': {
            'type': 'string',
            'required': True
        },
        'max_length': {
            'type': 'integer',
            'required': True
        },
    }

    global_schema = {
        'materials': {
            'type': 'list',
            'required': True,
            'schema': {
                'type': 'dict',
                'schema': material_schema
            }
        },
        'construct-info': {
            'type': 'dict',
            'required': True,
            'schema': construct_info_schema
        },
        'parts': {
            'type': 'list',
            'required': True,
            'schema': {
                'type': 'dict',
                'schema': part_schema
            }
        }
    }

    @classmethod
    def load(cls):
        """Load and validate the YAML project info file.

        If the data has already been loaded and cached, it skips reloading.
        Raises:
            ValidationError: If the loaded data does not match the schema.
        """
        if not hasattr(cls, "_info"):
            with open(cls.INFO_FILE_PATH, 'r', encoding='utf-8') as info_file:
                info = yaml.safe_load(info_file)
            validator = Validator(cls.global_schema)
            if not validator.validate(info):
                raise cls.ValidationError(
                    f"Validation failed: {validator.errors}"
                )
            setattr(cls, "_info", info)

    @classmethod
    def get_materials(cls) -> list[dict]:
        """Return the list of materials from the validated info data.

        Ensures the data is loaded and validated before accessing.
        Returns:
            list: A list of material dictionaries.
        """
        cls.load()
        return getattr(cls, "_info")['materials']

    @classmethod
    def get_construct_info(cls) -> dict:
        """Return the construction-related configuration from the validated info data.

        Ensures the data is loaded and validated before accessing.
        Returns:
            dict: A dictionary containing construction parameters.
        """
        cls.load()
        return getattr(cls, "_info")['construct-info']

    @classmethod
    def get_parts(cls) -> list[dict]:
        """Return the list of part definitions from the validated info data.

        Ensures the data is loaded and validated before accessing.
        Returns:
            list: A list of dictionaries, each representing a part.
        """
        cls.load()
        return getattr(cls, "_info")['parts']
