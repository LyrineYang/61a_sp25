def similar(self, k, similarity):
    others = list(Restaurants.all)
    others.remove(self)
    return sorted(others, key=lambda r: -similarity(r, self))[:k]
