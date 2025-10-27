from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TranspilerSerializer
from java_to_python_transpiler import TranspilerFailure, java_to_python_from_string

@api_view(['POST'])
def transpiler(request):
    class Transpiler:
        def __init__(self, python_source_code):
            self.python_source_code = python_source_code

    java_source_code = request.data.get("java_source_code", "")
    result: str | TranspilerFailure = java_to_python_from_string(java_source_code)
    python_source_code: str = (
        result.error_message if isinstance(result, TranspilerFailure) else result
    )

    transpiler_obj = Transpiler(python_source_code)
    serializer = TranspilerSerializer(transpiler_obj)

    return Response(serializer.data)

