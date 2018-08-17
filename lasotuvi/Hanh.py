from enum import Enum


class Hanh(Enum):
    """
    là một enum chứa giá trị các hành
    Kim = K = 1
    Thủy = T = 2
    Hỏa = H = 3
    Thổ = O = 4
    Mộc = M = 5
    """
    KIM = K = 1
    THUY = T = 2
    HOA = H = 3
    THO = O = 4
    MOC = M = 5

    __hanh_data = {
        KIM: {
            'cuc': 4,
            'ten_hanh': 'Kim',
            'ten_cuc': "Kim Tứ Cục",
            'css': 'hanhKim'
        },
        THUY: {
            'cuc': 2,
            'ten_hanh': 'Thủy',
            'ten_cuc': "Thủy nhị Cục",
            'css': 'hanhThuy'
        },
        HOA: {
            'cuc': 6,
            'ten_hanh': 'Hỏa',
            'ten_cuc': "Hỏa lục Cục",
            'css': 'hanhHoa'
        },
        THO: {
            'cuc': 5,
            'ten_hanh': 'Thổ',
            'ten_cuc': "Thổ Ngũ Cục",
            'css': 'hanhTho'
        },
        MOC: {
            'cuc': 3,
            'ten_hanh': 'Mộc',
            'ten_cuc': "Mộc Tam Cục",
            'css': 'hanhMoc'
        }

    }

    def __init__(self, hanh_id):
        self.id = hanh_id

    @property
    def css(self):
        return self.__hanh_data.value[self.id]['css']

    @property
    def cuc(self):
        return self.__hanh_data.value[self.id]['cuc']

    @property
    def ten_cuc(self):
        return self.__hanh_data.value[self.id]['ten_cuc']

    @property
    def ten(self):
        return self.__hanh_data.value[self.id]['ten_hanh']

    def __int__(self):
        return self.value

    def __str__(self):
        return self.name
