#!/usr/bin/env python
# coding: utf-8

#Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo

def init_browser():
    #browser set-up
    executable_path = {"executable_path": "C:/Users/lksh0/.wdm/drivers/chromedriver/win32/87.0.4280.20/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser
## NASA Mars News (Most recent article)
    #visit the website
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    #parse HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #step through HTML to find news title
    step1 = soup.find('ul', class_='item_list')
    step2 = step1.find('li', class_='slide')
    step3 = step2.find('div', class_='content_title')
    title = step3.text
    #continue step to find paragraph
    step4 = step2.find('div', class_='article_teaser_body')
    paragraph = step4.text
    
    #store results in dictionary
    NASA_site = {
        "title": title,
        "paragraph": paragraph
    }

## JPL Mars Space Image (Featured)
    #visit the website
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    #Scrape the page into BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Find the URL for the Image
    image_url = soup.find('li',class_='slide').a['data-fancybox-href']
    #Combine main website to image for full URL
    main = 'https://www.jpl.nasa.gov/'
    featured_image_url = main + image_url

    #store results in dictionary
    JPL = {'featured image': featured_image_url}

## Mars Facts (table)
    #Mars Facts website
    url = 'https://space-facts.com/mars/'
    #Read table data into Pandas
    mars_facts = pd.read_html(url)
    #Return results as a dataframe
    mars_df = mars_facts[0]
    #mars_df.head()
    #Convert table to HTML
    mars_df.to_html(header=False,bold_rows=False)


## Mars Hemispheres (images)
    #visit the website
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    #Scrape the page into BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #List to store hemisphere data dictionaries
    hemisphere_data = []
    #dictionary for each hemisphere's data
    hemisphere = {}
    ## Cerberus
    #dictionary for hemisphere
    hemisphere = {}
    #click on the link
    browser.find_by_css('a.product-item h3').click()
    #find href "SAMPLE" link to full size image and assign to dictionary
    sample = browser.find_link_by_text("Sample").first
    img_url = sample["href"]
   #get the title from the page
    title = browser.find_by_css('h2.title').text
    #append information to dictionary
    hemisphere['title'] = title.replace("Enhanced"," ")
    hemisphere['img_url'] = img_url
    #add the dictionary to the hemisphere_data list
    hemisphere_data.append(hemisphere)
    #go back to front page
    browser.back()
## Schiaparelli
    #dictionary for hemisphere
    hemisphere = {}
    #click on the link
    browser.find_by_css('a.product-item h3')[1].click()
    #find href "SAMPLE" link to full size image and assign to dictionary
    sample = browser.find_link_by_text("Sample").first
    img_url = sample["href"]
    #get the title from the page
    title = browser.find_by_css('h2.title').text
    #append information to dictionary
    hemisphere['title'] = title.replace("Enhanced"," ")
    hemisphere['img_url'] = img_url
    #add the dictionary to the hemisphere_data list
    hemisphere_data.append(hemisphere)
    #go back to front page
    browser.back()
## Syrtis Major
    #dictionary for hemisphere
    hemisphere = {}
    #click on the link
    browser.find_by_css('a.product-item h3')[2].click()
    #find href "SAMPLE" link to full size image and assign to dictionary
    sample = browser.find_link_by_text("Sample").first
    img_url = sample["href"]
    #get the title from the page
    title = browser.find_by_css('h2.title').text
    #append information to dictionary
    hemisphere['title'] = title.replace("Enhanced"," ")
    hemisphere['img_url'] = img_url
    #add the dictionary to the hemisphere_data list
    hemisphere_data.append(hemisphere)
    #go back to front page
    browser.back()
## Valles
    #dictionary for hemisphere
    hemisphere = {}
    #click on the link
    browser.find_by_css('a.product-item h3')[3].click()
    #find href "SAMPLE" link to full size image and assign to dictionary
    sample = browser.find_link_by_text("Sample").first
    img_url = sample["href"]
    #get the title from the page
    title = browser.find_by_css('h2.title').text
    #append information to dictionary
    hemisphere['title'] = title.replace("Enhanced"," ")
    hemisphere['img_url'] = img_url
    #add the dictionary to the hemisphere_data list
    hemisphere_data.append(hemisphere)
    #go back to front page
    browser.back()