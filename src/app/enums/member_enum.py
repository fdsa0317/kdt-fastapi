from enum import Enum

class MemberProvider(str, Enum):
    LOCAL = "LPCAL"
    GOOGLE = "GOOGLE"
    KAKAO = "KAKAO"
    NAVER = "NAVER"