# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field
from ._enums import ChatRole

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ChatChoice(_model_base.Model):
    """The representation of a single prompt completion as part of an overall chat completions
    request.
    Generally, ``n`` choices are generated per provided prompt with a default value of 1.
    Token limits and other settings may limit the number of choices generated.

    All required parameters must be populated in order to send to server.

    :ivar index: The ordered index associated with this chat completions choice. Required.
    :vartype index: int
    :ivar message: The chat message for a given chat completions prompt. Required.
    :vartype message: ~azure.ai.inference.models.ChatResponseMessage
    :ivar finish_reason: The reason that this chat completions choice completed its generated.
     Required. Known values are: "stop", "length", and "content_filter".
    :vartype finish_reason: str or ~azure.ai.inference.models.CompletionsFinishReason
    """

    index: int = rest_field()
    """The ordered index associated with this chat completions choice. Required."""
    message: "_models.ChatResponseMessage" = rest_field()
    """The chat message for a given chat completions prompt. Required."""
    finish_reason: Union[str, "_models.CompletionsFinishReason"] = rest_field()
    """The reason that this chat completions choice completed its generated. Required. Known values
     are: \"stop\", \"length\", and \"content_filter\"."""

    @overload
    def __init__(
        self,
        *,
        index: int,
        message: "_models.ChatResponseMessage",
        finish_reason: Union[str, "_models.CompletionsFinishReason"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletions(_model_base.Model):
    """Representation of the response data from a chat completions request.
    Completions support a wide variety of tasks and generate text that continues from or
    "completes"
    provided prompt data.

    All required parameters must be populated in order to send to server.

    :ivar id: A unique identifier associated with this chat completions response. Required.
    :vartype id: str
    :ivar object: The response object type, which is always ``chat.completion``. Required.
    :vartype object: str
    :ivar created: The first timestamp associated with generation activity for this completions
     response,
     represented as seconds since the beginning of the Unix epoch of 00:00 on 1 Jan 1970. Required.
    :vartype created: ~datetime.datetime
    :ivar model: The model used for the chat completion. Required.
    :vartype model: str
    :ivar choices: The collection of completions choices associated with this completions response.
     Generally, ``n`` choices are generated per provided prompt with a default value of 1.
     Token limits and other settings may limit the number of choices generated. Required.
    :vartype choices: list[~azure.ai.inference.models.ChatChoice]
    :ivar usage: Usage information for tokens processed and generated as part of this completions
     operation. Required.
    :vartype usage: ~azure.ai.inference.models.CompletionsUsage
    """

    id: str = rest_field()
    """A unique identifier associated with this chat completions response. Required."""
    object: str = rest_field()
    """The response object type, which is always ``chat.completion``. Required."""
    created: datetime.datetime = rest_field(format="unix-timestamp")
    """The first timestamp associated with generation activity for this completions response,
     represented as seconds since the beginning of the Unix epoch of 00:00 on 1 Jan 1970. Required."""
    model: str = rest_field()
    """The model used for the chat completion. Required."""
    choices: List["_models.ChatChoice"] = rest_field()
    """The collection of completions choices associated with this completions response.
     Generally, ``n`` choices are generated per provided prompt with a default value of 1.
     Token limits and other settings may limit the number of choices generated. Required."""
    usage: "_models.CompletionsUsage" = rest_field()
    """Usage information for tokens processed and generated as part of this completions operation.
     Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        object: str,
        created: datetime.datetime,
        model: str,
        choices: List["_models.ChatChoice"],
        usage: "_models.CompletionsUsage",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletionsToolCall(_model_base.Model):
    """An abstract representation of a tool call that must be resolved in a subsequent request to
    perform the requested
    chat completion.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ChatCompletionsFunctionToolCall

    All required parameters must be populated in order to send to server.

    :ivar type: The object type. Required. Default value is None.
    :vartype type: str
    :ivar id: The ID of the tool call. Required.
    :vartype id: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    type: str = rest_discriminator(name="type")
    """The object type. Required. Default value is None."""
    id: str = rest_field()
    """The ID of the tool call. Required."""

    @overload
    def __init__(
        self,
        *,
        type: str,
        id: str,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletionsFunctionToolCall(ChatCompletionsToolCall, discriminator="function"):
    """A tool call to a function tool, issued by the model in evaluation of a configured function
    tool, that represents
    a function invocation needed for a subsequent chat completions request to resolve.

    All required parameters must be populated in order to send to server.

    :ivar id: The ID of the tool call. Required.
    :vartype id: str
    :ivar type: The type of tool call, in this case always 'function'. Required. Default value is
     "function".
    :vartype type: str
    :ivar function: The details of the function invocation requested by the tool call. Required.
    :vartype function: ~azure.ai.inference.models.FunctionCall
    """

    type: Literal["function"] = rest_discriminator(name="type")  # type: ignore
    """The type of tool call, in this case always 'function'. Required. Default value is \"function\"."""
    function: "_models.FunctionCall" = rest_field()
    """The details of the function invocation requested by the tool call. Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        function: "_models.FunctionCall",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, type="function", **kwargs)


class ChatCompletionsToolDefinition(_model_base.Model):
    """An abstract representation of a tool that can be used by the model to improve a chat
    completions response.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ChatCompletionsFunctionToolDefinition

    All required parameters must be populated in order to send to server.

    :ivar type: The object type. Required. Default value is None.
    :vartype type: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    type: str = rest_discriminator(name="type")
    """The object type. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        type: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletionsFunctionToolDefinition(ChatCompletionsToolDefinition, discriminator="function"):
    """The definition information for a chat completions function tool that can call a function in
    response to a tool call.

    All required parameters must be populated in order to send to server.

    :ivar type: The object name, which is always 'function'. Required. Default value is "function".
    :vartype type: str
    :ivar function: The function definition details for the function tool. Required.
    :vartype function: ~azure.ai.inference.models.FunctionDefinition
    """

    type: Literal["function"] = rest_discriminator(name="type")  # type: ignore
    """The object name, which is always 'function'. Required. Default value is \"function\"."""
    function: "_models.FunctionDefinition" = rest_field()
    """The function definition details for the function tool. Required."""

    @overload
    def __init__(
        self,
        *,
        function: "_models.FunctionDefinition",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, type="function", **kwargs)


class ChatCompletionsResponseFormat(_model_base.Model):
    """An abstract representation of a response format configuration usable by Chat Completions. Can
    be used to enable JSON
    mode.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ChatCompletionsJsonResponseFormat, ChatCompletionsTextResponseFormat

    All required parameters must be populated in order to send to server.

    :ivar type: The discriminated type for the response format. Required. Default value is None.
    :vartype type: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    type: str = rest_discriminator(name="type")
    """The discriminated type for the response format. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        type: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletionsJsonResponseFormat(ChatCompletionsResponseFormat, discriminator="json_object"):
    """A response format for Chat Completions that restricts responses to emitting valid JSON objects.

    All required parameters must be populated in order to send to server.

    :ivar type: The discriminated object type, which is always 'json_object' for this format.
     Required. Default value is "json_object".
    :vartype type: str
    """

    type: Literal["json_object"] = rest_discriminator(name="type")  # type: ignore
    """The discriminated object type, which is always 'json_object' for this format. Required. Default
     value is \"json_object\"."""


class ChatCompletionsNamedToolSelection(_model_base.Model):
    """An abstract representation of an explicit, named tool selection to use for a chat completions
    request.

    All required parameters must be populated in order to send to server.

    :ivar type: The object type. Required.
    :vartype type: str
    """

    type: str = rest_discriminator(name="type")
    """The object type. Required."""


class ChatCompletionsOptions(_model_base.Model):  # pylint: disable=too-many-instance-attributes
    """The configuration information for a chat completions request.
    Completions support a wide variety of tasks and generate text that continues from or
    "completes"
    provided prompt data.

    All required parameters must be populated in order to send to server.

    :ivar messages: The collection of context messages associated with this chat completions
     request.
     Typical usage begins with a chat message for the System role that provides instructions for
     the behavior of the assistant, followed by alternating messages between the User and
     Assistant roles. Required.
    :vartype messages: list[~azure.ai.inference.models.ChatRequestMessage]
    :ivar frequency_penalty: A value that influences the probability of generated tokens appearing
     based on their cumulative
     frequency in generated text.
     Positive values will make tokens less likely to appear as their frequency increases and
     decrease the likelihood of the model repeating the same statements verbatim.
    :vartype frequency_penalty: float
    :ivar presence_penalty: A value that influences the probability of generated tokens appearing
     based on their existing
     presence in generated text.
     Positive values will make tokens less likely to appear when they already exist and increase
     the
     model's likelihood to output new topics.
    :vartype presence_penalty: float
    :ivar temperature: The sampling temperature to use that controls the apparent creativity of
     generated completions.
     Higher values will make output more random while lower values will make results more focused
     and deterministic.
     It is not recommended to modify temperature and top_p for the same completions request as the
     interaction of these two settings is difficult to predict.
    :vartype temperature: float
    :ivar top_p: An alternative to sampling with temperature called nucleus sampling. This value
     causes the
     model to consider the results of tokens with the provided probability mass. As an example, a
     value of 0.15 will cause only the tokens comprising the top 15% of probability mass to be
     considered.
     It is not recommended to modify temperature and top_p for the same completions request as the
     interaction of these two settings is difficult to predict.
    :vartype top_p: float
    :ivar max_tokens: The maximum number of tokens to generate.
    :vartype max_tokens: int
    :ivar response_format: An object specifying the format that the model must output. Used to
     enable JSON mode.
    :vartype response_format: ~azure.ai.inference.models.ChatCompletionsResponseFormat
    :ivar stop: A collection of textual sequences that will end completions generation.
    :vartype stop: list[str]
    :ivar stream: A value indicating whether chat completions should be streamed for this request.
    :vartype stream: bool
    :ivar tools: The available tool definitions that the chat completions request can use,
     including caller-defined functions.
    :vartype tools: list[~azure.ai.inference.models.ChatCompletionsToolDefinition]
    :ivar tool_choice: If specified, the model will configure which of the provided tools it can
     use for the chat completions response. Is either a Union[str,
     "_models.ChatCompletionsToolSelectionPreset"] type or a ChatCompletionsNamedToolSelection type.
    :vartype tool_choice: str or ~azure.ai.inference.models.ChatCompletionsToolSelectionPreset or
     ~azure.ai.inference.models.ChatCompletionsNamedToolSelection
    :ivar seed: If specified, the system will make a best effort to sample deterministically such
     that repeated requests with the
     same seed and parameters should return the same result. Determinism is not guaranteed, and you
     should refer to the
     system_fingerprint response parameter to monitor changes in the backend.".
    :vartype seed: int
    """

    messages: List["_models.ChatRequestMessage"] = rest_field()
    """The collection of context messages associated with this chat completions request.
     Typical usage begins with a chat message for the System role that provides instructions for
     the behavior of the assistant, followed by alternating messages between the User and
     Assistant roles. Required."""
    frequency_penalty: Optional[float] = rest_field()
    """A value that influences the probability of generated tokens appearing based on their cumulative
     frequency in generated text.
     Positive values will make tokens less likely to appear as their frequency increases and
     decrease the likelihood of the model repeating the same statements verbatim."""
    presence_penalty: Optional[float] = rest_field()
    """A value that influences the probability of generated tokens appearing based on their existing
     presence in generated text.
     Positive values will make tokens less likely to appear when they already exist and increase the
     model's likelihood to output new topics."""
    temperature: Optional[float] = rest_field()
    """The sampling temperature to use that controls the apparent creativity of generated completions.
     Higher values will make output more random while lower values will make results more focused
     and deterministic.
     It is not recommended to modify temperature and top_p for the same completions request as the
     interaction of these two settings is difficult to predict."""
    top_p: Optional[float] = rest_field()
    """An alternative to sampling with temperature called nucleus sampling. This value causes the
     model to consider the results of tokens with the provided probability mass. As an example, a
     value of 0.15 will cause only the tokens comprising the top 15% of probability mass to be
     considered.
     It is not recommended to modify temperature and top_p for the same completions request as the
     interaction of these two settings is difficult to predict."""
    max_tokens: Optional[int] = rest_field()
    """The maximum number of tokens to generate."""
    response_format: Optional["_models.ChatCompletionsResponseFormat"] = rest_field()
    """An object specifying the format that the model must output. Used to enable JSON mode."""
    stop: Optional[List[str]] = rest_field()
    """A collection of textual sequences that will end completions generation."""
    stream: Optional[bool] = rest_field()
    """A value indicating whether chat completions should be streamed for this request."""
    tools: Optional[List["_models.ChatCompletionsToolDefinition"]] = rest_field()
    """The available tool definitions that the chat completions request can use, including
     caller-defined functions."""
    tool_choice: Optional[
        Union[str, "_models.ChatCompletionsToolSelectionPreset", "_models.ChatCompletionsNamedToolSelection"]
    ] = rest_field()
    """If specified, the model will configure which of the provided tools it can use for the chat
     completions response. Is either a Union[str, \"_models.ChatCompletionsToolSelectionPreset\"]
     type or a ChatCompletionsNamedToolSelection type."""
    seed: Optional[int] = rest_field()
    """If specified, the system will make a best effort to sample deterministically such that repeated
     requests with the
     same seed and parameters should return the same result. Determinism is not guaranteed, and you
     should refer to the
     system_fingerprint response parameter to monitor changes in the backend.\"."""

    @overload
    def __init__(
        self,
        *,
        messages: List["_models.ChatRequestMessage"],
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        response_format: Optional["_models.ChatCompletionsResponseFormat"] = None,
        stop: Optional[List[str]] = None,
        stream: Optional[bool] = None,
        tools: Optional[List["_models.ChatCompletionsToolDefinition"]] = None,
        tool_choice: Optional[
            Union[str, "_models.ChatCompletionsToolSelectionPreset", "_models.ChatCompletionsNamedToolSelection"]
        ] = None,
        seed: Optional[int] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatCompletionsTextResponseFormat(ChatCompletionsResponseFormat, discriminator="text"):
    """The standard Chat Completions response format that can freely generate text and is not
    guaranteed to produce response
    content that adheres to a specific schema.

    All required parameters must be populated in order to send to server.

    :ivar type: The discriminated object type, which is always 'text' for this format. Required.
     Default value is "text".
    :vartype type: str
    """

    type: Literal["text"] = rest_discriminator(name="type")  # type: ignore
    """The discriminated object type, which is always 'text' for this format. Required. Default value
     is \"text\"."""


class ChatRequestMessage(_model_base.Model):
    """An abstract representation of a chat message as provided in a request.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ChatRequestAssistantMessage, ChatRequestSystemMessage, ChatRequestToolMessage,
    ChatRequestUserMessage

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with this message. Required. Known values are: "system",
     "user", "assistant", and "tool".
    :vartype role: str or ~azure.ai.inference.models.ChatRole
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    role: str = rest_discriminator(name="role")
    """The chat role associated with this message. Required. Known values are: \"system\", \"user\",
     \"assistant\", and \"tool\"."""

    @overload
    def __init__(
        self,
        *,
        role: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ChatRequestAssistantMessage(ChatRequestMessage, discriminator="assistant"):
    """A request chat message representing response or action from the assistant.

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with this message, which is always 'assistant' for
     assistant messages. Required. The role that provides responses to system-instructed,
     user-prompted input.
    :vartype role: str or ~azure.ai.inference.models.ASSISTANT
    :ivar content: The content of the message. Required.
    :vartype content: str
    :ivar name: An optional name for the participant.
    :vartype name: str
    """

    role: Literal[ChatRole.ASSISTANT] = rest_discriminator(name="role")  # type: ignore
    """The chat role associated with this message, which is always 'assistant' for assistant messages.
     Required. The role that provides responses to system-instructed, user-prompted input."""
    content: str = rest_field()
    """The content of the message. Required."""
    name: Optional[str] = rest_field()
    """An optional name for the participant."""

    @overload
    def __init__(
        self,
        *,
        content: str,
        name: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, role=ChatRole.ASSISTANT, **kwargs)


class ChatRequestSystemMessage(ChatRequestMessage, discriminator="system"):
    """A request chat message containing system instructions that influence how the model will
    generate a chat completions
    response.

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with this message, which is always 'system' for system
     messages. Required. The role that instructs or sets the behavior of the assistant.
    :vartype role: str or ~azure.ai.inference.models.SYSTEM
    :ivar content: The contents of the system message. Required.
    :vartype content: str
    :ivar name: An optional name for the participant.
    :vartype name: str
    """

    role: Literal[ChatRole.SYSTEM] = rest_discriminator(name="role")  # type: ignore
    """The chat role associated with this message, which is always 'system' for system messages.
     Required. The role that instructs or sets the behavior of the assistant."""
    content: str = rest_field()
    """The contents of the system message. Required."""
    name: Optional[str] = rest_field()
    """An optional name for the participant."""

    @overload
    def __init__(
        self,
        *,
        content: str,
        name: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, role=ChatRole.SYSTEM, **kwargs)


class ChatRequestToolMessage(ChatRequestMessage, discriminator="tool"):
    """A request chat message representing requested output from a configured tool.

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with this message, which is always 'tool' for tool
     messages. Required. The role that represents extension tool activity within a chat completions
     operation.
    :vartype role: str or ~azure.ai.inference.models.TOOL
    :ivar content: The content of the message. Required.
    :vartype content: str
    :ivar tool_call_id: The ID of the tool call resolved by the provided content. Required.
    :vartype tool_call_id: str
    """

    role: Literal[ChatRole.TOOL] = rest_discriminator(name="role")  # type: ignore
    """The chat role associated with this message, which is always 'tool' for tool messages. Required.
     The role that represents extension tool activity within a chat completions operation."""
    content: str = rest_field()
    """The content of the message. Required."""
    tool_call_id: str = rest_field()
    """The ID of the tool call resolved by the provided content. Required."""

    @overload
    def __init__(
        self,
        *,
        content: str,
        tool_call_id: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, role=ChatRole.TOOL, **kwargs)


class ChatRequestUserMessage(ChatRequestMessage, discriminator="user"):
    """A request chat message representing user input to the assistant.

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with this message, which is always 'user' for user
     messages. Required. The role that provides input for chat completions.
    :vartype role: str or ~azure.ai.inference.models.USER
    :ivar content: The contents of the user message, with available input types varying by selected
     model. Required.
    :vartype content: str
    :ivar name: An optional name for the participant.
    :vartype name: str
    """

    role: Literal[ChatRole.USER] = rest_discriminator(name="role")  # type: ignore
    """The chat role associated with this message, which is always 'user' for user messages. Required.
     The role that provides input for chat completions."""
    content: str = rest_field()
    """The contents of the user message, with available input types varying by selected model.
     Required."""
    name: Optional[str] = rest_field()
    """An optional name for the participant."""

    @overload
    def __init__(
        self,
        *,
        content: str,
        name: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, role=ChatRole.USER, **kwargs)


class ChatResponseMessage(_model_base.Model):
    """A representation of a chat message as received in a response.

    All required parameters must be populated in order to send to server.

    :ivar role: The chat role associated with the message. Required. Known values are: "system",
     "user", "assistant", and "tool".
    :vartype role: str or ~azure.ai.inference.models.ChatRole
    :ivar content: The content of the message. Required.
    :vartype content: str
    :ivar tool_calls: The tool calls that must be resolved and have their outputs appended to
     subsequent input messages for the chat
     completions request to resolve as configured.
    :vartype tool_calls: list[~azure.ai.inference.models.ChatCompletionsToolCall]
    """

    role: Union[str, "_models.ChatRole"] = rest_field()
    """The chat role associated with the message. Required. Known values are: \"system\", \"user\",
     \"assistant\", and \"tool\"."""
    content: str = rest_field()
    """The content of the message. Required."""
    tool_calls: Optional[List["_models.ChatCompletionsToolCall"]] = rest_field()
    """The tool calls that must be resolved and have their outputs appended to subsequent input
     messages for the chat
     completions request to resolve as configured."""

    @overload
    def __init__(
        self,
        *,
        role: Union[str, "_models.ChatRole"],
        content: str,
        tool_calls: Optional[List["_models.ChatCompletionsToolCall"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CompletionsUsage(_model_base.Model):
    """Representation of the token counts processed for a completions request.
    Counts consider all tokens across prompts, choices, choice alternates, best_of generations, and
    other consumers.

    All required parameters must be populated in order to send to server.

    :ivar completion_tokens: The number of tokens generated across all completions emissions.
     Required.
    :vartype completion_tokens: int
    :ivar prompt_tokens: The number of tokens in the provided prompts for the completions request.
     Required.
    :vartype prompt_tokens: int
    :ivar total_tokens: The total number of tokens processed for the completions request and
     response. Required.
    :vartype total_tokens: int
    """

    completion_tokens: int = rest_field()
    """The number of tokens generated across all completions emissions. Required."""
    prompt_tokens: int = rest_field()
    """The number of tokens in the provided prompts for the completions request. Required."""
    total_tokens: int = rest_field()
    """The total number of tokens processed for the completions request and response. Required."""

    @overload
    def __init__(
        self,
        *,
        completion_tokens: int,
        prompt_tokens: int,
        total_tokens: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FunctionCall(_model_base.Model):
    """The name and arguments of a function that should be called, as generated by the model.

    All required parameters must be populated in order to send to server.

    :ivar name: The name of the function to call. Required.
    :vartype name: str
    :ivar arguments: The arguments to call the function with, as generated by the model in JSON
     format.
     Note that the model does not always generate valid JSON, and may hallucinate parameters
     not defined by your function schema. Validate the arguments in your code before calling
     your function. Required.
    :vartype arguments: str
    """

    name: str = rest_field()
    """The name of the function to call. Required."""
    arguments: str = rest_field()
    """The arguments to call the function with, as generated by the model in JSON format.
     Note that the model does not always generate valid JSON, and may hallucinate parameters
     not defined by your function schema. Validate the arguments in your code before calling
     your function. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        arguments: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FunctionDefinition(_model_base.Model):
    """The definition of a caller-specified function that chat completions may invoke in response to
    matching user input.

    All required parameters must be populated in order to send to server.

    :ivar name: The name of the function to be called. Required.
    :vartype name: str
    :ivar description: A description of what the function does. The model will use this description
     when selecting the function and
     interpreting its parameters.
    :vartype description: str
    :ivar parameters: The parameters the function accepts, described as a JSON Schema object.
    :vartype parameters: any
    """

    name: str = rest_field()
    """The name of the function to be called. Required."""
    description: Optional[str] = rest_field()
    """A description of what the function does. The model will use this description when selecting the
     function and
     interpreting its parameters."""
    parameters: Optional[Any] = rest_field()
    """The parameters the function accepts, described as a JSON Schema object."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        parameters: Optional[Any] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
