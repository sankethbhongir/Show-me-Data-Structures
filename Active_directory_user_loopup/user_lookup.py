class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    def __repr__(self):
     s = f"parent group: {self.get_name()} \n users: {self.get_users()}"
     groups = [g for g in self.get_groups()]
     s+= f"\n groups: {groups}"
     return s
     
     def __str__(self):
         return self.get_name()
         
 
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

sub_child_user1 = "sub_child_user1"
sub_child1 = Group("subchild1")
sub_child1.add_user(sub_child_user1)
parent.add_group(sub_child1)



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
      
    """
    users = group.get_users()
    groups = group.get_groups()
    
    if user in users:
        return True
    
    for group in groups:
        user_lookup = is_user_in_group(user, group)
        if user_lookup:
            return True
        
    return False

#print(parent)
print(is_user_in_group('sub_child_user1', parent))