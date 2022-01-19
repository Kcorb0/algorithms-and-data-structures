
grid= [[1, 2, 7], 
       [4, 5, 6], 
       [8, 8, 9]]

def numCells(grid):
    
    dom_count = 0

    for idxr, row in enumerate(grid):
        for idxc, col in enumerate(row):
            checks = []

            # Check above
            if idxr > 0:
                checks.append(grid[idxr-1][idxc]) # above
                if idxc > 0:
                    checks.append(grid[idxr-1][idxc-1]) # above-left
                if idxc+1 < len(row):
                    checks.append(grid[idxr-1][idxc+1]) # above-right
            
            # Check below
            if idxr+1 < len(grid):
                checks.append(grid[idxr+1][idxc]) # above
                if idxc > 0:
                    checks.append(grid[idxr+1][idxc-1]) # above-left
                if idxc+1 < len(row):
                    checks.append(grid[idxr+1][idxc+1]) # above-right
            
            # Check sides
            if idxc > 0:
                checks.append(grid[idxr][idxc-1])
            
            if idxc+1 < len(row):
                checks.append(grid[idxr][idxc+1])
                
            if (col not in checks) and col > max(checks):
                dom_count += 1

    return dom_count
            

print(numCells(grid))