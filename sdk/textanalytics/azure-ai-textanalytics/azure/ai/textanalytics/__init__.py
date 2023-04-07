# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from ._text_analytics_client import TextAnalyticsClient
from ._version import VERSION
from ._base_client import TextAnalyticsApiVersion
from ._models import (
    DetectLanguageInput,
    TextDocumentInput,
    DetectedLanguage,
    DocumentError,
    CategorizedEntity,
    LinkedEntity,
    AnalyzeSentimentResult,
    RecognizeEntitiesResult,
    DetectLanguageResult,
    TextAnalyticsError,
    TextAnalyticsWarning,
    ExtractKeyPhrasesResult,
    RecognizeLinkedEntitiesResult,
    TextDocumentStatistics,
    LinkedEntityMatch,
    TextDocumentBatchStatistics,
    SentenceSentiment,
    SentimentConfidenceScores,
    MinedOpinion,
    TargetSentiment,
    AssessmentSentiment,
    RecognizePiiEntitiesResult,
    PiiEntity,
    PiiEntityDomain,
    AnalyzeHealthcareEntitiesResult,
    HealthcareEntity,
    HealthcareEntityDataSource,
    RecognizeEntitiesAction,
    RecognizeLinkedEntitiesAction,
    RecognizePiiEntitiesAction,
    ExtractKeyPhrasesAction,
    _AnalyzeActionsType,
    HealthcareRelation,
    HealthcareRelationRole,
    HealthcareEntityAssertion,
    AnalyzeSentimentAction,
    PiiEntityCategory,
    HealthcareEntityRelation,
    EntityConditionality,
    EntityCertainty,
    EntityAssociation,
    HealthcareEntityCategory,
    RecognizeCustomEntitiesAction,
    RecognizeCustomEntitiesResult,
    SingleLabelClassifyAction,
    MultiLabelClassifyAction,
    ClassifyDocumentResult,
    ClassificationCategory,
    AnalyzeHealthcareEntitiesAction,
    TextAnalysisKind,
    ExtractSummaryAction,
    ExtractSummaryResult,
    SummarySentence,
    AbstractiveSummaryResult,
    AbstractiveSummary,
    SummaryContext,
    AbstractiveSummaryAction,
)
from ._generated.models import (
    HealthcareDocumentType,
    ResolutionKind,
    AgeResolution,
    AreaResolution,
    CurrencyResolution,
    DateTimeResolution,
    InformationResolution,
    LengthResolution,
    NumberResolution,
    NumericRangeResolution,
    OrdinalResolution,
    SpeedResolution,
    TemperatureResolution,
    TemporalSpanResolution,
    VolumeResolution,
    WeightResolution,
    AgeUnit,
    AreaUnit,
    TemporalModifier,
    InformationUnit,
    LengthUnit,
    NumberKind,
    RangeKind,
    RelativeTo,
    SpeedUnit,
    TemperatureUnit,
    VolumeUnit,
    WeightUnit,
    DateTimeSubKind,
)
from ._lro import AnalyzeHealthcareEntitiesLROPoller, AnalyzeActionsLROPoller, TextAnalysisLROPoller

__all__ = [
    "TextAnalyticsApiVersion",
    "TextAnalyticsClient",
    "DetectLanguageInput",
    "TextDocumentInput",
    "DetectedLanguage",
    "RecognizeEntitiesResult",
    "DetectLanguageResult",
    "CategorizedEntity",
    "TextAnalyticsError",
    "TextAnalyticsWarning",
    "ExtractKeyPhrasesResult",
    "RecognizeLinkedEntitiesResult",
    "AnalyzeSentimentResult",
    "TextDocumentStatistics",
    "DocumentError",
    "LinkedEntity",
    "LinkedEntityMatch",
    "TextDocumentBatchStatistics",
    "SentenceSentiment",
    "SentimentConfidenceScores",
    "MinedOpinion",
    "TargetSentiment",
    "AssessmentSentiment",
    "RecognizePiiEntitiesResult",
    "PiiEntity",
    "PiiEntityDomain",
    "AnalyzeHealthcareEntitiesResult",
    "HealthcareEntity",
    "HealthcareEntityDataSource",
    "RecognizeEntitiesAction",
    "RecognizeLinkedEntitiesAction",
    "RecognizePiiEntitiesAction",
    "ExtractKeyPhrasesAction",
    "_AnalyzeActionsType",
    "PiiEntityCategory",
    "HealthcareEntityRelation",
    "HealthcareRelation",
    "HealthcareRelationRole",
    "HealthcareEntityAssertion",
    "EntityConditionality",
    "EntityCertainty",
    "EntityAssociation",
    "AnalyzeSentimentAction",
    "AnalyzeHealthcareEntitiesLROPoller",
    "AnalyzeActionsLROPoller",
    "HealthcareEntityCategory",
    "RecognizeCustomEntitiesAction",
    "RecognizeCustomEntitiesResult",
    "SingleLabelClassifyAction",
    "MultiLabelClassifyAction",
    "ClassifyDocumentResult",
    "ClassificationCategory",
    "AnalyzeHealthcareEntitiesAction",
    "TextAnalysisLROPoller",
    "TextAnalysisKind",
    "ExtractSummaryAction",
    "ExtractSummaryResult",
    "SummarySentence",
    "HealthcareDocumentType",
    "ResolutionKind",
    "AgeResolution",
    "AreaResolution",
    "CurrencyResolution",
    "DateTimeResolution",
    "InformationResolution",
    "LengthResolution",
    "NumberResolution",
    "NumericRangeResolution",
    "OrdinalResolution",
    "SpeedResolution",
    "TemperatureResolution",
    "TemporalSpanResolution",
    "VolumeResolution",
    "WeightResolution",
    "AgeUnit",
    "AreaUnit",
    "TemporalModifier",
    "InformationUnit",
    "LengthUnit",
    "NumberKind",
    "RangeKind",
    "RelativeTo",
    "SpeedUnit",
    "TemperatureUnit",
    "VolumeUnit",
    "WeightUnit",
    "AbstractiveSummaryResult",
    "AbstractiveSummary",
    "SummaryContext",
    "AbstractiveSummaryAction",
    "DateTimeSubKind",
]

__version__ = VERSION
