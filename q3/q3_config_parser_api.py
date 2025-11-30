import json
import sqlite3
import configparser
from flask import Flask, jsonify

CONFIG_FILE = "config.ini"
DB_FILE = "config_data.db"

app = Flask(__name__)


def parse_config(file_path: str) -> dict:
    """
    Reads the INI config file and returns a nested dict.
    Handles errors gracefully.
    """
    config = configparser.ConfigParser()
    try:
        read_files = config.read(file_path)
        if not read_files:
            raise FileNotFoundError(f"Config file '{file_path}' not found or unreadable.")

        result = {}
        for section in config.sections():
            result[section] = {}
            for key, value in config.items(section):
                result[section][key] = value

        return result

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return {}
    except configparser.Error as e:
        print(f"❌ Error parsing config file: {e}")
        return {}


def init_db():
    """Create table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS config_store (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_config_to_db(config_data: dict):
    """
    Saves given dict as JSON into SQLite.
    """
    if not config_data:
        print("⚠️ No configuration data to save.")
        return

    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        json_data = json.dumps(config_data)
        cur.execute("INSERT INTO config_store (data) VALUES (?)", (json_data,))
        conn.commit()
        conn.close()
        print("✅ Configuration data saved to database.")
    except sqlite3.Error as e:
        print(f"❌ Error saving data to database: {e}")


def get_latest_config_from_db() -> dict:
    """
    Returns the latest config JSON from DB as dict.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("SELECT data FROM config_store ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        conn.close()
        if row:
            return json.loads(row[0])
        return {}
    except sqlite3.Error as e:
        print(f"❌ Error fetching data from database: {e}")
        return {}


@app.route("/config", methods=["GET"])
def get_config():
    """
    GET /config
    Returns last saved config as JSON.
    """
    data = get_latest_config_from_db()
    if not data:
        return jsonify({"error": "No configuration data found"}), 404
    return jsonify(data), 200


def print_config_human_readable(config_data: dict):
    """
    Prints sample output like in the question.
    """
    if not config_data:
        print("⚠️ No configuration data to display.")
        return

    print("Configuration File Parser Results:")

    for section, kv_pairs in config_data.items():
        print(f"\n{section}:")
        for key, value in kv_pairs.items():
            print(f"- {key}: {value}")


if __name__ == "__main__":
    # 1) Initialize DB & parse config
    init_db()
    config_data = parse_config(CONFIG_FILE)

    # 2) Print in the required format
    print_config_human_readable(config_data)

    # 3) Save to DB as JSON
    save_config_to_db(config_data)

    # 4) Start Flask API for GET request
    print("\nStarting API server at http://127.0.0.1:5000/config")
    app.run(debug=True)
