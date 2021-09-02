{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50f57417",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd\n",
    "import time "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c761222",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e320144",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5d8c845",
   "metadata": {},
   "source": [
    "## Visit the NASA Mars News Site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2ed1afd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c144de4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "## slide_elem = news_soup.select_one('div.list_text')\n",
    "slide_elem = news_soup.select_one('div.list_text')\n",
    "slied_elem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac8d4f3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06513741",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first a tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99fa4359",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16ed117d",
   "metadata": {},
   "source": [
    "##  JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7acf6e75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32b75f09",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b841c39b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')\n",
    "img_soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b868c181",
   "metadata": {},
   "outputs": [],
   "source": [
    "# find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "887ed58e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the base url to create an absolute url\n",
    "## img_url = f'{url}/{img_url_rel}'\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8dcb7e1",
   "metadata": {},
   "source": [
    "## Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "989ae5f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88799b4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns=['Description', 'Mars', 'Earth']\n",
    "df.set_index('Description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "720a0596",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b91e8bde",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b17c8ce",
   "metadata": {},
   "source": [
    "## Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f673260",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "hemispheres_url = 'https://marshemispheres.com/'\n",
    "browser.visit(hemispheres_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bd3387f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere. Code written in Saturday Morning Office \n",
    "# hours with Katrina.\n",
    "for i in range(4):\n",
    "    # print(i)\n",
    "    browser.find_by_tag('h3')[i].click()\n",
    "    #time.sleep(3)\n",
    "    \n",
    "    # parse with soup\n",
    "    html = browser.html\n",
    "    image_soup = soup(html, 'html.parser')\n",
    "        \n",
    "    # find the image\n",
    "    full_image = image_soup.find('div', class_=\"downloads\")\n",
    "    image_link = (full_image.find('a').get('href'))\n",
    "   \n",
    "    # Image URL\n",
    "    image_url = hemispheres_url + image_link\n",
    "    # time.sleep(2)\n",
    "       \n",
    "    # Title of Image\n",
    "    title_image = image_soup.select_one('h2.title').text\n",
    "    print(title_image)\n",
    "    \n",
    "    # Dictionary \n",
    "    hemispheres = {\n",
    "        \"img_url\" : image_url,\n",
    "        \"title\" : title_image\n",
    "         }\n",
    "    \n",
    "    hemisphere_image_urls.append(hemispheres)   \n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc7a4cbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8963b347",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "b4b5931839941ebd384e865d5c5491c9ec565d0e081776c892ed2ed368527512"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
