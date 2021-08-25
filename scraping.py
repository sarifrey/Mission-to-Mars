
# Impnort Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
import time
from webdriver_manager.chrome import ChromeDriverManager

    
def scrape_all():  
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    # DO I NEED ALL THIS? 
    
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere_data(browser)
  
    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "mars_hemispheres" : hemisphere_image_urls,
    }
       
     # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site    
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
   
    return news_title, news_p

# JPL Space Images Featured Image
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    
    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None


    # Assing columns and set index of dataframe
    # df.columns=['Description', 'Mars', 'Earth']
    # df.set_index('Description', inplace=True)

# convert DataFrame back into HTML-ready code, add bootstrap
    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    return df.to_html()

# browser.quit()

# Mars Hemisphere scrape
def hemisphere_data(browser):
    # Use browser to visit the URL 
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)

# 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere. Code written in Saturday Morning Office 
# hours with Katrina.
    for i in range(4):
        print(i)
        browser.find_by_tag('h3')[i].click()
        # time.sleep(3)
        
        # parse with soup
        html = browser.html
        image_soup = soup(html, 'html.parser')
            
        # find the image
        full_image = image_soup.find('div', class_="downloads")
        image_link = (full_image.find('a').get('href'))
    
        # Image URL
        image_url = hemispheres_url + image_link
        # time.sleep(3)
       
    # Title of Image
        title_image = image_soup.select_one('h2.title').text
        print(title_image)
    
    # Dictionary 
        hemispheres = {
            "img_url" : image_url,
            "title" : title_image
            }
        hemisphere_image_urls.append(hemispheres)   
        browser.back()

        browser.quit()  
        return hemisphere_image_urls
# If running as script, print scraped data  
  
if __name__ == "__main__":
    print(scrape_all())