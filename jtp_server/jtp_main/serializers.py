from rest_framework import serializers


class TranspilerSerializer(serializers.Serializer):
    """
    Serializes data related to the Java to Python Transpiler.
    """

    python_source_code = serializers.CharField(max_length=500)

