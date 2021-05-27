import datetime
import json
import uuid
from threading import Thread

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Uuid.model_files.uuid_model import Uuid
from Uuid.threaded_uuid_saver import t_uuid_saver


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_uuid(request):
    try:
        uuid_dict = []
        timestamp = datetime.datetime.utcnow()
        uuid_value = uuid.uuid4().hex

        uuid_d = {str(timestamp): uuid_value}
        uuid_saved = Uuid.objects.all().order_by('-id')

        # Payload for background thread
        dict_payload = {
            'value': uuid_d
        }

        # Append latest pair to list
        uuid_dict.append(
            uuid_d
        )

        # Spin thread to save latest
        Thread(target=t_uuid_saver, kwargs=dict_payload).start()

        for i in uuid_saved:
            uuid_dict.append(
                # Cast to valid json
                json.loads(i.value.replace("'", '"'))
            )
        return Response({
            "responsecode": "200",
            "responsemessage": "UUID successfully generated",
            "data": uuid_dict

        })

    except Exception as e:
        print("Error at get_uuid: ", str(e))
        return Response({
            "responsecode": "403",
            "responsemessage": "something went wrong",
            "data": []

        })
