#!/usr/bin/env python
# coding: utf-8

# # Introduction to HTML, CSS, JavaScript & How websites work? 
For every website to be designed, HTML (HyperText Markup Language) is a must. This is the skeleton of a website.
Without it, no website can run. 
CSS (Cascading Style Sheets) adds beauty to that website and JavaScript adds the brain to allow the functioning of that website.Let us now take another example of a car. The HTML acts as the metallic body of a car and the CSS acts as the color and design of the car. Finally, 
the engine of a car is like the JavaScript on the website to add functionality.a client or a user sends a request to the webserver of the website, he wants to visit. The web server that has its own IP address stores 
all the files in the backend which can be written in PHP, Python, or Node.js.
The web server sends a response to the client in the form of HTML, CSS, and JavaScript. HTML is used as a standard language for any website design. It acts as a static skeleton to a web application. It’s a well-standardized system.
CSS is used to handle the presentation of the web page. It makes the website look attractive and beautiful.
JavaScript allows scripting on your website and makes it completely dynamic in nature. It provides front end scripting for your website and is
a high-level dynamic interpreted programming language. HTML, CSS, and JavaScript have a lot of concepts in them which we will take over through the span of this course.
Therefore, it cannot be learned all at once. If you are a beginner, learning HTML up to 80%, CSS up to 40-60%, 
 and JavaScript up to 50-70% will be more than enough to start building websites
 <!-- This is doctype -->
<!DOCTYPE html>
<!-- Our HTML code starts here -->
<html lang="en">
<!-- Our Head tag starts here -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>This is title</title>
</head>
<!-- Our Body tag starts here -->
<body>
    Yeh meri body ka content hai
</body>
</html>The HTML code contains some sections such as DOCTYPE, meta tags, head, and body. All the tags that we
include in an HTML file, needs to be first opened and then closed by angular brackets. Let us now understand different sections one by one.

Doctype HTML- Doctype HTML justifies that it is a HTML document. So, we are defining specifically for 
a browser to understand that it is an HTML document. To understand more about the type of documents, you can visit here.
<html lang= “en”> - It is the opening part of the HTML tag that tells us the language of the document is in English.
<head> - Head contains all the meta-tags in it which is used to describe the contents of a website. Meta means providing information
about information. Therefore, meta tags are used to define the keywords and descriptions on our website. Head also contains the title
of the website and all the external files like CSS and JavaScript that we link to it.
<body> - Body contains all the contents of the webpage in it. However, in the beginning, our website may look a little uglier
but after including stylesheets it will start looking attractive. 

the comments by writing “<!-- Your text -->” in this format. 

# # Title, Script, Link & Meta Tags 
The Meta Tags are used to define the Meta data in an HTML. They are mainly used in SEO (Search Engine Optimization) techniques
which help any particular website to rank better in Google or different search engines. It simply boosts the ranking of a webpage 
to get more traffic on any website.So let us understand various meta tags. 

<meta charset= “UTF-8”>
- It simply means that the characters that are used will be of UTF-8. It declares the page’s character encoding. 
It should contain a standard IANA MIME name for character encodings. Moreover, authors are encouraged to use UTF-8. <meta name= “viewport” content= “width=device-width, initial-scale=1.0">
- This tag is used to make your website responsive and adjust its width in such a way that it looks good in both PC or mobile.
It helps in making the website mobile friendly also.<meta http-equiv= “X-UA-Compatible” content= “ie=edge”>
- It helps any particular website to open in the highest compatibility mode available. It is mostly for those who are still \
using Internet Explorer. Because there are still some people who have not upgraded their system and are still using the older versions.

o add descriptions and keywords on our website, we still use meta tags.

<meta name= “description” content = “This is a description”>
- To add a description, we have to write the above statement and write your own description in the content part.
<meta name= “keywords” content= “html tutorial, css tutorial”>
- Keywords are those special words through which a user reach any website. You can add the keywords in the content part of the tag.
 

If we want our website to be indexed in Google or other search engines and bots should follow all the links present on the website, then we have to write-

<meta name= “robots” content= “INDEX, FOLLOW”><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="This is description">
    <meta name="keywords" content="html, html tutorials, web development">
    <meta name="robots" content="INDEX, FOLLOW">
    <title>Document</title>

    <!-- This is how you include external css -->
    <link rel="stylesheet" href="harry.css">

    

    <!-- This is how you include external JavaScript -->
    <script src="harry.js"></script>
</head>
<body> 


</body>
</html>To link our stylesheets named as “harry.css” in the HTML code, we have to write-

<link rel= “stylesheet” href= “harry.css”>
In the same way, as we have included CSS, we can also include a JavaScript file in <head> tag.

<script src = “harry.js”></script>
There are basically six types of heading tags ranging from <h1>, <h2>, <h3>, <h4>, <h5>, and <h6>. 
These are the six heading tags from h1 being the largest font size and h6 being the smallest font size. There is an important you should know about H1 tags.
In every website there is only one <h1> tag, which is the main heading of the website. You should never write the normal paragraph text as headings just to
make it bold. It is advised that using <h1> tag only once will help in SEOThen comes the paragraph tag which is denoted by <p>. Whenever we want to add a paragraph on our website then we can simply use paragraph tag in
the format-
<p>some random texts</p>The next tags that we are going to see are <strong> and <em> (emphasized) tags. Writing some texts between strong tags will make that portion of the text as bold. 
And writing any text between em tags, will convert that part as Italic. However, these texts can later be changed with the help of CSS.

Now to change a line in a paragraph we can easily use the <br> tag. It is a self-closing tag which helps to break a line. However, using too many <br> tags is not good for practice. 
We will discuss this more when we are going to learn CSS.

<p>first<br><br><br><br>This is a new line</p>
# # Img and Anchor tags
In the body tag, if you type “a", anchor tag will appear. Just hit the enter key or if you want you can manually write the whole tag. Refer to the declaration below:

<a href=""> </a>href is the attribute of anchor tag where you have to write the URL of the website or Link that you want to open. Next,
you have to write the Keyword on which you want the user to click so that he will be redirected to the linked website. Refer to the example below:

<a href="https://google.com">Go to Google</a>
o open a website in a new tab, you have to write something like this:

<a href="https://google.com" target = "_blank">Go to Google</a>this was all in the anchor tag of HTML now let’s move to the next topic I.e. handling Images in HTML. 

In order to insert an image in a webpage, you have to use the img tag. 

An img tag generally have two basic attributes “src" and “alt".

<img src="" alt="">Apart from this, let's see another example where we can adjust the height and width of the image using the URL only. Well, this is not something that we can do in every URL.
Here we can do it because the developers of the website have created this URL accordingly. 

For instance:

<img src="https://source.unsplash.com/1600x900/?nature,water" alt= "Error loading image">Apart from this, let's see another example where we can adjust the height and width of the image using the URL only. Well, this is not something 
that we can do in every URL. Here we can do it because the developers of the website have created this URL accordingly. 

For instance:

<img src="https://source.unsplash.com/1600x900/?nature,water" alt= "Error loading image"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Links and images</title>
</head>
<body>
    <a href="https://google.com" target="_blank">Go to google</a><br>
    <a href="https://facebook.com" target="_blank">Go to facebook</a><br>
    <a href="https://twitter.com" target="_blank">Go to twitter</a><br>
    <a href="https://linkedin.com" target="_blank">Go to Linkedin</a><br>
    <a href="/tut4.html" target="_blank">Tut 4</a>
    <a href="/tut5.html" target="_blank">Tut 5</a>

    <!-- Image is not present hence alt text is shown -->
    <!-- <img src="harry.jpg" alt="Error loading image"> -->
    <img src="https://source.unsplash.com/200x110/?nature,water" alt="remote image" width="233" height="34">


</body>
</html>
# # Lists and Tables
Give the title as Tables and Lists in <title> tag. 

The lists are basically of two types-

Ordered lists (ol)
<ol>

          <li>This is the first item of my unordered list</li>

</ol>
Unordered lists (ul)
<ul>

          <li>This is the first item if my unordered list</li>

</ul>The difference between an ordered and an unordered list is that the ordered list displays the list in this format -

1.

2.

3.

….

On the other hand, the unordered lists display the list in the following format-

.
.
.
….Both the lists have more than one attribute which we can write using the type command. For example, if we write:

<ol type= “I”>
 Then we will get the lists as I, II, III, and so on. In the same format, we can also get the lists as A, B, C, and so on.

This applies on unordered lists also. If we write

<ul type= “square”>
Then we will get a bulleted square instead of a circle. There are various other references available from which you can see all the attributes. 
There is no need to learn all these things. You will get perfect by practising.HTML also allows the nesting of lists. It simply means we can add a list into another list.

 <ul type="circle">
        <li>This is first item of my unordered list</li>
        <li>This is second item of my unordered list</li>

        <ul>
            <li>Another one</li>
            <li>Another two</li>
            <li>Another three</li>
 </ul>The main part is the table tag, and it consists of two parts: the table head and table body. The <thead> consists of the main head of the table and <tbody>
consists of the body of the table. 

<tr> is used to justify that it is the part of a row. Inside the <tr> tag, we give the headings of a row under the <th> tag. The final structure of a table looks like-In a table, there are mostly two things to remember, the head and the body of a table. To add more rows to the table, we can simply add a <tr> tag and add any number of rows in a table.

I believe you have understood clearly what the lists and tables are. Tables and lists are two primary components of a website that helps in making it more attractive.
There will be more tutorials coming to assist you in developing your site.
So be patient and keep practising the things taught till now.  <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Tables and Lists</title>
</head>

<body>
    <ul type="circle">
        <li>This is first item of my unordered list</li>
        <li>This is second item of my unordered list</li>

        <ul>
            <li>Another one</li>
            <li>Another two</li>
            <li>Another three</li>
        </ul>


        <li>This is third item of my unordered list</li>
    </ul>
    <ol type="a">
        <li>This is first item of my ordered list</li>
        <li>This is second item of my ordered list</li>
        <li>This is third item of my ordered list</li>
    </ol>

    <!-- Tables -->
    <h3>HTML Table</h3>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Employee Id</th>
                <th>Employee Role</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> Harry </td>
                <td> 34343 </td>
                <td> Programmer </td>
            </tr>
            <tr>
                <td> Rohan Das</td>
                <td> 3483 </td>
                <td> HTML Expert </td>
            </tr>
            <tr>
                <td> Shubham </td>
                <td> 7564 </td>
                <td> Android Developer </td>
            </tr>
        </tbody>
    </table>

</body>

</html>
# # Forms & Input Tags
Whenever we add a <form> tag in the HTML, it is going to ask for some action for submitting that particular form in the backend for future reference. 
So, for now, we will write it as backend.php. All the data submitted in a form will be stored automatically in the backend “backend.php” after submitting it.

The template will look like-

<form action= “backend.php”>
Then comes the <input>tags which are present inside the form, where the user provides the input. These inputs can be of any type whether text, button, checkbox, date,
time, etc. Input Tags are used to create interactive controls for web-based forms in order to accept data from the user. 

The <span> is an in-line element and <div> is a block element. Which means, if we use two separate div tags for different inputs, then all the inputs will come on different lines.
We will learn about the span and div in detail in the upcoming tutorial. Till then we will use the <br> tags for breaking a line.

To get the input as text, the syntax is-
<input type= “text”>To get the input type as an email in the form, the syntax is-
<div>
            Email: <input type="email" name="myEmail">
</div>
The name here is used so that the backend can recognize the tag that we are using.

To get the submit button in the form, the syntax is-
<div>
          <input type= “submit” value= “submit now”>
</div>
We can also add date and time in the form. To add these, the general syntax is-
<div>
         <input type= “date” name= ”myDate” id= “”>
</div>
It will give the complete date form in the format of “dd/mm/yyyy”.\

To add any numeric text in the HTML form, the syntax is-
<div>
             Number: <input type= “number” name “myNumber”>
</div>
While filling several online forms, you must have seen the radio buttons and checkboxes in the form. Radio buttons are such buttons that allows to select
any one of the following options amongst all. For example, while selecting the gender, we can only select either male or female. Whereas the checkbox allows selecting 
the multiple options available. The example of both the formats are as follows-

For checkbox-
 <div>
            Are you eligible?: <input type="checkbox" name="myEligibility" checked>
 </div>
For Radio buttons-
<div>
            Gender: Male <input type="radio" name="myGender"> Female <input type="radio" name="myGender">
            Other <input type="radio" name="myGender">
 </div>
To reset all the information, entered in the form, we take the help of a reset button. To get the reset button, we have to write-
<div>
            Input type= “reset” value= “Reset Now”
</div>
After inserting all these input tags, our form will look like-<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Forms</title>
</head>

<body>
    <h2>This is HTML forms tutorial</h2>
    <form action="backend.php">
        <label for="name"> Name</label>
        <div>
            <input type="text" name="myName" id="name">
        </div>
        <br>
        <div>
            Role: <input type="text" name="myRole">
        </div>
        <br>
        <div>
            Email: <input type="email" name="myEmail">
        </div>

        <br>
        <div>
            Date: <input type="date" name="myDate">
        </div>
        <br>
        <div>
            Bonus: <input type="number" name="myBonus">
        </div>
        <br>
        <div>
            Are you eligible?: <input type="checkbox" name="myEligibility" checked>
        </div>
        <br>
        <div>
            Gender: Male <input type="radio" name="myGender"> Female <input type="radio" name="myGender">
            Other <input type="radio" name="myGender">
        </div>

        <br>
        <div>
            Write about yourself: <br><textarea name="myText" cols="90" rows="10"></textarea>
        </div>

        <br>
        <div>
            <label for="car">Car</label>
            <select name="myCar" id="car">
                <option value="ind">Indica</option>
                <option value="swf" selected>Swift</option>
            </select>
        </div>
        <br>

        <div>
            <input type="submit" value="Submit Now">
            <input type="reset" value="Reset Now">
        </div>
    </form>
</body>

</html>

# # Inline & Block Elements
Inline elements are those elements which only occupy the space bounded by the tags defining the element, instead of breaking the flow of element. 
On the other hand, block-level elements take up the entire space of its parent element. Let us understand this with an example-

If we write any text in the paragraph tag like this-

<p>This is a paragraph</p>

<p>This is also a paragraph</p>
OR

<p>This is a paragraph</p> <p>This is also a paragraph</p>We want both the texts in the same line but it is not so. Can you think why?

It is because the paragraph tag is a block element. The Block element means that it will take the full width of a single line and does not allow any other
content to fit in it. But, if we write both the texts between the <span> tags like-

<span>This is a paragraph</span> <span>This is also a paragraph</span>
Then we see that both the texts will appear in the same line. It is because the <span> tag is an inline element. It allows all the elements in the same line.

To understand it more, we can take the help of CSS by applying the border. However, you need not worry about the border as it is a part of CSS. I’m using this just for the case
of an example. 

<p style= “border: 2px solid, red;”>This is a paragraph</p> <p style= “border: 2ox solid blue;”>This is also a paragraph</p>

<span style= “border: 2px solid red;”>This is a span</span> <span style = “border: 2px solid red;”>This is also a span</span>
After testing the above code in the live server, you will know the main difference between inline and block elementsThe above example shows how inline elements will take only its portion of text whereas the block element will take the whole width of the line. 
You will understand it more with the help of different colours through CSS. Anchor <a> tags also behaves like an inline element. 

We have two different options of making our text appear in a single line. The first one is either with the help of CSS through borders or with the help of inline elements. 
As we have reached the end of this tutorial, I want you to find out whether li, em, div is inline or block elements. 

So, I believe till now you must have understood the major difference between Inline and Block elements. Stay with the course to learn more things in this complete web 
development Bootcamp.

Code as described/written in the video
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Inline and Block elements</title>
</head>
<body>
    <strong style="border: 2px solid red;">this is a paragraph</strong> <a style="border: 2px solid blue;">
        this is also a paragraph</a>
    <span style="border: 2px solid red;">this is a span</span> <span style="border: 2px solid red;">this is also a span</span>

    li, em, div, img
</body>
</html>
# # Ids & Classes in HTML 
The ID is an identifier which must be unique in the whole HTML document. It is used to find an element while linking, scripting, or styling. Whereas, Classes allow CSS and
JavaScript to select and access specific elements.
I'll try to explain with the vert basic example. When a new child is born, we urge to give him a name or his identity by which he will be known further.
Or if you are having a pet, you must have given him some name to call. In the same way, IDs refer to giving a name to any particular element for its identity.
It simply refers giving an identity to an element. We know, no two names can be given to any of the two members of the family. In the same way, one ID can be 
given to only one element on a website. Therefore, in the below example, the id mainBox cannot be given to any other element.

<div id= “mainBox” class= “redBG”>Now the question arises what is the need for an ID in HTML? The answer is, while using JavaScript or CSS, we can target one full element and can make the necessary changes in it. In the same way, we can grab the full element and change the border or width or many more things through CSS.

Let us now understand what are classes with an example. Assume that I am having 100 elements in my HTML and I want to give a red background to all the 100 elements. To do this, we have two options. Either we have to select each element and assign a red background to it or we can create a class redBG and assign a red background to it. Then we can give this class to the elements in which we want a red background color. To avoid confusion, I am assuming that the class redBG is already defined.

One point to note here is we can assign only one ID to a particular element but it is not so in the case of classes. An element can have more than one class in itself. The more classes we add in an element, the more property will get added to it.

Classes are denoted by a dot ‘.’ and ID is denoted by hash ‘#’. For example, to get a redBG class in an element we can simply write that element name followed by .redBG. The below picture shows everything, you have learned till now-<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ids and classes in HTML</title>
</head>
<body>
    <h3>Ids and classes tutorial</h3>
    <div id="mainBox" class="redBg blackBorder">
        this is mainbox
    </div>
    <span class="redBg"></span>
    <!-- Select and press ctrl + / to comment -->
    <!-- Emmet -->
    <!-- . is for class and # is for id -->
    <span class="redBg"></span>
    <span id="mainSpan"></span>
    <div class="redBg blackBorder anotherClass"></div>

    <!-- Emmet takes div tag as default -->
    <div class="blackBackground"></div>

    <!-- Creating multiple elements using Emmet -->
    <!-- span.myClass.myClass2.myClass3*4 + <Tab> to print 4 similar elements using Emmet -->
    <span class="myClass myClass2 myClass3">First</span>
    <span class="myClass myClass2 myClass3">Second</span>
    <span class="myClass myClass2 myClass3">Third</span>
    <span class="myClass myClass2 myClass3">Fourth</span>

</body>
</html>

# # HTML Entities
This tutorial is about different Entities used in the HTML. An entity is a piece of text (“string”) that begins with an ‘&’ and ends with a ‘;’. These are frequently used to display reserved characters, and invisible characters. As usual, let us begin the tutorial by making a new HTML file as tut11.html and add an instant boilerplate to get the basic template of HTML. Give the title as HTML Entities in the <title> tag.

Try to understand with the below example. If we write the code as

<div class= “container”>
            <p>This is a Paragraph</p>
</div>
<div class= “container”>
          <p>This is another Paragraph</p>
</div>You will normally say that all the extra spaces will reflect back on the webpage. But it is not so. Because HTML treats all the extra spaces as a single space only and automatically removes all of them. Therefore, if you want
to use extra spaces or any special characters, then you have to use HTML entities. To get extra space we can use &nbsp (non-breaking space) after that particular text. For example-

<div class= “container”>
          <p>This is another &nbsp Paragraph</p>
</div>
By writing this way, we can create 1 extra space after the word another. By adding five &nbsp, we can get 5 extra spaces. However, I do not recommend using this method because it looks unprofessional. We will learn to create extra spaces in CSS with the help of margin, padding, or selectors that looks more professional. Entities are also used to write some special characters that you cannot write from keyboards and also those words that are reserved in HTML. For example, if we want <p> to appear in the result, then it is not possible without the help of entities. 

<div class= “container”>
          <p>This is another Paragraph<p></p>
</div>
By writing the above code, we will see that we cannot obtain the <p> in our result. Therefore, the solution for this is we can take the help of HTML entities. We have to write in this format-

<div class= “container”>
          <p>This is another Paragraph &lt;p&gt; </p>
</div>
There is a list of different reserved characters and hundreds of special characters that you cannot write without entities. There is no need to learn all those entities available. You are always free to take the help of various references available.

So, this is all for this tutorial and I hope you have got the basic knowledge about HTML entities. If you still have any queries, feel free to ask.

Code as described/written in the video
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML Entities</title>
</head>
<body>
    <div class="container">
        <p>This is a paragraph</p>
    </div>
    <div class="container">
        <p>This is another     paragraph with two spaces</p>
        <p>Paragraph is written like this <p> </p>
        <p>Pound is written like this £ </p>
        <p>Copyright is written like this © </p>
        <p>Another character is  ⇛ </p>
        <p>Another character is  ¼ </p>
        <p>Empty character is written like this ​ </p>
    </div>
</body>
</html>
Previous
