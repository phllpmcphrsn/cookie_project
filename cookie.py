class Cookie:
    """
    Cookie class stores the yield from the base recipe and the
    desired yield. Also, the difference between the two is
    calculated for processing the cost of the desired batch of
    cookies' yield cost
    """
    def __init__(self, recipe_yield, desired_yield, prep_time):
        """Initialize Cookie object
        
        Args:
        recipe_yield (int): number of cookies in a single
                            batch
        desired_yield (int): number of cookies desired
        prep_time (int): time it takes to prepare one batch of
                         cookies in minutes
        """
        self.base_recipe_yield = recipe_yield
        self.desired_recipe_yield = desired_yield
        self.yield_difference = round(recipe_yield/desired_yield,2)
    