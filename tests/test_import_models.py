import re


def test_import_draft_normalizes_required_fields():
    from scripts import ImportDraft

    draft = ImportDraft.from_mapping(
        {
            "title": "  Hello\nWorld  ",
            "source_type": "  Web  ",
            "source_url": " https://example.com/a?b=1 ",
            "content": "Line1\r\nLine2\n",
            "tags": ["  a ", None, "b", ""],
        }
    )

    assert draft.title == "Hello World"
    assert draft.source_type == "web"
    assert draft.source_url == "https://example.com/a?b=1"
    assert draft.tags == ["a", "b"]

    assert re.fullmatch(r"[0-9a-f]{64}", draft.source_id)
    assert re.fullmatch(r"[0-9a-f]{64}", draft.content_hash)


def test_import_draft_hashes_are_stable():
    from scripts import ImportDraft

    payload = {
        "title": "Test",
        "source_type": "web",
        "source_url": "https://example.com/x",
        "content": "same content",
    }
    one = ImportDraft.from_mapping(payload)
    two = ImportDraft.from_mapping(payload)

    assert one.source_id == two.source_id
    assert one.content_hash == two.content_hash
