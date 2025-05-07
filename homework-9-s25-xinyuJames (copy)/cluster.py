from point import makePointList, Point


class Cluster:
    """A class representing a cluster of points.

    Attributes:
      center: A Point object representing the exact center of the cluster.
      points: A set of Point objects that constitute our cluster.
    """

    def __init__(self, center=Point([0, 0])):
        """Inits a Cluster with a specific center (defaults to [0,0])."""
        self.center = center
        self.points = set()

    @property
    def coords(self):
        return self.center.coords

    @property
    def dim(self):
        return self.center.dim

    def addPoint(self, p):
        self.points.add(p)

    def removePoint(self, p):
        self.points.remove(p)

    @property
    def avgDistance(self):
        """Calculates the average distance of points in the cluster to the center.

        Returns:
          A float representing the average distance from all points in self.points
          to self.center.
        """
        # fill in


        tot = 0.0
        for point in self.points:
            tot += point.distFrom(self.center)

        return tot/len(self.points)

    def updateCenter(self):
        """Updates self.center to be the average of all points in the cluster.

        If no points are in the cluster, then self.center should be unchanged.

        Returns:
          The coords of self.center.
        """
        # fill in
        # Hint: make sure self.center is a Point object after this function runs.
        if len(self.points) == 0:
            return self.center

        # add up all points in same coordinate and divided by len
        rtn_coord = [0.0] * self.center.dim
        for point in self.points:
            for i in range(self.center.dim):
                rtn_coord[i] += point[i]
        
        rtn_coord = [axis/len(self.points) for axis in rtn_coord]
        self.center = Point(rtn_coord)

        return self.center.coords

    def printAllPoints(self):
        print(str(self))
        for p in self.points:
            print("   {}".format(p))

    def __str__(self):
        return "Cluster: {} points and center = {}".format(
            len(self.points), self.center
        )

    def __repr__(self):
        return self.__str__()


def createClusters(data):
    """Creates clusters with centers from a k-by-d numpy array.

    Args:
      data: A k-by-d numpy array representing k d-dimensional points.

    Returns:
      A list of Clusters with each cluster centered at a d-dimensional
      point from each row of data.
    """
    centers = makePointList(data)
    return [Cluster(c) for c in centers]


if __name__ == "__main__":

    p1 = Point([2.5, 4.0])
    p2 = Point([3.0, 5.0])
    p3 = Point([1.0, 3.0])
    c = Cluster(Point([2.0, 2.0]))
    print(c)

    c.addPoint(p1)
    c.addPoint(p2)
    c.addPoint(p3)
    print("Updated", c)
    print("Average distance:", c.avgDistance)
    c.updateCenter()
    print("Updated", c)
    print("Updated average distance:", c.avgDistance)
    assert isinstance(
        c.center, Point
    ), "After updateCenter, the center must remain a Point object."
