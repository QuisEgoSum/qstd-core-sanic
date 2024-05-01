import enum
import typing
import uuid
import ipaddress
import datetime

from marshmallow import fields, types
from marshmallow.utils import missing as missing_

from qstd_core.marshmallow import Schema

T = typing.TypeVar('T')


class Field(fields.Field, typing.Generic[T]):
    field_name: str
    deprecated: typing.Optional[bool]
    name: str

    def __init__(
        self,
        *,
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...

    def openapi_schema(self) -> dict: ...


class Raw(Field[typing.Any], fields.Raw): ...


class Nested(Field[typing.Any], fields.Raw):
    def __init__(
        self,
        # Nested args
        nested: fields.SchemaABC
        | type
        | str
        | dict[str, fields.Field | type]
        | typing.Callable[[], fields.SchemaABC | type | dict[str, fields.Field | type]],
        *,
        only: types.StrSequenceOrSet | None = None,
        exclude: types.StrSequenceOrSet = (),
        many: bool = False,
        unknown: str | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Pluck(Field[typing.Any], fields.Pluck):
    def __init__(
        self,
        # Pluck args
        nested: fields.SchemaABC | type | str | typing.Callable[[], fields.SchemaABC],
        field_name: str,
        *,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class List(Field[typing.List[T]], fields.List):
    def __init__(
        self,
        # List args
        cls_or_instance: Field[T] | type,
        *,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Tuple(Field[tuple], fields.Tuple):

    def __init__(
        self,
        # Tuple args
        tuple_fields: typing.List[Field | typing.Tuple[Field]],
        *,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class String(Field[str], fields.String): ...


class UUID(Field[uuid.UUID], fields.UUID): ...



class Number(Field[typing.Union[float, int, str]], fields.Number):
    def __init__(
        self,
        *,
        # Number args
        as_string: bool = False,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Integer(Field[int], fields.Integer):
    def __init__(
        self,
        # Integer args
        strict: bool = False,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Float(Field[float], fields.Float):
    def __init__(
        self,
        *,
        # Float args
        allow_nan: bool = False,
        as_string: bool = False,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Decimal(Field[Decimal], fields.Decimal):
    def __init__(
        self,
        # Decimal args
        places: int | None = None,
        rounding: str | None = None,
        *,
        allow_nan: bool = False,
        as_string: bool = False,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Boolean(Field[bool], fields.Boolean):
    def __init__(
        self,
        *,
        truthy: set | None = None,
        falsy: set | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class _DateTime(Field):
    def __init__(
        self,
        # DateTime args
        format: str | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class DateTime(_DateTime[datetime.datetime], fields.DateTime): ...


class NaiveDateTime(Field[datetime.datetime], fields.NaiveDateTime):
    def __init__(
        self,
        # NaiveDateTime args
        format: str | None = None,
        *,
        timezone: datetime.timezone | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class AwareDateTime(Field[datetime.datetime], fields.AwareDateTime):
    def __init__(
        self,
        # AwareDateTime
        format: str | None = None,
        *,
        default_timezone: datetime.tzinfo | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Time(_DateTime[datetime.time]):
    pass


class Date(Field[datetime.date], fields.Date):
    def __init__(
        self,
        # DateTime args
        format: str | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class TimeDelta(Field[datetime.timedelta], fields.TimeDelta):
    SECONDS = "seconds"
    def __init__(
        self,
        # TimeDelta args
        precision: str = SECONDS,
        serialization_type: type[int | float] = int,
        *,
        default_timezone: datetime.tzinfo | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Mapping(Field[dict], fields.Mapping):
    def __init__(
        self,
        keys: fields.Field | type | None = None,
        values: fields.Field | type | None = None,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Dict(Mapping): ...


class Url(Field[str], fields.Url):
    def __init__(
        self,
        *,
        # Url args
        relative: bool = False,
        absolute: bool = True,
        schemes: types.StrSequenceOrSet | None = None,
        require_tld: bool = True,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Email(String): ...


class _IP:
    def __init__(
        self,
        # IP Field
        exploded=False,
        *,
        # Field args
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any = missing_,
        missing: typing.Any = missing_,
        dump_default: typing.Any = missing_,
        default: typing.Any = missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class IP(_IP, Field[typing.Union[ipaddress.IPv4Address, ipaddress.IPv6Address]], fields.IP): ...


class IPv4(_IP, Field[ipaddress.IPv4Address], fields.IPv4): ...


class IPv6(_IP, Field[ipaddress.IPv6Address], fields.IPv6): ...


class IPInterface(
    _IP,
    Field[typing.Union[ipaddress.IPv4Interface, ipaddress.IPv6Interface]],
    fields.IPInterface
): ...


class IPv4Interface(_IP, Field[ipaddress.IPv4Interface], fields.IPv4Interface): ...


class IPv6Interface(_IP, Field[ipaddress.IPv6Interface], fields.IPv6Interface): ...


class Enum(Field[enum.Enum], fields.Enum):
    # noinspection PyShadowingNames
    def __init__(
        self,
        # Enum args
        enum,
        by_value=False,
        # Field args
        *,
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Method(Field[typing.Any], fields.Method):

    def __init__(
        self,
        serialize: str | None = None,
        deserialize: str | None = None,
        # Field args
        *,
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Function(Field[typing.Any], fields.Function):

    def __init__(
        self,
        serialize: (
            None
            | typing.Callable[[typing.Any], typing.Any]
            | typing.Callable[[typing.Any, dict], typing.Any]
        ) = None,
        deserialize: (
            None
            | typing.Callable[[typing.Any], typing.Any]
            | typing.Callable[[typing.Any, dict], typing.Any]
        ) = None,
        # Field args
        *,
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...



class Constant(Field[typing.Any], fields.Constant):
    def __init__(
        self,
        constant: typing.Any,
        # Field args
        *,
        transform: typing.Union[
            typing.Callable[[typing.Union[str, T]], T], typing.List[typing.Callable[[typing.Union[str, T]], T]]
        ] = None,
        transform_after: typing.Union[
            typing.Callable[[T], typing.Any], typing.List[typing.Callable[[T], typing.Any]]
        ] = None,
        description: str = None,
        meta_one_of: typing.List[Schema] = None,
        deprecated: bool = None,
        example: T = None,
        # Marshmallow args
        load_default: typing.Any= missing_,
        missing: typing.Any= missing_,
        dump_default: typing.Any= missing_,
        default: typing.Any= missing_,
        data_key: str | None = None,
        attribute: str | None = None,
        validate: typing.Union[
            None,
            typing.Callable[[typing.Any], typing.Any],
            typing.Iterable[typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        required: bool = False,
        allow_none: bool | None = None,
        load_only: bool = False,
        dump_only: bool = False,
        error_messages: dict[str, str] | None = None,
        metadata: typing.Mapping[str, typing.Any] | None = None,
        **additional_metadata
    ): ...


class Inferred(Field[typing.Any], fields.Inferred): ...


# Aliases
URL = Url
Str = String
Bool = Boolean
Int = Integer