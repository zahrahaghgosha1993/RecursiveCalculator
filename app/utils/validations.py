from builtins import list
from functools import partial, update_wrapper

from flask import request
from jsonschema.validators import validator_for

from .exeptions import JsonValidationError


def validate_schema(schema):
    def wrapper(fn):
        def decorated(*args, **kwargs):
            validator_kwargs = {
                'schema': schema,
                'format_checker': 'JSON_SCHEMA_FORMAT_CHECKER'
            }
            validator_cls = validator_for(schema)
            validator = validator_cls(**validator_kwargs)
            errors = list(validator.iter_errors(request.get_json()))
            if errors:
                raise JsonValidationError('Error validating against schema', errors)

            return fn(*args, **kwargs)

        pfunc = partial(decorated)

        update_wrapper(pfunc, decorated)

        return pfunc

    return wrapper
