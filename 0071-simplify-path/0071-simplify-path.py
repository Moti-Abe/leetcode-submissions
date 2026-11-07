class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        def dfs(i, dirs):
            if i == len(parts):
                return "/" + "/".join(dirs)
            
            current = parts[i]

            if current == "" or current == ".":
                return dfs(i+1,dirs)
            elif current == "..":
                if dirs:
                    dirs.pop()
                return dfs(i+1, dirs)
            else:
                dirs.append(current)
                return dfs(i+1, dirs)
        
        return dfs(0,[])