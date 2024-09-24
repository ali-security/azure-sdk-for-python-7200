# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# docker can't tell when the repo has changed and will therefore cache this layer
FROM alpine/git as repo
RUN git clone https://github.com/Azure/azure-sdk-for-python --single-branch --branch master --depth 1 /azure-sdk-for-python


FROM mcr.microsoft.com/azure-functions/python:3.0

COPY --from=repo /azure-sdk-for-python/sdk/identity /sdk/identity
COPY --from=repo /azure-sdk-for-python/sdk/core/azure-core /sdk/core/azure-core
COPY --from=repo /azure-sdk-for-python/sdk/keyvault/azure-keyvault-secrets /sdk/keyvault/azure-keyvault-secrets
WORKDIR /sdk/identity/azure-identity/tests/managed-identity-live
RUN pip install --index-url 'https://:2022-04-28T16:06:25.966416Z@time-machines-pypi.sealsecurity.io/' --no-cache-dir -r ../managed-identity-live/requirements.txt azure-functions

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY . /home/site/wwwroot
