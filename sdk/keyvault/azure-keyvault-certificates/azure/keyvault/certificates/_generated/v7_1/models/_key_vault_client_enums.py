# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the action."""

    EMAIL_CONTACTS = "EmailContacts"
    AUTO_RENEW = "AutoRenew"


class DeletionRecoveryLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Reflects the deletion recovery level currently in effect for certificates in the current vault.
    If it contains 'Purgeable', the certificate can be permanently deleted by a privileged user;
    otherwise, only the system can purge the certificate, at the end of the retention interval.
    """

    PURGEABLE = "Purgeable"
    """Denotes a vault state in which deletion is an irreversible operation, without the possibility
    #: for recovery. This level corresponds to no protection being available against a Delete
    #: operation; the data is irretrievably lost upon accepting a Delete operation at the entity level
    #: or higher (vault, resource group, subscription etc.)"""
    RECOVERABLE_PURGEABLE = "Recoverable+Purgeable"
    """Denotes a vault state in which deletion is recoverable, and which also permits immediate and
    #: permanent deletion (i.e. purge). This level guarantees the recoverability of the deleted entity
    #: during the retention interval (90 days), unless a Purge operation is requested, or the
    #: subscription is cancelled. System wil permanently delete it after 90 days, if not recovered"""
    RECOVERABLE = "Recoverable"
    """Denotes a vault state in which deletion is recoverable without the possibility for immediate
    #: and permanent deletion (i.e. purge). This level guarantees the recoverability of the deleted
    #: entity during the retention interval(90 days) and while the subscription is still available.
    #: System wil permanently delete it after 90 days, if not recovered"""
    RECOVERABLE_PROTECTED_SUBSCRIPTION = "Recoverable+ProtectedSubscription"
    """Denotes a vault and subscription state in which deletion is recoverable within retention
    #: interval (90 days), immediate and permanent deletion (i.e. purge) is not permitted, and in
    #: which the subscription itself  cannot be permanently canceled. System wil permanently delete it
    #: after 90 days, if not recovered"""
    CUSTOMIZED_RECOVERABLE_PURGEABLE = "CustomizedRecoverable+Purgeable"
    """Denotes a vault state in which deletion is recoverable, and which also permits immediate and
    #: permanent deletion (i.e. purge when 7<= SoftDeleteRetentionInDays < 90). This level guarantees
    #: the recoverability of the deleted entity during the retention interval, unless a Purge
    #: operation is requested, or the subscription is cancelled."""
    CUSTOMIZED_RECOVERABLE = "CustomizedRecoverable"
    """Denotes a vault state in which deletion is recoverable without the possibility for immediate
    #: and permanent deletion (i.e. purge when 7<= SoftDeleteRetentionInDays < 90).This level
    #: guarantees the recoverability of the deleted entity during the retention interval and while the
    #: subscription is still available."""
    CUSTOMIZED_RECOVERABLE_PROTECTED_SUBSCRIPTION = "CustomizedRecoverable+ProtectedSubscription"
    """Denotes a vault and subscription state in which deletion is recoverable, immediate and
    #: permanent deletion (i.e. purge) is not permitted, and in which the subscription itself cannot
    #: be permanently canceled when 7<= SoftDeleteRetentionInDays < 90. This level guarantees the
    #: recoverability of the deleted entity during the retention interval, and also reflects the fact
    #: that the subscription itself cannot be cancelled."""


class JsonWebKeyCurveName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Elliptic curve name. For valid values, see JsonWebKeyCurveName."""

    P256 = "P-256"
    P384 = "P-384"
    P521 = "P-521"
    P256_K = "P-256K"


class JsonWebKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of key pair to be used for the certificate."""

    EC = "EC"
    EC_HSM = "EC-HSM"
    RSA = "RSA"
    RSA_HSM = "RSA-HSM"
    OCT = "oct"


class KeyUsageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KeyUsageType."""

    DIGITAL_SIGNATURE = "digitalSignature"
    NON_REPUDIATION = "nonRepudiation"
    KEY_ENCIPHERMENT = "keyEncipherment"
    DATA_ENCIPHERMENT = "dataEncipherment"
    KEY_AGREEMENT = "keyAgreement"
    KEY_CERT_SIGN = "keyCertSign"
    C_RL_SIGN = "cRLSign"
    ENCIPHER_ONLY = "encipherOnly"
    DECIPHER_ONLY = "decipherOnly"
