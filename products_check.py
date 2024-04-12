import csv
import requests

# Replace 'YOUR_TOKEN' with your actual API token
API_TOKEN = 'acefdc2e8e7611f4997c680d7bb9992637380e37f9b5f07d9af4bd08c35de161'

# G2 API endpoint for products
API_ENDPOINT = 'https://data.g2.com/api/v1/products'

def check_product_availability(product_name):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    params = {
        'filter[name]': product_name
    }
    response = requests.get(API_ENDPOINT, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            products = data['data']
            if products:
                # Check if the product we're interested in is listed
                for product in products:
                    if 'attributes' in product and 'name' in product['attributes'] and product['attributes']['name'] == product_name:
                        return True
            else:
                return False
        else:
            # Handle missing 'data' key in response
            print('Error: No data found in response')
            return None
    else:
        # Handle API error
        print('Error:', response.status_code)
        return None

def check_products_in_csv(csv_file):
    unavailable_products = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            product_name = row[0]  
            is_listed = check_product_availability(product_name)
            if is_listed is None:
                print(f'Failed to check availability for {product_name}.')
            elif not is_listed:
                print(f'{product_name} is not listed on G2.')
                unavailable_products.append(product_name)
    return unavailable_products

def write_to_csv(unavailable_products, output_csv):
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Unavailable Products'])
        for product in unavailable_products:
            writer.writerow([product])
    print(f'Unavailable products written to {output_csv}.')

def main():
    # Example CSV file containing product names
    csv_file = '/Users/mohanrao/Downloads/products1.csv'
    output_csv = '/Users/mohanrao/Downloads/unavailable_products.csv'
    unavailable_products = check_products_in_csv(csv_file)
    write_to_csv(unavailable_products, output_csv)

if __name__ == "__main__":
    main()

