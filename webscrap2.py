from operator import lt, div

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", { "class": "_3O0U0u"})
print(len(containers))
print(soup.prettify(containers[0]))
&lt;div class="_3O0U0u"&gt;
 &lt;div data-id="MOBFRZZHMHQVNDFA" style="width:100%"&gt;
  &lt;div class="_1UoZlX"&gt;
   &lt;a class="_31qSD5" href="/samsung-galaxy-m01-blue-32-gb/p/itmc068b26305a0d?pid=MOBFRZZHMHQVNDFA&amp;amp;lid=LSTMOBFRZZHMHQVNDFAZXGBO6&amp;amp;marketplace=FLIPKART&amp;amp;srno=s_1_1&amp;amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;amp;fm=organic&amp;amp;iid=f9a57085-7ab9-4aba-b59d-5a4cbecd03e9.MOBFRZZHMHQVNDFA.SEARCH&amp;amp;ssid=zu9bg122ao0000001596818422200&amp;amp;qH=0258c7d48242959a" rel="noopener noreferrer" target="_blank"&gt;
    &lt;div class="_3SQWE6"&gt;
     &lt;div class="_1OCn9C"&gt;
      &lt;div&gt;
       &lt;div class="_3BTv9X" style="height:200px;width:200px"&gt;
        &lt;img alt="Samsung Galaxy M01 (Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/&gt;
       &lt;/div&gt;
      &lt;/div&gt;
     &lt;/div&gt;
     &lt;div class="_2lesQu"&gt;
      &lt;div class="_1O_CiZ"&gt;
       &lt;span class="_1iHA1p"&gt;
        &lt;div class="_2kFyHg"&gt;
         &lt;label&gt;
          &lt;input class="_3uUUD5" readonly="" type="checkbox"/&gt;
          &lt;div class="_1p7h2j"&gt;
          &lt;/div&gt;
         &lt;/label&gt;
        &lt;/div&gt;
       &lt;/span&gt;
       &lt;label class="_10TB-Q"&gt;
        &lt;span&gt;
         Add to Compare
        &lt;/span&gt;
       &lt;/label&gt;
      &lt;/div&gt;
     &lt;/div&gt;
     &lt;div class="_3gDSOa _32A6AP"&gt;
      &lt;div class="DsQ2eg"&gt;
       &lt;svg class="_2oLiqr" height="16" viewbox="0 0 20 16" width="16" xmlns="http://www.w3.org/2000/svg"&gt;
        &lt;path class="_35Y7Yo" d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"&gt;
        &lt;/path&gt;
       &lt;/svg&gt;
      &lt;/div&gt;
     &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="_1-2Iqu row"&gt;
     &lt;div class="col col-7-12"&gt;
      &lt;div class="_3wU53n"&gt;
       Samsung Galaxy M01 (Blue, 32 GB)
      &lt;/div&gt;
      &lt;div class="niH0FQ"&gt;
       &lt;span class="_2_KrJI" id="productRating_LSTMOBFRZZHMHQVNDFAZXGBO6_MOBFRZZHMHQVNDFA_"&gt;
        &lt;div class="hGSR34"&gt;
         4.2
         &lt;img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/&gt;
        &lt;/div&gt;
       &lt;/span&gt;
       &lt;span class="_38sUEc"&gt;
        &lt;span&gt;
         &lt;span&gt;
          5,040 Ratings
         &lt;/span&gt;
         &lt;span class="_1VpSqZ"&gt;
          &amp;amp;
         &lt;/span&gt;
         &lt;span&gt;
          371 Reviews
         &lt;/span&gt;
        &lt;/span&gt;
       &lt;/span&gt;
      &lt;/div&gt;
      &lt;div class="_3ULzGw"&gt;
       &lt;ul class="vFw0gD"&gt;
        &lt;li class="tVe95H"&gt;
         3 GB RAM | 32 GB ROM | Expandable Upto 512 GB
        &lt;/li&gt;
        &lt;li class="tVe95H"&gt;
         14.48 cm (5.7 inch) HD+ Display
        &lt;/li&gt;
        &lt;li class="tVe95H"&gt;
         13MP + 2MP | 5MP Front Camera
        &lt;/li&gt;
        &lt;li class="tVe95H"&gt;
         4000 mAh Lithium-ion Battery
        &lt;/li&gt;
        &lt;li class="tVe95H"&gt;
         Qualcomm Snapdragon (SDM439) Octa Core Processor
        &lt;/li&gt;
        &lt;li class="tVe95H"&gt;
         1 Year Manufacturer Warranty for Phone and 6 Months Warranty for in the Box Accessories
        &lt;/li&gt;
       &lt;/ul&gt;
      &lt;/div&gt;
     &lt;/div&gt;
     &lt;div class="col col-5-12 _2o7WAb"&gt;
      &lt;div class="_6BWGkk"&gt;
       &lt;div class="_1uv9Cb"&gt;
        &lt;div class="_1vC4OE _2rQ-NK"&gt;
         ₹9,899
        &lt;/div&gt;
       &lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="_3n6o0t"&gt;
       &lt;img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/&gt;
      &lt;/div&gt;
     &lt;/div&gt;
    &lt;/div&gt;
   &lt;/a&gt;
  &lt;/div&gt;
 &lt;/div&gt;
&lt;/div&gt;
container = containers[0]
print(container.div.img["alt"])
price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
print(price[0].text)
ratings = container.findAll("div", {"class": "niH0FQ"})
print(ratings[0].text)
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text
    print("Product_Name:"+ product_name)
    print("Price: " + price)
    print("Ratings:" + rating)