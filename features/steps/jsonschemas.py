

sample_json_schema = """
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "uuid": {"type": "string"},
    "name": {"type": "string"},
    "sys_name": {"type": "string"},
    "short_name": {"type": "string"},
    "activity_code": {"type": ["string", "null"]},
    "id": {"type": "integer"},
    "creation_datetime": {"type": "string"},
    "ar_code": {"type": ["string", "null"]},
    "active": {"type": "integer"},
    "modification_datetime": {"type": "string"},
    "account_code": {"type": ["string", "null"]},
    "type": {"type": "string"},
    "rrd_name": {"type": ["string", "null"]}
  },
  "required": [
    "uuid",
    "name",
    "sys_name",
    "short_name",
    "activity_code",
    "id",
    "creation_datetime",
    "ar_code",
    "active",
    "modification_datetime",
    "account_code",
    "type",
    "rrd_name"
  ]
}
"""