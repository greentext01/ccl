from caracal.util.de_camel_case import de_camel_case


def bundle_sprite(sprite, blocks, costumes):
    return {
        "isStage": sprite.is_stage,
        "name": de_camel_case(sprite.__name__),
        "variables": {},
        "lists": {},
        "broadcasts": {},
        "blocks": blocks,
        "comments": {},
        "currentCostume": sprite.start_costume,
        "costumes": costumes,
        "sounds": [],
        "volume": sprite.volume,
        "layerOrder": sprite.start_layer,
        "tempo": sprite.tempo,
        "videoTransparency": sprite.video_transparency,
        "videoState": sprite.video_state,
        "textToSpeechLanguage": sprite.text_to_speech_language,
    }
