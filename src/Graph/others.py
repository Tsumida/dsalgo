# =================================================================================
# err msg
ERR_INVALID_STORAGE_TYPE = "Error, invalid storage type: {}"
ERR_NODE_EXISTS = "Error, node {} exists."
ERR_EDGE_EXISTS = "Error, edge {} exists."
# =================================================================================

PHY_MAT = "matrix"
PHY_ADJ_LIS = "adjacent lis"
# =================================================================================

class GraphException(Exception):

    def __init__(self, msg:str):
        self.msg = msg

    def __str__(self):
        return self.msg
