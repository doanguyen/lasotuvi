from enum import unique, Enum
from typing import TypeVar


@unique
class AmDuong(Enum):
    Am = -1
    Duong = 1


AmDuongVar = TypeVar("AmDuongVar", bound=AmDuong)


@unique
class Tinh(Enum):
    """
    1: Chính tinh, 2: Phụ tinh nói chung
    3: Quý tinh, 4: Quyền tinh, 5: Phúc tinh, 6: Văn tinh
    7: Đài các tinh, 8: Đào hoa tinh

    11: Sát tinh, 12: Bại tinh, 13: Ám tinh, 14: Dâm tinh,
    15: Hình tinh, 16: Ác Tinh
    """

    CHINH_TINH = 1
    PHU_TINH = 2
    QUY_TINH = 3
    QUYEN_TINH = 4

    PHUC_TINH = 5
    VAN_TINH = 6
    DAI_CAC_TINH = 7
    DAO_HOA_TINH = 8
    SAT_TINH = 11
    BAI_TINH = 12
    AM_TINH = 13
    DAM_TINH = 14
    HINH_TINH = 15
    AC_TINH = 16


TinhVar = TypeVar("TinhVar", bound=Tinh)