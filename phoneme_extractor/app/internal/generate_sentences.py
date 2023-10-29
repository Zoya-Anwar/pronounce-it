import re

from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='pronounce-it-403503',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='my-experiment',

    # description of the experiment above
    experiment_description='my experiment description'
)

# Construct the full path to the key file
from vertexai.preview.language_models import TextGenerationModel

def generate_sentence_french(temperature: float = .2, word="travaille"):
    """Ideation example with a Large Language Model"""

    parameters = {
        "temperature": temperature,
        "max_output_tokens": 256,
        "top_p": .8,
        "top_k": 40,
    }

    # Create a TextGenerationModel
    model = TextGenerationModel.from_pretrained("text-bison@001")

    # Generate an idea in French
    response = model.predict(
        f"""Donnez une phrase de dix mots utilisant exactement ce mot {word} en français. Mettez cette phrase 
                    entre ''. 
                    """,
        **parameters,
    )

    # Use a regular expression to extract the phrase in quotes (if quotes are present)
    match = re.search(r'["\'](.*?)["\']', response.text)

    if match:
        phrase = match.group(1)
        print(response.text)
        print("Extracted Phrase:", phrase)
    else:
        phrase = response.text

    if word not in phrase.lower():
        generate_sentence_french(word=word)
    else:
        print(f"Response from Model: {phrase}")
        return phrase

if __name__ == "__main__":
    generate_sentence_french()