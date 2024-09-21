import pika, json
import logging
import pika.spec

def upload(f, fs, channel, access):
    logging.info("Uploading video..")
    try:
        fid = fs.put(f)
    except Exception as err:
        logging.error(err)
        return "internal server error", 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }
    
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                # Persist messages in the queue in the event of a pod crash or restart (RabbitMQ pod)
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as err:
        fs.delete(fid)
        logging.error(err)
        return "internal server error", 500
    
    