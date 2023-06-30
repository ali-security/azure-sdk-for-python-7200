# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools
import logging
import json
import base64

from azure.core.exceptions import ClientAuthenticationError

from ..._internal import within_credential_chain

_LOGGER = logging.getLogger(__name__)


def log_get_token_async(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        try:
            token = await fn(*args, **kwargs)
            _LOGGER.log(
                logging.DEBUG if within_credential_chain.get() else logging.INFO, "%s succeeded", fn.__qualname__
            )
            if _LOGGER.isEnabledFor(logging.DEBUG):
                try:
                    base64_meta_data = token.token.split(".")[1].encode("utf-8") + b'=='
                    json_bytes = base64.decodebytes(base64_meta_data)
                    json_string = json_bytes.decode('utf-8')
                    json_dict = json.loads(json_string)
                    upn = json_dict.get('upn', 'unavailableUpn')
                    log_string = '[Authenticated account] Client ID: {}. Tenant ID: {}. User Principal Name: {}. ' \
                                 'Object ID (user): {}'.format(json_dict['appid'],
                                                               json_dict['tid'],
                                                               upn,
                                                               json_dict['oid']
                                                               )
                    _LOGGER.debug(log_string)
                except Exception:  # pylint: disable=broad-except
                    _LOGGER.debug("Fail to log the account information")
            return token
        except Exception as ex: # pylint: disable=broad-except
            _LOGGER.log(
                logging.DEBUG if within_credential_chain.get() else logging.WARNING,
                "%s failed: %s",
                fn.__qualname__,
                ex,
                exc_info=_LOGGER.isEnabledFor(logging.DEBUG),
            )
            raise

    return wrapper


def wrap_exceptions(fn):
    """Prevents leaking exceptions defined outside azure-core by raising ClientAuthenticationError from them.

    :param fn: The function to wrap.
    :type fn: ~typing.Callable
    :return: The wrapped function.
    :rtype: callable
    """

    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        try:
            result = await fn(*args, **kwargs)
            return result
        except ClientAuthenticationError:
            raise
        except Exception as ex:  # pylint:disable=broad-except
            auth_error = ClientAuthenticationError(message="Authentication failed: {}".format(ex))
            raise auth_error from ex

    return wrapper
