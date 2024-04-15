from enum import Enum


class RoleEnum(str, Enum):
    shop = "shop"
    client = "client"
    admin = "admin"
    shipper = "shipper"
