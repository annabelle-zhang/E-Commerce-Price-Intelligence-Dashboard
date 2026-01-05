from bs4 import BeautifulSoup
import requests
import csv
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def scrape_newegg_product(search_term):

    try:
        formatted_search = search_term.replace(' ', '+')
        url = f'https://www.newegg.com/p/pl?d={formatted_search}'
        
        html_text = requests.get(url, headers=headers, timeout=10).text
        soup = BeautifulSoup(html_text, 'lxml')
        products = soup.find_all('div', class_='item-cell')
        
        if not products:
            print(f"  ⚠️  No products found for '{search_term}'")
            return []
        
        scraped_data = []
        
        for product in products:
            name_tag = product.find('a', class_='item-title')
            features_tag = product.find('ul', class_='item-features')
            original_price_tag = product.find('li', class_='price-was')
            curr_price_tag = product.find('li', class_='price-current')
            
            name = name_tag.text.strip() if name_tag else None
            features = features_tag.text.strip() if features_tag else None
            original_price = original_price_tag.text.strip() if original_price_tag else None
            curr_price = curr_price_tag.text.strip() if curr_price_tag else None
            if not all([name, features, original_price, curr_price]):
                continue # skip incomplete entries
            
            scraped_data.append({
                'Search Term': search_term,
                'Name': name,
                'Features': features,
                'Original Price': original_price,
                'Current Price': curr_price
            })
        
        return scraped_data
        
    except requests.exceptions.RequestException as e:
        print(f"couldn't find '{search_term}': {e}\n")
        return []
    except Exception as e:
        print(f"error for '{search_term}': {e}\n")
        return []

def main():
    input_file = 'product_names.csv' 
    output_file = 'newegg_data.csv'

    search_terms = []
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            search_terms.append(row['names'])
    
    print(f"Starting scrape for {len(search_terms)} products...\n")
    
    all_scraped_data = []

    for i, search_term in enumerate(search_terms, 1):
        print(f"[{i}/{len(search_terms)}] ", end="")
        
        results = scrape_newegg_product(search_term)
        all_scraped_data.extend(results)
        
        time.sleep(2)  # 2 second delay between searches

    if all_scraped_data:
        field_names = ['Search Term', 'Name', 'Features', 'Original Price', 'Current Price']
        file_exists = os.path.isfile(output_file)
        
        with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerows(all_scraped_data)

        print(f"data saved to '{output_file}'")
    else:
        print("\nnothing scraped")

if __name__ == "__main__":
    main()