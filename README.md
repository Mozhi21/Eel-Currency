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

 👉 See folder for [screentshots](https://drive.google.com/drive/folders/1MAqQfowIyvuIGnM1J-c_pNzooaRHFzc1?usp=share_link) 


|    url            |      flag (clik to see each screenshot)              |     
|-------------------|-------------------------|
|  project2.5700.network/fakebook/569241248/ | [8dfb98d0ce8f05dff94f7ba019932dae3092434aae8843dd526068fe044eb5f6](https://drive.google.com/file/d/1YSbd-MwQL-Vy-t8YPD2UhNDhUrPgbDaC/view?usp=share_link)        |
|  project2.5700.network/fakebook/918222354/ | [8c4f831ab0da4eb39beb781d077669bbf370e69fe399b7d411d802ee1234971d](https://drive.google.com/file/d/1CReEl_BG0zzSUm-byUgEn0Gw59DeIBiP/view?usp=share_link)        | 
|  project2.5700.network/fakebook/862222411/ | [86b572e7056b0692200ce995d37fdf6f34abeaf90247155159a228fc3b1b5216](https://drive.google.com/file/d/16ksjoh4uqCegsDOdbwUx3k5LAbWfY8T0/view?usp=share_link)        | 
|  project2.5700.network/fakebook/768684842/ | [2fa8a7226ec30bf891b4696ae34c534445f985cb0bc0c0293f505145af95e47f](https://drive.google.com/file/d/1as7cQvah8MDylT91l4S_Vcr5wrY0RiYP/view?usp=share_link)        |
|  project2.5700.network/fakebook/528130223/ | [0f2cdd5ec07f84eff7dd9eeb58d7be243d4af96e8e1f5af819123883870f4c73](https://drive.google.com/file/d/1tBwfzyZ_KIBmCL13s9u2F4oqH0bTpgpy/view?usp=share_link)        |
![Xinyi's screenshots](https://drive.google.com/uc?export=view&id=1I6Uh5uMpViR4xOsxx2xw6PmvC7S2jbPO)|![Xinyi's falgs](https://drive.google.com/u/0/uc?id=1C1vXm7BT2u-7ipLeqP4aGoVphegC2TlJ&export=download)
   
Flgs found by **Mozhi Shen** 

|    url            |      flag               |     
|-------------------|-------------------------|
|  project2.5700.network/fakebook/725614836/ | [6a7ec6b2349f8d6a588593024834c8d0660ab9edd971fdbdb24811744609ed2f](https://drive.google.com/file/d/1pKGLk1qoAmOv4jVCYhIR9utj2ODAhPXz/view)    |
|  project2.5700.network/fakebook/178995388/ | [538cbf92b1ce0d0141d78090bcd667c803be978405d8ccf8486357473f33e15e](https://drive.google.com/file/d/1y3ZHh__UOOn_2hBNukvWd-mXI1uwVwIo/view?usp=share_link)   | 
|  project2.5700.network/fakebook/813499438/ | [9f634036a8abe3e3d9f23dcc5f35aad543b7b6874535759404ed1dfe1dd7cd24](https://drive.google.com/file/d/1jlrJ4zvC-Th83qaABh_VqBTSMHow6hNx/view?usp=sharing)        | 
|  project2.5700.network/fakebook/961886470/ | [dbdf0df829d683723f32f77c69c12c4718fb63662f3ac8bcc9728b37f425d1a8](https://drive.google.com/file/d/1pAhau7hGtVB7J-34QRZ29H6Rki38Zquv/view?usp=sharing)        |
|  project2.5700.network/fakebook/492181438/ | [ffd0662de5de6fbae7e86f4f2d6e6221c8054e4c2f215efb35fb8b97ca1c85de](https://drive.google.com/file/d/1_5-OqhmD3l_ce8QT8KgzPrVHX5X9R4Y8/view?usp=sharing)     |

![Mozhi's falgs](https://drive.google.com/uc?export=view&id=1jDhwrgSYayqtdwSJoZ7545QdPZRRvgR8)

Flgs found by **Hui Hu** 

|    url            |      flag (clik to see each screenshot)              |     
|-------------------|-------------------------|
|  project2.5700.network/fakebook/103771976/ | [ccf87d989f7643d2324517dc95052b818eb293983ee92dd494c70210ff3461b3](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag1.png)        |
|  project2.5700.network/fakebook/105473746/ | [cc989c325342ac357e038d97195688497847b67141ca4d52cb4d81ef5b335d02](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag2.png)        | 
|  project2.5700.network/fakebook/810885469/ | [c33c686dbf4f2eaa989a16a25f342a1f5b081be18ba8661f49f5394cfd8d0907](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag3.png)        | 
|  project2.5700.network/fakebook/438763355/ | [203dd70b48cdab6f3f9e3e221269211b9fb9914c7e89cd73600d17752e8c51f8](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag4.pngg)        |
|  project2.5700.network/fakebook/941127588/ | [46e9d1bb131ed25a43a7c3dfe3ab601ea7c3116c2d383bb9511c58a071b3501a](https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flag5.png)        |

<div  align="center">    
   <img src="https://raw.githubusercontent.com/huwang12138/markdown-picture/main/flags.png" height = "320" alt="splash_demo" align=center />
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

:star: **Hui Hu**:

1. `socket.recv()` is a blocking call, which means the program is blocked, or halted, until `socket.recv()` finish its operations, and the program can resume its execution. When socket is blocking, `socket.recv` will return as long as the network buffers have bytes. If bytes in the network buffers are more than `socket.recv` can handle, it will return the maximum number of bytes it can handle. If bytes in the network buffers are less than `socket.recv` can handle, it will return all the bytes in the network buffers. One trick lays here, if we cannot find the correct buffer size when receiving header data, we will keep getting empty bytes, which causes a infinite loop. 

2. The `Set-Cookie` field name contains a series of attributes that specify the details of the cookie, including its name, value, expiration time, domain, path, and other metadata. For example:

   `Set-Cookie: sessionid=xxxxxxx; csrftoken=xxxxxxxx; name=value; Expires=Wed, 21 Oct 2023 07:28:00 GMT; Path=/; Domain=example.com; Secure; HttpOnly`
We only need `sessionid` and `csrftoken`.
## Tests
**Xinyi Feng**: I use a lot of print in my code, to check what the request header and body looks like and what message given back.
Also, I print out the craweling process in my console like `print("start crawl url:", url)` to check the url is crawling. Besides, I import timer just for checking the crawling speed. And last, print the flags when I find one. 


@ 2023  Northeastern University
