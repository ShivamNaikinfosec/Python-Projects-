import boto3
import time
from datetime import datetime

# Initialize the AWS Timestream Write Client
timestream_client = boto3.client('timestream-write', region_name='us-east-1')

DATABASE_NAME = "WeatherSmartyDB"
TABLE_NAME = "GroundTruthReports"

def stream_forum_post_to_timestream(post_data):
    """
    Call this function inside social.py whenever an ingester parses 
    or a user creates a severe weather report thread.
    """
    current_time_ms = str(int(time.time() * 1000))
    
    # Dimensions are your metadata attributes (categorical fields used for filtering)
    dimensions = [
        {'Name': 'source_platform', 'Value': post_data.get('source_platform', 'native')},
        {'Name': 'author_role', 'Value': post_data.get('author_role', 'CHASER')},
        # Combine Lat/Lon into a string or separate them into dimensions
        {'Name': 'latitude', 'Value': str(post_data.get('latitude', 0.0))},
        {'Name': 'longitude', 'Value': str(post_data.get('longitude', 0.0))}
    ]
    
    # Records contain the actual numerical/textual measurements
    record = {
        'Dimensions': dimensions,
        'MeasureName': 'severe_threat_indicators',
        'MeasureValue': post_data.get('raw_text', ''),
        'MeasureValueType': 'VARCHAR',
        'Time': current_time_ms,
        'TimeUnit': 'MILLISECONDS'
    }
    
    try:
        response = timestream_client.write_records(
            DatabaseName=DATABASE_NAME,
            TableName=TABLE_NAME,
            Records=[record]
        )
        return response
    except Exception as e:
        print(f"Failed to stream ground truth data to AWS Timestream: {str(e)}")
        # Implement local dead-letter logging fallback here
