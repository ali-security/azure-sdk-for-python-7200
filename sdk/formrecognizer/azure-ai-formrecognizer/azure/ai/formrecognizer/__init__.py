# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from ._version import VERSION
from ._form_recognizer_client import FormRecognizerClient
from ._form_training_client import FormTrainingClient
from ._document_analysis_client import DocumentAnalysisClient
from ._document_model_administration_client import DocumentModelAdministrationClient
from ._polling import DocumentModelAdministrationLROPoller
from ._models import (
    FormElement,
    LengthUnit,
    TrainingStatus,
    CustomFormModelStatus,
    FormContentType,
    FormTable,
    FormTableCell,
    TrainingDocumentInfo,
    FormRecognizerError,
    CustomFormModelInfo,
    AccountProperties,
    Point,
    FormPageRange,
    RecognizedForm,
    FormField,
    FieldData,
    FormPage,
    FormLine,
    FormWord,
    CustomFormModel,
    CustomFormSubmodel,
    CustomFormModelField,
    FieldValueType,
    CustomFormModelProperties,
    FormSelectionMark,
    TextAppearance,
    AnalyzeResult,
    AnalyzedDocument,
    BoundingRegion,
    AddressValue,
    AnalysisFeature,
    CurrencyValue,
    CustomDocumentModelsDetails,
    ModelBuildMode,
    DocumentClassifierDetails,
    DocumentField,
    DocumentKeyValuePair,
    DocumentKeyValueElement,
    DocumentLanguage,
    DocumentLine,
    DocumentPage,
    DocumentParagraph,
    DocumentSelectionMark,
    DocumentSpan,
    DocumentStyle,
    DocumentTable,
    DocumentTableCell,
    DocumentWord,
    OperationSummary,
    OperationDetails,
    DocumentModelDetails,
    DocumentModelSummary,
    DocumentTypeDetails,
    ResourceDetails,
    DocumentAnalysisError,
    DocumentAnalysisInnerError,
    TargetAuthorization,
    QuotaDetails,
)
from ._generated.models import (  # patched models
    ClassifierDocumentTypeDetails,
    AzureBlobFileListSource,
    AzureBlobContentSource,
)
from ._api_versions import FormRecognizerApiVersion, DocumentAnalysisApiVersion


__all__ = [
    "FormRecognizerApiVersion",
    "DocumentAnalysisClient",
    "DocumentModelAdministrationClient",
    "FormRecognizerClient",
    "FormTrainingClient",
    "LengthUnit",
    "TrainingStatus",
    "CustomFormModelStatus",
    "FormContentType",
    "FormElement",
    "FormTable",
    "FormTableCell",
    "TrainingDocumentInfo",
    "FormRecognizerError",
    "CustomFormModelInfo",
    "AccountProperties",
    "Point",
    "FormPageRange",
    "RecognizedForm",
    "FormField",
    "FieldData",
    "FormPage",
    "FormLine",
    "FormWord",
    "CustomFormModel",
    "CustomFormSubmodel",
    "CustomFormModelField",
    "FieldValueType",
    "CustomFormModelProperties",
    "FormSelectionMark",
    "TextAppearance",
    "AnalyzeResult",
    "AnalyzedDocument",
    "BoundingRegion",
    "AddressValue",
    "AnalysisFeature",
    "CurrencyValue",
    "CustomDocumentModelsDetails",
    "ModelBuildMode",
    "DocumentClassifierDetails",
    "DocumentField",
    "DocumentKeyValueElement",
    "DocumentKeyValuePair",
    "DocumentLanguage",
    "DocumentLine",
    "DocumentPage",
    "DocumentParagraph",
    "DocumentSelectionMark",
    "DocumentSpan",
    "DocumentStyle",
    "DocumentTable",
    "DocumentTableCell",
    "DocumentWord",
    "DocumentModelAdministrationLROPoller",
    "OperationSummary",
    "OperationDetails",
    "DocumentAnalysisApiVersion",
    "DocumentModelDetails",
    "DocumentModelSummary",
    "DocumentTypeDetails",
    "ResourceDetails",
    "DocumentAnalysisError",
    "DocumentAnalysisInnerError",
    "TargetAuthorization",
    "ClassifierDocumentTypeDetails",
    "AzureBlobFileListSource",
    "AzureBlobContentSource",
    "QuotaDetails",
]

__VERSION__ = VERSION
