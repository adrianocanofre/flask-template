POST_INPUT_SCHEMA = """
    {
        "type": "object",
        "additionalProperties": false,
        "properties": {
            "id": {"type": "integer"},
            "property1": {"type": "string"},
            "property2": {"type": "string"}
        },
        "required": [
            "id",
            "property1",
            "property2"
        ]
    }
    """
