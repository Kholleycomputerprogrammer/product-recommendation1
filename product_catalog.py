from product_data import products

# Step 1 - Print out the products to see the data that you are working with.
print("Product Catalog Preview:")
for product in products[:5]:  # Just print the first few for brevity
    print(product)

# Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").strip().upper()

# Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)

# Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })

# Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags)

# Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append((product["name"], matches))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

# Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_tags)

print("\nRecommended Products:")
for name, match_count in results:
    print(f"- {name} ({match_count} match(es))")

