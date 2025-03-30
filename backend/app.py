from flask import Flask, request, jsonify
from deepgram import Deepgram
from dotenv import load_dotenv
import json
import os


# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load API keys
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
GPT_API_KEY = os.getenv("GPT_API_KEY")

# Get current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct file paths
CONFIG_PATH = os.path.join(BASE_DIR, "../config/config.json")
PROMPTS_PATH = os.path.join(BASE_DIR, "../data/prompts.json")
RESULTS_PATH = os.path.join(BASE_DIR, "../data/results.json")

# Load config and prompts
with open(CONFIG_PATH) as config_file:
    config_data = json.load(config_file)

with open(PROMPTS_PATH) as prompts_file:
    prompts_data = json.load(prompts_file)

# Deepgram client setup
dg_client = Deepgram(DEEPGRAM_API_KEY)

@app.route("/")
def home():
    return "Gen AI Interviewer Backend is Running!"

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files["audio"]
        if audio_file.mimetype not in ["audio/wav", "audio/mp3", "audio/mpeg"]:
            return jsonify({"error": "Unsupported audio format"}), 400

        source = {"buffer": audio_file.read(), "mimetype": audio_file.mimetype}

        response = dg_client.transcription.sync_prerecorded(source, {"punctuate": True})
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

        return jsonify({"transcript": transcript})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/submit-response", methods=["POST"])
def submit_response():
    try:
        data = request.get_json()
        candidate_response = data.get("response", "")

        # Analyze response with GPT
        analysis_result = analyze_response_with_gpt(candidate_response)

        # Store results locally
        with open(RESULTS_PATH, "a") as results_file:
            json.dump(analysis_result, results_file)
            results_file.write("\n")

        return jsonify({"result": "Response submitted successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get-results", methods=["GET"])
def get_results():
    try:
        with open(RESULTS_PATH, "r") as results_file:
            results = results_file.readlines()
        return jsonify({"results": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_response_with_gpt(response):
    # Dummy GPT logic for now
    analysis_result = {
        "response": response,
        "score": 8,
        "verdict": "Good understanding of concepts."
    }
    return analysis_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
