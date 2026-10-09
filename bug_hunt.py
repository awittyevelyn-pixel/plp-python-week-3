# bug_hunt.py

# Program Goal: Keep adding items to a cart until budget is spent or limit is reached,
# tracking total cost and item count.

budget = 50
total_cost = 0
item_count = 0
item_price = 15

# BUG: The condition `total_cost > budget` starts as False (0 > 50), so the loop never runs at all.
# FIX: Change `total_cost > budget` to `total_cost + item_price <= budget`.
while total_cost > budget:
    
    # BUG: We add item_price to total_cost before checking if we can afford it, causing an overcharge.
    # FIX: Check or update total_cost after verifying budget constraints inside the loop logic.
    total_cost += item_price
    
    # BUG: item_count is never incremented inside the loop, leaving the counter at 0 forever.
    # FIX: Add `item_count += 1` inside the loop body.
    
    print(f"Added item. Total cost so far: ${total_cost}")

print(f"Shopping finished! Total items: {item_count}, Total spent: ${total_cost}")