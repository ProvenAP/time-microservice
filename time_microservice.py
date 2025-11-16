"""
Time Microservice - CS361

Three endpoints:

GET /time/current - Returns current UTC time
GET /time/timezone?timezone=<tz> - Returns time in specified timezone
GET /time/military - Returns time in 24-hour military format

"""

from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/time/current', methods=['GET'])
def get_current_time():
    current_time = datetime.now(pytz.UTC)
    
    response = {
        "success": True,
        "current_time": current_time.isoformat(),
        "timezone": "UTC",
        "formatted_time": current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    }
    
    return jsonify(response), 200


@app.route('/time/timezone', methods=['GET'])
def get_timezone_time():
    timezone_str = request.args.get('timezone')
    
    if not timezone_str:
        return jsonify({
            "success": False,
            "error": "timezone parameter is required"
        }), 400
    
    try:
        tz = pytz.timezone(timezone_str)
    except:
        return jsonify({
            "success": False,
            "error": f"Invalid timezone: {timezone_str}"
        }), 400
    
    current_time = datetime.now(tz)
    
    response = {
        "success": True,
        "current_time": current_time.isoformat(),
        "timezone": timezone_str,
        "formatted_time": current_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")
    }
    
    return jsonify(response), 200


@app.route('/time/military', methods=['GET'])
def get_military_time():
    current_time = datetime.now(pytz.UTC)
    military_time = current_time.strftime("%H:%M:%S")
    
    response = {
        "success": True,
        "military_time": military_time,
        "timezone": "UTC",
        "format": "24-hour"
    }
    
    return jsonify(response), 200


if __name__ == '__main__':
    print("Starting Time Microservice on http://localhost:3000")
    app.run(host='0.0.0.0', port=3000, debug=True)