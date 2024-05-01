import typing
from marshmallow import Schema as DefaultSchema

from .validate import Range
from .fields import Integer, List, Nested, Field


class Schema(DefaultSchema):
    schema_title: str
    schema_description: str

    fields: typing.Dict[str, Field]

    @classmethod
    def pagination(cls):
        class PaginationResponse(Schema):
            total = Integer(required=True, validate=Range(min=0))
            data = List(Nested(cls()), required=True)
        return PaginationResponse()

    def openapi_schema(self):
        schema = dict(
            type='object',
            properties=dict(),
            required=list()
        )
        if hasattr(self, 'title'):
            schema['title'] = self.title
        else:
            schema['title'] = self.__class__.__name__
        if hasattr(self, 'schema_description'):
            schema['properties']['description'] = self.schema_description
        for field_name in self.fields:
            if self.only and field_name not in self.only:
                continue
            field = self.fields[field_name]
            property_name = field.data_key or field_name
            schema['properties'][property_name] = field.openapi_schema()
            if field.required is True:
                schema['required'].append(property_name)

        if self.many is True:
            schema = dict(
                title=schema['title'],
                type='array',
                items=schema
            )
        return schema





