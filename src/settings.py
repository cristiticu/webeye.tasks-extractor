from dotenv import load_dotenv
import os

load_dotenv('.env')

ENVIRONMENT = os.environ.get('ENVIRONMENT')
AWS_REGION = os.environ.get('AWS_REGION', '')
RESOURCE_PREFIX = "production" if ENVIRONMENT == "production" else "stage"

DYNAMODB_URL_OVERRIDE = os.environ.get('DYNAMODB_URL_OVERRIDE')
TABLE_PREFIX = os.environ.get('TABLE_PREFIX', RESOURCE_PREFIX)
SCHEDULED_TASKS_TABLE_NAME = "webeye.scheduled-tasks"
SCHEDULED_TASKS_TABLE_REGION = "eu-central-1"
SCHEDULED_TASKS_SCHEDULE_GSI = "schedule-gsi"

AVAILABLE_FREQUENCIES = [1, 2, 5, 10, 15, 30]
AVAILABLE_DAY_FILTERS = ["all", "weekdays", "weekend"]

SQS_QUEUE_URL_BASE = "https://sqs.eu-central-1.amazonaws.com/396913704378"
SQS_CHECK_QUEUE_URL = f"{SQS_QUEUE_URL_BASE}/{RESOURCE_PREFIX}_webeye-check-queue"
SQS_AGGREGATIONS_QUEUE_URL = f"{SQS_QUEUE_URL_BASE}/{RESOURCE_PREFIX}_webeye-aggregate-queue"
