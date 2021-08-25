from google.cloud import translate

projectId = "swetha-test-project-245110"
loc = "global"


def detect_language(text, project_id=projectId):
    """Detecting the language of a text string."""

    client = translate.TranslationServiceClient()

    location = loc

    parent = f"projects/{project_id}/locations/{location}"

    response = client.detect_language(
        content=text,
        parent=parent,
        mime_type="text/plain",
    )

    for language in response.languages:
        print("Language code: {}".format(language.language_code))
        print("Confidence: {}".format(language.confidence))
        return language.language_code


def translate_text(text, project_id=projectId):
    """Translating Text."""

    language_detected = detect_language(text)

    if language_detected != 'en':
        client = translate.TranslationServiceClient()

        location = "global"

        parent = f"projects/{project_id}/locations/{location}"

        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": language_detected,
                "target_language_code": "en",
            }
        )

        for translation in response.translations:
            print("Translated text: {}".format(translation.translated_text))
            return translation.translated_text
