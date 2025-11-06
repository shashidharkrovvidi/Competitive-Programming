#https://leetcode.com/problems/accounts-merge/description/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            parent.setdefault(x,x)
            parent.setdefault(y,y)
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email, email)
                email_to_name[email] = name
        
        groups = defaultdict(list)
        result = []

        print(parent)
        print("=================\n")
       

        for email in parent:
            root = find(email)
            groups[root].append(email)

        print(groups)
        
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))
        
        return result
            


            

