from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TranspilerSerializer
from java_to_python_transpiler import TranspilerFailure, java_to_python_from_string

@api_view(['POST'])
def transpiler(request):
    """
    The only api view for this project. Accepts a POST request with Java source code
    and returns the transpiled Python source code or an error message.
    """

    # Outputted/Transpiled source code is put in an object for serialization
    class Transpiler:
        def __init__(self, source_code: str):

            # `python_source_code` is what will be accessed on the frontend when
            # the response is received and deserialized into JSON.
            self.python_source_code = source_code

    java_source_code: str = request.data.get("java_source_code", "")
    result: str | TranspilerFailure = java_to_python_from_string(java_source_code)
    python_source_code: str = (
        result.error_message if isinstance(result, TranspilerFailure) else result
    )

    transpiler_obj = Transpiler(python_source_code)
    serializer = TranspilerSerializer(transpiler_obj)

    return Response(serializer.data)
