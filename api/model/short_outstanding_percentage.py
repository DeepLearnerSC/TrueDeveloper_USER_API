from .base_model import BaseModel

class ShortOutstandingPercentage(BaseModel):
    def __init__(
	    self,
        security_id,
        date,
        short_outstanding_percentage,
        floating_shares,
        short_outstanding_shares
        ):
        vars = locals()
        self.__dict__.update(vars)
        del self.__dict__["self"]
