# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import pdb

from nio.events import (
    BadEvent,
    RedactedEvent,
    RoomTopicEvent,
    RoomNameEvent,
    RoomAliasEvent,
    RoomMessageText,
    RoomMessageEmote,
    PowerLevelsEvent
)


class TestClass(object):
    @staticmethod
    def _load_response(filename):
        # type: (str) -> Dict[Any, Any]
        with open(filename) as f:
            return json.loads(f.read(), encoding="utf-8")

    def test_redacted_event(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/redacted.json")
        response = RedactedEvent.from_dict(parsed_dict)
        assert isinstance(response, RedactedEvent)

    def test_malformed_event(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/redacted_invalid.json")
        response = RedactedEvent.from_dict(parsed_dict)
        assert isinstance(response, BadEvent)

    def test_topic_event(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/topic.json")
        event = RoomTopicEvent.from_dict(parsed_dict)
        assert isinstance(event, RoomTopicEvent)

    def test_name_event(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/name.json")
        event = RoomNameEvent.from_dict(parsed_dict)
        assert isinstance(event, RoomNameEvent)

    def test_alias_event(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/alias.json")
        event = RoomAliasEvent.from_dict(parsed_dict)
        assert isinstance(event, RoomAliasEvent)

    def test_message_text(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/message_text.json")
        event = RoomMessageText.from_dict(parsed_dict)
        assert isinstance(event, RoomMessageText)

    def test_message_emote(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/message_emote.json")
        event = RoomMessageEmote.from_dict(parsed_dict)
        assert isinstance(event, RoomMessageEmote)

    def test_power_levels(self):
        parsed_dict = TestClass._load_response(
            "tests/data/events/power_levels.json")
        event = PowerLevelsEvent.from_dict(parsed_dict)
        assert isinstance(event, PowerLevelsEvent)