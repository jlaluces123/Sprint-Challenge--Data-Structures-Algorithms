class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)  

    # --> Make a callback on both sides of the tree
    if self.left:
      self.left.depth_first_for_each(cb) # --> Pass in callback function || same for right side of tree
    elif self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    # --> Try to use queue structure


    # ------------------ works, but not happy with it -------------
    # queue = []
    # queue.append(self)

    # # --> Create loop for when queue has items in it
    # while len(queue) > 0:
    #   root_node = queue[0] # --> hold root node

    #   if root_node.left:
    #     queue.append(root_node.left) # --> Append all nodes from left side of the root node to our queue

    #   if root_node.right:
    #     queue.append(root_node.right) # --> Same thing for all nodes on the right side of the root node

    #   queue.pop(0)
    #   cb(root_node.value)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
