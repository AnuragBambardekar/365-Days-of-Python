import uuid
import time

def is_timestamp_based(uuid_obj):
    return uuid_obj.version == 1

def extract_timestamp(uuid_obj):
    if is_timestamp_based(uuid_obj):
        timestamp = uuid_obj.time
        return timestamp
    else:
        return None

def main():
    # Generate a timestamp-based UUID (version 1)
    timestamp_uuid = uuid.uuid1()

    # Check if the UUID is timestamp-based
    if is_timestamp_based(timestamp_uuid):
        print("This UUID is timestamp-based.")

        # Extract and print the timestamp
        timestamp = extract_timestamp(timestamp_uuid)
        print(f"Timestamp: {timestamp} (UTC)")

    else:
        print("This UUID is not timestamp-based.")

if __name__ == "__main__":
    main()
