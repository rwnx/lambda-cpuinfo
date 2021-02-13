import json
import platform
from cpuinfo import get_cpu_info



def getcpu(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(get_cpu_info())
    }

