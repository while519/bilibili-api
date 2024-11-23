"""
bilibili_api

哔哩哔哩的各种 API 调用便捷整合（视频、动态、直播等），另外附加一些常用的功能。
"""

import asyncio
import platform

from .utils.sync import sync
from .utils.credential_refresh import Credential
from .utils.picture import Picture
from .utils.short import get_real_url
from .utils.parse_link import ResourceType, parse_link
from .utils.aid_bvid_transformer import aid2bvid, bvid2aid
from .utils.danmaku import DmMode, Danmaku, DmFontSize, SpecialDanmaku
from .utils.network import (
    HEADERS,
    get_session,
    set_session,
    get_aiohttp_session,
    set_aiohttp_session,
    get_httpx_sync_session,
    set_httpx_sync_session,
    get_buvid3
)
from .utils.geetest import Geetest, GeetestMeta
from .errors import (
    ApiException,
    ArgsException,
    CredentialNoAcTimeValueException,
    CredentialNoBiliJctException,
    CredentialNoBuvid3Exception,
    CredentialNoDedeUserIDException,
    CredentialNoSessdataException,
    DanmakuClosedException,
    DynamicExceedImagesException,
    ExClimbWuzhiException,
    GeetestServerNotFoundException,
    GeetestUndoneException,
    LiveException,
    LoginError,
    NetworkException,
    ResponseCodeException,
    ResponseException,
    StatementException,
    VideoUploadException,
)
from . import (
    app,
    article_category,
    article,
    ass,
    audio_uploader,
    audio,
    bangumi,
    black_room,
    channel_series,
    cheese,
    client,
    comment,
    creative_center,
    dynamic,
    emoji,
    favorite_list,
    festival,
    game,
    homepage,
    hot,
    interactive_video,
    live_area,
    live,
    login_func,
    login,
    login_v2,
    manga,
    music,
    note,
    opus,
    rank,
    search,
    session,
    festival,
    homepage,
    login_v2,
    settings,
    show,
    topic,
    user,
    video_tag,
    video_uploader,
    video_zone,
    video,
    vote,
    watchroom
)

BILIBILI_API_VERSION = "16.3.0"

# 如果系统为 Windows，则修改默认策略，以解决代理报错问题
if "windows" in platform.system().lower():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore

__all__ = [
    "ApiException",
    "ArgsException",
    "BILIBILI_API_VERSION",
    "Credential",
    "CredentialNoBiliJctException",
    "CredentialNoBuvid3Exception",
    "CredentialNoDedeUserIDException",
    "CredentialNoSessdataException",
    "Danmaku",
    "DanmakuClosedException",
    "DmFontSize",
    "DmMode",
    "DynamicExceedImagesException",
    "Geetest",
    "GeetestMeta",
    "HEADERS",
    "LiveException",
    "LoginError",
    "NetworkException",
    "Picture",
    "ResourceType",
    "ResponseCodeException",
    "ResponseException",
    "SpecialDanmaku",
    "VideoUploadException",
    "aid2bvid",
    "app",
    "article",
    "article_category",
    "ass",
    "audio",
    "audio_uploader",
    "bangumi",
    "black_room",
    "bvid2aid",
    "channel_series",
    "cheese",
    "client",
    "comment",
    "creative_center",
    "dynamic",
    "emoji",
    "favorite_list",
    "festival",
    "game",
    "get_aiohttp_session",
    "get_httpx_sync_session",
    "get_real_url",
    "get_session",
    "homepage",
    "hot",
    "interactive_video",
    "live",
    "live_area",
    "login",
    "login_v2",
    "login_func",
    "manga",
    "music",
    "note",
    "opus",
    "parse_link",
    "rank",
    "search",
    "session",
    "set_aiohttp_session",
    "set_httpx_sync_session",
    "set_session",
    "settings",
    "show",
    "sync",
    "topic",
    "user",
    "video",
    "video_tag",
    "video_uploader",
    "video_zone",
    "vote",
    "watchroom",
    "ExClimbWuzhiException",
    "StatementException",
    "CredentialNoAcTimeValueException",
    "get_buvid3",
]
