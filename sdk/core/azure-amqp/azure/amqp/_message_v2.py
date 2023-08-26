#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
from typing import MutableSequence, Sequence
import uuid
from datetime import datetime
from dataclasses import field
from typing_extensions import (
    Literal,
    Optional,
    Union,
    AnyStr,
    Mapping,
    Tuple,
    List
)

from ._types_v2 import (
    AMQPTypes,
    AMQPDefinition,
    AMQP_FULL_TYPES,
    AMQP_BASIC_TYPES,
    AMQP_DEFINED_TYPES,
    dataclass_decorator,
    TYPE_KEY,
    VALUE_KEY,
    AMQP_NONE
)

from .constants import MessageDeliveryState


@dataclass_decorator
class Header:
    """Transport headers for a Message.

    The header section carries standard delivery details about the transfer of a Message through the AMQP
    network. If the header section is omitted the receiver MUST assume the appropriate default values for
    the fields within the header unless other target or node specific defaults have otherwise been set."""

    durable: Optional[bool]  = None
    """Specify durability requirements.
        Durable Messages MUST NOT be lost even if an intermediary is unexpectedly terminated and restarted.
        A target which is not capable of fulfilling this guarantee MUST NOT accept messages where the durable
        header is set to true: if the source allows the rejected outcome then the message should be rejected
        with the precondition-failed error, otherwise the link must be detached by the receiver with the same error."""
    priority: Optional[int] = None
    """Relative Message priority.
        This field contains the relative Message priority. Higher numbers indicate higher priority Messages.
        Messages with higher priorities MAY be delivered before those with lower priorities. An AMQP intermediary
        implementing distinct priority levels MUST do so in the following manner:
        
            - If n distince priorities are implemented and n is less than 10 - priorities 0 to (5 - ceiling(n/2))
              MUST be treated equivalently and MUST be the lowest effective priority. The priorities (4 + fioor(n/2))
              and above MUST be treated equivalently and MUST be the highest effective priority. The priorities
              (5 ceiling(n/2)) to (4 + fioor(n/2)) inclusive MUST be treated as distinct priorities.
            - If n distinct priorities are implemented and n is 10 or greater - priorities 0 to (n - 1) MUST be
              distinct, and priorities n and above MUST be equivalent to priority (n - 1). Thus, for example, if 2
              distinct priorities are implemented, then levels 0 to 4 are equivalent, and levels 5 to 9 are equivalent
              and levels 4 and 5 are distinct. If 3 distinct priorities are implements the 0 to 3 are equivalent,
              5 to 9 are equivalent and 3, 4 and 5 are distinct. This scheme ensures that if two priorities are distinct
              for a server which implements m separate priority levels they are also distinct for a server which
              implements n different priority levels where n > m."""
    ttl: Optional[int] = None
    """Time to live in ms.
        Duration in milliseconds for which the Message should be considered 'live'. If this is set then a message
        expiration time will be computed based on the time of arrival at an intermediary. Messages that live longer
        than their expiration time will be discarded (or dead lettered). When a message is transmitted by an
        intermediary that was received with a ttl, the transmitted message's header should contain a ttl that is
        computed as the difference between the current time and the formerly computed message expiration
        time, i.e. the reduced ttl, so that messages will eventually die if they end up in a delivery loop."""
    first_acquirer: Optional[bool] = None
    """If this value is true, then this message has not been acquired by any other Link.
        If this value is false, then this message may have previously been acquired by another Link or Links."""
    delivery_count: Optional[int] = None, 
    """The number of prior unsuccessful delivery attempts.
        The number of unsuccessful previous attempts to deliver this message. If this value is non-zero it may
        be taken as an indication that the delivery may be a duplicate. On first delivery, the value is zero.
        It is incremented upon an outcome being settled at the sender, according to rules defined for each outcome."""
    _code: Literal[0x00000070] = field(default=0x00000070, init=False, repr=False, hash=False)

    def _describe(self) -> AMQPDefinition[AMQPTypes.described, Tuple[AMQPDefinition[AMQPTypes.ulong, int], AMQPDefinition[AMQPTypes.list, List[AMQPDefinition]]]]:
        body: List[AMQPDefinition] = []
        if self.delivery_count is not None:
            body = [
                AMQP_NONE if self.durable is None else {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.durable},
                AMQP_NONE if self.priority is None else {TYPE_KEY: AMQPTypes.ubyte, VALUE_KEY: self.priority},
                AMQP_NONE if self.ttl is None else {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.ttl},
                AMQP_NONE if self.first_acquirer is None else {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.first_acquirer},
                {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.delivery_count},
            ]
        elif self.first_acquirer is not None:
            body = [
                AMQP_NONE if self.durable is None else {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.durable},
                AMQP_NONE if self.priority is None else {TYPE_KEY: AMQPTypes.ubyte, VALUE_KEY: self.priority},
                AMQP_NONE if self.ttl is None else {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.ttl},
                {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.first_acquirer},
            ]
        elif self.ttl is not None:
            body = [
                AMQP_NONE if self.durable is None else {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.durable},
                AMQP_NONE if self.priority is None else {TYPE_KEY: AMQPTypes.ubyte, VALUE_KEY: self.priority},
                {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.ttl},
            ]
        elif self.priority is not None:
            body = [
                AMQP_NONE if self.durable is None else {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.durable},
                {TYPE_KEY: AMQPTypes.ubyte, VALUE_KEY: self.priority},
            ]
        elif self.durable is not None:
            body = [
                {TYPE_KEY: AMQPTypes.boolean, VALUE_KEY: self.durable},
            ]
        return {
            TYPE_KEY: AMQPTypes.described,
            VALUE_KEY: (
                {TYPE_KEY: AMQPTypes.ulong, VALUE_KEY: self._code},
                {TYPE_KEY: AMQPTypes.list, VALUE_KEY: body},
            ),
        }


@dataclass_decorator
class Properties:
    message_id: Optional[Union[int, uuid.UUID, bytes, str]] = None
    """Application Message identifier.
        Message-id is an optional property which uniquely identifies a Message within the Message system.
        The Message producer is usually responsible for setting the message-id in such a way that it is assured
        to be globally unique. A broker MAY discard a Message as a duplicate if the value of the message-id
        matches that of a previously received Message sent to the same Node."""
    user_id: Optional[Union[bytes, bytearray]] = None
    """Creating user id.
        The identity of the user responsible for producing the Message. The client sets this value, and it MAY
        be authenticated by intermediaries."""
    to: Optional[AnyStr] = None
    """The address of the Node the Message is destined for.
        The to field identifies the Node that is the intended destination of the Message. On any given transfer
        this may not be the Node at the receiving end of the Link."""
    subject: Optional[AnyStr] = None
    """The subject of the message.
        A common field for summary information about the Message content and purpose."""
    reply_to: Optional[AnyStr] = None
    """The Node to send replies to. The address of the Node to send replies to."""
    correlation_id: Optional[Union[int, uuid.UUID, bytes, str]] = None
    """Application correlation identifier.
        This is a client-specific id that may be used to mark or identify Messages between clients."""
    content_type: Optional[AnyStr] = None
    """MIME content type.
        The RFC-2046 MIME type for the Message's application-data section (body). As per RFC-2046 this may contain
        a charset parameter defining the character encoding used: e.g. 'text/plain; charset="utf-8"'.
        For clarity, the correct MIME type for a truly opaque binary section is application/octet-stream.
        When using an application-data section with a section code other than data, contenttype, if set, SHOULD
        be set to a MIME type of message/x-amqp+?, where '?' is either data, map or list."""
    content_encoding: Optional[AnyStr] = None
    """MIME content type.
        The Content-Encoding property is used as a modifier to the content-type. When present, its value indicates
        what additional content encodings have been applied to the application-data, and thus what decoding
        mechanisms must be applied in order to obtain the media-type referenced by the content-type header field.
        Content-Encoding is primarily used to allow a document to be compressed without losing the identity of
        its underlying content type. Content Encodings are to be interpreted as per Section 3.5 of RFC 2616.
        Valid Content Encodings are registered at IANA as "Hypertext Transfer Protocol (HTTP) Parameters"
        (http://www.iana.org/assignments/http-parameters/httpparameters.xml). Content-Encoding MUST not be set when
        the application-data section is other than data. Implementations MUST NOT use the identity encoding.
        Instead, implementations should not set this property. Implementations SHOULD NOT use the compress
        encoding, except as to remain compatible with messages originally sent with other protocols,
        e.g. HTTP or SMTP. Implementations SHOULD NOT specify multiple content encoding values except as to be
        compatible with messages originally sent with other protocols, e.g. HTTP or SMTP."""
    absolute_expiry_time: Optional[Union[int, datetime]] = None
    """The time when this message is considered expired.
        An absolute time when this message is considered to be expired."""
    creation_time: Optional[Union[int, datetime]] = None
    """The time when this message was created.
        An absolute time when this message was created."""
    group_id: Optional[AnyStr] = None
    """The group this message belongs to.
        Identifies the group the message belongs to."""
    group_sequence: Optional[int] = None
    """The sequence-no of this message within its group.
        The relative position of this message within its group."""
    reply_to_group_id: Optional[AnyStr] = None
    """The group the reply message belongs to.
        This is a client-specific id that is used so that client can send replies to this message to a specific group."""
    _code: Literal[0x00000073] = field(default=0x00000073, init=False, repr=False, hash=False)

    def _describe(self) -> AMQPDefinition[AMQPTypes.described, Tuple[AMQPDefinition[AMQPTypes.ulong, int], AMQPDefinition[AMQPTypes.list, List[AMQPDefinition]]]]:
        body: List[AMQPDefinition] = []
        if self.reply_to_group_id is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                AMQP_NONE if self.content_encoding is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
                AMQP_NONE if self.absolute_expiry_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.absolute_expiry_time},
                AMQP_NONE if self.creation_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.creation_time},
                AMQP_NONE if self.group_id is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.group_id},
                AMQP_NONE if self.group_sequence is None else {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.group_sequence},
                {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to_group_id},
            ]
        elif self.group_sequence is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                AMQP_NONE if self.content_encoding is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
                AMQP_NONE if self.absolute_expiry_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.absolute_expiry_time},
                AMQP_NONE if self.creation_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.creation_time},
                AMQP_NONE if self.group_id is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.group_id},
                {TYPE_KEY: AMQPTypes.uint, VALUE_KEY: self.group_sequence},
            ]
        elif self.group_id is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                AMQP_NONE if self.content_encoding is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
                AMQP_NONE if self.absolute_expiry_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.absolute_expiry_time},
                AMQP_NONE if self.creation_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.creation_time},
                {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.group_id},
            ]
        elif self.creation_time is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                AMQP_NONE if self.content_encoding is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
                AMQP_NONE if self.absolute_expiry_time is None else {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.absolute_expiry_time},
                {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.creation_time},
            ]
        elif self.absolute_expiry_time is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                AMQP_NONE if self.content_encoding is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
                {TYPE_KEY: AMQPTypes.timestamp, VALUE_KEY: self.absolute_expiry_time},
            ]
        elif self.content_encoding is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                AMQP_NONE if self.content_type is None else {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
                {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_encoding},
            ]
        elif self.content_type is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                AMQP_NONE if self.correlation_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
                {TYPE_KEY: AMQPTypes.symbol, VALUE_KEY: self.content_type},
            ]
        elif self.correlation_id is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                AMQP_NONE if self.reply_to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
                {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.correlation_id},
            ]
        elif self.reply_to is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                AMQP_NONE if self.subject is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
                {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.reply_to},
            ]
        elif self.subject is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                AMQP_NONE if self.to is None else {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
                {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.subject},
            ]
        elif self.to is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                AMQP_NONE if self.user_id is None else {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},
                {TYPE_KEY: AMQPTypes.string, VALUE_KEY: self.to},
            ]
        elif self.user_id is not None:
            body = [
                AMQP_NONE if self.message_id is None else {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
                {TYPE_KEY: AMQPTypes.binary, VALUE_KEY: self.user_id},

            ]
        elif self.message_id is not None:
            body = [
                {TYPE_KEY: AMQPTypes.message_id, VALUE_KEY: self.message_id},
            ]
        return {
            TYPE_KEY: AMQPTypes.described,
            VALUE_KEY: (
                {TYPE_KEY: AMQPTypes.ulong, VALUE_KEY: self._code},
                {TYPE_KEY: AMQPTypes.list, VALUE_KEY: body},
            ),
        }

@dataclass_decorator
class Message:
    """An annotated message consists of the bare message plus sections for annotation at the head and tail of the bare message.

    There are two classes of annotations: annotations that travel with the message indefinitely, and
    annotations that are consumed by the next node.
    The exact structure of a message, together with its encoding, is defined by the message format. This document
    defines the structure and semantics of message format 0 (MESSAGE-FORMAT). Altogether a message consists of the
    following sections:

        - Zero or one header.
        - Zero or one delivery-annotations.
        - Zero or one message-annotations.
        - Zero or one properties.
        - Zero or one application-properties.
        - The body consists of either: one or more data sections, one or more amqp-sequence sections,
          or a single amqp-value section.
        - Zero or one footer."""

    header: Optional[Header] = None
    """Transport headers for a Message.
        The header section carries standard delivery details about the transfer of a Message through the AMQP
        network. If the header section is omitted the receiver MUST assume the appropriate default values for
        the fields within the header unless other target or node specific defaults have otherwise been set."""
    delivery_annotations: Optional[Mapping[Union[AnyStr, int], AMQP_DEFINED_TYPES]] = None
    """The delivery-annotations section is used for delivery-specific non-standard
        properties at the head of the message. Delivery annotations convey information from the sending peer to
        the receiving peer. If the recipient does not understand the annotation it cannot be acted upon and its
        effects (such as any implied propagation) cannot be acted upon. Annotations may be specific to one
        implementation, or common to multiple implementations. The capabilities negotiated on link attach and on
        the source and target should be used to establish which annotations a peer supports. A registry of defined
        annotations and their meanings can be found here: http://www.amqp.org/specification/1.0/delivery-annotations.
        If the delivery-annotations section is omitted, it is equivalent to a delivery-annotations section
        containing an empty map of annotations."""
    message_annotations: Optional[Mapping[Union[AnyStr, int], AMQP_DEFINED_TYPES]] = None
    """The message-annotations section is used for properties of the message which
        are aimed at the infrastructure and should be propagated across every delivery step. Message annotations
        convey information about the message. Intermediaries MUST propagate the annotations unless the annotations
        are explicitly augmented or modified (e.g. by the use of the modified outcome).
        The capabilities negotiated on link attach and on the source and target may be used to establish which
        annotations a peer understands, however it a network of AMQP intermediaries it may not be possible to know
        if every intermediary will understand the annotation. Note that for some annotation it may not be necessary
        for the intermediary to understand their purpose - they may be being used purely as an attribute which can be
        filtered on. A registry of defined annotations and their meanings can be found here:
        http://www.amqp.org/specification/1.0/message-annotations. If the message-annotations section is omitted,
        it is equivalent to a message-annotations section containing an empty map of annotations."""
    properties: Optional[Properties] = None
    """Immutable properties of the Message.
        The properties section is used for a defined set of standard properties of the message. The properties
        section is part of the bare message and thus must, if retransmitted by an intermediary, remain completely
        unaltered."""
    application_properties: Optional[Mapping[str, Union[AMQPDefinition, AMQP_BASIC_TYPES]]] = None
    """The application-properties section is a part of the bare message used
        for structured application data. Intermediaries may use the data within this structure for the purposes
        of filtering or routing. The keys of this map are restricted to be of type string (which excludes the
        possibility of a null key) and the values are restricted to be of simple types only (that is excluding
        map, list, and array types)."""
    data: Optional[Sequence[Union[bytes, bytearray]]] = None
    """A data section contains opaque binary data."""
    sequence: Optional[Sequence[AMQP_FULL_TYPES]] = None
    """A sequence section contains an arbitrary number of structured data elements."""
    value: Optional[AMQP_FULL_TYPES] = None
    """An amqp-value section contains a single AMQP value."""
    footer: Optional[Mapping[Union[AnyStr, int], AMQP_DEFINED_TYPES]] = None
    """Transport footers for a Message.
        The footer section is used for details about the message or delivery which can only be calculated or
        evaluated once the whole bare message has been constructed or seen (for example message hashes, HMACs,
        signatures and encryption details). A registry of defined footers and their meanings can be found
        here: http://www.amqp.org/specification/1.0/footer."""
    format: Literal[0] = field(default=0, init=False, repr=False, hash=False)


@dataclass_decorator
class BatchMessage(Message):
    format: Literal[0x80013700] = field(default=0x80013700, init=False, repr=False, hash=False)


@dataclass_decorator
class _MessageDelivery:
    """Used internally for storing the state of an outgoing Message."""

    message: Message
    state: MessageDeliveryState = MessageDeliveryState.WaitingToBeSent
    expiry: Optional[int] = None
    reason: Optional[str] = field(default=None, init=False)
    delivery: Optional[str] = field(default=None, init=False)
    error: Optional[Exception] = field(default=None, init=False)
