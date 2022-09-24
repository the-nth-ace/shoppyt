import imp
from conn.db import get_session
import models
import scalars
from utils.utils import get_valid_data


async def get_vendors(info):
    """Get all vendors resolver"""
    async with get_session() as session:
        db_vendors = await session.query(models.Vendor).all()
    vendors_list = []
    for ven in db_vendors:
        ven_dict = get_valid_data(ven, models.Vendor)
        vendors_list.append(scalars.Vendor(**ven_dict))

    return vendors_list
