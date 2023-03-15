from django.utils.translation import gettext


def create_error_list(errors: dict) -> dict:
    cleaned_errors = {}

    for key, value in errors.items():

        if key not in cleaned_errors:
            cleaned_errors[key] = {}

        if isinstance(value, str):
            cleaned_errors[key] = [value]

        elif isinstance(value, list):
            cleaned_errors[key] = [str(i) for i in value]

    return {gettext('errors'): cleaned_errors}


def create_missing_key_error(self, key: str) -> dict:
    errors = {key: f'Missing key "{key}".'}
    return self.create_error_list(errors)


def handle_request_key_errors(request, expected_request_keys: list, can_be_empty=True):
    errors = {}

    if not request.data and not can_be_empty:
        errors.update({'request_body': 'No data present'})
        return create_error_list(errors=errors)

    if isinstance(request.data, dict):
        for request_key in expected_request_keys:
            request_key_value = request.data.get(request_key, None)
            if request_key_value is None:
                if request_key not in errors.keys():
                    errors.update({request_key: ['Missing key']})
                else:
                    errors[request_key].append('Missing key')

    if errors == {}:
        return errors

    return create_error_list(errors=errors)
