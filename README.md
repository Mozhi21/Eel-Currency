# HTTP WEBCRAWLER - CS 5700


 **Group members:**
 
 :woman_technologist:   **Xinyi Feng** : [FentPams](https://github.com/FentPams) &nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:feng.xinyi@northeastern.edu">
<img align="mid" alt="XinyiFeng | email" width="20px" src="https://www.logo.wine/a/logo/Gmail/Gmail-Logo.wine.svg" src = "feng.xinyi@northeastern.edu" />
</a> contatct me via: feng.xinyi@northeastern.edu

 :man_technologist:     **Mozhi Shen** : [Mozhi21](https://github.com/Mozhi21) &nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:shen.moz@northeastern.edu">
<img align="mid" alt="MozhiShen | email" width="20px" src="https://www.logo.wine/a/logo/Gmail/Gmail-Logo.wine.svg" src = "shen.moz@northeastern.edu" />
</a> contatct me via: shen.moz@northeastern.edu

 :man_technologist:     **Hui Hu** : [Hui-Hwoo](https://github.com/Hui-Hwoo) &nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:hu.hui1@northeastern.edu">
<img align="mid" alt="HuiHu | email" width="20px" src="https://www.logo.wine/a/logo/Gmail/Gmail-Logo.wine.svg" src = "hu.hui1@northeastern.edu" />
</a> contatct me via: hu.hui1@northeastern.edu


**Professor**: Hamandi Lama 


![My Skills](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Table of Contents

- [Background](#background)
- [How to run it](#run)
- [Method](#method)
- [Result](#result)
- [Feedback and thoughts](#thoughts)
- [The way I test](#tests)



## Background

- This webcrawler is only for CS5700 assignment.
- The site to crawl: [Fakebook](https://project2.5700.network/)
- Our goal is to implement a web crawler that gathers 5 secret flags with format ```<h2 class='secret_flag' style="color:red">FLAG: 64-characters-of-random-alphanumerics</h2>``` 


## Run
Go to the diretcory where the *webcrwler.py* in, and execute on the command line using the following syntax:

```
python3 webcrawler.py [username] [password]
```

## Method
We use Breadth-First Search (BFS) to crawl friends' list, get the URL and check the flags. Below are the detailed explanation on each function and method we used: 

**`FakebookHTMLParser:`** This custom HTML parser class is responsible for processing the server's HTTP responses. It extends Python's HTMLParser and implements the following methods:

- `handle_starttag():` Processes HTML start tags to find CSRF tokens, URLs to crawl, and secret flags.
- `handle_data():` Processes the data between HTML tags, such as extracting the secret flag and determining if there is a next page of friends.
- `parse_cmd_line():` This function parses command-line arguments to retrieve the username and password required for logging into the Fakebook site.

**`create_socket():`** This function creates a TLS-wrapped socket, which establishes a secure connection to the HTTP server. The connection is made to the host project2.5700.network on port 443, the standard HTTPS port.

**`send_get_request():`** This function sends an HTTP GET request over the established connection. The request is constructed with the appropriate headers, including the Host, and if available, the Cookie header with the session and CSRF tokens.

**`login_user():`** This function logs in to the Fakebook site by sending an HTTP POST request with the required login credentials and CSRF token. The POST request includes the Content-Type, Content-Length, and Cookie headers.

**`receive_msg():`** This function reads the server's response after sending an HTTP request. It first reads the response header until it encounters "\r\n\r\n", then reads the response body based on the Content-Length value specified in the header.

**`update_cookies():`** This function processes the Set-Cookie header lines in the server's response to update the cookies dictionary. The cookies are used for maintaining the session and CSRF tokens in subsequent requests.

**`main():`** The main function of the program is responsible for the following tasks:

- Parsing the username and password from the command line.
- Creating a TLS-wrapped socket for a secure connection.
- Sending GET requests for the root and login pages, updating the cookies, and extracting the CSRF token.
- Logging in to the site using the login_user() function and a POST request.
- Initiating the web crawling process using a Breadth-First Search (BFS) algorithm and deque data structure to store the URLs to be crawled.
- Continuously sending GET requests for new URLs and processing the responses using the custom HTML parser.
- The networking aspect of the code focuses on establishing a secure connection to an HTTP server, sending HTTP requests (GET and POST), processing the server's responses, and maintaining session and CSRF tokens through cookies.
To summarize, the code uses a BFS algorithm to crawl the Fakebook site and a custom HTML parser to extract secret flags and URLs.


## Result



Flags found by **Xinyi Feng** 

 👉 See folder for [screentshots](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/tree/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi) 


|    url            |      flag (clik to see each screenshot)              |     
|-------------------|-------------------------|
|  project2.5700.network/fakebook/569241248/ | [8dfb98d0ce8f05dff94f7ba019932dae3092434aae8843dd526068fe044eb5f6](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/blob/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi/8dfb98d0ce8f05dff9417ba019932dae3092434aae8843dd526068fe044eb5f6.png)        |
|  project2.5700.network/fakebook/918222354/ | [8c4f831ab0da4eb39beb781d077669bbf370e69fe399b7d411d802ee1234971d](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/blob/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi/8c4%C2%A3831ab0da4eb39beb781d077669bb370e69fe399b7d411d802ee1234971d.png)        | 
|  project2.5700.network/fakebook/862222411/ | [86b572e7056b0692200ce995d37fdf6f34abeaf90247155159a228fc3b1b5216](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/blob/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi/86b57270560692200ce995d37fdf6f34abeaf90247155159a228fc3b1b5216.png)        | 
|  project2.5700.network/fakebook/768684842/ | [2fa8a7226ec30bf891b4696ae34c534445f985cb0bc0c0293f505145af95e47f](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/blob/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi/2f8a7226ec30bf891b4696ae34c534445f985cb0bc0c0293505145af95e47f.png)        |
|  project2.5700.network/fakebook/528130223/ | [0f2cdd5ec07f84eff7dd9eeb58d7be243d4af96e8e1f5af819123883870f4c73](https://github.com/CS5700-Hamandi-SP23/sp23-webcrawler-FentPams/blob/main/SP23%20webcrawler%20starter%20code/Flags_screenshot_Xinyi/0f2cdd5ec07f84eff7dd9eeb58d7be243d4af968e1f5af819123883870f4c73.png)        |
<div  align="center">    
   <img src="./Flags_screenshot_Xinyi/5flags_screenshots .png" width = "690" height = "720" alt="splash_demo" align=center />
</div>
<div  align="center">    
   <img src="./Flags_screenshot_Xinyi/Xinyi Feng_Flag_Screenshot.png" width = "690" height = "720" alt="splash_demo" align=center />
</div>
   
Flgs found by **Mozhi Shen** 

|    url            |      flag               |     
|-------------------|-------------------------|
|                   |                         |


Flgs found by **Hui Hu** 

|    url            |      flag (clik to see each screenshot)              |     
|-------------------|-------------------------|
|  project2.5700.network/fakebook/103771976/ | [ccf87d989f7643d2324517dc95052b818eb293983ee92dd494c70210ff3461b3](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag1.png)        |
|  project2.5700.network/fakebook/105473746/ | [cc989c325342ac357e038d97195688497847b67141ca4d52cb4d81ef5b335d02](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag2.png)        | 
|  project2.5700.network/fakebook/810885469/ | [c33c686dbf4f2eaa989a16a25f342a1f5b081be18ba8661f49f5394cfd8d0907](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag3.png)        | 
|  project2.5700.network/fakebook/438763355/ | [203dd70b48cdab6f3f9e3e221269211b9fb9914c7e89cd73600d17752e8c51f8](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag4.pngg)        |
|  project2.5700.network/fakebook/941127588/ | [46e9d1bb131ed25a43a7c3dfe3ab601ea7c3116c2d383bb9511c58a071b3501a](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag5.png)        |

<div  align="center">    
   <img src="https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flags.png" width = "690" height = "720" alt="splash_demo" align=center />
</div>



## Thoughts

:star: **Xinyi Feng**: I'd like to share how I **speed up** my crawling

**From 1.5 hours → 20 mins**


1. Keep the socket alive, 1 socket through the program, instead of creating a new socket for each request.
 In FakebookHTMLParser class, the `handle_starttag`   function,  we turn attr into dictionary structure `attrs = dict(attrs)` (used to be a list), which speed up in looking up.
2. `In FakebookHTMLParser` class, we add a flag `self.has_next_page = False`
the `handle_data`  function, we complete crawling one’s friend list when the “next” URL doesn’t exist, saving us a one-time request. 
3. In `receive_msg` function,  for reading the header data until "\r\n\r\n" is found, we used to use `while b"\r\n\r\n" not in header_data:` which will check the whole header data; now we use `while not header_data.endswith(b"\r\n\r\n"):` which only needs to check the end of the header data.

4. Break the crawling when all 5 flags are found. 

## Tests
**Xinyi Feng**: I use a lot of print in my code, to check what the request header and body looks like and what message given back.
Also, I print out the craweling process in my console like `print("start crawl url:", url)` to check the url is crawling. Besides, I import timer just for checking the crawling speed. And last, print the flags when I find one. 


@ 2023  Northeastern University
