from app.caption.styles import get_style_prompt


def test_formal():

    prompt = get_style_prompt("formal")

    assert "formal" in prompt.lower()


def test_sarcastic():

    prompt = get_style_prompt("sarcastic")

    assert "sarcastic" in prompt.lower()