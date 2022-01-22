#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from enum import Enum

LIST_TRACKS_URL = r"https://studio.youtube.com/youtubei/v1/creator_music/list_tracks?" \
                  r"alt=json&key=AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo"
GET_TRACKS_URL = r"https://studio.youtube.com/youtubei/v1/creator_music/get_tracks?" \
                 r"alt=json&key=AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo"


class SoundEffectCategory(Enum):
    CROWDS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_CROWDS"
    FOLEY = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_FOLEY"
    EMERGENCY = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_EMERGENCY"
    HUMAN_VOICES = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_HUMAN_VOICES"
    HOUSEHOLD = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_HOUSEHOLD"
    HORROR = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_HORROR"
    DOORS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_DOORS"
    CARTOON = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_CARTOON"
    ALARMS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_ALARMS"
    AMBIENCES = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_AMBIENCES"
    ANIMALS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_ANIMALS"
    IMPACTS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_IMPACTS"
    OFFICE = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_OFFICE"
    SCIENCE_FICTION = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_SCIENCE_FICTION"
    TOOLS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_TOOLS"
    SPORTS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_SPORTS"
    TRANSPORTATION = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_TRANSPORTATION"
    WATER = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_WATER"
    WEAPONS = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_WEAPONS"
    WEATHER = "CREATOR_MUSIC_SOUND_EFFECT_CATEGORY_WEATHER"


class Genre(Enum):
    HOLIDAY = "CREATOR_MUSIC_GENRE_HOLIDAY"
    JAZZ_AND_BLUES = "CREATOR_MUSIC_GENRE_JAZZ_AND_BLUES"
    ALTERNATIVE_AND_PUNK = "CREATOR_MUSIC_GENRE_ALTERNATIVE_AND_PUNK"
    AMBIENT = "CREATOR_MUSIC_GENRE_AMBIENT"
    CINEMATIC = "CREATOR_MUSIC_GENRE_CINEMATIC"
    CLASSICAL = "CREATOR_MUSIC_GENRE_CLASSICAL"
    CHILDRENS = "CREATOR_MUSIC_GENRE_CHILDRENS"
    COUNTRY_AND_FOLK = "CREATOR_MUSIC_GENRE_COUNTRY_AND_FOLK"
    HIP_HOP_AND_RAP = "CREATOR_MUSIC_GENRE_HIP_HOP_AND_RAP"
    DANCE_AND_ELECTRONICS = "CREATOR_MUSIC_GENRE_DANCE_AND_ELECTRONICS"
    POP = "CREATOR_MUSIC_GENRE_POP"
    RNB_AND_SOUL = "CREATOR_MUSIC_GENRE_RNB_AND_SOUL"
    REGGAE = "CREATOR_MUSIC_GENRE_REGGAE"
    ROCK = "CREATOR_MUSIC_GENRE_ROCK"


class Mood(Enum):
    ANGRY = "CREATOR_MUSIC_MOOD_ANGRY"
    CALM = "CREATOR_MUSIC_MOOD_CALM"
    BRIGHT = "CREATOR_MUSIC_MOOD_BRIGHT"
    DARK = "CREATOR_MUSIC_MOOD_DARK"
    FUNKY = "CREATOR_MUSIC_MOOD_FUNKY"
    DRAMATIC = "CREATOR_MUSIC_MOOD_DRAMATIC"
    HAPPY = "CREATOR_MUSIC_MOOD_HAPPY"
    INSPIRATIONAL = "CREATOR_MUSIC_MOOD_INSPIRATIONAL"
    ROMANTIC = "CREATOR_MUSIC_MOOD_ROMANTIC"
    SAD = "CREATOR_MUSIC_MOOD_SAD"


class LicenseType(Enum):
    YOUTUBE = "CREATOR_MUSIC_LICENSE_TYPE_YOUTUBE"
    CCBY_4 = "CREATOR_MUSIC_LICENSE_TYPE_CCBY_4"


class OrderDirection(Enum):
    ASC = "ORDER_DIRECTION_ASC"
    DESC = "ORDER_DIRECTION_DESC"


class OrderField(Enum):
    TRACK_TITLE = "CREATOR_MUSIC_TRACK_SORT_FIELD_TRACK_TITLE"
    ARTIST_NAME = "CREATOR_MUSIC_TRACK_SORT_FIELD_ARTIST_NAME"
    DURATION = "CREATOR_MUSIC_TRACK_SORT_FIELD_DURATION"
    RELEASE_DATE = "CREATOR_MUSIC_TRACK_SORT_FIELD_RELEASE_DATE"


@dataclass
class TrackOrder:
    orderField: OrderField
    orderDirection: OrderDirection


@dataclass
class DurationRange:
    start: int
    end: int


class TrackType(Enum):
    SOUNDEFFECT = "CREATOR_MUSIC_TRACK_TYPE_SOUNDEFFECT"
    MUSIC = "CREATOR_MUSIC_TRACK_TYPE_MUSIC"